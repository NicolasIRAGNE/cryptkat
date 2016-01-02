from fonctions.conversion import *


def cesar(messageClair, rotation, pas):
	message = ""
	i=0
	for i in range(0,len(messageClair)):
			if messageClair[i] == " ":
				rotation+=int(pas)
				message+=str(messageClair[i])
			elif messageClair[i].isalpha() == False:
				message+=str(messageClair[i])
			else:
				messageCrypte = (conversion(messageClair[i]) + rotation)%26
				messageCrypte = conversion(messageCrypte)
				message += str(messageCrypte)
	return(message)