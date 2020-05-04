# coding: utf-8
import time

def min_dist(a_traiter, dist):
 
	tmp = [float("inf")] * len(dist)
	for i in a_traiter:
		tmp[i] = dist[i]
	minimum = min(tmp)
	return tmp.index(minimum)
	
class Graphe:

	sommets = []
	aretes = []
	fichier = ""

	#'fichier' = fichier contenant les sommets et la pondération
	def __init__(self,fichier):
		self.sommets = []
		self.aretes = []
		self.fichier = fichier

	def init_aretes(self):
		f = open(self.fichier,"r")
		#chaine == "" : fin du fichier
		while(1):
			chaine = f.readline()
			if(chaine == ""):
				break
			if(chaine[0] == 'E'):
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("E ","")
				#On sépare la chaine grâce aux espaces
				arete = chaine.split(" ")
				#On ajoute [s1, s2, poid] à la liste des aretes
				(self.aretes).append(arete)
				#print chaine
		f.close()

	def init_sommets(self):
		f = open(self.fichier,"r")
		#chaine == "" -> fin du fichier
		while(1):
			chaine = f.readline()
			if(chaine == ""):
				break
			if(chaine[0] == 'V'):
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("V ","")
				#On sépare la chaine grâce aux espaces
				sommet = chaine.split(" ")
				(self.sommets).append(sommet)
				
		f.close()
		
	def init_graph(self):
		f = open(self.fichier,"r")

		for chaine in f:
			#Permet d'avoir les informations sur un sommet
			if chaine[0] == "V" :
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("V ","")
			
				#On sépare la chaine grâce aux espaces
				infoSommet = chaine.split(" ")
				
				#On ajoute [numSommet, numLigne, nom] à la liste des sommets
				(self.sommets).append(infoSommet)
			
			#Permet d'avoir les informations sur les aretes
			elif chaine[0] == "E" :
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("E ","")
			
				#On sépare la chaine grâce aux espaces
				arete = chaine.split(" ")
				
				#On ajoute [s1, s2, poid] à la liste des aretes
				(self.aretes).append(arete)

		f.close()


	def def_voisins(self, sommet):
		
		fichier = open(self.fichier,"r")
		voisins = []
		ligne = fichier.readline()
		while(ligne != ""):			#Fin du fichier
			ligne = ligne.replace("\n","")
			ligne = ligne.split(" ")
			#print "ligne[0] = " + ligne[0] + " ligne[1] = " + ligne[1] + " ligne[2] = " + ligne[2]
			if( (ligne[0] == "E") and (int(ligne[1]) == sommet) ):
				voisins.append(ligne[2])
			elif( (ligne[0] == "E") and (int(ligne[2]) == sommet) ):
				voisins.append(ligne[1])
			ligne = fichier.readline()
		
		fichier.close()
		return voisins
		
		
	def from_name_to_id(self, sommet):		### MODIFIE ###
		cmpt = 0
		identifiant = []
		#~ print sommet
		sommet = sommet.replace(" ","_")
		while (cmpt < len(self.sommets)) :
			if(sommet == self.sommets[cmpt][5]):
				while (sommet == self.sommets[cmpt][5]):
					identifiant.append( int(self.sommets[cmpt][0]) )
					print self.sommets[cmpt][5] + self.sommets[cmpt][3] + "... Check"
					cmpt = cmpt+1
				break						#On prend en compte toutes les lignes, et on évite de parcourir les reste de la liste
			cmpt = cmpt+1
		if(len(identifiant) == 0):
			print "Un problème est survenu dans la fonction 'from_name_to_id'..."
			exit()
		return identifiant
		
	def distance(self, en_cours, voisin):
		
		distance = -1
		fichier = open(self.fichier,"r")
		ligne = fichier.readline()
		while(ligne != ""):
			ligne = ligne.replace("\n","")
			ligne = ligne.split(" ")
			if(ligne[0] == "E" and int(ligne[1]) == en_cours and int(ligne[2]) == voisin):
				distance = int(ligne[3])
				break
			elif(ligne[0] == "E" and int(ligne[1]) == voisin and int(ligne[2]) == en_cours):
				distance = int(ligne[3])
				break
			ligne = fichier.readline()
		fichier.close()
		return distance

		
	def dijsktra(self, sommet1, sommet2):		### MODIFIE ###
		
		depart = self.from_name_to_id(sommet1)	#Correspond au numéro du sommet de départ
		arrive = self.from_name_to_id(sommet2)	#Correspond au numéro du sommet d'arrivé
		chemins = []
		
		for point_depart in depart:
			for point_arrive in arrive:
		
				### PHASE D'INITIALISATION ###
				predecesseur = [None] * (len(self.sommets))	
				a_traiter = []		
				dist = []	
				for s in range(len(self.sommets)):		#s prend la valeur de tous les sommets
					dist.append(float("inf"))
					a_traiter.append(s)
				dist[point_depart] = 0
				
				### PHASE DE RECHERCHE ###
				
				en_cours = -1
				while(a_traiter != []):
					
					en_cours = min_dist(a_traiter, dist)
					a_traiter.remove(en_cours)
					voisins = self.def_voisins(en_cours)
					
					for v in voisins:
						
						v = int(v)
						nouvelle_dist = dist[en_cours] + self.distance(en_cours, v)
						if(nouvelle_dist < dist[v]):
							dist[v] = nouvelle_dist
							predecesseur[v] = en_cours
							
				chemins.append( self.creer_chemin(predecesseur, point_depart, point_arrive) )
				
		#On cherche le chemin le plus court de tous ceux qu'on a obtenus
		chemin_plus_court = self.def_temps_chemins(chemins)
		#~ print str(chemins)
		
		return chemins[ chemin_plus_court ]
		

	def recherche(self, position):
		cmpt = 0
		position = position.replace(" ","_")
		while (cmpt < len(self.sommets)) :
			if (position == (self.sommets[cmpt][5])):
				print ("Le sommet {0} exite".format(position))
				return True
			cmpt = cmpt+1

		return False
		
	def cherche_num_ligne(self,num_sommet):		#Cherche le numéro de la ligne par rapport au numéro du sommet 
		cmpt = 0
		ligne = -1
		while (cmpt < len(self.sommets)) :
			if (num_sommet == int(self.sommets[cmpt][0])):	#Je récupère la ligne qui correspond au sommet
				ligne = self.sommets[cmpt][3]
			cmpt = cmpt+1
		
		if(ligne == -1):
			print "Problème dansla fonction cherche_num_ligne..."
			exit()
		return ligne
		
			
	def itineraire_sans_detail(self,chemin):	#Affiche les correspondances
		depart = chemin[0]
		correspondance = [depart]
		ligne = self.cherche_num_ligne(depart)
		ligne_bis = -1
		for i in range(len(chemin)):
			ligne_bis = self.cherche_num_ligne(chemin[i])
			if(ligne_bis != ligne):
				correspondance.append(chemin[i])
				ligne = ligne_bis
				
		print "Vous avez "+str(len(correspondance))+ " ligne(s) à prendre"
				
		return correspondance
		
	def creer_chemin(self, predecesseur, depart, arrive):
	
		#print predecesseur
		chemin = []
		chemin.append(arrive)
		sommet = predecesseur[arrive]
		tmp = 0
		while(sommet != depart):
			chemin.append(sommet)
			tmp = predecesseur[sommet]
			sommet = tmp
		chemin.append(depart)
		
		chemin[:] = chemin[::-1]
		
		#Pour éviter de prendre en compte un changement de ligne de la station de départ
		if(self.sommets[chemin[0]][5] == self.sommets[chemin[1]][5]):	#Si la 1ère station a le même nom que la 2ème...
			chemin.pop(0)
		
		return chemin		#retourne la liste 'chemin' inversée
		
	def def_temps_chemins(self, chemin):			### MODIFIE ###
		temps_chemin = []
		for j in range(len(chemin)):
			temps = 0
			for i in range(len(chemin[j])-1):
				for cmpt in range(len(self.aretes)):
					if( chemin[j][i] == int(self.aretes[cmpt][0]) and chemin[j][i+1] == int(self.aretes[cmpt][1]) ):
						temps = temps + int(self.aretes[cmpt][2])
						break
					if( chemin[j][i] == int(self.aretes[cmpt][1]) and chemin[j][i+1] == int(self.aretes[cmpt][0]) ):
						temps = temps + int(self.aretes[cmpt][2])
						break
			temps_chemin.append( temps )
		minimum = min(temps_chemin)
		#~ print "Tout les temps : " + str(temps_chemin) + " le minimum : " + str(minimum)
		return temps_chemin.index( minimum )
		
		
	def def_time(self, chemin):
		temps = 0
		for i in range(len(chemin)-1):
			for cmpt in range(len(self.aretes)):
				if( chemin[i] == int(self.aretes[cmpt][0]) and chemin[i+1] == int(self.aretes[cmpt][1]) ):
					temps = temps + int(self.aretes[cmpt][2])
					break
				if( chemin[i] == int(self.aretes[cmpt][1]) and chemin[i+1] == int(self.aretes[cmpt][0]) ):
					temps = temps + int(self.aretes[cmpt][2])
					break
		return temps

G = Graphe("metro.txt")
G.init_aretes()
G.init_sommets()

#Station de départ
while 1 :
	start = raw_input("Station de depart : ")
	resultat = G.recherche(start)
	if resultat == True:
		break
	else:
		print("La station n'existe pas réessayé")

#Station d'arrivée'
while 1 :
	end = raw_input("Station d'arrivée : ")
	resultat = G.recherche(end)
	if (resultat == True) and (start != end) :
		break

	elif (end == start):
		print("La station d'arrivé doit être différente de la station de départ")

	else:
		print("La station n'existe pas réessayé")
		
		
chemin = G.dijsktra(start,end)
#~ print "CHEMIN DANS MAIN : " + str(chemin)
print "Liste des sommets par lesquels on passe : "+str(chemin)
correspondance = G.itineraire_sans_detail(chemin)
print "Liste des correspondance : "+str(correspondance)

seconds = G.def_time(chemin)
minutes = seconds // 60
hours = minutes // 60

print "Votre temps de transports : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60)


