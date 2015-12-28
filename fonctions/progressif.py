from fonctions.conversion import *

def cesarProgressif(messageClair, rotation):
	message = ""
	i=0
	for i in range(0,len(messageClair)):
		if rotation<0:
			rotation = -rotation
			if messageClair[i] == " ":
				rotation += 1
				message+=str(messageClair[i])
			elif messageClair[i].isalpha() == False:
				message+=str(messageClair[i])
				i+=1
			else:
				messageCrypte = conversion(messageClair[i]) - rotation
				messageCrypte = conversion(messageCrypte)
				message += str(messageCrypte)
		else:
			if messageClair[i] == " ":
				rotation+=1
				message+=str(messageClair[i])
			elif messageClair[i].isalpha() == False:
				message+=str(messageClair[i])
			else:
				messageCrypte = conversion(messageClair[i]) + rotation
				messageCrypte = conversion(messageCrypte)
				message += str(messageCrypte)
	return(message)