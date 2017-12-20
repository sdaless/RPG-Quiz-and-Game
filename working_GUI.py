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

		#app.setRadioButton("choiceA", 1, callFunction=True)
		#app.setRadioButton("choiceB", 1, callFunction=True)
		#app.setRadioButton("choiceC", 1, callFunction=True)
		#app.setRadioButton("choiceD", 1, callFunction=True)
		#app.setRadioButton("choiceE", 1, callFunction=True)
		
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
		app.addEmptyMessage("ee")
		app.addEmptyMessage("ff")


		app.stopPage()





		app.startPage()
		app.addLabel("l4", "If you were a supervillain, who would you be?")
		app.addEmptyMessage("eee")
		app.addEmptyMessage("fff")
		app.addRadioButton("choice4", "Two-Face")
		app.addRadioButton("choice4", "Riddler")
		app.addRadioButton("choice4", "Bane")
		app.addRadioButton("choice4", "Catwoman")
		app.addRadioButton("choice4", "Poison Ivy")

				
		app.stopPage()




		app.startPage()
		app.addLabel("l5", "What mythical creature would you be?")
		app.addEmptyMessage("gg")
		app.addEmptyMessage("hh")
		app.addRadioButton("choice5", "Centaur")
		app.addRadioButton("choice5", "Elf")
		app.addRadioButton("choice5", "Ogre")
		app.addRadioButton("choice5", "Basilisk")
		app.addRadioButton("choice5", "Angel")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l6", "Which personality trait best describes you?")
		app.addEmptyMessage("ii")
		app.addEmptyMessage("jj")
		app.addRadioButton("choice6", "Courageous")
		app.addRadioButton("choice6", "Wise")
		app.addRadioButton("choice6", "Powerful")
		app.addRadioButton("choice6", "Cunning")
		app.addRadioButton("choice6", "Compassionate")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l7", "Which of the following seems to be a recurring") 
		app.addLabel("l77", "problem for you?")
		app.addEmptyMessage("kk")
		app.addEmptyMessage("ll")
		app.addRadioButton("choice7", "I tend to see things in black-and-white,") 
		app.addLabel("l077", "good-or-bad.")
		app.addRadioButton("choice7", "I tend to overanalyze situations.")
		app.addRadioButton("choice7", "I tend to lose my temper too quickly.")
		app.addRadioButton("choice7", "I tend to be sadistic.")
		app.addRadioButton("choice7", "I tend to have my kindness taken for") 
		app.addLabel("granted.")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l8", "What role do you see yourself playing in an action") 
		app.addLabel("l88", "movie?")
		app.addEmptyMessage("mm")
		app.addEmptyMessage("nn")
		app.addRadioButton("choice8", "The Hero")
		app.addRadioButton("choice8", "The Sidekick")
		app.addRadioButton("choice8", "The Rival")
		app.addRadioButton("choice8", "The Anti-hero")
		app.addRadioButton("choice8", "The Group Mom")
		
	
		app.stopPage()




		app.startPage()
		app.addLabel("l9", "Which occupation below would you choose?")
		app.addEmptyMessage("oo")
		app.addEmptyMessage("pp")
		app.addRadioButton("choice9", "Lawyer")
		app.addRadioButton("choice9", "College professor")
		app.addRadioButton("choice9", "Professional Boxer")
		app.addRadioButton("choice9", "Mercenary")
		app.addRadioButton("choice9", "EMT worker")
		
	
		app.stopPage()




		app.startPage()
		app.addLabel("l10", "Which book/series is your favorite out of the") 
		app.addLabel("l110", "following?")
		app.addEmptyMessage("qq")
		app.addEmptyMessage("rr")
		app.addRadioButton("choice10", "Divergent")
		app.addRadioButton("choice10", "Harry Potter")
		app.addRadioButton("choice10", "Sun Tzu's Art of War")
		app.addRadioButton("choice10", "V for Vendetta")
		app.addRadioButton("choice10", "The Giving Tree")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l11", "Pick a virtue out of the following (shoutout 2") 
		app.addLabel("l111", "whoever gets the reference):")
		app.addEmptyMessage("ss")
		app.addEmptyMessage("tt")
		app.addRadioButton("choice11", "Candor")
		app.addRadioButton("choice11", "Erudite")
		app.addRadioButton("choice11", "Abegnation")
		app.addRadioButton("choice11", "Dauntless")
		app.addRadioButton("choice11", "Amity")
		app.addButton("SUBMIT", press)
	

		app.stopPage()



		if button == "SUBMIT":
			app.getRadioButton()
			result()

			#app.setRadioButtonChangeFunction("choice", "choice2", "choice3", press)


		#app.startPage()
		#app.addLabel("final", "You're ", archetype, "!")
		#app.stopPage()
		app.stopPagedWindow()
	

	else:
		app.stop()


app.addButtons(["Start Quiz", "Exit"], press)

#archetype = result()

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