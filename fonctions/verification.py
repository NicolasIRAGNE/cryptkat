def verification(chaine):
    nouvelleChaine=""
    for i in range(0, len(chaine)):
        if chaine[i].isalpha() == False:
            pass
        else:
            nouvelleChaine += chaine[i]
    return nouvelleChaine