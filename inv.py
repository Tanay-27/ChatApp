from flask import Flask, Response
import cv2
import numpy as np

app = Flask(__name__)
# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'  
video = cv2.VideoCapture(0)
def invisible(img,background):
	img = np.flip(img, axis = 1)  #return_val, img = capture_video.read() 
	background = np.flip(background, axis = 1) # flipping of the frame 
	# convert the image - BGR to HSV  as we focused on detection of red color converting BGR to HSV for better 
	# detection or you can convert it to gray 
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
	# ranges should be carefully chosen setting the lower and upper range for mask1 
	lower_red = np.array([100, 40, 40])	 
	upper_red = np.array([100, 255, 255]) 
	mask1 = cv2.inRange(hsv, lower_red, upper_red) 
	# setting the lower and upper range for mask2 
	lower_red = np.array([155, 40, 40]) 
	upper_red = np.array([180, 255, 255]) 
	mask2 = cv2.inRange(hsv, lower_red, upper_red) 
	#----------------------------------------------------------------------# 
	mask1 = mask1 + mask2 
	# Refining the mask corresponding to the detected red color 
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), 
										np.uint8), iterations = 2) 
	mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
	mask2 = cv2.bitwise_not(mask1) 
	# Generating the final output 
	res1 = cv2.bitwise_and(background, background, mask = mask1) 
	res2 = cv2.bitwise_and(img, img, mask = mask2) 
	final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
	return final_output

def gen(video):
    for i in range(60): 
        return_val, background = video.read() 
        if return_val == False : 
            continue
    while True:
        success, image = video.read()
        image = invisible(image,background)
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run( threaded=True)