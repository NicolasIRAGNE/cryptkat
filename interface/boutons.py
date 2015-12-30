from tkinter import *
from interface.fenetre import *
from interface.icones import *
from fonctions.conversion import *
from fonctions.atbash import *
from fonctions.rot import *
from fonctions.progressif import *
import fonctions.morse
import fonctions.vigenere
import fonctions.bruteforce

def fonction_bouton_vigenere_crypter():
    champResultat.delete(0, END)
    fonctions.vigenere.crypter(str(saisieMessage.get()).lower(), str(saisieCle.get()))
    champResultat.insert(0,fonctions.vigenere.crypter(str(saisieMessage.get()).lower(), str(saisieCle.get().lower())))

def fonction_bouton_vigenere_decrypter():
    champResultat.delete(0, END)
    champResultat.insert(0,fonctions.vigenere.decrypter(str(saisieMessage.get()).lower(), str(saisieCle.get().lower())))

def fonction_bouton_morse_crypter():
    champResultat.delete(0, END)
    champResultat.insert(0,fonctions.morse.crypter(saisieMessage.get().lower()))

def fonction_bouton_morse_decrypter():
    champResultat.delete(0, END)
    champResultat.insert(0, fonctions.morse.decrypter(saisieMessage.get().lower()))

def fonction_bouton_morse_audio():
    fonctions.morse.lire(fonctions.morse.decrypter(saisieMessage.get().lower()))
    #champResultat.delete(0, END)
    #champResultat.insert(0,fonctions.morse.crypter(saisieMessage.get().lower()))

def fonction_bouton_rotation():
    champResultat.delete(0, END)
    champResultat.insert(0,effectuerRotation(str(saisieMessage.get()).lower(), int(saisieRotation.get())%26))

def fonction_bouton_rotation_bruteforce():
    champResultat.delete(0, END)
    fonctions.bruteforce.rotation(str(saisieMessage.get().lower()))
    champResultat.insert(0, "Voir console !")

def fonction_bouton_miroir():
    champResultat.delete(0, END)
    champResultat.insert(0,(miroir(str(saisieMessage.get().lower()))))

def fonction_bouton_cesar_progressif():
    champResultat.delete(0, END)
    champResultat.insert(0,cesar(str(saisieMessage.get().lower()), int(saisieRotation.get())%26, int(champPas.get())))



labelSaisieMessage = Label(fen, text="Entrez votre message ici.")
saisieMessage = Entry(fen, width=40)

labelSaisieCle = Label(fen, text="Entrez votre clÃ© ici")
saisieCle = Entry(fen)

boutonCrypterVigenere = Button(fen,compound=LEFT,image=clerouge, text='Vigenere (Crypter)    ', width =150, command=fonction_bouton_vigenere_crypter)
boutonDecrypterVigenere = Button(fen,text='Vigenere (Decrypter)',compound=LEFT,image=cleverte, width =150, command=fonction_bouton_vigenere_decrypter)

boutonRotation = Button(fen,compound=LEFT,image=rotationImage, text="        Rotation              ", width = 150, command=fonction_bouton_rotation)
labelRotation = Label(fen, text="Rotation dÃ©sirÃ©e:")
labelRotation2 = Label(fen, text="(nombre entier)")
saisieRotation = Entry(fen)

boutonRotationBruteforce = Button(fen,compound=LEFT,image=bruteforceImage, text="Bruteforce Rotation  ", width = 150, command=fonction_bouton_rotation_bruteforce)

boutonCesarProgressif = Button(fen, compound= LEFT, image=bruteforceImage, text = "Cesar progressif", width=150, command = fonction_bouton_cesar_progressif)
labelPas = Label(fen, text="Pas:")
champPas = Entry(fen)

boutonMiroir = Button(fen,compound=LEFT,image=miroirImage, text="   Miroir (Atbash)      ", width = 150, command=fonction_bouton_miroir)

boutonMorseCrypter = Button(fen, text="Morse (Crypter)",compound=LEFT,image=morseImage, width = 150, command=fonction_bouton_morse_crypter)
boutonMorseDecrypter = Button(fen, text="Morse (Decrypter)",compound=LEFT,image=morseImage2, width = 150, command=fonction_bouton_morse_decrypter)
boutonMorseAudio = Button(fen, image=sound, width = 50, command=fonction_bouton_morse_audio)

labelResultat = Label(fen, text="RÃ©sultat:")
champResultat = Entry(fen, width=40)

boutonQuitter = Button(fen,text='Quitter',compound=LEFT,image=quitter, width =150, command=fen.destroy)