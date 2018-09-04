import csv
import os.path



def fiche_joueur():
	joueur_pseudo = input("Entrez votre pseudo : ") 
	fname = "crash.csv"
	
	if len(joueur_pseudo)<4:
		print("Ce pseudo est invalide, il doit contenir au moins 4 caractères")
		return fiche_joueur()
	
	else:
		if os.path.exists(fname)!=True:
			
			dico_pseudo = open(fname, "w", newline='' ) 
			writer = csv.writer(dico_pseudo)
			writer.writerow( ['Pseudo'] )
			writer.writerow([joueur_pseudo])	
			print("Vous êtes le premier à ouvrir ce jeu", joueur_pseudo)
			
			dico_score = open(joueur_pseudo+".csv", "w", newline='' ) 
			writer = csv.writer(dico_score)
			writer.writerow( ['Score'] )
			writer.writerow( [0] )
		
		else:
			dico_pseudo = open(fname,"r",newline='' ).read()
			
			if joueur_pseudo in dico_pseudo:
				print("Joueur existant")
				
				dico_score = open(joueur_pseudo+".csv", "r", newline='' ) 
				file_lines = dico_score.readlines()
				last_line = file_lines [len(file_lines)-1] 
							
				print("Bonjour {}, votre dernier score est de {}.".format(joueur_pseudo, last_line))
										
			else:
				dico_pseudo = open(fname, "a",newline='' ) 
				writer = csv.writer(dico_pseudo)
				writer.writerow([joueur_pseudo])
				
				dico_score = open(joueur_pseudo+".csv", "w", newline='' ) 
				writer = csv.writer(dico_score)
				writer.writerow( ['Score'] )
				writer.writerow( [0] )
				print("Bienvenu", joueur_pseudo)
	return joueur_pseudo
	

		
def quizz1():
	
	Q10 = "Question 1 - Quel est la couleur du cheval blanc d'Henri IV"
	R11 = "1 - Noir"
	R12 = "2 - Gris"
	R13 = "3 - Blanc"
	R14 = "4 - Caramel"
	print(Q10, "\n", R11, "\n", R12, "\n", R13, "\n", R14, "\n")

	reponse_joueur_Q10=input("Entrez le chiffre de votre réponse : ")
	score_joueur_1 = 0
	
	if reponse_joueur_Q10 != "1" and reponse_joueur_Q10 != "2" and reponse_joueur_Q10 != "3" and reponse_joueur_Q10 != "4":
			print("Ceci n'est pas une réponse"+"\n")
			return quizz1()
	else:
		if reponse_joueur_Q10 == "3":
			score_joueur_1+=1
			return score_joueur_1
		else:
			score_joueur_1 = 0
			return score_joueur_1
				
def quizz2():
			
	Q20 = "Question 2 - Quel est le prenom d'Henri IV"
	R21 = "1 - Henri"
	R22 = "2 - Licorne"
	R23 = "3 - Blanc"
	R24 = "4 - Phillipe"
	print("\n", Q20, "\n", R21, "\n", R22, "\n", R23, "\n", R24, "\n")

	reponse_joueur_Q20=input("Entrez le chiffre de votre réponse : ")
	score_joueur_2 = 0
	
	
	if reponse_joueur_Q20 != "1" and reponse_joueur_Q20 != "2" and reponse_joueur_Q20 != "3" and reponse_joueur_Q20 != "4":
			print("Ceci n'est pas une réponse"+"\n")
			return quizz2()
	else:
		if reponse_joueur_Q20 == "1":
			score_joueur_2+=1
			return score_joueur_2
		else:
			score_joueur_2 = 0
			return score_joueur_2		
				
	
joueur = fiche_joueur()
score = quizz1()+quizz2()


print("Votre score est de ", score,"/2")
	
dico_score = open(joueur+".csv", "a", newline='' ) 
writer = csv.writer(dico_score)
writer.writerow([score])
