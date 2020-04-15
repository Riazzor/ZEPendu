#-*- coding : utf-8 -*-
import os
from fonctions import *


continuerPartie = 'o'
nom = ""
while nom == "":
	try :



		nom = choixNom()
	except KeyboardInterrupt:
		finDePartie()
		nom = ""


while continuerPartie != 'n':
	mot, chance = choixMot()

	try :
		while chance != 0:# tant qu'on a pas épuisé ces tentatives, on continue la partie
			chance = tourJeu(ListeLettreTrouve, mot, chance)

		affichage(mot, ListeLettreTrouve)

		scoreJoueur(mot, ListeLettreTrouve, nom)
		afficherMeilleurScore()
		continuerPartie = choixLettre("Voulez-vous continuer la partie?", 'o', 'n')
	except KeyboardInterrupt:
		finDePartie()
		continuerPartie = 'o'



os.system("pause")
