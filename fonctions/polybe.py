from tkinter import *
from tkinter.scrolledtext import ScrolledText
from random import *



def initPolybe():
	fenPolybe = Toplevel()
	fenPolybe.resizable(0,0)
	fenPolybe.title("Carré de Polybe")
	mainA = Entry(fenPolybe,width=5, background = "yellow")
	mainB = Entry(fenPolybe,width=5, background = "yellow")
	mainC = Entry(fenPolybe,width=5, background = "yellow")
	mainD = Entry(fenPolybe,width=5, background = "yellow")
	mainE = Entry(fenPolybe,width=5, background = "yellow")
	main1 = Entry(fenPolybe,width=5, background = "yellow")
	main2 = Entry(fenPolybe,width=5, background = "yellow")
	main3 = Entry(fenPolybe,width=5, background = "yellow")
	main4 = Entry(fenPolybe,width=5, background = "yellow")
	main5 = Entry(fenPolybe,width=5, background = "yellow")
	A1 = Entry(fenPolybe,width=5)
	A2 = Entry(fenPolybe,width=5)
	A3 = Entry(fenPolybe,width=5)
	A4 = Entry(fenPolybe,width=5)
	A5 = Entry(fenPolybe,width=5)
	B1 = Entry(fenPolybe,width=5)
	B2 = Entry(fenPolybe,width=5)
	B3 = Entry(fenPolybe,width=5)
	B4 = Entry(fenPolybe,width=5)
	B5 = Entry(fenPolybe,width=5)
	C1 = Entry(fenPolybe,width=5)
	C2 = Entry(fenPolybe,width=5)
	C3 = Entry(fenPolybe,width=5)
	C4 = Entry(fenPolybe,width=5)
	C5 = Entry(fenPolybe,width=5)
	D1 = Entry(fenPolybe,width=5)
	D2 = Entry(fenPolybe,width=5)
	D3 = Entry(fenPolybe,width=5)
	D4 = Entry(fenPolybe,width=5)
	D5 = Entry(fenPolybe,width=5)
	E1 = Entry(fenPolybe,width=5)
	E2 = Entry(fenPolybe,width=5)
	E3 = Entry(fenPolybe,width=5)
	E4 = Entry(fenPolybe,width=5)
	E5 = Entry(fenPolybe,width=5)

	mainA.grid(column= 0,row =1 )
	mainB.grid(column= 0,row =2 )
	mainC.grid(column= 0,row =3 )
	mainD.grid(column= 0,row =4 )
	mainE.grid(column= 0,row =5 )
	main1.grid(column= 1,row =0,sticky = W  )
	main2.grid(column= 2,row =0,sticky = W  )
	main3.grid(column= 3,row =0,sticky = W  )
	main4.grid(column= 4,row =0,sticky = W  )
	main5.grid(column= 5,row =0,sticky = W  )
	
	A1.grid(column=1 ,row =1,sticky = W )
	A2.grid(column=2 ,row =1,sticky = W )
	A3.grid(column=3 ,row =1,sticky = W )
	A4.grid(column=4 ,row =1,sticky = W )
	A5.grid(column=5 ,row =1,sticky = W )
	B1.grid(column=1 ,row =2,sticky = W )
	B2.grid(column=2 ,row =2,sticky = W )
	B3.grid(column=3 ,row =2,sticky = W )
	B4.grid(column=4 ,row =2,sticky = W )
	B5.grid(column=5 ,row = 2,sticky = W )
	C1.grid(column=1 ,row =3,sticky = W )
	C2.grid(column=2 ,row =3,sticky = W )
	C3.grid(column= 3,row =3 ,sticky = W )
	C4.grid(column= 4,row =3,sticky = W )
	C5.grid(column=5 ,row =3,sticky = W )
	D1.grid(column=1 ,row =4 ,sticky = W )
	D2.grid(column=2 ,row =4 ,sticky = W )
	D3.grid(column=3 ,row =4 ,sticky = W )
	D4.grid(column=4 ,row =4 ,sticky = W )
	D5.grid(column=5 ,row =4 ,sticky = W )
	E1.grid(column=1 ,row =5 ,sticky = W )
	E2.grid(column=2 ,row =5 ,sticky = W )
	E3.grid(column=3 ,row =5 ,sticky = W )
	E4.grid(column=4 ,row =5 ,sticky = W )
	E5.grid(column=5 ,row =5 ,sticky = W )

	main1.insert(0, "1")
	main2.insert(0, "2")
	main3.insert(0, "3")
	main4.insert(0, "4")
	main5.insert(0, "5")
	mainA.insert(0, "A")
	mainB.insert(0, "B")
	mainC.insert(0, "C")
	mainD.insert(0, "D")
	mainE.insert(0, "E")
	A1.insert(0, "A")
	A2.insert(0, "B")
	A3.insert(0, "C")
	A4.insert(0, "D")
	A5.insert(0, "E")
	B1.insert(0, "F")
	B2.insert(0, "G")
	B3.insert(0, "H")
	B4.insert(0, "I")
	B5.insert(0, "J")
	C1.insert(0, "K")
	C2.insert(0, "L")
	C3.insert(0, "M")
	C4.insert(0, "N")
	C5.insert(0, "O")
	D1.insert(0, "P")
	D2.insert(0, "Q")
	D3.insert(0, "R")
	D4.insert(0, "S")
	D5.insert(0, "T")
	E1.insert(0, "U")
	E2.insert(0, "V")
	E3.insert(0, "X")
	E4.insert(0, "Y")
	E5.insert(0, "Z")

	def melanger():
		cases = [A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, C1, C2, C3, C4, C5, D1, D2, D3, D4, D5, E1, E2, E3, E4, E5]
		shuffle(alphabet)
		for i in range(0, len(cases)):
			cases[i].delete(0, END)
			cases[i].insert(0, alphabet[i].upper())
	
	def getMainListPos(liste, x):
		i=0
		for y in liste:
			i+=1
			if y == x:
				return i
	
	def conversion(lettre):
		i=0
		for l in alphabet:
			i+=1
			if l == lettre:
				return i
	
	def conversion2(position):
		i=-1
		for l in alphabet:
			i=i+1
			if position == conversion(alphabet[i]):
				return alphabet[i]
		
	def crypter(pos):
		mainList = [main1.get(), main2.get(), main3.get(), main4.get(), main5.get()]
		if pos<=5:
			return(str(mainA.get()) + str(mainList[(pos%5)-1]))
		elif pos<=10:
			return(str(mainB.get()) + str(mainList[(pos%5)-1]))
		elif pos<=15:
			return(str(mainC.get()) + str(mainList[(pos%5)-1]))
		elif pos<=20:
			return(str(mainD.get()) + str(mainList[(pos%5)-1]))
		else:
			return(str(mainE.get()) + str(mainList[(pos%5)-1]))
	
	def crypter2(message):
		messageCrypte = ""
		i=0
		for i in range(0, len(message)):
			if message[i] not in alphabet:
				messageCrypte+=message[i]
			else:
				messageCrypte+=str(crypter(conversion(message[i])))
		return messageCrypte
	
	
	
	def fonction_bouton_crypter_polybe():
		resultatPolybe.delete("1.0", END)
		resultatPolybe.insert(END, crypter2(saisieMessagePolybe.get("1.0", END).lower()))
	
	def fonction_bouton_decrypter_polybe():
		resultatPolybe.delete("1.0", END)
		kendji = str(saisieMessagePolybe.get("1.0", END))
		kendji = kendji.strip()
		resultatPolybe.insert(END, decrypter2(kendji))
		#resultatPolybe.insert(END, decrypter2(str(saisieMessagePolybe.get("1.0", END))))
	
	def fonction_bouton_cle_down():
		alphabet = [A1.get().lower(), A2.get().lower(), A3.get().lower(), A4.get().lower(), A5.get().lower(), B1.get().lower(), B2.get().lower(), B3.get().lower(), B4.get().lower(), B5.get().lower(), C1.get().lower(), C2.get().lower(), C3.get().lower(), C4.get().lower(), C5.get().lower(), D1.get().lower(), D2.get().lower(), D3.get().lower(), D4.get().lower(), D5.get().lower(), E1.get().lower(), E2.get().lower(), E3.get().lower(), E4.get().lower(), E5.get().lower()]
		mainList = [str(main1.get()), str(main2.get()), str(main3.get()), str(main4.get()), str(main5.get())]
		mainList2 = [str(mainA.get()), str(mainB.get()), str(mainC.get()), str(mainD.get()), str(mainE.get())]
		champCle.delete(0, END)
		champCle.insert(0,"".join(mainList) + " " + "".join(mainList2) + " " + "".join(alphabet))
	
	def fonction_bouton_cle_up():
		casesABCDE = [mainA, mainB, mainC, mainD, mainE]
		cases12345 = [main1, main2, main3, main4, main5]
		cases = [A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, C1, C2, C3, C4, C5, D1, D2, D3, D4, D5, E1, E2, E3, E4, E5]
		cle = champCle.get()
		cle = cle.split(" ")
		print(cle)
		cle1 = cle[0]
		cle2 = cle[1]
		cle3 = cle[2]
		for i in range(0, 25):
			cases[i].delete(0, END)
			cases[i].insert(0, cle3[i].upper())
		for i in range(0, 5):
			cases12345[i].delete(0, END)
			cases12345[i].insert(0, cle1[i])
		for i in range(0, 5):
			casesABCDE[i].delete(0, END)
			casesABCDE[i].insert(0, cle2[i])
	
	def decrypter(messageCrypte):
		message = ""
		mainList = [main1.get(), main2.get(), main3.get(), main4.get(), main5.get()]
		mainList2 = [mainA.get(), mainB.get(), mainC.get(), mainD.get(), mainE.get()]
		for i in range(0,len(messageCrypte),2):
			pos = 0
			if messageCrypte[i] in mainList2:
				pos+=getMainListPos(mainList2,(messageCrypte[i]))*5-5
			else:
				pass
			if messageCrypte[i+1] in mainList:
				pos+=getMainListPos(mainList, messageCrypte[i+1])
			else: 
				pass
			message += conversion2(pos)
		return message
	
	def decrypter2(messageCrypte):
		messageCrypte = messageCrypte.split(" ")
		message = ""
		for i in range(0, len(messageCrypte)):
			message += decrypter(messageCrypte[i])
			message += " "
		return message
	
	
	boutonMelanger = Button(fenPolybe, width = 3, text = "Shuffle", command=melanger)
	boutonMelanger.grid( row = 8, column = 3)
	
	champCle = Entry(fenPolybe, width = 40) 
	champCle.grid(column = 0, row = 9, columnspan = 6)
	
	boutonCleUp = Button(fenPolybe, width = 3, text = "up", command = fonction_bouton_cle_up)
	boutonCleDown = Button(fenPolybe, width = 3, text = "down", command = fonction_bouton_cle_down)
	
	
	boutonCleUp.grid(row = 8, column = 1, columnspan = 1)
	boutonCleDown.grid(row = 8, column = 2, columnspan = 1)
	
	
	boutonCrypterPolybe = Button(fenPolybe, width = 15, text="Chiffrer", command = fonction_bouton_crypter_polybe)
	boutonDecrypterPolybe = Button(fenPolybe, width = 15, text = "Déchiffrer", command = fonction_bouton_decrypter_polybe)
	
	saisieMessagePolybe = ScrolledText(fenPolybe, width = 30, height = 3)
	resultatPolybe = ScrolledText(fenPolybe, width = 30, height = 3)
	
	
	labelMessage = Label(fenPolybe, text = "Message:")
	labelResultat = Label(fenPolybe, text = "Résultat:")
	
	saisieMessagePolybe.grid(column = 0, row=11, columnspan = 6)
	boutonCrypterPolybe.grid(column = 0, row = 12, columnspan = 3)
	boutonDecrypterPolybe.grid(column =2, row = 12, columnspan = 6)
	labelMessage.grid(column = 0, row = 10, columnspan = 6)
	labelResultat.grid(column = 0, row = 13, columnspan = 6)
	resultatPolybe.grid(column = 0, row = 14, columnspan=6)
	
	alphabet = [A1.get().lower(), A2.get().lower(), A3.get().lower(), A4.get().lower(), A5.get().lower(), B1.get().lower(), B2.get().lower(), B3.get().lower(), B4.get().lower(), B5.get().lower(), C1.get().lower(), C2.get().lower(), C3.get().lower(), C4.get().lower(), C5.get().lower(), D1.get().lower(), D2.get().lower(), D3.get().lower(), D4.get().lower(), D5.get().lower(), E1.get().lower(), E2.get().lower(), E3.get().lower(), E4.get().lower(), E5.get().lower()]
	mainList = [str(main1.get()), str(main2.get()), str(main3.get()), str(main4.get()), str(main5.get())]
	mainList2 = [str(mainA.get()), str(mainB.get()), str(mainC.get()), str(mainD.get()), str(mainE.get())]
	
	fonction_bouton_cle_down()	