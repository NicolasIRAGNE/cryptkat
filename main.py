﻿#----------------------------------------------------------------------------------------------------------------------------------
#IMPORTATIONS DES DIFFERENTS MODULES UTILISES
from tkinter import *
from interface.fenetre import fen
from interface.icones import *
from fonctions.conversion import *
from fonctions.atbash import *
from fonctions.rot import *
from interface.boutons import *
from fonctions.verification import *
from winsound import Beep
from time import sleep
import fonctions.morse
import fonctions.vigenere
from interface.initialisation import initialiser
#----------------------------------------------------------------------------------------------------------------------------------

#log 2.9
#reorganisé tout le bazar

#log 3.0
#bon c'est cool y'a la bruteforce maintenant c'est rigolo, mais c'est vraiment super super moche, et j'aime pas ça

#log 3.1
#c'est moins moche, c'est cool

#log 3.2
#nouvelle icone thx antoine

#log 3.3
#clé vigenere moins buggée

#log 3.4
#youhouu decryptage morse par contre C BUGG2§§§§§§

#----------------------------------------------------------------------------------------------------------------------------------
#INITIALISATION DE LA FENETRE
initialiser()
#----------------------------------------------------------------------------------------------------------------------------------
