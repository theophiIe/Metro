# coding: utf-8

class Graphe:

    sommets = []
    aretes = []
    fichier = ""

    #'fichier' = fichier contenant les sommets et la pondération
    def __init__(self,fichier):
        self.sommets = None
        self.aretes = None
        self.fichier = fichier
    
    def init_sommets(self):
        f = open(self.fichier,"r")
        chaine = f.readline()
        f.close()
        print chaine[:]

    #def init_aretes(self):

    #sommet1 = départ   sommet2 = arrivée
    #def dijk(self,sommet1,sommet2):



G = Graphe("metro_test.txt")
G.init_sommets()
