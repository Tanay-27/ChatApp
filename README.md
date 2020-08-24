# Invisibility Cloak
A Potterhead tries to replicate the invisiblity cloak with the help of opencv
The usable hosted version is under construction, till then one may follow the below mentioned steps to download and use the invisibility cloak


### Cloning the github repository
One may fork the repo and then clone it or
` git clone https://github.com/Tanay-27/Invisibility.git `
### Installing the dependencies
` pip install -r requirements.txt `
### Running the program
` python inv.py `
#### The command prompt will be showing the localhost address http://localhost:5000/, copy paste the address in the browser of your choice,
#### wait for 2-3 seconds before coming in front the screen
#### bring any red coloured object, preferably a blanket or long cloth, hide yourself and enjoy

### Explanation
__Steps:-__
- Procuring the background 
- Fliping the images 
- Converting to HSV Format
- Making Masks
- Bitwise AND
- Displaying Output
- Basic app to be used locally using flask

### Masks
The entire magic behind the project lies in the masks
2 masks have been used here-
First the input frame is added with a mask which removes the red portion from the image
Next the removed part from the image is replaced by anding the compliment of the first mask with the background
The 2 frames thus created are added equally and thus the invisible magic is successfully created.

#### Credits
https://www.geeksforgeeks.org/
