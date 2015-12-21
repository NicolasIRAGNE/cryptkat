from fonctions.conversion import *
def rotation(messageClair):
	print ("------------------------------------------------------")
	message =""
	i = 0
	for x in range(0,26):
		message =""
		for i in range(0,len(messageClair)):
			if messageClair[i].isalpha() == False:
				message += str(messageClair[i])
				i+=1
			else:
				messageCrypte = conversion(messageClair[i]) + x
				messageCrypte = conversion(messageCrypte)
				message += str(messageCrypte)
		if x<10:
			print(str(x) + ":" + "  " + str(message)) 
		else:
			print(str(x) + ":" + " " + str(message))
	print ("------------------------------------------------------")