##### ALGO DE DIJSKTRA 1 #####

class Graph:
  def __init__(self):
    self.noeuds = set()
    self.aretes = defaultdict(list)
    self.distances = {}

  def ajout_noeud(self, valeur):
    self.noeuds.add(valeur)

  def ajout_aretes(self, noeuds_depart, noeuds_arrive, distance):
    self.aretes[noeuds_depart].append(noeuds_arrive)
    self.aretes[noeuds_arrive].append(noeuds_depart)
    self.distances[(noeuds_depart, noeuds_arrive)] = distance


def dijsktra(graph, initialisation):
	
  visiter = {initialisation: 0}
  
  # Chemin que l'on va parcourir
  
  chemin = {} 

  # noeuds = Ensemble des Noeuds du graphe	
  
  noeuds = set(graph.noeuds)

  # node = UN noeud du graphe	
  
  while noeuds: 
    minimum_node = None
    for node in noeuds:
      if node in visiter:
        if minimum_node is None:
         minimum_node = node
        elif visiter[node] < visiter[minimum_node]:
          minimum_node = node

    if minimum_node is None:
      break

    noeuds.remove(minimum_node)
    poids_actuel  = visiter[minimum_node]

    for arete in graph.aretes[minimum_node]:
      poids = poids_actuel  + graph.distances[(minimum_node, arete)]
      if arete not in visiter or poids  < visiter[arete]:
        visiter[arete] = poids 
        chemin[arete] = minimum_node

  return visiter, chemin
  
 ###############################
 
 
 
##### ALGO DE DIJSKTRA 2 #####
 import math
 
 
class Graphe():
 
    def __init__(self, noeuds):
        self.matriceAdj = noeuds.copy()
 
    def Afficher(self, src, dist):
        print("les chemins les plus courts allant de ", src, " est : ")
        for noeud in range(len(self.matriceAdj)):
            print((noeud+1), "\t", dist[noeud])
 
    def minDistance(self, dist, S, T):
 
        # Initilaize minimum distance for next node
        min = math.inf
        min_index = -1
 
        for v in T:
            if dist[v-1] < min:
                min = dist[v-1]
                min_index = v-1
 
        # supprimer de T et ajouter dans S
        T.remove(min_index+1)
        S.append(min_index+1)
        return min_index
 
    def dijkstra(self, src):
 
        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src-1] = 0
        precedence[src-1] = src-1
        S = []
        T = [(i+1) for i in range(len(self.matriceAdj))]
 
        while len(S) < len(self.matriceAdj):
 
            # Choisir un sommet u qui n'est pas dans l'ensemble S et
            # qui a une valeur de distance minimale
            u = self.minDistance(dist, S, T)
 
            # relaxation des sommets
            for v in range(len(self.matriceAdj)):
                if (self.matriceAdj[u][v] > 0) and (dist[v] > (dist[u] + self.matriceAdj[u][v])):
                    dist[v] = dist[u] + self.matriceAdj[u][v]
                    precedence[v] = u
        self.Afficher(src, dist)
 
 
# Test
# les sommets sont numérotés à partir de 1
matriceAdj = [[0, 2, 4, 0, 0, 0],
              [0, 0, 1, 0, 7, 0],
              [0, 0, 0, 3, 0, 0],
              [0, 0, 0, 0, 2, 5],
              [0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0],
              ]
g = Graphe(matriceAdj)
g.dijkstra(1)
 ###############################
 
 
