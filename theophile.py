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

    def init_sommets(self):
        file = open(self.fichier,"r")

        for chaine in file :
            if chaine[0:1] == "V" :
                chaine = chaine.replace("\n","")
                chaine = chaine.replace("V ","")
            
                #On sépare la chaine grâce aux espaces
                infoSommet = chaine.split(" ")
                #On ajoute [numSommet, numLigne, nom] à la liste des sommets
                (self.sommets).append(infoSommet)
                print (chaine)
        file.close()

    def init_aretes(self):
        file = open(self.fichier,"r")

        for chaine in file :
            if chaine[0:1] == "E" :
                chaine = chaine.replace("\n","")
                chaine = chaine.replace("E ","")
            
                #On sépare la chaine grâce aux espaces
                arete = chaine.split(" ")
                #On ajoute [s1, s2, poid] à la liste des aretes
                (self.aretes).append(arete)
                print (chaine)
        file.close()

    #fusion des deux fonctions du dessus pour eviter de lire plusieur fois le fichiers car lourd en execution
    #Possible de fusionner les deux if car beaucoup d'action en commun
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
                print (chaine)
            
            #Permet d'avoir les informations sur les aretes
            if chaine[0:1] == "E" :
                chaine = chaine.replace("\n","")
                chaine = chaine.replace("E ","")
            
                #On sépare la chaine grâce aux espaces
                arete = chaine.split(" ")
                
                #On ajoute [s1, s2, poid] à la liste des aretes
                (self.aretes).append(arete)
                print (chaine)

        file.close()

G = Graphe("metro.txt")
G.init_aretes()
print (G.aretes)

#Exemple pour lire un poid :
print ("")
print ("Voici les 2 premier poids : ")
print (G.aretes[0][2])
print (G.aretes[1][2])
#etc,etc...
