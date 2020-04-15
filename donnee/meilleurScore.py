import pickle
import os

"""importer le dictionnaire contenant le meilleur score"""
try:
		with open("F:/bureau/Python/tp/ZEPendu/donnee/MeilleurScore.flo", 'rb') as fichier:
			lePickle = pickle.Unpickler(fichier)
			MeilleurScore = lePickle.load()
except FileNotFoundError:
	MeilleurScore = {}
	with open("F:/bureau/Python/tp/ZEPendu/donnee/MeilleurScore.flo", 'wb') as fichier:
		lePickle = pickle.Pickler(fichier)
		lePickle.dump(MeilleurScore)


def sauvegardeScore():
	with open("F:/bureau/Python/tp/ZEPendu/donnee/MeilleurScore.flo", 'wb') as fichier:
		monPickle = pickle.Pickler(fichier)
		monPickle.dump(MeilleurScore)

if __name__ == "__main__":
	print(MeilleurScore)
	os.system("pause")
