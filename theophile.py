# coding: utf-8
from tkinter import * 

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
    aretes = []
    fichier = ""

    #'fichier' = fichier contenant les sommets et la pondération
    def __init__(self,fichier):
        self.sommets = []
        self.aretes = []
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

	#Algo de dijsktra pour trouver le plus court chemin
    def dijsktra(self, sommet1, sommet2):
		
        depart = self.from_name_to_id(sommet1)
        arrive = self.from_name_to_id(sommet2)
		
		### PHASE D'INITIALISATION ###
		
        predecesseur = [None] * (len(self.sommets) + 1)		#Car le sommet 'zéro' n'éxiste pas
        a_traiter = []		
        dist = [None]										#dist[0] = None car il n'y a pas de sommet 'zéro'
        for s in range(1,len(self.sommets)+1):				#s prendra les valeurs dans l'intervalle [1,len(self.sommets)]
            dist.append(float("inf"))
            a_traiter.append(s)
        dist[depart] = 0
		
		### PHASE DE RECHERCHE ###
		
        en_cours = -1
        while(a_traiter != []):
			
            en_cours = min_dist(a_traiter, dist)
            print ("en_cours = "+str(en_cours))
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
def clic(event):
    xb= str(recupX(event.x))
    yb= str(recupY(event.y))
    print ("x = {0}\t y = {1}".format(xb,yb))
    rechercheStation(xb,yb)

#Recherche la station selectionné sur la graphe par rapport au coordonnées 
def rechercheStation(x,y):
    cmpt = 0
    while (cmpt < len(G.sommets)) :
        if (int(x) <= int((G.sommets[cmpt][1]))+1 and int(x) >= int((G.sommets[cmpt][1]))-1 and int(y) <= int((G.sommets[cmpt][2]))+1 and int(y) >= int((G.sommets[cmpt][2]))-1):
            print ("Vous avez selectionne la station : {0}".format(G.sommets[cmpt][4]))
            break
        cmpt = cmpt+1

#Fonction trop longue la découper?
def graphique():
    #init de la fenetre 
    fenetre = Tk()

    #init de la toile en 1000 par 1000
    canvas = Canvas(fenetre, width=800, height=600, background='white')

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
    
    canvas.bind("<Button-1> ", clic)
    
    canvas.pack()
    fenetre.mainloop()


G = Graphe("metro.txt")
G.init_graph()
print (G.aretes)
print ("\n\n\n")
print (G.sommets)

#Exemple pour lire un poid :
print ("")
print ("Voici les 2 premier poids : ")
print (G.aretes[0][2])
print (G.aretes[1][2])
#etc,etc...
graphique()

