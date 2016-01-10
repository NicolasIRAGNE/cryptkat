from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interface.fenetre import *
from interface.icones import *
from fonctions.conversion import *
from fonctions.atbash import *
from fonctions.rot import *
from fonctions.progressif import *
import fonctions.morse
import fonctions.vigenere
import fonctions.bruteforce
from fonctions.polybe import *

def fonction_bouton_vigenere_crypter():
    champResultat.delete("1.0", END)
    fonctions.vigenere.crypter(str(saisieMessage.get("1.0",END)).lower(), str(saisieCle.get()))
    champResultat.insert(END,fonctions.vigenere.crypter(str(saisieMessage.get("1.0",END)).lower(), str(saisieCle.get().lower())))

def fonction_bouton_vigenere_decrypter():
    champResultat.delete("1.0", END)
    champResultat.insert(END,fonctions.vigenere.decrypter(str(saisieMessage.get("1.0",END)).lower(), str(saisieCle.get().lower())))

def fonction_bouton_morse_crypter():
    champResultat.delete("1.0", END)
    champResultat.insert(END,fonctions.morse.crypter(saisieMessage.get("1.0",END).lower()))

def fonction_bouton_morse_decrypter():
    champResultat.delete("1.0", END)
    champResultat.insert(END, fonctions.morse.decrypter(saisieMessage.get("1.0",END).lower()))

def fonction_bouton_morse_audio():
    fonctions.morse.lire(fonctions.morse.decrypter(saisieMessage.get("1.0",END).lower()))
    #champResultat.delete("1.0", END)
    #champResultat.insert(0,fonctions.morse.crypter(saisieMessage.get().lower()))

def fonction_bouton_rotation():
    champResultat.delete("1.0", END)
    champResultat.insert(END,effectuerRotation(str(saisieMessage.get("1.0",END)).lower(), int(saisieRotation.get())%26))

def fonction_bouton_rotation_bruteforce():
    champResultat.delete("1.0", END)
    fonctions.bruteforce.rotation(str(saisieMessage.get("1.0",END).lower()))
    champResultat.insert(END, "Voir console !")

def fonction_bouton_miroir():
    champResultat.delete("1.0", END)
    champResultat.insert(END,(miroir(str(saisieMessage.get("1.0",END).lower()))))

def fonction_bouton_cesar_progressif():
    champResultat.delete("1.0", END)
    champResultat.insert(END,cesar(str(saisieMessage.get("1.0",END).lower()), int(saisieRotation.get())%26, int(champPas.get())))

def fonction_bouton_inverser_resultat():
    saisieMessage.delete("1.0", END)
    saisieMessage.insert(END, champResultat.get("1.0", END))

def ouvrir_polybe():
    initPolybe()


labelSaisieMessage = Label(fen, text="Entrez votre message ici.")
saisieMessage = ScrolledText(fen, width=40, height = 3)

labelSaisieCle = Label(fen, text="Entrez votre clé ici")
saisieCle = Entry(fen)

boutonCrypterVigenere = Button(fen,compound=LEFT,image=clerouge, text='Vigenere (Crypter)    ', width =150, command=fonction_bouton_vigenere_crypter)
boutonDecrypterVigenere = Button(fen,text='Vigenere (Decrypter)',compound=LEFT,image=cleverte, width =150, command=fonction_bouton_vigenere_decrypter)

boutonRotation = Button(fen,compound=LEFT,image=rotationImage, text="        Rotation              ", width = 150, command=fonction_bouton_rotation)
labelRotation = Label(fen, text="Rotation désirée:")
labelRotation2 = Label(fen, text="(nombre entier)")
saisieRotation = Entry(fen)

boutonRotationBruteforce = Button(fen,compound=LEFT,image=bruteforceImage, text="Bruteforce Rotation  ", width = 150, command=fonction_bouton_rotation_bruteforce)

boutonCesarProgressif = Button(fen, compound= LEFT, image=cesarImage, text = "Cesar progressif", width=150, command = fonction_bouton_cesar_progressif)
labelPas = Label(fen, text="Pas:")
champPas = Entry(fen)

boutonMiroir = Button(fen,compound=LEFT,image=miroirImage, text="   Miroir (Atbash)      ", width = 150, command=fonction_bouton_miroir)

boutonMorseCrypter = Button(fen, text="Morse (Crypter)",compound=LEFT,image=morseImage, width = 150, command=fonction_bouton_morse_crypter)
boutonMorseDecrypter = Button(fen, text="Morse (Decrypter)",compound=LEFT,image=morseImage2, width = 150, command=fonction_bouton_morse_decrypter)
boutonMorseAudio = Button(fen, image=sound, width = 50, command=fonction_bouton_morse_audio)

labelResultat = Label(fen, text="Résultat:")
champResultat = ScrolledText(fen, width=40, height = 3)

boutonInverserResultat = Button(fen, text="Inverser", width = 10, command = fonction_bouton_inverser_resultat )

boutonPolybe = Button(fen, text= "polybe", width =10, command = ouvrir_polybe)

boutonQuitter = Button(fen,text='Quitter',compound=LEFT,image=quitter, width =150, command=fen.destroy)