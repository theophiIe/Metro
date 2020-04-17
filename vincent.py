# coding: utf-8

def min_dist(a_traiter, dist):
 
	tmp = [float("inf")] * len(dist)
	for i in a_traiter:
		tmp[i] = dist[i]
	minimum = min(tmp)
	return tmp.index(minimum)
	
def creer_chemin(predecesseur, depart, arrive):
	
	chemin = []
	chemin.append(arrive)
	sommet = predecesseur[arrive]
	tmp = 0
	while(sommet != depart):
		chemin.append(sommet)
		tmp = predecesseur[sommet]
		sommet = tmp
	chemin.append(depart)
	
	return chemin[::-1]		#retourne la liste 'chemin' inversée
	
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
			if( (ligne[0] == "E") and (int(ligne[1]) == sommet) ):
				voisins.append(ligne[2])
			elif( (ligne[0] == "E") and (int(ligne[2]) == sommet) ):
				voisins.append(ligne[1])
			ligne = fichier.readline()
		
		fichier.close()
		return voisins
		
	def from_name_to_id(self, sommet):
		
		fichier = open(self.fichier,"r")
		identifiant = -1				#Si 'identifiant' garde la valeur '-1', une erreur s'est produite
		ligne = fichier.readline()
		while(ligne != ""):				#Signifie la fin du fichier
			ligne = ligne.replace("\n","")
			ligne = ligne.split(" ")
			if(ligne[0] == "V" and ligne[2] == sommet):
				identifiant = int(ligne[1])
				break
			ligne = fichier.readline()
		fichier.close()
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

		
	def dijsktra(self, sommet1, sommet2):
		
		depart = self.from_name_to_id(sommet1)
		arrive = self.from_name_to_id(sommet2)
		
		### PHASE D'INITIALISATION ###
		predecesseur = [None] * (len(self.sommets))		###
		a_traiter = []		
		dist = []				###
		for s in range(len(self.sommets)):		#s prend la valeur de tous les sommets	###
			dist.append(float("inf"))
			a_traiter.append(s)
		dist[depart] = 0
		
		### PHASE DE RECHERCHE ###
		
		en_cours = -1
		while(a_traiter != []):
			
			en_cours = min_dist(a_traiter, dist)
			print "en_cours = "+str(en_cours)
			a_traiter.remove(en_cours)
			voisins = self.def_voisins(en_cours)
			
			for v in voisins:
				
				v = int(v)
				nouvelle_dist = dist[en_cours] + self.distance(en_cours, v)
				if(nouvelle_dist < dist[v]):
					dist[v] = nouvelle_dist
					predecesseur[v] = en_cours
		
		return creer_chemin(predecesseur, depart, arrive)
		

	def recherche(self, position):
		cmpt = 0
		position = position.replace(" ","_")
		while (cmpt < len(self.sommets)) :
			if (position == (self.sommets[cmpt][1])):
				print ("Le sommet {0} exite".format(position))
				return True
			cmpt = cmpt+1

		return False


G = Graphe("metro_test.txt")
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

	elif end == start:
		print("La station d'arrivé doit être différente de la stion de départ")

	else:
		print("La station n'existe pas réessayé")

print G.dijsktra(start,end)
