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
        while(1):
            chaine = f.readline()
            chaine = chaine.replace("\n","")
            #On stoppe à la fin du fichier
            if (chaine == ""):
                break
            #On sépare la chaine grâce aux espaces
            arete = chaine.split(" ")
            #On ajoute [s1, s2, poid] à la liste des aretes
            (self.aretes).append(arete)
            print chaine
        f.close()

    #def init_sommets(self):

    #sommet1 = départ   sommet2 = arrivée
    #def dijk(self,sommet1,sommet2):



G = Graphe("metro_test.txt")
G.init_aretes()
print G.aretes
