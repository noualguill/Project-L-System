from turtle import *
import re
import sys
from random import *

############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne l'axiome du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve l'axiome dans le fichier puis découpe la chaine juste pour récupérer l'axiome compris entre les guillemets

def AXIOME(text):
	chaine_axiome="axiome"
	line=""
	axiome="Veuillez entrer un Axiome dAns le fichier"
	for i in text:
		if (chaine_axiome in i):
			line=i
			ligne_pos_axiome=line.find("\"")
			ligne_pos__axiome_fin=line.rfind("\"")
			axiome=line[ligne_pos_axiome+1:ligne_pos__axiome_fin]	
	return(axiome)


############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne la valeur de la règle a du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve a= dans le fichier puis découpe la chaine juste pour récupérer la valeur de la règle a , en cas d'abscence de regle a dans le fichier , la valeur de la regle a prend par défaut ""

def REGLE_A(text):
	chaine_regle_a="a="
	stock=[]
	liste_regle_a=[]
	liste_regle_a_final=[]

	for i in text:
		if (chaine_regle_a in i):
			line=i
			liste_regle_a.append(line)

	for j in range(0,len(liste_regle_a)):
		ligne_pos_a=liste_regle_a[j].find("=")
		ligne_pos__a_fin=liste_regle_a[j].rfind("\"")
		stock=liste_regle_a[j][ligne_pos_a+1:ligne_pos__a_fin]
		liste_regle_a_final.append(stock)
	return(liste_regle_a_final)
		

############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne la valeur de la règle b du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve b= dans le fichier puis découpe la chaine juste pour récupérer la valeur de la règle b , en cas d'abscence de regle b dans le fichier, la valeur de la regle b prend par défaut ""

def REGLE_B(text):
	chaine_regle_b="b="
	stock=[]
	liste_regle_b=[]
	liste_regle_b_final=[]

	for i in text:
		if (chaine_regle_b in i):
			line=i
			liste_regle_b.append(line)

	for j in range(0,len(liste_regle_b)):
		ligne_pos_b=liste_regle_b[j].find("=")
		ligne_pos__b_fin=liste_regle_b[j].rfind("\"")
		stock=liste_regle_b[j][ligne_pos_b+1:ligne_pos__b_fin]
		liste_regle_b_final.append(stock)

	return(liste_regle_b_final)
	

############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne la valeur de l'angle du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve l'angle dans le fichier puis découpe la chaine juste pour récupérer la valeur de l'angle , en cas d'abscence d'angle dans le fichier , la valeur de l'angle prend par défaut ""

def ANGLE(text): 
	chaine_angle ="angle"
	line=""
	angle=""
	for i in text:
		if (chaine_angle in i):
			line=i
			ligne_pos_angle=line.find("=")
			angle=line[ligne_pos_angle+1:-1]
			angle=float(angle)
	return(angle)


############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne la valeur de la taille du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve la taille dans le fichier puis découpe la chaine juste pour récupérer la valeur de la taille , en cas d'abscence de taille dans le fichier , la valeur de la taille prend par défaut 3

def TAILLE(text): 
	chaine_taille ="taille"
	line=""
	taille=3 # taille par défaut si aucune n'a été enregistrée dans le fichier
	for i in text:
		if (chaine_taille in i):
			line=i
			ligne_pos_taille=line.find("=")
			taille=line[ligne_pos_taille+1:-1]
			taille=float(taille)
	return(taille)


############################################################
# Fonction qui parcourt le fichier d'entrée
# Elle retourne la valeur du niveau du fichier
# Cette fonction récupère tout d'abord la ligne où se trouve le niveau dans le fichier puis découpe la chaine juste pour récupérer la valeur du niveau

def NIVEAU(text):
	chaine_niveau ="niveau"
	line=""
	niveau=""
	for i in text:
		if(chaine_niveau in i):
			line=i
			ligne_pos_niveau=line.find("=")
			niveau=line[ligne_pos_niveau+1:-1]
			niveau=int(niveau)
	return(niveau)
	
############################################################
# Elle retourne la valeur de l'axiome après les changements d'une ou plusieurs regles en fonction de l'application des niveaux
# Cette fonction remplace soit un a ou un b par la ou les regles extraites du fichier si la regle a est égale "" on remplace a par du " " par exemple

def REMPLACE(text):
	liste_regle_a_final=REGLE_A(text)
	liste_regle_b_final=REGLE_B(text)
	axiome_stock=axiome
	"""if liste_regle_a_final=="":
		a=""
	else:
		a="a"
	if liste_regle_b_final=="":
		b=""
	else:
		b="b"""
	if len(liste_regle_a_final)>len(liste_regle_b_final):
		longeur_regle=len(liste_regle_a_final)
		while len(liste_regle_b_final)!=len(liste_regle_a_final):
			liste_regle_b_final.append("")	
	else:
		longeur_regle=len(liste_regle_b_final)
		while len(liste_regle_a_final)!=len(liste_regle_b_final):
			liste_regle_a_final.append("")
	if liste_regle_a_final==liste_regle_b_final:
		longeur_regle=len(liste_regle_a_final)
	if niveau>=1:
		for i in range(0,niveau):
			for j in range(0,longeur_regle):
				if (liste_regle_a_final[j]==""):
					a=""
				else:
					a="a"
				if (liste_regle_b_final[j]==""):
					b=""
				else:
					b="b"
				axiome_final=axiome_stock.replace(a,liste_regle_a_final[j]).replace(b,liste_regle_b_final[j])
				axiome_stock=axiome_final
	if niveau==0:
		axiome_final=axiome
	return(axiome_final)


############################################################
# Elle retourne la valeur de la règle a du fichier
# Cette fonction permet d'ecrire dans un fichier externe grâce au module turtle , en parcourant l'axiome final .Si un caractere lu correspond à un caractere pre-defini , il écrit dans le fichier externe a correspondance

def ANIMATION():
	fichier = open(fichier_sortie, "w") #Ouvre le fichier animation.py en mode écriture.
	fichier.write("from turtle import *\n") #Importe le module turtle.
	N=COLOR()
	F=COLOR()
	axiome_final=final
	longueur= len(axiome_final) 
	fichier.write('PositionInit=[]\nAngleInit=[]\n')
	for i in range(0,longueur): #
		if axiome_final[i]=="a":
			fichier.write('pd();fd('+str(taille)+');\n')
		if axiome_final[i]=="b":
			fichier.write('pu();fd('+str(taille)+');\n')
		if axiome_final[i]=="+":
			fichier.write('right('+str(angle)+');\n')
		if axiome_final[i]=="-":
			fichier.write('left('+str(angle)+');\n')
		if axiome_final[i]=="*":
			fichier.write('right('+str(180)+');\n')
		if axiome_final[i]=="[":
			fichier.write('PositionInit.append(pos());\nAngleInit.append(heading());\n')
		if axiome_final[i]=="]":
			fichier.write('up();goto(PositionInit.pop());\nseth(AngleInit.pop());pd()\n')
######################### Caractère bonus #########################
		if axiome_final[i]=="N": # change la couleur du traçage en une couleur au hasard comprise dans une liste de couleur à la place de noir , qui est la couleur de base
			fichier.write("color("+N+")\n")
		if axiome_final[i]=="F":
			fichier.write("bgcolor("+F+")\n")
		if axiome_final[i]==">":# augmente la vitesse du traçage
			fichier.write("speed(\"fastest\")\n")
		if axiome_final[i]=="E":#augmente l'epaisseur du trait
			fichier.write("width(5)\n")
		if axiome_final[i]=="!": # change la taille du curseur en taille 10
			fichier.write("shapesize(outline=10)\n")	
	fichier.write('exitonclick();')
	fichier.close()

############################################################
# Fonction qui permet de choisir au hasard une couleur parmi la liste pre-definie pour le tracage de l'animation

def COLOR():
	liste_color=["\"red\"","\"brown\"","\"yellow\"","\"black\"","\"blue\"","\"green\"","\"pink\"","\"orange\"",]
	stock_random=choice(liste_color)
	return(stock_random)


############################################################

if __name__=='__main__':
	liste_arg=[]    # bloc de ligne de commande , permet de définir comment lancer les lignes de commande en suivant un modele precis 
	for arg in sys.argv:
		liste_arg.append(arg)
	if len(liste_arg)==5:
		if (liste_arg[1]=="-i") and(liste_arg[3]=="-o"):
			fichier_entree=liste_arg[2]
			fichier_sortie=liste_arg[4]
		else:
			print("Veuillez relancer le programme en écrivant comme tel par exemple et en respectant l'ordre des arguments : python3 init.py -i fichier.txt -o animation.py ")
			sys.exit(1)
	else:
		fichier_entree=input("Entrer le nom du fichier d'entrée que vous souhaitez en mettant bien l'extension .txt à la fin (exemple:fichier.txt) : ")
		fichier_sortie=input("Entrer le nom du fichier généré que vous souhaitez en mettant bien l'extension .py à la fin (exemple:animation.py) : ")
	try:
		monFichier=fichier_entree
		f=open(monFichier, "r")
		text=f.readlines()
		axiome=AXIOME(text)
		regle_a=REGLE_A(text)
		regle_b=REGLE_B(text)
		angle=ANGLE(text)
		taille=TAILLE(text)
		niveau=NIVEAU(text)
		final=REMPLACE(text)
		ANIMATION()
		f.close()
	except (IOError):
		print("Erreur, mauvaise extension du fichier ou fichier ne correspond pas au modèle.")


