# coding: utf-8
from tkinter import *
import sys

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
	return chemin[::-1] 	#On renvoie la liste inversée

class Graphe:

    sommets = []
    aretes  = []
    fichier = ""

    #'fichier' = fichier contenant les sommets et la pondération
    def __init__(self,fichier):
        self.sommets = []
        self.aretes  = []
        self.fichier = fichier

    def init_graph(self):
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

    def def_voisins(self, sommet):
        voisins = []
        cmpt = 0

        while(cmpt < len(self.aretes)):
            if(sommet == int(self.aretes[cmpt][0])):
                voisins.append(int(self.aretes[cmpt][1]))

            elif(sommet == int(self.aretes[cmpt][1])):
                voisins.append(int(self.aretes[cmpt][0]))

            cmpt = cmpt+1

        return voisins
		
    def from_name_to_id(self, sommet):
        cmpt = 0

        while (cmpt < len(self.sommets)) :
            if(sommet == self.sommets[cmpt][4]):
                identifiant = int(self.sommets[cmpt][0])
                break

            cmpt = cmpt+1

        return identifiant
        		
    def distance(self, en_cours, voisin):
        distance = 0
        cmpt = 0

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
        predecesseur = [None] * (len(self.sommets))
        a_traiter = []		
        dist = []
        for s in range(len(self.sommets)):
            dist.append(float("inf"))
            a_traiter.append(s)

        dist[depart] = 0
		
		### PHASE DE RECHERCHE ###
        en_cours = -1
        while(a_traiter != []):
            en_cours = min_dist(a_traiter, dist)
            print ("en_cours = {0}".format(en_cours))
            a_traiter.remove(en_cours)
            voisins = self.def_voisins(en_cours)
			
            for v in voisins:
                v = int(v)
                nouvelle_dist = dist[en_cours] + self.distance(en_cours, v)
                if(nouvelle_dist < dist[v]):
                    dist[v] = nouvelle_dist
                    predecesseur[v] = en_cours
		
        return creer_chemin(predecesseur, depart, arrive)
		
#Création du graphique 

#Coordonées x pour l'affichage sur le graphe
def chgX(x):
    return (int(x)-750)*3.5

#Récupération des coordonnées x après un clic sur le graphe
def recupX(x):
    return int(int(x)/3.5 + 750)

#Coordonées y pour l'affichage sur le graphe
def chgY(y):
    return int(y) * 1.2

#Récupération des coordonnées y après un clic sur le graphe
def recupY(y):
    return int(int(y) / 1.2)

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


#Creation de la fonction graphique (Faire une classe graphique?)

#Evenement apres un clic gauche
def clic(event):
    xb= str(recupX(event.x))
    yb= str(recupY(event.y))
    print ("x = {0}\t y = {1}".format(xb,yb))
    
    global nbreClic
    global stationDebut
    global stationFin

    if(nbreClic == 0):
        stationDebut = rechercheStation(xb,yb)
        if(stationDebut != ""):
            print("La station de depart est : " + stationDebut)
            canvas.itemconfigure(stationStrart, text="Station de départ : " + stationDebut)
            increGlobal()

    elif(nbreClic == 1):
        stationFin = rechercheStation(xb,yb)
        if(stationFin != "" and stationFin != stationDebut):
            canvas.itemconfigure(stationEnd, text="Station d'arrivée : " + stationFin)
            print("La station d'arrivée est : " + stationFin)
            increGlobal()

#Evenement apres une touche pressé
def clavier(event):
    global nbreClic
    global stationDebut
    global stationFin

    touche = event.keysym
    print(touche)
    if(touche == "r"):
        nbreClic = 0
        stationDebut = ""
        canvas.itemconfigure(stationStrart, text="Station de départ : " + stationDebut)
        stationFin = ""
        canvas.itemconfigure(stationEnd, text="Station d'arrivée : " + stationFin)

    elif(touche == "q" or touche == "Escape"):
        sys.exit(0)

    elif(touche == "t"):
        listeTrajet = G.dijsktra(stationDebut,stationFin)
        print(listeTrajet)
        trajet(listeTrajet)

def trajet(liste):
    global canvas
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

        canvas.create_line(x1, y1, x2, y2, fill="#FF0000")
        

#Incrementation de la varible global nbreClic
def increGlobal():
    global nbreClic
    nbreClic = nbreClic +1

#Recherche la station selectionné sur la graphe par rapport au coordonnées 
def rechercheStation(x,y):
    cmpt = 0
    while (cmpt < len(G.sommets)) :
        if (int(x) <= int((G.sommets[cmpt][1]))+1 and int(x) >= int((G.sommets[cmpt][1]))-1 and int(y) <= int((G.sommets[cmpt][2]))+1 and int(y) >= int((G.sommets[cmpt][2]))-1):
            return G.sommets[cmpt][4]
            
        cmpt = cmpt+1

    null = ""
    return null

#Fonction trop longue la découper?
def graphique():
    #init de la fenetre 
    
    #init de la toile en 800 par 1000
    global canvas

    r = 1
    cmptSommets = 0
    cmptAretes = 0

    while (cmptAretes < len(G.aretes)) :
        sommet1 = G.aretes[cmptAretes][0]
        sommet2 = G.aretes[cmptAretes][1]
        while (cmptSommets < len(G.sommets)) :
            if sommet1 == G.sommets[cmptSommets][0] :
                testx1 = G.sommets[cmptSommets][1]
                x1 = chgX(testx1)
                testy1 = G.sommets[cmptSommets][2]
                y1 = chgY(testy1)
                cmptSommets = 0
                break

            cmptSommets = cmptSommets + 1

        while (cmptSommets < len(G.sommets)) :
            if sommet2 == G.sommets[cmptSommets][0] :
                testx2 = G.sommets[cmptSommets][1]
                x2 = chgX(testx2)
                testy2 = G.sommets[cmptSommets][2]
                y2 = chgY(testy2)
                couleur = chgCoul(G.sommets[cmptSommets][3])
                cmptSommets = 0
                break
            
            cmptSommets = cmptSommets + 1

        canvas.create_line(x1, y1, x2, y2, fill=couleur)
        cmptAretes = cmptAretes + 1

        #init du rayon des cercles
    
    cmptSommets = 0
    
    while (cmptSommets < len(G.sommets)) :
        testx = G.sommets[cmptSommets][1]
        x = chgX(testx)
        testy = G.sommets[cmptSommets][2]
        y = chgY(testy)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
        cmptSommets = cmptSommets + 1

    canvas.create_text(400, 30, text="Metro parisien", font="Arial 22 italic", fill="blue")

    #Gestion event
    
    canvas.bind("<Button-1> ", clic)
    canvas.focus_set()

    canvas.bind("<Key>", clavier)
    
    canvas.pack()
    fenetre.mainloop()


G = Graphe("metro.txt")
G.init_graph()
print (G.aretes)
print ("\n\n\n")
print (G.sommets)

#init des variables globales

fenetre = Tk()
canvas = Canvas(fenetre, width=800, height=600, background='white')

stationDebut = ""
stationFin = ""
nbreClic = 0

stationStrart = canvas.create_text(25, 80, anchor = W,text="Station de départ : ", font="Arial 18 italic", fill="black")
stationEnd    = canvas.create_text(25, 120, anchor = W, text="Station d'arrivée : ", font="Arial 18 italic", fill="black")

graphique()

