# Créé par Nicolas, le 05/12/2015 en Python 3.2

def conversion(lettre): #Cette fonction assigne à chaque lettre de l'alphabet un nombre (a = 0 et z = 25) et à chaque nombre une lettre.
    if lettre == "a" or lettre == "à":
        return 0
    if lettre == "b":
        return 1
    if lettre == "c" or lettre == "ç":
        return 2
    if lettre == "d":
        return 3
    if lettre == "e" or lettre == "é" or lettre == "è" or lettre == "ê":
        return 4
    if lettre == "f":
        return 5
    if lettre == "g":
        return 6
    if lettre == "h":
        return 7
    if lettre == "i":
        return 8
    if lettre == "j":
        return 9
    if lettre == "k":
        return 10
    if lettre == "l":
        return 11
    if lettre == "m":
        return 12
    if lettre == "n":
        return 13
    if lettre == "o" or lettre == "ô" or lettre == "ö":
        return 14
    if lettre == "p":
        return 15
    if lettre == "q":
        return 16
    if lettre == "r":
        return 17
    if lettre == "s":
        return 18
    if lettre == "t":
        return 19
    if lettre == "u" or lettre  == "ù":
        return 20
    if lettre == "v":
        return 21
    if lettre == "w":
        return 22
    if lettre == "x":
        return 23
    if lettre == "y":
        return 24
    if lettre == "z":
        return 25
    if lettre > 25:
        lettre = lettre -26
    if lettre < 0:
        lettre = 26 + lettre
    if lettre == 0:
        return "a"
    if lettre == 1:
        return "b"
    if lettre == 2:
        return "c"
    if lettre == 3:
        return "d"
    if lettre == 4:
        return "e"
    if lettre == 5:
        return "f"
    if lettre == 6:
        return "g"
    if lettre == 7:
        return "h"
    if lettre == 8:
        return "i"
    if lettre == 9:
        return "j"
    if lettre == 10:
        return "k"
    if lettre == 11:
        return "l"
    if lettre == 12:
        return "m"
    if lettre == 13:
        return "n"
    if lettre == 14:
        return "o"
    if lettre == 15:
        return "p"
    if lettre == 16:
        return "q"
    if lettre == 17:
        return "r"
    if lettre == 18:
        return "s"
    if lettre == 19:
        return "t"
    if lettre == 20:
        return "u"
    if lettre == 21:
        return "v"
    if lettre == 22:
        return "w"
    if lettre == 23:
        return "x"
    if lettre == 24:
        return "y"
    if lettre == 25:
        return "z"
