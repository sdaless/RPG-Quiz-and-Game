# import the freaking library
# import tkinter as tk
from appJar import gui
# from graphics import *

# need classes?

# create a GUI variable called app
app = gui("Character Archetype Quiz", "600x400")
app.setResizable(canResize=False)
app.setBg("light blue")
app.setFont(18, font="Courier")
app.setLocation("CENTER")
app.setGuiPadding(2, 4)


# add & configure widgets - widgets get a name, to help reference later
app.addLabel("title", "What Character Archetype are you?")
# username = app.addLabelEntry("Welcome! Enter your name: ")
app.addLabel("subtitle", "Click one of the buttons below to continue!") 
app.setLabelBg("title", "white")

# add homescreen images
app.setImageLocation("Image Folder")
app.addImage("mage", "mage2.gif")

# this stuff
a = 0
b = 0
c = 0
d = 0
e = 0

def tally(x):
	if x == "Sword" or "Speak my mind and use force only if need be." or "Superman":
		global a
		a += 1
		return a
	if x == "Wand (assuming you could cast spells)" or "Cast brujería on my enemies." or "Doctor Strange":
		global b
		b += 1
		return b
	if x == "C":
		global c
		c += 1
		return c
	if x == "D":
		global d
		d += 1
		return d
	if x == "E":
		global e
		e += 1
		return e

# buttons
def press(button):
	if button == "Start Quiz":
		#clear away everything
		app.removeAllWidgets()
		app.startPagedWindow("Welcome!")

		app.startPage()
		app.addLabel("l1", "If you were caught in a position to defend") 
		app.addLabel("l01", "yourself, which weapon would you prefer?")
		app.addEmptyMessage("0")
		app.addEmptyMessage("00")
		app.addRadioButton("choice", "Sword")
		app.addRadioButton("choice", "Wand (assuming you could cast spells)")
		app.addRadioButton("choice", "Fists")
		app.addRadioButton("choice", "Daggers")
		app.addRadioButton("choice", "Peace and love, man.")
		app.addEmptyMessage("01")
		app.addEmptyMessage("02")
		app.addEmptyMessage("03")
		
		app.stopPage()
		


		app.startPage()
		app.addLabel("l2", "How do you tend to handle conflicts?")
		app.addEmptyMessage("aa")
		app.addEmptyMessage("bb")
		app.addRadioButton("choice2", "Speak my mind and use force only if need be.")
		app.addRadioButton("choice2", "Cast brujería on my enemies.")
		app.addRadioButton("choice2", "Fight them. No one wants to catch these hands.")
		app.addRadioButton("choice2", "Secretly plot their demise. They better sleep") 
		app.addLabel("l02", "with one eye open.")
		app.addRadioButton("choice2", "I am a tender soul that cannot handle conflict.")
	
		app.stopPage()



		app.startPage()
		app.addLabel("l3", "If you were a superhero, who would you be?")
		app.addEmptyMessage("cc")
		app.addEmptyMessage("dd")
		app.addRadioButton("choice3", "Superman")
		app.addRadioButton("choice3", "Doctor Strange")
		app.addRadioButton("choice3", "Wonderwoman")
		app.addRadioButton("choice3", "Batman")
		app.addRadioButton("choice3", "Aquaman")

		app.stopPage()


		app.startPage()
		app.addLabel("final", "You're ", archetype, "!")
		app.stopPage()
		app.stopPagedWindow()
	

	else:
		app.stop()


app.addButtons(["Start Quiz", "Exit"], press)

archetype = result()

def result():
	if a > b and a > c and a > d and a > e:
		print("a Knight")
	elif b > a and b > c and b > d and b > e:
		print("a Mage")
	elif c > a and c > b and c > d and c > e:
		print("a Tank")
	elif d > a and d > b and d > c and d > e:
		print("an Assassin")
	elif e > a and e > b and e > c and e > d:
		print("a Healer!")
	else:
		print("2 complicated. Please take quiz again and change like one of your answers.")

#result()

# start the bloody GUI
app.go()