
from functions import *

import Tkinter as Tk
import random
import os
import time

from playsound import playsound
import AppKit

Data1 = open("DataBase.txt", "r")
Data = Data1.read()
Megacharacteristics = Data.split("\n")


characteristics = []
characteristicsstr = []
index = 0

for n in Megacharacteristics:
	if n == "End":
		break
	characteristics.append(n.split(";"))
	characteristicsstr.append(characteristics[index][0])
	index += 1

ListeEnt = ""
for n in characteristicsstr:
	ListeEnt = ListeEnt + n +", "


ListQuestion = ["What color is your animal ?","What size is your animal ?","Where does your animal lives?"]
ListQuestionSyntyp = ["ADJ","ADJ","NOUN"]

Done = []
rep = ""
Bob = "images/bob sleeps.gif"

root = Tk.Tk()
root.attributes("-fullscreen", True)

Background = Tk.PhotoImage(file = 'images/landscape.gif')
Background_label = Tk.Label(root,image = Background)
Background_label.place(relwidth = 1, relheight = 1)

Frame1 = Tk.Frame(root,bg = '#3AEE0E')
Frame1.place(relx = 0.05, rely = 0.05,relwidth =0.9,relheight = 0.9)
welCome = "Welcome to Devinator \nChoose an animal among the one shown :"
Textstart = Tk.Label(Frame1,text =welCome,bg = '#98DE86')

Imgdp = Tk.PhotoImage(file = 'images/StartPict.gif')
Imagedepart = Tk.Label(Frame1,image = Imgdp)

Textstart.pack()
Imagedepart.pack()


bouton_next = Tk.Button(Frame1,text="I made my choice",command = root.quit,bg = '#98DE86')
bouton_next.pack(side = 'bottom',fill= 'x')
root.update()

synthesize_text(welCome)
playsound("output.mp3")
root.mainloop()

Frame1.destroy()

while  "exit" not in rep :

# --------------------Choosing what question to ask-------------------------------------

	QuestComplex = random.choice([True,False])

	if QuestComplex == True and len(ListQuestion) >= 1:
	
		repstr = random.choice(ListQuestion)

		TypeSyn = ListQuestionSyntyp[ListQuestion.index(repstr)]
	

	else:	
		while cle in Done:
			characteristicscle = list(random.choice(characteristics))
			cle = random.choice(characteristicscle[4:])

		Done.append(cle)
		repstr = "Does your animal has " + cle + "?"
		QuestComplex = False
			
			
	Lenstart = len(characteristics)
		
	

#------------------------- Graphic interface ------------------------
	
	FrameBob = Tk.Frame(root,bg = '#98DE86')
	FrameBob.place(relx = 0.5, rely = 0.1, relwidth = 0.4, relheight = 0.4)
	FrameBob1 =  Tk.Frame(FrameBob,bd = 10)
	FrameBob1.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight=0.8)


	imgbob = Tk.PhotoImage(file=Bob)
	imagebob = Tk.Label(FrameBob1,image =imgbob)
	imagebob.pack()


	FrameTxt = Tk.Frame(root,bg = '#3AEE0E')
	FrameTxt.place(relx = 0.1,rely = 0.6, relwidth = 0.6, relheight = 0.4)
	FrameTxt1 =  Tk.Frame(FrameTxt, bd= 2)
	FrameTxt1.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight=0.8)

	question = Tk.Label(FrameTxt1,text=repstr)
	question.pack()

	root.update()
	
	#----------------------- Asking the question oraly ------------------------
	synthesize_text(repstr)

	playsound("output.mp3")

   	#----------------------- Retrieving the response audio --------------------
	
	root.bell()
	main()
	phrase = phrase.split(" ")
	
	if "confirm" in phrase:
		phrase.remove("confirm")
	elif "cancel" in phrase:
		QuestComplex = "cancel"
		phrase.remove("cancel")

	phrase = " ".join(phrase)
	rep = str(phrase)
	print("Your response:",rep)

	
	
	root.update()

	time.sleep(2)
	
	

# ------------ Exploiting yes/no question ---------

	if "yes" in rep and QuestComplex == False:
		Entite = list(characteristics)
		for i in characteristics:

			if cle not in i:
				Entite.remove(i)

		characteristics = Entite

	elif "no" in rep and QuestComplex == False:
		Entite = list(characteristics)
		for i in characteristics:

			if cle in i:
				Entite.remove(i)

		characteristics = Entite

	if QuestComplex == True:
		decoding(rep,TypeSyn)
		
		if Lenstart != len(characteristics):
			ListQuestion.remove(repstr)
			ListQuestionSyntyp.remove(TypeSyn)
		else:
			synthesize_text("I did not understand")
			playsound("output.mp3")
			while Lenstart == len(characteristics):
				FrameTxt1.destroy()
				root.update()
				synthesize_text("Could you rephrase ?")
				playsound("output.mp3")
				
				FrameTxt1 =  Tk.Frame(FrameTxt, bd= 2)
				FrameTxt1.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight=0.8)
				question = Tk.Label(FrameTxt1,text=repstr)
				question.pack()
				root.update()
				main()

				phrase = phrase.split(" ")
	
				if "confirm" in phrase:
					phrase.remove("confirm")
				elif "cancel" in phrase:
					QuestComplex = "cancel"
					phrase.remove("cancel")

				phrase = " ".join(phrase)
				rep = str(phrase)
				decoding(rep,TypeSyn)
				
				


	#------------- Sponge Bob Expression --------------------------
	
	""" Sponge Bob's is happy when the question/answer help him eliminate possible animals """

	if Lenstart-len(characteristics) == 1:
		Bob = "images/bob sad.gif"
	if Lenstart-len(characteristics) > 1:
		Bob = "images/bob happy middle.gif"
	if Lenstart-len(characteristics) > 2:
		Bob = "images/bob happy a lot.gif"

	FrameBob.destroy()
	FrameTxt.destroy()
	root.update()


# Launches when the programm believes it found the right answer

	if len(characteristics)==1:

		Foundd = characteristics[0][0]
		if "'" in Foundd:
			Foundd = Foundd.split("'")
		else:
			Foundd = Foundd.split(" ")

		img = "images/"+ Foundd[1] + ".gif"
		fin = "Your animal is the" + characteristics[0][0] + "\n" + "Say 'exit' if it is \nOr say 'no'  "



		FrameFin1 = Tk.Frame(root,bg = '#E6E61D')
		FrameFin1.place(relx = 0.05,rely = 0.05, relwidth = 0.9, relheight = 0.9)
		FrameFin = Tk.Frame(FrameFin1, bd = 2)
		FrameFin.place(relx = 0.05,rely = 0.05, relwidth = 0.9, relheight = 0.9)

		imgfin = Tk.PhotoImage(file=img)
		imagefin = Tk.Label(FrameFin,image =imgfin)
		Final = Tk.Label(FrameFin,text=fin, bg = '#E6E61D')
		imagefin.pack()
		Final.pack()
		root.update()

		synthesize_text(fin)

		playsound("output.mp3")

		main()

		rep = phrase

		if "exit" in rep or "yes" in rep:
			break

		if "exit" not in rep:
			# Program go back to start but without the wrong answer

			FrameFin1.destroy()
			root.update()

			ListQuestion = ["What color is your animal ?","What size is your animal ?","Where does your animal lives?"]
			ListQuestionSyntyp = ["ADJ","ADJ","NOUN"]
			
			Megacharacteristics = Data.split("\n")
			characteristics = []
			characteristicsstr = []
			index = 0
			for n in Megacharacteristics:
				if n == "End":
					break
				characteristics.append(n.split(";"))
				characteristicsstr.append(characteristics[index][0])
				index += 1

			Done = []


# If no animal matches the description ==> end the programm

	if len(characteristics)==0:
		
		Textfin = Tk.Label(text ="Your animal is not in the list")
		Textfin.pack()
		synthesize_text("Your animal is not in the list")
		playsound("output.mp3")
		root.update()
		time.sleep(5)
		break

		