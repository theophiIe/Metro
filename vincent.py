######## Simple exemple de l'oriente objet chez python ##########

class truc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def somme(self):
        print("Somme : "+str(self.a+self.b)+"\n")

mon_truc = truc(4,2)
mon_truc.somme()
