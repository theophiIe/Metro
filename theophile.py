# ##### Exemple de création d'un dictionnaire pour init un graphe ####

# import json

# path = "metro.txt"
# file = open(path, "r")
# Graphe = dict()
# for line in file :
#     if line[0:1] == "E" :
#         sommet1 = line[2:5] 
#         sommet2 = line[6:9]
#         Graphe[sommet1] = [sommet2] #edge entre s1 et s2

# print(json.dumps(Graphe, indent = 1))
# file.close()

####################################################################

# ##### Exemple d'init d'un graphe ####

# def create_graph(oriente = False, pondere = True) :
# 	graphe = { 'noeud': {}, 'arete': {}, 'nbre_arete': 0, 'poid_arete': 0, 'oriente': oriente, 'pondere': pondere, 'abscisse': 0, 'ordonnee': 0 }
# 	return graphe

# def add_node(g, noeud):
# 	return g['noeud'][noeud] # return node attributes

# def add_edge(g, noeud1, noeud2):
# 	# create nodes if they do not exist
# 	if noeud1 not in g['noeud']: add_node(g, noeud1) # ensure n1 exists
# 	if noeud2 not in g['noeud']: add_node(g, noeud2) # ensure n2 exists
# 	# add edge(s) only if they do not exist
# 	if noeud2 not in g['arete'][noeud1]:
# 		if not g['oriente']:
# 			g['arete'][noeud2][noeud1] = g['arete'][noeud1][noeud2] # share the same attributes as n1->n2
# 		g['nbre_arete'] += 1
# 	return g['arete'][noeud1][noeud2] # return edge attributes

# def load_SIF(filename, pondere = True):
# 	# line syntax: nodeD <relationship type> nodeE nodeF nodeB
# 	graphe = create_graph(pondere) # new empty graph
# 	with open(filename) as f: # OPEN FILE
# 		# PROCESS THE REMAINING LINES
# 		row = f.readline().rstrip() # read next line and remove ending whitespaces
# 		while row:
# 			vals = row.split('\t') # split line on tab
# 			for i in range(2, len(vals)):
# 				add_edge(graphe, vals[0], vals[i])
# 			row = f.readline().rstrip() # read next line
# 	return graphe # return graph

####################################################################

#### Test d'utilistion du XML ####

#Utilisation de xmltodict pour l'installer : python3 -m pip install xmltodict
# import xmltodict 

# with open('data.xml') as fd:
#     doc = xmltodict.parse(fd.read())

# print (doc['mydocument']['@has']) # == u'an attribute'
# print (doc['mydocument']['and']['many']) # == [u'elements', u'more elements']
# print (doc['mydocument']['plus']['@a']) # == u'complex'
# print (doc['mydocument']['plus']['#text']) # == u'element as well'

####################################################################

# représentation d'un graphe à l'aide de liste d'adjacence
class Graphe:
    def __init__(self):
        # créer un dictionnaire pour stocker la liste d'adjacence
        self.Liste = {}
 
    # Ajouter une arête entre deux sommets
    def addArete(self, u, v):
        if v not in self.Liste:
            self.Liste[v] = []
 
        if u not in self.Liste:
            self.Liste[u] = []
 
        self.Liste[u].append(v)
 
    # Parcours en profondeur
    def Parcours_profondeur(self, s, visited):
 
        # Marquer le noeud courant comme visité et l'afficher
        visited[s-1] = True
        print(s, end=" ")
 
        # recommencer avec tous les noeuds voisins
        for i in self.Liste[s]:
            if visited[i-1] == False:
                self.Parcours_profondeur(i, visited)
 
 
g = Graphe()
g.addArete(1, 3)
g.addArete(1, 4)
g.addArete(1, 5)
g.addArete(1, 6)
g.addArete(2, 3)
g.addArete(3, 1)
g.addArete(3, 2)
g.addArete(4, 1)
g.addArete(4, 5)
g.addArete(5, 1)
g.addArete(5, 4)
g.addArete(6, 1)
 
visited = [False] * (len(g.Liste))
print("Parcours en profondeur à partir du sommet 1")
g.Parcours_profondeur(1, visited) 