# import the freaking library
import tkinter as tk
from appJar import gui

# need classes?


# create a GUI variable called app
app = gui("Character Archetype Quiz", "600x400")
app.setResizable(canResize=False)
app.setBg("light blue")
app.setFont(18, font="Courier")
app.setLocation("CENTER")


# add & configure widgets - widgets get a name, to help reference later
app.addLabel("title", "What Character Archetype are you?")
username = app.addLabelEntry("Welcome! Enter your name: ")
app.addLabel("subtitle", "Click one of the buttons below to continue!") 
app.setLabelBg("title", "white")


# add homescreen images
app.setImageLocation("Image Folder")
app.addImage("mage", "mage2.gif")

# buttons
def press(button):
	if button == "Start Quiz":		

	else:
		app.stop()

app.addButtons(["Start Quiz", "Exit"], press)

# start the bloody GUI
app.go()