from tkinter import *
import time
import sys

class Graphe:

	sommets = []		#On stocke les sommets du graphe
	aretes  = []		#On stocke les arêtes du graphe
	fichier = ""		#On stocke le nom du fichiers qui définit le graphe

	#'fichier' est le fichier contenant les sommets et la pondération
	def __init__(self,fichier):			#C'est le constructeur de la classe 'Graphe'. 
		self.sommets = []
		self.aretes  = []
		self.fichier = fichier

	def init_graph(self):				#Initialisation d'un objet de la classe 'Graphe', en chargeant les données du fichier
		file = open(self.fichier,"r")

		for chaine in file :
			#Permet d'avoir les informations sur un sommet
			if chaine[0:1] == "V" :
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("V ","")
            
				#On sépare la chaine grâce aux espaces
				infoSommet = chaine.split(" ")
                
				#On ajoute [numSommet, numLigne, nom] à la liste des sommets
				(self.sommets).append(infoSommet)
            
			#Permet d'avoir les informations sur les aretes
			elif chaine[0:1] == "E" :
				chaine = chaine.replace("\n","")
				chaine = chaine.replace("E ","")
            
				#On sépare la chaine grâce aux espaces
				arete = chaine.split(" ")
                
				#On ajoute [s1, s2, poid] à la liste des aretes
				(self.aretes).append(arete)

		file.close()

	def creer_chemin(self, predecesseur, depart, arrive):	#Retourne le chemin le plus court entre le départ et l'arrivée
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

	def def_voisins(self, sommet):		#Cherche les voisins du sommet entré en paramètre
		voisins = []
		cmpt = 0

		while(cmpt < len(self.aretes)):
			if(sommet == int(self.aretes[cmpt][0])):
				voisins.append(int(self.aretes[cmpt][1]))

			elif(sommet == int(self.aretes[cmpt][1])):
				voisins.append(int(self.aretes[cmpt][0]))
			
			#Liste des stations à sens unique
			if  (sommet  ==  34  and voisins.count(92)  != 0): voisins.remove(92)
			elif(sommet  ==  248 and voisins.count(34)  != 0): voisins.remove(34)
			elif(sommet  ==  280 and voisins.count(248) != 0): voisins.remove(248)
			elif(sommet  ==  92  and voisins.count(280) != 0): voisins.remove(280)
			elif(sommet  ==  145 and voisins.count(201) != 0): voisins.remove(201)
			elif(sommet  ==  373 and voisins.count(196) != 0): voisins.remove(196)
			elif(sommet  ==  196 and voisins.count(373) != 0): voisins.remove(373)
			elif(sommet  ==  259 and voisins.count(196) != 0): voisins.remove(196)
			elif(sommet  ==  36  and voisins.count(259) != 0): voisins.remove(259)
			elif(sommet  ==  198 and voisins.count(36)  != 0): voisins.remove(36)
			elif(sommet  ==  52  and voisins.count(198) != 0): voisins.remove(198)
			elif(sommet  ==  201 and voisins.count(52)  != 0): voisins.remove(52)

			cmpt = cmpt+1

		return voisins
		
	def from_name_to_id(self, sommet):		#Permet de trouver le numéro correspondant au sommet entré en paramètre 
		cmpt = 0

		while (cmpt < len(self.sommets)) :
			if(sommet == self.sommets[cmpt][5]):
				identifiant = int(self.sommets[cmpt][0])
				break

			cmpt = cmpt+1

		return identifiant
    
	def distance(self, en_cours, voisin):		#Cherche la disance entre 'en_cours' et 'voisin'
		distance = 0
		cmpt = 0

		#Nous avons deux conditions pour prendre en compte les deux cas possible :
		#dans le tableau, on peut avoir [ 'en_cours', 'voisin', 'distance' ] OU [ 'voisin', 'en_cours', 'distance' ] 
		while(cmpt < len(self.aretes)):	
			if(en_cours == int(self.aretes[cmpt][0]) and voisin == int(self.aretes[cmpt][1])):
				distance = int(self.aretes[cmpt][2])
				break

			elif(voisin == int(self.aretes[cmpt][0]) and en_cours == int(self.aretes[cmpt][1])):
				distance = int(self.aretes[cmpt][2])
				break

			cmpt = cmpt+1
        
		return distance
	
	#Algo de dijsktra pour trouver le plus court chemin
	def dijsktra(self, sommet1, sommet2):
		
		depart = self.from_name_to_id(sommet1)
		arrive = self.from_name_to_id(sommet2)
		
		### PHASE D'INITIALISATION ###
		predecesseur = [None] * (len(self.sommets))		#Création d'une liste aussi grande que le nombre de sommets, que l'on rempli de 'None'
		a_traiter = []		
		dist = []
		for s in range(len(self.sommets)):
			dist.append(float("inf"))
			a_traiter.append(s)			#On ajoute tous les sommets dans la liste des sommets à traiter

		dist[depart] = 0				#La distance entre le point de départ et le point de départ est de 0
		
		### PHASE DE RECHERCHE ###
		en_cours = -1
		while(a_traiter != []):
			en_cours = min_dist(a_traiter, dist)		#Le prochain sommet de la liste 'a_traiter' que l'on traite est celui qui, pour l'instant, est le plus proche du départ
			#print ("en_cours = {0}".format(en_cours))
			a_traiter.remove(en_cours)					#Le sommet que l'on traite ne fait plus partie de la liste 'a_traiter'
			voisins = self.def_voisins(en_cours)
			
			for v in voisins:		#Dans cette boucle, on met à jour la liste des distances et des prédécesseurs, en fonction des voisins du sommet 'en_cours'
				v = int(v)
				nouvelle_dist = dist[en_cours] + self.distance(en_cours, v)
				if(nouvelle_dist < dist[v]):
					dist[v] = nouvelle_dist
					predecesseur[v] = en_cours
		
		return self.creer_chemin(predecesseur, depart, arrive)	#Grâce a la liste des prédécesseurs, on peut établir le chemin le plus court

	def itineraire_sans_detail(self,chemin):	#Retourne les correspondances
		depart = chemin[0]
		correspondance = [depart]
		ligne = fromIdToNbrLine(depart)
		ligne_bis = -1
		for i in range(len(chemin)):
			ligne_bis = fromIdToNbrLine(chemin[i])
			if(ligne_bis != ligne):
				correspondance.append(chemin[i])
				ligne = ligne_bis
				
		return correspondance
		
	def def_time(self, chemin):		#Calcul le temps du trajet en métro
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

	def recherche(self, position):	#Vérivie si la station choisie existe
		cmpt = 0
		position = position.replace(" ","_")
		while (cmpt < len(self.sommets)) :
			if (position == (self.sommets[cmpt][5])):
				print ("Le sommet {0} exite".format(position))
				return True
			cmpt = cmpt+1

		return False

# Return le un nom de station à partir de son id
def fromIdToName(id):
	if(id == int(G.sommets[id][0])):
		name = G.sommets[id][5]
		return name	

	else:
		cmpt = 0
		while (cmpt < len(G.sommets)):
			if(id == int(G.sommets[cmpt][0])):
				name = G.sommets[cmpt][5]
				break

			cmpt = cmpt+1

		return name	
		
# Return la valeur de terminus (0 ou 1) d'une station à partir de son id
def fromIdToTerminus(id):
	if(id == int(G.sommets[id][0])):
		terminus = G.sommets[id][4]
		return terminus	

	else:
		cmpt = 0
		while (cmpt < len(G.sommets)):
			if(id == int(G.sommets[cmpt][0])):
				terminus = G.sommets[cmpt][4]
				break

			cmpt = cmpt+1

		return terminus	

# Return la valeur le numéro de ligne à partir de l'id de la station
def fromIdToNbrLine(id):
	if(id == int(G.sommets[id][0])):
		nbreLine = G.sommets[id][3]
		return nbreLine	

	else:
		cmpt = 0
		while (cmpt < len(G.sommets)):
			if(id == int(G.sommets[cmpt][0])):
				nbreLine = G.sommets[cmpt][3]
				break

			cmpt = cmpt+1

		return nbreLine	

#Retourne le sommet de la liste 'a_traiter' ayant la plus petite distance avec le point de départ (à l'itération actuelle)
def min_dist(a_traiter, dist):
	tmp = [float("inf")] * len(dist)
	for i in a_traiter:
		tmp[i] = dist[i]

	minimum = min(tmp)
	return tmp.index(minimum)

#Fonction de recherche de terminus
def FindTerminus(listeTrajet):
	cmptTraj = 0
	listeTerminus = []

	while(cmptTraj<len(listeTrajet)-1):
		numLigne1 = fromIdToNbrLine(listeTrajet[cmptTraj])
		numLigne2 = fromIdToNbrLine(listeTrajet[cmptTraj+1])
		terminus  = fromIdToTerminus(listeTrajet[cmptTraj])

		# Si les numéros de ligne sont differents
		if(numLigne1 != numLigne2):
			idStation = listeTrajet[cmptTraj]
			idStPrecd = listeTrajet[cmptTraj-1]
            
			# On boucle tant qu'on ne trouve pas de terminus
			while(int(terminus) != 1):
				cmptA = 0
				while(cmptA<len(G.aretes)):
					if(idStation == int(G.aretes[cmptA][0]) and idStPrecd != int(G.aretes[cmptA][1])):
						numLine = fromIdToNbrLine(int(G.aretes[cmptA][0]))
						if(numLine == numLigne1):
							idStPrecd = idStation
							idStation = int(G.aretes[cmptA][1])
							break

					elif(idStation == int(G.aretes[cmptA][1]) and idStPrecd != int(G.aretes[cmptA][0])):
						numLine = fromIdToNbrLine(int(G.aretes[cmptA][1]))
						if(numLine == numLigne1):
							idStPrecd = idStation
							idStation = int(G.aretes[cmptA][0])
							break

					cmptA = cmptA+1

				terminus    = fromIdToTerminus(idStation)
				nameStation = fromIdToName(idStation)
            
			nameStation = fromIdToName(idStation)
			listeTerminus.append(nameStation)

		cmptTraj = cmptTraj+1

    ### XXXXXXXXXXX Recherche du terminus pour les lignes droites et la derniere correspondance XXXXXXXXXXX ####

	idStation = listeTrajet[len(listeTrajet)-1] # derniere station de la liste listeTrajet
	idStPrecd = listeTrajet[len(listeTrajet)-2] # avant derniere station de la liste listeTrajet
	terminus = fromIdToTerminus(idStation)		# on initialise terminus avec la valeur de terminus de idStation pour ne pas tester si c'est déjà un terminus

	# On boucle tant qu'on n'a pas trouvé le terminus
	while(int(terminus) != 1):
		cmptA = 0
		while(cmptA<len(G.aretes)):
			if(idStation == int(G.aretes[cmptA][0]) and idStPrecd != int(G.aretes[cmptA][1])):
				numLine = fromIdToNbrLine(int(G.aretes[cmptA][1]))
				if(numLine == numLigne1):
					idStPrecd = idStation
					idStation = int(G.aretes[cmptA][1])
					break

			elif(idStation == int(G.aretes[cmptA][1]) and idStPrecd != int(G.aretes[cmptA][0])):
				numLine = fromIdToNbrLine(int(G.aretes[cmptA][1]))
				if(numLine == numLigne1):
					idStPrecd = idStation
					idStation = int(G.aretes[cmptA][0])
					break

			cmptA = cmptA+1

		terminus    = fromIdToTerminus(idStation)
		nameStation = fromIdToName(idStation)

	nameStation = fromIdToName(idStation)
	listeTerminus.append(nameStation)

	print(listeTerminus)
	return listeTerminus

# XXXXXXXXXXXX PARTIE GRAPHIQUE XXXXXXXXXXXX #

#Coordonées x pour l'affichage sur le graphe
def chgX(x):
	return (int(x)-750)*5.55

#Récupération des coordonnées x après un clic sur le graphe
def recupX(x):
	return int(int(x)/5.55 + 750)

#Coordonées y pour l'affichage sur le graphe
def chgY(y):
	return (int(y)-120) * 2.0

#Récupération des coordonnées y après un clic sur le graphe
def recupY(y):
	return int(int(y) / 2.0 + 120)

#Couleur des arêtes du graphe
def chgCoul(num_coul):
	if num_coul == "01" :
		return "#FFCD00"

	elif num_coul == "02" :
		return "#003CA6"

	elif num_coul == "03" :
		return "#837902"

	elif num_coul == "04" :
		return "#CF009E"

	elif num_coul == "05" :
		return "#FF7E2E"

	elif num_coul == "06" and num_coul == "7b" :
		return "#6ECA97"

	elif num_coul == "07" :
		return "#FA9ABA"

	elif num_coul == "08" :
		return "#E19BDF"

	elif num_coul == "09" :
		return "#B6BD00"

	elif num_coul == "10" :
		return "#C9910D"

	elif num_coul == "11" :
		return "#704B1C"

	elif num_coul == "12" :
		return "#007852"

	elif num_coul == "13" and num_coul == "3b" :
		return "#6EC4E8"

	elif num_coul == "14" :
		return "#62259D"

class Application:
	tabLigne  = []
	tabPoint  = []
	tabTrajet = []

	stationDebut = ""
	stationFin   = ""
	tempsTrajet  = ""
	nbreClic = 0

	def __init__(self):
		self.fenetre = Tk()
		self.fenetre.title('Métro RATP')
		self.canvas = Canvas(self.fenetre, width=1440, height=720, background='#F5F5DC')
		self.canvas.create_rectangle(95, 200, 1125, 700, outline="#050D9E", width=2, dash=(3,5))
		self.photoImport  = PhotoImage(file="ratp.GIF")
		self.canvas.create_image(1320, 0, anchor = NW, image = self.photoImport)

		self.stationStrart = self.canvas.create_text(25, 40,  anchor = W, text="Station de départ : ", font="Arial 16 italic", fill="#050D9E")
		self.stationEnd    = self.canvas.create_text(25, 80,  anchor = W, text="Station d'arrivée : ", font="Arial 16 italic", fill="#050D9E")
		self.cheminMetro   = self.canvas.create_text(25, 130, anchor = W, text="Métro emprunté : ",    font="Arial 16 italic", fill="#050D9E")

		self.tabLigne  = []
		self.tabPoint  = []
		self.tabTrajet = []

		self.stationDebut = ""
		self.stationFin   = ""
		self.tempsTrajet  = ""
		self.nbreClic = 0

	#Evenement apres un clic gauche
	def clic(self, event):
		xb= str(recupX(event.x))
		yb= str(recupY(event.y))
		print ("x = {0}\t y = {1}".format(xb,yb))
		
		# Initialisation de la station de départ 
		if(self.nbreClic == 0):
			self.stationDebut = rechercheStation(xb,yb)
			if(self.stationDebut != ""):
				print("La station de depart est : {0}".format(self.stationDebut))
				self.canvas.itemconfigure(self.stationStrart, text="Station de départ : " + self.stationDebut.replace("_"," "))
				self.nbreClic = self.nbreClic +1

		# Initialisation de la station d'arrivé
		elif(self.nbreClic == 1):
			self.stationFin = rechercheStation(xb,yb)
			if(self.stationFin != "" and self.stationFin != self.stationDebut):
				self.canvas.itemconfigure(self.stationEnd, text="Station d'arrivée : " + self.stationFin.replace("_"," "))
				print("La station d'arrivée est : {0}".format(self.stationFin))
				self.nbreClic = self.nbreClic +1

	#Evenement apres une touche pressé
	def clavier(self, event):
		touche = event.keysym
		
		# Reset de la partie graphique
		if(touche == "r"):
			self.nbreClic = 0
			
			print("Reset")
			self.stationDebut = ""
			self.canvas.itemconfigure(self.stationStrart, text="Station de départ : " + self.stationDebut)
			
			self.stationFin = ""
			self.canvas.itemconfigure(self.stationEnd, text="Station d'arrivée : " + self.stationFin)
			
			chemin = "Métro emprunté : "
			self.canvas.itemconfigure(self.cheminMetro, text=chemin)
			
			A.suppTrajet()
			graphique()
		
		# Arret du programme
		elif(touche == "q" or touche == "Escape"):
			print("Arrêt du programme")
			sys.exit(0)
		
		# Lancement de la recherche de trajet
		elif(touche == "t" and self.stationDebut != "" and self.stationFin != ""):
			#Recherche du trajet le plus court
			print("Recherche du trajet entre {0} et {1}".format(self.stationDebut, self.stationFin))
			listeTrajet = G.dijsktra(self.stationDebut,self.stationFin)
			
			#On retire le dernier élement de la liste si c'est la même station
			if(fromIdToName( listeTrajet[ len(listeTrajet) - 1 ] ) == fromIdToName( listeTrajet[ len(listeTrajet) - 2 ])):
				listeTrajet.remove(listeTrajet[ len(listeTrajet) - 1 ])
			
			print(listeTrajet)
			A.trajet(listeTrajet)

			correspondance = G.itineraire_sans_detail(listeTrajet)
			print("Liste des correspondance : {0}".format(correspondance))
	
			# Durée du trajet
			seconds = G.def_time(listeTrajet)
			minutes = seconds // 60
			hours = minutes // 60
			print("Votre temps de transports : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60))
			
			#Recherche des terminus + affichage du trajet
			listeTerminus = FindTerminus(listeTrajet)

			chemin = "Vous êtes à " + self.stationDebut.replace("_"," ")
			chemin = chemin + ", Prendre la ligne " + fromIdToNbrLine(listeTrajet[0]) + " direction " + listeTerminus[0].replace("_"," ")
			
			cmpt = 1
			while(cmpt < len(listeTerminus)):
				chemin = chemin + "\nA " + fromIdToName(correspondance[cmpt]).replace("_"," ") + ", prenez la ligne " + fromIdToNbrLine(correspondance[cmpt]) + " direction " + listeTerminus[cmpt].replace("_"," ")
				cmpt = cmpt+1

			chemin = chemin + "\nVous devriez arriver à " + self.stationFin.replace("_"," ") + " dans : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60)
			self.canvas.itemconfigure(self.cheminMetro, text=chemin)

	# Dessine les arêtes entre les stations
	def drawLine(self):
		cmptSommets = 0
		cmptAretes = 0

		while (cmptAretes < len(G.aretes)) :
			sommet1 = G.aretes[cmptAretes][0]
			sommet2 = G.aretes[cmptAretes][1]
			while (cmptSommets < len(G.sommets)) :
				if sommet1 == G.sommets[cmptSommets][0] :
					x1 = chgX(G.sommets[cmptSommets][1])
					y1 = chgY(G.sommets[cmptSommets][2])
					cmptSommets = 0
					break

				cmptSommets = cmptSommets + 1

			while (cmptSommets < len(G.sommets)) :
				if sommet2 == G.sommets[cmptSommets][0] :
					x2 = chgX(G.sommets[cmptSommets][1])
					y2 = chgY(G.sommets[cmptSommets][2])
					couleur = chgCoul(G.sommets[cmptSommets][3])
					cmptSommets = 0
					break
				
				cmptSommets = cmptSommets + 1
			
			self.tabLigne.append(self.canvas.create_line(x1, y1, x2, y2, fill=couleur))
			cmptAretes = cmptAretes + 1

	# Dessine les stations 
	def drawStation(self):
		cmptSommets = 0
		r = 1

		while (cmptSommets < len(G.sommets)) :
			testx = G.sommets[cmptSommets][1]
			x = chgX(testx)
			testy = G.sommets[cmptSommets][2]
			y = chgY(testy)
			self.tabPoint.append(self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black"))
			cmptSommets = cmptSommets + 1

	# Dessine la légende du graphe 
	def legende(self):
		self.canvas.create_text(1150,350, anchor = W,text="Ligne de Métro: ", font="Arial 16 italic", fill="black")

		self.canvas.create_text(1200,385, anchor = W,text="M1", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,380,1180,390,fill="#FFCD00") 

		self.canvas.create_text(1200,415, anchor = W,text="M2", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,410,1180,420,fill="#003CA6")

		self.canvas.create_text(1200,445, anchor = W,text="M3", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,440,1180,450,fill="#837902")

		self.canvas.create_text(1200,475, anchor = W,text="M4", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,470,1180,480,fill="#CF009E")

		self.canvas.create_text(1200,505, anchor = W,text="M5", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,500,1180,510,fill="#FF7E2E")

		self.canvas.create_text(1190,535, anchor = W,text="M6 / 7b", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,530,1180,540,fill="#6ECA97")

		self.canvas.create_text(1200,565, anchor = W,text="M7", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1150,560,1180,570,fill="#FA9ABA")

		self.canvas.create_text(1310,385, anchor = W,text="M8", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,380,1290,390,fill="#E19BDF")

		self.canvas.create_text(1310,415, anchor = W,text="M9", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,410,1290,420,fill="#B6BD00")

		self.canvas.create_text(1310,445, anchor = W,text="M10", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,440,1290,450,fill="#C9910D")

		self.canvas.create_text(1310,475, anchor = W,text="M11", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,470,1290,480,fill="#704B1C")

		self.canvas.create_text(1310,505, anchor = W,text="M12", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,500,1290,510,fill="#007852")

		self.canvas.create_text(1300,535, anchor = W,text="M13 / 3b", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,530,1290,540,fill="#6EC4E8")

		self.canvas.create_text(1310,565, anchor = W,text="M14", font="Arial 14 italic", fill="black")
		self.canvas.create_rectangle(1260,560,1290,570,fill="#62259D")

	# Dessin du parcours à prendre sur le graphe
	def trajet(self, liste):
		cmptL = 0
		cmptS = 0

		while(cmptL<len(liste)-1):
			while(cmptS<len(G.sommets)):
				if(liste[cmptL] == int(G.sommets[cmptS][0])):
					x1 = chgX(G.sommets[cmptS][1])
					y1 = chgY(G.sommets[cmptS][2])
					break

				cmptS = cmptS+1
			
			cmptS = 0
			
			while(cmptS<len(G.sommets)):
				if(liste[cmptL + 1] == int(G.sommets[cmptS][0])):
					x2 = chgX(G.sommets[cmptS][1])
					y2 = chgY(G.sommets[cmptS][2])
					break

				cmptS = cmptS+1

			cmptS = 0
			cmptL = cmptL + 1

			self.tabTrajet.append(self.canvas.create_line(x1, y1, x2, y2, fill="#FF0000"))

	def suppTrajet(self):
		cmpt = 0
		while(cmpt < len(self.tabTrajet)):
			self.canvas.delete(self.tabTrajet[cmpt])
			cmpt = cmpt+1

		self.tabTrajet.clear()

def graphique():

	A.canvas.itemconfigure(A.stationStrart, text="Station de départ : " + A.stationDebut)
	A.canvas.itemconfigure(A.stationEnd,    text="Station d'arrivée : " + A.stationFin)
	
	#Gestion event
	A.canvas.bind("<Button-1> ", A.clic)
	A.canvas.focus_set()

	A.canvas.bind("<Key>", A.clavier)
	
	A.canvas.pack()
	A.fenetre.mainloop()

#Recherche la station selectionné sur la graphe par rapport au coordonnées 
def rechercheStation(x,y):
	cmpt = 0
	while (cmpt < len(G.sommets)) :
		if (int(x) <= int((G.sommets[cmpt][1]))+1 and int(x) >= int((G.sommets[cmpt][1]))-1 and int(y) <= int((G.sommets[cmpt][2]))+1 and int(y) >= int((G.sommets[cmpt][2]))-1):
			return G.sommets[cmpt][5]
            
		cmpt = cmpt+1

	null = ""
	return null

# XXXXXXXXXXXX Version textuelle XXXXXXXXXXXX #

def stationDepart():
	start = ""

	while 1 :
		start = input("Station de depart : ")
		resultat = G.recherche(start)
		if resultat == True:
			return start
		
		else:
			print("La station n'existe pas réessayé")

def stationArrivee(start):
	end = ""

	while 1 :
		end = input("Station d'arrivée : ")
		resultat = G.recherche(end)
		if (resultat == True) and (start != end) :
			return end

		elif (end == start):
			print("La station d'arrivé doit être différente de la station de départ")

		else:
			print("La station n'existe pas réessayé")

def Afftrajet(start, end):
	start = start.replace(" ","_")
	end   = end.replace(" ","_")
	print("Recherche du trajet entre {0} et {1}".format(start, end))
	listeTrajet = G.dijsktra(start,end)

	#On retire le dernier élement de la liste si c'est la même station
	if(fromIdToName( listeTrajet[ len(listeTrajet) - 1 ] ) == fromIdToName( listeTrajet[ len(listeTrajet) - 2 ])):
		listeTrajet.remove(listeTrajet[ len(listeTrajet) - 1 ])

	print(listeTrajet)
	
	correspondance = G.itineraire_sans_detail(listeTrajet)
	print("Liste des correspondance : {0}".format(correspondance))
	
	#Recherche des terminus + affichage du trajet
	listeTerminus = FindTerminus(listeTrajet)

	chemin = "Vous êtes à " + start
	chemin = chemin + ", Prendre la ligne " + fromIdToNbrLine(listeTrajet[0]) + " direction " + listeTerminus[0].replace("_"," ")
	
	cmpt = 1
	while(cmpt < len(listeTerminus)):
		chemin = chemin + "\nA " + fromIdToName(correspondance[cmpt]).replace("_"," ") + ", prenez la ligne " + fromIdToNbrLine(correspondance[cmpt]) + " direction " + listeTerminus[cmpt].replace("_"," ")
		cmpt = cmpt+1

	# Durée du trajet
	seconds = G.def_time(listeTrajet)
	minutes = seconds // 60
	hours = minutes // 60

	chemin = chemin + "\nVous devriez arriver à " + end + " dans : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60)
	print(chemin)

def question():
	while(TRUE):
		rep = input("Voulez-vous utiliser la partie graphique? [y/n] : ")
		if(rep == "y" or rep == "n"):
			return rep

def main(rep):
	if(rep == 'y'):
		A.legende()
		A.drawLine()    
		A.drawStation()
		graphique()

	elif(rep == 'n'):
		start = stationDepart()
		end   = stationArrivee(start)
		Afftrajet(start, end)

#L'objet 'G' est maintenant initialisé grâce aux données contenu dans le fichier "metro.txt"
G = Graphe("metro.txt")
G.init_graph()

rep = question()
if(rep == 'y'):
	A = Application() 

main(rep)
