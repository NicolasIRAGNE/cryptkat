from tkinter import *
from random import choice
fen = Tk()
fen.title("PROJET 3.95")
fen.resizable(0,0)
messagesPossibles = [
"Bonjour !",
"Salut !",
"Hey !",
"Master of puppets I'm pulling your \nstrings",
"Ca fait 3 mois Antoine",
"Ceci est un message d'exemple",
"Coucou", "Les dataries feront l'affaire",
"Les framboises sont perchées sur le tabouret de mon grand père",
"C'est pas faux",
".... . -.-- ",
"Bonjour !",
"Long live Motörhead!",
"Yoooooo"
]
messageAccueil = choice(messagesPossibles)