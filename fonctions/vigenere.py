# Créé par Nicolas, le 05/12/2015 en Python 3.2
from fonctions.conversion import *
from fonctions.verification import *

def crypter(messageClair,cleEntree):
        longueurMessage = len(messageClair)
        cle = verification(cleEntree)
        cle = cle.lower()
        longueurCle = len(cle)
        j = 0
        message = ""
        while longueurCle < longueurMessage:
                longueurCle = len(cle)
                cle = str(cle) + str(cle)

        for i in range(0,longueurMessage):
            if messageClair[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
                message += str(messageClair[i])
                i = i +1

            else:
                messageCrypte = conversion(messageClair[i]) + conversion(cle[j])

                messageCrypte = conversion(messageCrypte)
                message += str(messageCrypte)

                i = i + 1
                j = j + 1
        return(message)

def decrypter(messageCrypte,cleEntree):
        longueurMessage = len(messageCrypte)
        cle = verification(cleEntree)
        longueurCle = len(cle)
        j=0
        message = ""
        while longueurCle < longueurMessage:
            longueurCle = len(cle)
            cle = str(cle) + str(cle)

        for i in range(0,longueurMessage):
            if messageCrypte[i].isalpha() == False: #si caractère != lettre, le caractère est ajouté à la chaîne message
                message += str(messageCrypte[i])
                i = i +1
            else:
                messageClair = conversion(messageCrypte[i]) - conversion(cle[j])
                messageClair = conversion(messageClair)
                message += str(messageClair)

                i = i + 1
                j = j + 1
        return(message)