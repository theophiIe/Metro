# coding: utf-8

class Graphe:

    sommets = []
    aretes = []
    fichier = ""

    #'fichier' = fichier contenant les sommets et la pondération
    def __init__(self,fichier):
        self.sommets = []
        self.aretes = []
        self.fichier = fichier

    # def init_sommets(self):
    #     file = open(self.fichier,"r")

    #     for chaine in file :
    #         if chaine[0:1] == "V" :
    #             chaine = chaine.replace("\n","")
    #             chaine = chaine.replace("V ","")
            
    #             #On sépare la chaine grâce aux espaces
    #             infoSommet = chaine.split(" ")
    #             #On ajoute [numSommet, numLigne, nom] à la liste des sommets
    #             (self.sommets).append(infoSommet)
    #     file.close()

    # def init_aretes(self):
    #     file = open(self.fichier,"r")

    #     for chaine in file :
    #         if chaine[0:1] == "E" :
    #             chaine = chaine.replace("\n","")
    #             chaine = chaine.replace("E ","")
            
    #             #On sépare la chaine grâce aux espaces
    #             arete = chaine.split(" ")
    #             #On ajoute [s1, s2, poid] à la liste des aretes
    #             (self.aretes).append(arete)
    #     file.close()

    #fusion des deux fonctions du dessus pour eviter de lire plusieur fois le fichiers car lourd en execution
    #Possible de fusionner les deux if car beaucoup d'action en commun
    #Probleme le nom des stations de metrons ecris en plus d'un mot sont decoupe dans la liste modifications potentielle du metro.txt en mettatn un _ par exemple 
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

    def dijkstra(self, start, end):
        print ("Début de l'algo de Dikjstra")
        

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



#Ecrire un focntion recherche pour éviter d'écrire deux fois la meme chose 
#Point de depart
# cmpt = 0
# startExit = False

# while startExit != True :
#     start = input("Station de depart : ")
#     start = start.replace(" ","_")
#     while (cmpt < len(G.sommets)) :
#         if (start == (G.sommets[cmpt][1])):
#             print ("Le sommet {0} exite".format(start))
#             startExit = True
#             break
#         cmpt = cmpt+1

# #Point d'arrivee
# cmpt = 0
# endExit = False

# while endExit != True :
#     end = input("Station d'arrivee : ")
#     end = end.replace(" ","_")
#     while (cmpt <= len(G.sommets)) :
#         if (end == (G.sommets[cmpt][1])):
#             print ("Le sommet {0} exite".format(end))
#             endExit = True
#             break
#         cmpt = cmpt+1


#Test de la fonction recherche

def recherche(position):
    cmpt = 0

    position = position.replace(" ","_")
    while (cmpt < len(G.sommets)) :
        if (position == (G.sommets[cmpt][3])):
            print ("Le sommet {0} exite".format(position))
            return True
        cmpt = cmpt+1

    return False

#Station de départ
while 1 :
    start = input("Station de depart : ")
    resultat = recherche(start)
    if resultat == True:
        break
    else:
        print("La station n'existe pas réessayé")

#Station d'arrivée'
while 1 :
    end = input("Station d'arrivee : ")
    resultat = recherche(end)
    if (resultat == True) and (start != end) :
        break
    
    elif end == start:
        print("La station d'arrivé doit être différente de la stion de départ")

    else:
        print("La station n'existe pas réessayé")


#Création du graphique 

from tkinter import * 

#Creation de la fonction graphique (Faire une classe graphique?)
def graphique():
    #init de la fenetre 
    fenetre = Tk()

    #init de la toile en 1000 par 1000
    canvas = Canvas(fenetre, width=1000, height=1000, background='white')
    
    cmptSommets = 0

    #init du rayon des cercles
    r = 3

    while (cmptSommets < len(G.sommets)) :
        x = G.sommets[cmptSommets][1]
        y = G.sommets[cmptSommets][2]
        canvas.create_oval(x-r,y-r,x+r,y+r, fill="black")
        cmptSommets = cmptSommets + 1
    
    cmptSommets = 0
    cmptAretes = 0

    while (cmptAretes < len(G.aretes)) :
        sommet1 = G.aretes[cmptAretes][0]
        sommet2 = G.aretes[cmptAretes][1]
        while (cmptSommets < len(G.sommets)) :
            if sommet1 == G.sommets[cmptSommets][0] :
                x1 = G.sommets[cmptSommets][1]
                y1 = G.sommets[cmptSommets][2]

            elif sommet2 == G.sommets[cmptSommets][0] :
                x2 = G.sommets[cmptSommets][1]
                y2 = G.sommets[cmptSommets][2]
            
            cmptSommets = cmptSommets + 1

        canvas.create_line(x1, y1, x2, y2)
        cmptAretes = cmptAretes + 1

    canvas.pack()
    fenetre.mainloop()


