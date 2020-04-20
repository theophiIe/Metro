# coding: utf-8
from tkinter import *
import time
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
            if(sommet == self.sommets[cmpt][5]):
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

    def itineraire_sans_detail(self,chemin):	#Affiche les correspondances
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
		

def fromIdToName(id):
    cmpt = 0

    while (cmpt < len(G.sommets)):
        if(id == int(G.sommets[cmpt][0])):
            name = G.sommets[cmpt][5]
            break

        cmpt = cmpt+1

    return name

def fromIdToTerminus(id):
    cmpt = 0

    while (cmpt < len(G.sommets)):
        if(id == int(G.sommets[cmpt][0])):
            terminus = G.sommets[cmpt][4]
            break

        cmpt = cmpt+1

    return terminus

def fromIdToNbrLine(id):
    cmpt = 0

    while (cmpt < len(G.sommets)):
        if(id == int(G.sommets[cmpt][0])):
            nbreLine = G.sommets[cmpt][3]
            break

        cmpt = cmpt+1

    return nbreLine

def FindTerminus(listeTrajet):
    cmptTraj = 0
    listeTerminus = []

    while(cmptTraj<len(listeTrajet)-1):
        numLigne1 = fromIdToNbrLine(listeTrajet[cmptTraj])
        terminus  = fromIdToTerminus(listeTrajet[cmptTraj])
        numLigne2 = fromIdToNbrLine(listeTrajet[cmptTraj+1])

        if(numLigne1 != numLigne2):
            idStation = listeTrajet[cmptTraj]
            idStPrecd = listeTrajet[cmptTraj-1]
            
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

                terminus    = fromIdToTerminus(idStation) #creer la fonction
                nameStation = fromIdToName(idStation)
            
            #print ("Le terminus de la staion n°{0} = {1}".format(idStation,nameStation))
            nameStation = fromIdToName(idStation)
            listeTerminus.append(nameStation)

        cmptTraj = cmptTraj+1

    ### XXXXXXXXXXX Recherche pour ligne droite et derniere correspondance XXXXXXXXXXX ####

    idStation = listeTrajet[len(listeTrajet)-1]
    idStPrecd = listeTrajet[len(listeTrajet)-2]
    while(int(terminus) != 1):
        cmptA = 0
        while(cmptA<len(G.aretes)):
            if(idStation == int(G.aretes[cmptA][0]) and idStPrecd != int(G.aretes[cmptA][1])):
                numLine   = fromIdToNbrLine(int(G.aretes[cmptA][1]))
                if(numLine == numLigne1):
                    idStPrecd = idStation
                    idStation = int(G.aretes[cmptA][1])
                    break

            elif(idStation == int(G.aretes[cmptA][1]) and idStPrecd != int(G.aretes[cmptA][0])):
                numLine   = fromIdToNbrLine(int(G.aretes[cmptA][1]))
                if(numLine == numLigne1):
                    idStPrecd = idStation
                    idStation = int(G.aretes[cmptA][0])
                    break

            cmptA = cmptA+1

        terminus    = fromIdToTerminus(idStation) #creer la fonction
        nameStation = fromIdToName(idStation)

    listeTerminus.append(nameStation)

    #Permet d'enlever les doublons
    #listeTerminus = list(set(listeTerminus))

    print(listeTerminus)
    return listeTerminus

#Création du graphique 

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
            print("La station de depart est : {0}".format(stationDebut))
            canvas.itemconfigure(stationStrart, text="Station de départ : " + stationDebut.replace("_"," "))
            increGlobal()

    elif(nbreClic == 1):
        stationFin = rechercheStation(xb,yb)
        if(stationFin != "" and stationFin != stationDebut):
            canvas.itemconfigure(stationEnd, text="Station d'arrivée : " + stationFin.replace("_"," "))
            print("La station d'arrivée est : {0}".format(stationFin))
            increGlobal()

#Evenement apres une touche pressé
def clavier(event):
    global nbreClic
    global stationDebut
    global stationFin
    global canvas

    touche = event.keysym
    print(touche)
    if(touche == "r"):
        nbreClic = 0
        stationDebut = ""
        canvas.itemconfigure(stationStrart, text="Station de départ : " + stationDebut)
        stationFin = ""
        canvas.itemconfigure(stationEnd, text="Station d'arrivée : " + stationFin)
        
        canvas.delete(ALL)
        graphique()
        
    elif(touche == "q" or touche == "Escape"):
        sys.exit(0)

    elif(touche == "t"):
        listeTrajet = G.dijsktra(stationDebut,stationFin)
        print(listeTrajet)
        trajet(listeTrajet)

        correspondance = G.itineraire_sans_detail(listeTrajet)
        print("Liste des correspondance : {0}".format(correspondance))
   
        seconds = G.def_time(listeTrajet)
        minutes = seconds // 60
        hours = minutes // 60

        print("Votre temps de transports : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60))
        #canvas.itemconfigure(tempsTrajet, text="Durée du trajet : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60))
        
        listeTerminus = FindTerminus(listeTrajet)

        chemin = "Vous êtes à " + stationDebut.replace("_"," ")
        chemin = chemin + ", Prendre la ligne " + fromIdToNbrLine(listeTrajet[0]) + " direction " + listeTerminus[0].replace("_"," ")
        
        cmpt = 1
        while(cmpt < len(listeTerminus)):
            chemin = chemin + "\nA " + fromIdToName(correspondance[cmpt]).replace("_"," ") + ", prenez la ligne " + fromIdToNbrLine(correspondance[cmpt]) + " direction " + listeTerminus[cmpt].replace("_"," ")
            cmpt = cmpt+1

        chemin = chemin + "\nVous devriez arriver à " + stationFin.replace("_"," ") + " dans : %02d h %02d min %02d sec" % (hours, minutes % 60, seconds % 60)
        canvas.itemconfigure(cheminMetro, text=chemin)
        


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
            return G.sommets[cmpt][5]
            
        cmpt = cmpt+1

    null = ""
    return null

def drawLine():
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

        canvas.create_line(x1, y1, x2, y2, fill=couleur)
        cmptAretes = cmptAretes + 1

def drawStation():
    cmptSommets = 0
    r = 1

    while (cmptSommets < len(G.sommets)) :
        testx = G.sommets[cmptSommets][1]
        x = chgX(testx)
        testy = G.sommets[cmptSommets][2]
        y = chgY(testy)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
        cmptSommets = cmptSommets + 1

#Fonction trop longue la découper?
def graphique():
    global canvas

    drawLine()    
    drawStation()

    canvas.itemconfigure(stationStrart, text="Station de départ : " + stationDebut)
    
    canvas.itemconfigure(stationEnd, text="Station d'arrivée : " + stationFin)
    
    canvas.create_rectangle(95,200,1125,700,outline="#050D9E",width=2,dash=(3,5))

    canvas.create_image(1320,0, anchor = NW, image = photoImport)
    #Gestion event
    
    canvas.bind("<Button-1> ", clic)
    canvas.focus_set()

    canvas.bind("<Key>", clavier)
    
    canvas.pack()
    fenetre.mainloop()


G = Graphe("metro.txt")
G.init_graph()

#init des variables globales

fenetre = Tk()
fenetre.title('Métro RATP')
canvas = Canvas(fenetre, width=1440, height=720, background='#F5F5DC')

stationDebut = ""
stationFin   = ""
tempsTrajet  = ""
cheminMetro  = ""
photoImport  = PhotoImage(file="ratp.GIF")
nbreClic = 0

stationStrart = canvas.create_text(25, 40, anchor = W,text="Station de départ : ", font="Arial 16 italic", fill="#050D9E")
stationEnd    = canvas.create_text(25, 80, anchor = W, text="Station d'arrivée : ", font="Arial 16 italic", fill="#050D9E")
#tempsTrajet   = canvas.create_text(25, 120, anchor = W, text="Durée du trajet : ", font="Arial 16 italic", fill="#050D9E")
cheminMetro   = canvas.create_text(25, 130, anchor = W, text="Métro emprunté : ", font="Arial 16 italic", fill="#050D9E")

#Légende
Legende = ""
m1 = ""
m2 = ""
m3 = ""
m4 = ""
m5 = ""
m6 = ""
m7 = ""
m8 = ""
m9 = ""
m10 = ""
m11 = ""
m12 = ""
m13 = ""
m14 = ""

Legende = canvas.create_text(1150,350, anchor = W,text="Ligne de Métro: ", font="Arial 16 italic", fill="black")

m1 = canvas.create_text(1200,385, anchor = W,text="M1", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,380,1180,390,fill="#FFCD00") 

m2 = canvas.create_text(1200,415, anchor = W,text="M2", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,410,1180,420,fill="#003CA6")

m3 = canvas.create_text(1200,445, anchor = W,text="M3", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,440,1180,450,fill="#837902")

m4 = canvas.create_text(1200,475, anchor = W,text="M4", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,470,1180,480,fill="#CF009E")

m5 = canvas.create_text(1200,505, anchor = W,text="M5", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,500,1180,510,fill="#FF7E2E")

m6 = canvas.create_text(1190,535, anchor = W,text="M6 / 7b", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,530,1180,540,fill="#6ECA97")

m7 = canvas.create_text(1200,565, anchor = W,text="M7", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1150,560,1180,570,fill="#FA9ABA")

m8 = canvas.create_text(1310,385, anchor = W,text="M8", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,380,1290,390,fill="#E19BDF")

m9 = canvas.create_text(1310,415, anchor = W,text="M9", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,410,1290,420,fill="#B6BD00")

m10 = canvas.create_text(1310,445, anchor = W,text="M10", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,440,1290,450,fill="#C9910D")

m11 = canvas.create_text(1310,475, anchor = W,text="M11", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,470,1290,480,fill="#704B1C")

m12 = canvas.create_text(1310,505, anchor = W,text="M12", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,500,1290,510,fill="#007852")

m13 = canvas.create_text(1300,535, anchor = W,text="M13 / 3b", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,530,1290,540,fill="#6EC4E8")

m14 = canvas.create_text(1310,565, anchor = W,text="M14", font="Arial 14 italic", fill="black")
canvas.create_rectangle(1260,560,1290,570,fill="#62259D")

graphique()

