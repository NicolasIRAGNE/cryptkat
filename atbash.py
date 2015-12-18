# Créé par Nicolas, le 07/12/2015 en Python 3.2

#Le chiffrement atbash consite à inverser l'alphabet; a devient ainsi z, b devient y et ainsi de suite.
def atbash(lettre):
    if lettre == "a" or lettre == "à":
        return "z"
    if lettre == "b":
        return "y"
    if lettre == "c" or lettre == "ç":
        return "x"
    if lettre == "d":
        return "w"
    if lettre == "e" or lettre == "é" or lettre == "è" or lettre == "ê":
        return "v"
    if lettre == "f":
        return "u"
    if lettre == "g":
        return "t"
    if lettre == "h":
        return "s"
    if lettre == "i":
        return "r"
    if lettre == "j":
        return "q"
    if lettre == "k":
        return "p"
    if lettre == "l":
        return "o"
    if lettre == "m":
        return "n"
    if lettre == "n":
        return "m"
    if lettre == "o":
        return "l"
    if lettre == "p":
        return "k"
    if lettre == "q":
        return "j"
    if lettre == "r":
        return "i"
    if lettre == "s":
        return "h"
    if lettre == "t":
        return "g"
    if lettre == "u" or lettre  == "ù":
        return "f"
    if lettre == "v":
        return"e"
    if lettre == "w":
        return "d"
    if lettre == "x":
        return "c"
    if lettre == "y":
        return "b"
    if lettre == "z":
        return "a"

def miroir(messageClair):
    message =""
    i = 0
    for i in range(0, len(messageClair)):
        if messageClair[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
                message += str(messageClair[i])
        else:
            message+=str(atbash(messageClair[i]))
    return(message)


