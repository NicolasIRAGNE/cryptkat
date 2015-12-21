from tkinter import *
from interface.fenetre import *
from interface.icones import *
from fonctions.conversion import *
from fonctions.atbash import *
from fonctions.rot import *
import fonctions.morse
import fonctions.vigenere
import fonctions.bruteforce

def boutonVC():
    champResultat.delete(0, END)
    fonctions.vigenere.crypter(str(saisieMessage.get()).lower(), str(saisieCle.get()))
    champResultat.insert(0,fonctions.vigenere.crypter(str(saisieMessage.get()).lower(), str(saisieCle.get())))

def boutonVD():
    champResultat.delete(0, END)
    champResultat.insert(0,fonctions.vigenere.decrypter(str(saisieMessage.get()).lower(), str(saisieCle.get())))

def boutonMorse():
    champResultat.delete(0, END)
    champResultat.insert(0,fonctions.morse.traduire(saisieMessage.get().lower()))

def boutonMorseAudio():
    fonctions.morse.lire(saisieMessage.get().lower())
    champResultat.delete(0, END)
    champResultat.insert(0,fonctions.morse.traduire(saisieMessage.get().lower()))


def boutonRotation():
    champResultat.delete(0, END)
    champResultat.insert(0,effectuerRotation(str(saisieMessage.get()).lower(), int(saisieRotation.get())%26))

def fonctionRotationBruteforce():
    champResultat.delete(0, END)
    fonctions.bruteforce.rotation(str(saisieMessage.get().lower()))
    champResultat.insert(0, "Voir console !")

def boutonMiroir():
    champResultat.delete(0, END)
    champResultat.insert(0,(miroir(str(saisieMessage.get().lower()))))



labelSaisieMessage = Label(fen, text="Entrez votre message ici.")
saisieMessage = Entry(fen, width=40)

labelSaisieCle = Label(fen, text="Entrez votre clé ici")
saisieCle = Entry(fen)

boutonCrypterVigenere = Button(fen,compound=LEFT,image=clerouge, text='Crypter (Vigenere)', width =150, command=boutonVC)
boutonDecrypterVigenere = Button(fen,text='Décrypter (Vigenere)',compound=LEFT,image=cleverte, width =150, command=boutonVD)

boutonRotation = Button(fen,compound=LEFT,image=rotationImage, text="Rotation", width = 150, command=boutonRotation)
labelRotation = Label(fen, text="Rotation désirée:")
labelRotation2 = Label(fen, text="(nombre entier)")
saisieRotation = Entry(fen)

boutonRotationBruteforce = Button(fen,compound=LEFT,image=rotationImage, text="Bruteforce Rotation", width = 150, command=fonctionRotationBruteforce)

boutonMiroir = Button(fen,compound=LEFT,image=miroirImage, text="Miroir (Atbash)", width = 150, command=boutonMiroir)

boutonMorse = Button(fen, text="Morse",compound=LEFT,image=morseImage, width = 150, command=boutonMorse)
boutonMorseAudio = Button(fen, image=sound, width = 50, command=boutonMorseAudio)

labelResultat = Label(fen, text="Résultat:")
champResultat = Entry(fen, width=40)

boutonQuitter = Button(fen,text='Quitter',compound=LEFT,image=quitter, width =150, command=fen.destroy)