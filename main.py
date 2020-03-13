# import json

# path = "metro.txt"
# file = open(path, "r")
# Graphe = dict()
# for line in file :
#     if line[0:1] == "E" :
#         sommet1 = line[2:5]
#         sommet2 = line[6:9]
#         Graphe[sommet1] = [sommet2]

# print(json.dumps(Graphe, indent = 1))

# file.close()

def create_graph(oriente = False, pondere = True) :
	graphe = { 'noeud': {}, 'arete': {}, 'nbre_arete': 0, 'poid_arete': 0, 'oriente': oriente, 'pondere': pondere, 'abscisse': 0, 'ordonnee': 0 }
	return graphe

def add_node(g, noeud):
	return g['noeud'][noeud] # return node attributes

def add_edge(g, noeud1, noeud2):
	# create nodes if they do not exist
	if noeud1 not in g['noeud']: add_node(g, noeud1) # ensure n1 exists
	if noeud2 not in g['noeud']: add_node(g, noeud2) # ensure n2 exists
	# add edge(s) only if they do not exist
	if noeud2 not in g['arete'][noeud1]:
		if not g['oriente']:
			g['arete'][noeud2][noeud1] = g['arete'][noeud1][noeud2] # share the same attributes as n1->n2
		g['nbre_arete'] += 1
	return g['arete'][noeud1][noeud2] # return edge attributes

def load_SIF(filename, pondere = True):
	# line syntax: nodeD <relationship type> nodeE nodeF nodeB
	graphe = create_graph(pondere) # new empty graph
	with open(filename) as f: # OPEN FILE
		# PROCESS THE REMAINING LINES
		row = f.readline().rstrip() # read next line and remove ending whitespaces
		while row:
			vals = row.split('\t') # split line on tab
			for i in range(2, len(vals)):
				add_edge(graphe, vals[0], vals[i])
			row = f.readline().rstrip() # read next line
	return graphe # return graph
