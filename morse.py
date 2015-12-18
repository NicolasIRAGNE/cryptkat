#----------------------------------------------------------------------------------------------------------------------------------
#IMPORTATIONS DES DIFFERENTS MODULES UTILISES
from winsound import Beep
from time import sleep
from tkinter import *
#----------------------------------------------------------------------------------------------------------------------------------

sam = 2
def ti(x): #Un ti correspond à un son court, de fréquence 800 Hz, avec 100 ms de durée
    for i in range (0,x):
        Beep(800, 100)

def ta(x):
    for i in range (0,x): #Un ta correspond à un son court, de fréquence 800 Hz, avec 300 ms de durée
        Beep(800, 300)

def morse(lettre): #Cette fonction permet d'émettre une séquence de sons pour chaque lettre. Il y a 0.1 sec d'attente entre chaque lettre, et 0.18 sec d'attente entre chaque mot.
    if lettre == " ": #Les ti sont marqués d'un ".", les ta d'un "-" et les espaces d'un "/"
        sleep(0.18)
    if lettre == "a" or lettre =="à":
        ti(1)
        ta(1)
        sleep(0.1)
    if lettre == "b":
        ta(1)
        ti(3)
        sleep(0.1)
    if lettre == "c" or lettre =="ç":
        ta(1)
        ti(1)
        ta(1)
        ti(1)
        sleep(0.1)
    if lettre == "d":
        ta(1)
        ti(2)
        sleep(0.1)
    if lettre == "e" or lettre == "é" or lettre =="è" or lettre =="ê":
        ti(1)
        sleep(0.1)
    if lettre == "f":
        ti(2)
        ta(1)
        ti(2)
        sleep(0.1)
    if lettre == "g":
        ta(2)
        ti(1)
        sleep(0.1)
    if lettre == "h":
        ti(4)
        sleep(0.1)
    if lettre =="i":
        ti(2)
        sleep(0.1)
    if lettre == "j":
        ti(1)
        ta(3)
        sleep(0.1)
    if lettre == "k":
        ta(1)
        ti(1)
        ta(1)
        sleep(0.1)
    if lettre == "l":
        ti(1)
        ta(1)
        ti(2)
        sleep(0.1)
    if lettre == 'm':
        ta(2)
        sleep(0.1)
    if lettre == "n":
        ta(1)
        ti(1)
        sleep(0.1)
    if lettre == "o" or lettre == "ô":
        ta(3)
        sleep(0.1)
    if lettre == "p":
        ti(1)
        ta(2)
        ti(1)
        sleep(0.1)
    if lettre =="q":
        ta(2)
        ti(1)
        ta(1)
        sleep(0.1)
    if lettre =='r':
        ti(1)
        ta(1)
        ti(1)
        sleep(0.1)
    if lettre =="s":
        ti(3)
        sleep(0.1)
    if lettre =="t":
        ta(1)
        sleep(0.1)
    if lettre =='u':
        ti(2)
        ta(1)
        sleep(0.1)
    if lettre == "v":
        ti(3)
        ta(1)
        sleep(0.1)
    if lettre == 'w':
        ti(1)
        ta(2)
        sleep(0.1)
    if lettre == "x":
        ta(1)
        ti(2)
        ta(1)
        sleep(0.1)
    if lettre == "y":
        ta(1)
        ti(1)
        ta(2)
        sleep(0.1)
    if lettre == "z":
        ta(2)
        ti(2)
        sleep(0.1)
    if lettre == "1":
        ti(1)
        ta(4)
        sleep(0.1)
    if lettre == "2":
        ti(2)
        ta(3)
        sleep(0.1)
    if lettre =="3":
        ti(3)
        ti(2)
        sleep(0.1)
    if lettre =="4":
        ti(4)
        ta(1)
        sleep(0.1)
    if lettre == "5":
        ti(5)
        sleep(0.1)
    if lettre == "6":
        ta(1)
        ti(4)
        sleep(0.1)
    if lettre == "7":
        ta(2)
        ti(3)
        sleep(0.1)
    if lettre == "8":
        ta(3)
        ti(2)
        sleep(0.1)
    if lettre =="9":
        ta(4)
        ti(1)
        sleep(0.1)
    if lettre == "0":
        ta(5)
        sleep(0.1)

def morseEcrit(lettre): #Cette fonction retourne la transcription en morse d'une lettre.
    if lettre == " ":
        return "/"
    if lettre == "a" or lettre =="à":
        return ".-"
    if lettre == "b":
        return "-..."
    if lettre == "c" or lettre =="ç":
        return "-.-."
    if lettre == "d":
        return "-.."
    if lettre == "e" or lettre == "é" or lettre =="è" or lettre =="ê":
        return "."
    if lettre == "f":
        return "..-."
    if lettre == "g":
        return "--."
    if lettre == "h":
        return "...."
    if lettre =="i":
        return ".."
    if lettre == "j":
        return ".---"
    if lettre == "k":
        return "-.-"
    if lettre == "l":
        return ".-.."
    if lettre == 'm':
        return "--"
    if lettre == "n":
        return "-."
    if lettre == "o" or lettre == "ô":
        return "---"
    if lettre == "p":
        return ".--."
    if lettre =="q":
        return "--.-"
    if lettre =='r':
        return ".-."
    if lettre =="s":
        return "..."
    if lettre =="t":
        return "-"
    if lettre =='u':
        return "..-"
    if lettre == "v":
        return "...-"
    if lettre == 'w':
        return ".--"
    if lettre == "x":
        return "-..-"
    if lettre == "y":
        return "-.--"
    if lettre == "z":
        return "--.."
    if lettre == "1":
        return ".----"
    if lettre == "2":
        return "..---"
    if lettre =="3":
        return "...--"
    if lettre =="4":
        return "....-"
    if lettre == "5":
        return "....."
    if lettre == "6":
        return "-...."
    if lettre == "7":
        return "--..."
    if lettre == "8":
        return "---.."
    if lettre =="9":
        return "----."
    if lettre == "0":
        return "-----"


def traduire(messageClair): #Cette fonction permet de traduire un message en morse écrit
    message = str()
    for i in range(0, len(messageClair)):
        if messageClair[i] == " ":
            message+=str("/ ")
        elif messageClair[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
            if messageClair[i] == "0" or messageClair[i] =="1" or messageClair[i] =="2" or messageClair[i] =="3" or messageClair[i] =="4" or messageClair[i] =="5" or messageClair[i] =="6" or messageClair[i] =="7" or messageClair[i] =="8" or messageClair[i] =="9":
                message += str(morseEcrit(messageClair[i])) + str(" ")
            else:
                message += messageClair[i]
        else:
            message+=str(morseEcrit(messageClair[i])) + str(" ")
    return(message)

def lire(messageClair): #Cette fonction permet de lire un message entier en code morse
    for i in range(0,len(messageClair)):
        if messageClair[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
            if messageClair[i] == "0" or messageClair[i] =="1" or messageClair[i] =="2" or messageClair[i] =="3" or messageClair[i] =="4" or messageClair[i] =="5" or messageClair[i] =="6" or messageClair[i] =="7" or messageClair[i] =="8" or messageClair[i] =="9":
                morse(messageClair[i])
            else:
                pass
        else:
            morse(messageClair[i])
