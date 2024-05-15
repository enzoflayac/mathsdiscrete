import networkx as nx  # Importation de la bibliothèque NetworkX pour la manipulation de graphes
import matplotlib.pyplot as plt  # Importation de la bibliothèque matplotlib pour le traçage de graphiques
import numpy as np  # Importation de la bibliothèque numpy pour les calculs numériques

class Arete:  # Définition de la classe Arete pour représenter une arête dans un graphe
    
    def __init__(self):  # Définition du constructeur
        self.sommet_initial = 0  # Initialisation du sommet initial de l'arête
        self.sommet_final = 0  # Initialisation du sommet final de l'arête
        self.cout_arete = 0  # Initialisation du coût de l'arête
        
    
    
    def saisie_arete(self):  # Méthode pour saisir les détails d'une arête
        self.sommet_initial = int(input("Entrez le sommet initial : "))  # Saisie du sommet initial
        self.sommet_final = int(input("Entrez le sommet final : "))  # Saisie du sommet final
        self.cout_arete = int(input("Entrez le coût de l'arête : "))  # Saisie du coût de l'arête
        return (self.sommet_initial, self.sommet_final, self.cout_arete)  # Retourne les détails de l'arête sous forme de tuple
        
class Graphe:  # Définition de la classe Graphe pour représenter un graphe
    
    def __init__(self):  # Définition du constructeur
        self.nombre_sommet = 0  # Initialisation du nombre de sommets dans le graphe
        self.arbre_couvant = []  # Initialisation de la liste des arêtes de l'arbre couvrant minimal
        self.liste_aretes = [  # Initialisation d'une liste d'arêtes prédéfinies
        [1, 2, 3], [1, 4, 6], [1, 10, 9],
        [2, 3, 2], [2, 4, 4], [2, 10, 9], [2, 9, 9],
        [3, 4, 2], [3, 5, 9], [3, 9, 8],
        [4, 5, 9],
        [5, 6, 4], [5, 7, 5], [5, 9, 7],
        [6, 7, 1], [6, 8, 4],
        [7, 8, 3], [7, 9, 9],
        [8, 9, 10], [8, 10, 10],
        [9, 10, 8]
        ]
        
    
    
    def saisie_graphe(self):  # Méthode pour saisir les détails du graphe (non utilisée dans ce script)
        self.nombre_sommet = int(input("Entrez le nombre d'arêtes de votre graphe : "))  # Saisie du nombre d'arêtes
        enter = 0  # Initialisation d'une variable pour la saisie des arêtes
        for i in range(self.nombre_sommet):  # Boucle pour saisir chaque arête
            enter = arete.saisie_arete()  # Appel de la méthode saisie_arete de la classe Arete
            self.liste_aretes.append(enter)  # Ajout de l'arête à la liste des arêtes du graphe
        return self.liste_aretes  # Retourne la liste des arêtes du graphe
    
    
    
    def tri_par_cout(self):  # Méthode pour trier les arêtes par coût
        liste_aretes = self.liste_aretes  # Récupération de la liste des arêtes du graphe
        liste_aretes = sorted(liste_aretes, key=lambda x: x[2])  # Tri de la liste des arêtes par le troisième élément (coût)
        print(liste_aretes)  # Affichage des arêtes triées par coût
        return liste_aretes  # Retourne la liste des arêtes triées par coût
    
    
    
    def ajout_arbre_couvant(self):  # Méthode pour trouver l'arbre couvrant minimal (algorithme de Kruskal)
        listes_triees = self.tri_par_cout()  # Appel de la méthode tri_par_cout pour trier les arêtes par coût

        for arete in listes_triees:  # Parcours des arêtes triées par coût
            if len(self.arbre_couvant) == 0:  # Si l'arbre couvrant est vide
                self.arbre_couvant.append(arete)  # Ajout de l'arête à l'arbre couvrant
            else:
                cycle = False  # Initialisation d'un indicateur de cycle à False
                for edge in self.arbre_couvant:  # Parcours des arêtes de l'arbre couvrant
                    if (arete[0] == edge[0] and arete[1] == edge[1]) or (arete[0] == edge[1] and arete[1] == edge[0]):
                        cycle = True  # S'il y a un cycle, on met l'indicateur à True
                        break
                    if self.detect_cycle(arete, self.arbre_couvant):
                        cycle = True  # S'il y a un cycle, on met l'indicateur à True
                        break
                if not cycle:  # Si aucun cycle n'a été détecté
                    self.arbre_couvant.append(arete)  # Ajout de l'arête à l'arbre couvrant

        print("Arbre couvrant minimal (Kruskal) :", self.arbre_couvant)  # Affichage de l'arbre couvrant minimal
    
    
    
    def detect_cycle(self, arete, arbre_couvant):  # Méthode pour détecter les cycles dans l'arbre couvrant
        sommets_visites = set()  # Initialisation d'un ensemble pour stocker les sommets visités
        for edge in arbre_couvant:  # Parcours des arêtes de l'arbre couvrant
            sommets_visites.add(edge[0])  # Ajout du sommet initial à l'ensemble
            sommets_visites.add(edge[1])  # Ajout du sommet final à l'ensemble

        visited = set()  # Initialisation d'un ensemble pour stocker les sommets visités
        queue = [arete[0]]  # Initialisation d'une file avec le sommet initial de l'arête

        while queue:  # Tant que la file n'est pas vide
            sommet = queue.pop(0)  # Retrait du premier élément de la file
            if sommet == arete[1]:  # Si le sommet est égal au sommet final de l'arête
                return True  # Il y a un cycle, on retourne True
            visited.add(sommet)  # Ajout du sommet à l'ensemble des sommets visités
            for edge in arbre_couvant:  # Parcours des arêtes de l'arbre couvrant
                if edge[0] == sommet and edge[1] not in visited:  # Si le sommet est le sommet initial de l'arête et que le sommet final n'a pas été visité
                    queue.append(edge[1])  # Ajout du sommet final à la file
                elif edge[1] == sommet and edge[0] not in visited:  # Si le sommet est le sommet final de l'arête et que le sommet initial n'a pas été visité
                    queue.append(edge[0])  # Ajout du sommet initial à la file

        return False  # S'il n'y a pas de cycle, on retourne False
    
    def nbr_sommet_arbre_couvant(self):  # Méthode pour compter le nombre de sommets dans l'arbre couvrant
        liste_nbr_sommet_abre_couvant = []  # Initialisation d'une liste pour stocker les sommets de l'arbre couvrant
        for i in range(len(self.arbre_couvant)):  # Parcours des arêtes de l'arbre couvrant
            for j in range(2):  # Parcours des sommets de chaque arête
                if self.arbre_couvant[i][j] not in liste_nbr_sommet_abre_couvant:  # Si le sommet n'est pas déjà dans la liste
                    liste_nbr_sommet_abre_couvant.append(self.arbre_couvant[i][j])  # Ajout du sommet à la liste
        return len(liste_nbr_sommet_abre_couvant)  # Retourne le nombre de sommets de l'arbre couvrant
    
    def adjacence(self):  # Méthode pour générer la matrice d'adjacence de l'arbre couvrant
        liste_matrice = []  # Initialisation de la liste pour stocker la matrice d'adjacence
        nbr_arrete_arbre_couvant = self.nbr_sommet_arbre_couvant()  # Récupération du nombre de sommets de l'arbre couvrant
        for i in range(nbr_arrete_arbre_couvant):  # Parcours des sommets de l'arbre couvrant
            initialisation_ligne = []  # Initialisation de la ligne de la matrice d'adjacence
            for j in range(nbr_arrete_arbre_couvant):  # Parcours des sommets de l'arbre couvrant
                initialisation_ligne.append(0)  # Ajout de 0 à la ligne de la matrice d'adjacence
            liste_matrice.append(initialisation_ligne)  # Ajout de la ligne à la liste de la matrice d'adjacence
        for i in range(nbr_arrete_arbre_couvant - 1):  # Parcours des arêtes de l'arbre couvrant
            liste_temp = [self.arbre_couvant[i][0], self.arbre_couvant[i][1]]  # Récupération des sommets de l'arête
            if liste_matrice[liste_temp[0] - 1][liste_temp[1] - 1] == 0 and liste_matrice[liste_temp[1] - 1][liste_temp[0] - 1] == 0:
                liste_matrice[liste_temp[0] - 1][liste_temp[1] - 1] = 1  # Ajout de 1 à la position correspondante dans la matrice
                liste_matrice[liste_temp[1] - 1][liste_temp[0] - 1] = 1  # Ajout de 1 à la position correspondante dans la matrice
        return liste_matrice  # Retourne la matrice d'adjacence de l'arbre couvrant
    
    def afficher_matrice(self):  # Méthode pour afficher la matrice d'adjacence de l'arbre couvrant
        liste_matrice = self.adjacence()  # Récupération de la matrice d'adjacence de l'arbre couvrant
        iteration = len(liste_matrice)  # Calcul du nombre d'itérations
        print("")  # Affichage d'une ligne vide
        for i in range(iteration):  # Parcours des lignes de la matrice
            for j in range(iteration):  # Parcours des colonnes de la matrice
                print(liste_matrice[i][j], end=" ")  # Affichage de chaque élément de la matrice
            print("")  # Affichage d'une ligne vide entre chaque ligne de la matrice

# Création d'un objet Arete
arete = Arete()
# Création d'un objet Graphe
graphe = Graphe()
# Appel de la méthode ajout_arbre_couvant pour trouver l'arbre couvrant minimal
graphe.ajout_arbre_couvant()
# Appel de la méthode afficher_matrice pour afficher la matrice d'adjacence de l'arbre couvrant
graphe.afficher_matrice()

# Création d'un objet de graphe non dirigé
G = nx.Graph()

# Ajout des arêtes à partir de l'arbre couvrant minimal
for arete in graphe.arbre_couvant:
    G.add_edge(arete[1], arete[0])

# Création d'un dictionnaire pour associer des noms aux sommets
noms_sommets = {
    1: 'Bordeaux',
    2: 'Nantes',
    3: 'Paris',
    4: 'Rennes',
    5: 'Rouen',
    6: 'Lille',
    7: 'Nancy',
    8: 'Strasbourg',
    9: 'Lyon',
    10: 'Marseille'
}

positions = {
    1: (0, -1),
    2: (2, 0),
    3: (3, 2),
    4: (2, 3),
    5: (5, 4),
    6: (6, 5),
    7: (7, 3),
    8: (8, 2),
    9: (7, 0),
    10: (4, -3)
}

# Dessin du graphe avec les noms des sommets
pos = nx.spring_layout(G)  # Positionnement des nœuds
nx.draw(G, pos=positions, with_labels=True, labels=noms_sommets, node_color='lightblue', node_size=1000)  # Dessin du graphe avec les noms des sommets
labels = nx.get_edge_attributes(G, 'weight')  # Obtention des poids des arêtes
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Dessin des poids des arêtes

plt.title("Graphe de l'arbre couvrant minimal avec noms de sommets")
plt.show()
