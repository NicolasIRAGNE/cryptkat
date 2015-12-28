# Créé par Nicolas, le 04/12/2015 en Python 3.2
from fonctions.conversion import *

def effectuerRotation(messageClair, rotation):
    message =""
    i = 0
    for i in range(0, len(messageClair)):
        if messageClair[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
            message += str(messageClair[i])
            i = i +1
        else:
            messageCrypte = conversion(messageClair[i]) + rotation
            messageCrypte = conversion(messageCrypte)
            message += str(messageCrypte)
    return(message)




