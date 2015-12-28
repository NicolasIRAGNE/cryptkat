#----------------------------------------------------------------------------------------------------------------------------------
#IMPORTATIONS DES DIFFERENTS MODULES UTILISES
from winsound import Beep
from time import sleep
from tkinter import *
#----------------------------------------------------------------------------------------------------------------------------------


def ti(x): #Un ti correspond à un son court, de fréquence 800 Hz, avec 100 ms de durée
    for i in range (0,x):
        Beep(800, 75)

def ta(x):
    for i in range (0,x): #Un ta correspond à un son court, de fréquence 800 Hz, avec 300 ms de durée
        Beep(800, 250)

def morseAudio(lettre):
    for i in range(0, len(str(lettre))):
        if lettre[i] == ".":
            ti(1)
            sleep(0.04)
        elif lettre[i] == "-":
            ta(1)
            sleep(0.04)
        else:
            pass
    sleep(0.16)


def morseEcrit(lettre): #Cette fonction retourne la transcription en morse d'une lettre.
    if lettre == " ":
        return "/"
    elif lettre == "a" or lettre =="à":
        return ".-"
    elif lettre == "b":
        return "-..."
    elif lettre == "c" or lettre =="ç":
        return "-.-."
    elif lettre == "d":
        return "-.."
    elif lettre == "e" or lettre == "é" or lettre =="è" or lettre =="ê":
        return "."
    elif lettre == "f":
        return "..-."
    elif lettre == "g":
        return "--."
    elif lettre == "h":
        return "...."
    elif lettre =="i":
        return ".."
    elif lettre == "j":
        return ".---"
    elif lettre == "k":
        return "-.-"
    elif lettre == "l":
        return ".-.."
    elif lettre == 'm':
        return "--"
    elif lettre == "n":
        return "-."
    elif lettre == "o" or lettre == "ô":
        return "---"
    elif lettre == "p":
        return ".--."
    elif lettre =="q":
        return "--.-"
    elif lettre =='r':
        return ".-."
    elif lettre =="s":
        return "..."
    elif lettre =="t":
        return "-"
    elif lettre =='u':
        return "..-"
    elif lettre == "v":
        return "...-"
    elif lettre == 'w':
        return ".--"
    elif lettre == "x":
        return "-..-"
    elif lettre == "y":
        return "-.--"
    elif lettre == "z":
        return "--.."
    elif lettre == "1":
        return ".----"
    elif lettre == "2":
        return "..---"
    elif lettre =="3":
        return "...--"
    elif lettre =="4":
        return "....-"
    elif lettre == "5":
        return "....."
    elif lettre == "6":
        return "-...."
    elif lettre == "7":
        return "--..."
    elif lettre == "8":
        return "---.."
    elif lettre =="9":
        return "----."
    elif lettre == "0":
        return "-----"
    elif lettre == ".-":
        return "a"
    elif lettre == "-...":
        return "b"
    elif lettre == "-.-.":
        return "c"
    elif lettre == "-..":
        return "d"
    elif lettre == ".":
        return "e"
    elif lettre == "..-.":
        return "f"
    elif lettre == "--.":
        return "g"
    elif lettre == "....":
        return "h"
    elif lettre == "..":
        return "i"
    elif lettre == ".---":
        return "j"
    elif lettre == "-.-":
        return "k"
    elif lettre == ".-..":
        return "l"
    elif lettre == "--":
        return "m"
    elif lettre == "-.":
        return "n"
    elif lettre == "---":
        return "o"
    elif lettre == ".--.":
        return "p"
    elif lettre == "--.-":
        return "q"
    elif lettre == ".-.":
        return "r"
    elif lettre == "...":
        return "s"
    elif lettre == "-":
        return "t"
    elif lettre == "..-":
        return "u"
    elif lettre == "...-":
        return "v"
    elif lettre == ".--":
        return "w"
    elif lettre == "-..-":
        return "x"
    elif lettre == "-.--":
        return "y"
    elif lettre == "--..":
        return "z"
    else:
        return(lettre)





def crypter(messageClair): #Cette fonction permet de traduire un message en morse écrit
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
        try:
            morseAudio(morseEcrit(messageClair[i]))
        except:
            pass

def decrypter(messageCrypte):
    message = str()
    messageCrypte = messageCrypte.split(" ")
    for i in range(0, len(messageCrypte)):
        if messageCrypte[i] == "/":
            message+=str(" ")
        else:
            message+=str(morseEcrit(messageCrypte[i]))
    return(message)

