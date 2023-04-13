Python-GUI-Project

Description-->
The GUI project is built using Python and Tkinter.

Library Used-->
import tkinter

How to run-->
Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command:
1. pip install -r requirement.txt
2. python -m pip install pyinstaller
3. pyinstaller filename.py --onefile

This GUI has following functionalities:-->

1. This project follows OOPS concept.
2. The main function of this GUI is to give a fact everytime you click on clickme button. End point used is-->"https://uselessfacts.jsph.pl/random.json?language=en"
3. There are radio buttons, entry widget, label and a text box with slider, multiple header with some pop up messages when help option is used.
4. There is a button attached to slider, that is, when selected age and click on button below it, it gives a pop up message. 
5. There is all_functions.py file which gets the url from constant.py and gets the JSON response from it. Response is then parsed to python dictionary and text is    shown on GUI. 




