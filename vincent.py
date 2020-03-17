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
        #chaine == "" : fin du fichier
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

    #sommet1 = départ   sommet2 = arrivée
   # def dijk(self,sommet1,sommet2):
        #On vérifie que les deux sommets existent
   #     if(sommet1 not in self.sommets):
   #         print "Votre point de départ n'est pas bon..."
   #         return
   #     if(sommet2 not in self.sommets):
   #         print "Votre point d'arrivé n'est pas bon"
   #         return
   #     T = [sommet1]
   #     distance_sommet = 0



G = Graphe("metro_test.txt")
G.init_aretes()
G.init_sommets()
print G.aretes
print ""
print G.sommets
print ""

sommet1 = raw_input("Où êtes-vous ?  ")
sommet2 = raw_input("Où voulez-vous aller ?  ")

#G.dijk(sommet1,sommet2)
