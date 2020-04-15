import os
import random
from donnee.DATA import *
import string
from donnee.meilleurScore import *


def finDePartie():
	choix = choixLettre("Voulez-vous quittez la partie?", 'o', 'n')
	if choix == 'o':
		exit()
	
	

def choixNom():#nom du joueur
	"""On va faire choisir son pseudo au joueur.
	"""
	nom = ""
	
	while nom == "":
		nom = input("Quelle est votre pseudo : ")
		if len(nom) < 3:
			print("Entrez un nom de 3 caractères/chiffres minimum:")
			nom = ""
		if nom in MeilleurScore.keys():							#Le joueur a-t-il déjà un score d'enregistrer?
			print(nom, "éxiste déja, voulez vous l'écraser?")
			choix = choixLettre("oui/non", 'o', 'n')			#le joueur décide s'il veut écraser la sauvegarde.
			if choix == 'n':									#on relance le choix du pseudo
				nom = ""
				continue
			else:
				MeilleurScore[nom] = 0							#On efface l'ancienne valeur
				
	
			
	return nom
	
def tourJeu(ListeLettreTrouve, mot, chance):#les actions du tour
	"""A chaque tour, on affiche les lettre à trouver.
	on fait choisir une lettre.
	on compare et on vérifie les lettres trouvées dans le mot
	
	"""
	if affichage(mot, ListeLettreTrouve) > 0: 	#s'il reste des lettre à trouvées.
	
		lettre = choixLettre()
		if lettre in ListeLettreTrouve:			#si cette lettre est déjà renseigné,
			chance -= 1							#on enlève aussi une chance.
			ListeLettreTrouve.append('*')		#==>pour le comptage des points
		else:		
			ListeLettreTrouve.append(lettre)
			if lettre not in mot:
				chance -= 1
			
	else:
		chance = 0
			
	return chance
		
	
	
	
	

def choixMot():#mot aléatoire dans la liste
	"""cette fonction va choisir un mot au hasard dans une liste.
	Elle calcul le nombre de chance en fonction de la taille du mot.
	"""
	mot = liste[random.randrange(len(liste))]	#Une liste éxistante de mot.
#	if len(mot) > 8:							#choix du mot aléatoire dans la liste.
#		chance = 8								#Calcul du nombre de chance
#	elif len(mot) <= 4:
#		chance = 4
#	else:	
#		chance = len(mot) - 1
	chance = 8
	return mot, chance
	
def choixLettre(*val):#lettre choisi(pour le mot ou pour une question en oui/non)
	"""
	Renvoie le choix de l'utilisateur. soit une lettre de l'alphabet,
	soit l'un des choix proposé(minimum 2). Dans ce cas, le premier argument doit être le 
	message adressé au joueur.
	Sinon, écrire le message tout seul."""
	
	
	
	if len(val) < 2 or val == ():				#première boucle à effectué si aucun paramètre entré
		ListeAlpha = list(string.ascii_letters)	#le choix devra etre dans l'alphabet
#		ListeAlpha.extend(['é','è','à'])		Après la MAJ, les accents ne sont plus possibles.
		if len(val) == 1:
			print(val[0])						#si message à afficher
		chx = ""
		while chx == "":						#boucle tant que choix insatisfaisant
			chx = input("Entrez une lettre :")
			if chx not in ListeAlpha:
				print("Vous devez entrer une lettre!")
				chx = ""
	else:										#deuxième pour que le choix correspondent
		chx = ""								#aux paramètres entrés.
		print(val[0])
		val = list(val)
		del val[0]
		while chx == "":
			print("/".join(val))
			chx = input()
			chx = chx.lower()
			print()
			if chx not in val:
				print("\nvous devez choisir", " ou ".join(val))
				chx = ""
	
	
	return chx.lower()
	
	
def affichage(mot, ListeLettreTrouve):#affichage des lettres trouvées et inconnues
	"""fonction affichant les lettres trouvé et * pour les lettres inconnues
	Renvoie le nombre de caractère encore inconnu.
	"""
	inconnu = 0							#nombre de caractère inconnu
	for lettre in mot:					#on parcourt les lettres du mot à trouver.
		if lettre in ListeLettreTrouve:	#si une lettre correspond dans la liste de lettre entrée par le joueur, on l'affiche.
			print(lettre, end='')
		else:							#sinon on affiche une étoile.
			print('*', end='')
			inconnu += 1
	
	
	print()
	return inconnu
	
	
def scoreJoueur(mot, ListeLettreTrouve, nomJoueur):#sauvegarde du score du joueur
	"""Cette fonction va calculé le score du joueur.
	le score est sauvegardé dans un dictionnaire MeilleurScore"""
	i = 0
	pts = 0
	for lettre in mot:
		if lettre in ListeLettreTrouve:	#+10 points par lettres trouvées.
			pts += 10
			i += 1						#i est le nombre de lettre trouvées.
		
			
			
	
			
	if i == len(mot) :					#si toutes les lettres ont été trouvées +50 pour griffondor
		pts += 50
		for lettre in ListeLettreTrouve:#on enlève tout de même 5 pts par mauvaises lettres
			if lettre not in mot:
				pts -= 5
	
	else:
		print("le mot était", mot)
		pts = 0
	
	
	MeilleurScore[nomJoueur] = pts
	
	sauvegardeScore()
	
	
	print("vous avez", pts, "points")
	
	#remise à zéro:
	ListeLettreTrouve.clear()    	

		
		
def afficherMeilleurScore():#Afficher si besoin les meilleurs scores.
	print("Meilleur Score : ")
	for score in MeilleurScore.items():
		print(str(score[0]).center(35), ':', score[1])
		
		


if __name__ == "__main__":
	#mot, chance = choixMot()
	#print(mot, chance)
	
	#print(choixLettre())
	#print(choixLettre('sauce aux pistout?', 'o', 'n'))
	
	#print(choixNom())
	
	#print(affichage("travail", "tvelppr"))
	print(MeilleurScore)
	#print(choixNom())
	
	
	os.system("pause")
