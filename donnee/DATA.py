import pickle
#import os


#Importation d'une liste de mot pour le pendu


#Création du fichier de mot
#with open("D:/bureau/programme Python/tp/ZEPendu/donnee/ListeMotPendu.txt", 'r') as fichier:
#	chaine = fichier.read()
#	liste = chaine.split('\n')

#with  open("D:/bureau/programme Python/tp/ZEPendu/donnee/ListeMot.flo", 'wb') as fichier:
#	monPickle = pickle.Pickler(fichier)
#	monPickle.dump(liste)

with open("F:/bureau/Python/tp/ZEPendu/donnee/ListeMot.flo", 'rb') as fichier:
	monPickle = pickle.Unpickler(fichier)
	liste = monPickle.load()


ListeLettreTrouve = list()

#print(chaine)
#print(liste)
#os.system("pause")

#def choixMot():
#	mot = liste[random.randrange(len(liste))]

#	return mot
