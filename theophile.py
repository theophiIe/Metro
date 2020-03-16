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
    
    def init_aretes(self):
        f = open(self.fichier,"r")

        for chaine in f :
            if chaine[0:1] == "E" :
                chaine = chaine.replace("\n","")
                chaine = chaine.replace("E ","")
            
                #On sépare la chaine grâce aux espaces
                arete = chaine.split(" ")
                #On ajoute [s1, s2, poid] à la liste des aretes
                (self.aretes).append(arete)
                print (chaine)
        f.close()

    #def init_sommets(self):

    #sommet1 = départ   sommet2 = arrivée
    #def dijk(self,sommet1,sommet2):



G = Graphe("metro.txt")
G.init_aretes()
print (G.aretes)

#Exemple pour lire un poid :
print ("")
print ("Voici les 2 premier poids : ")
print (G.aretes[0][2])
print (G.aretes[1][2])
#etc,etc...
