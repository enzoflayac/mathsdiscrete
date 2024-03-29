class Arete:
    def __init__(self):
        self.sommet_initial=0
        self.sommet_final=0
        self.cout_arete=0
        
        
    def saisie_arete(self):
        self.sommet_initial=int(input("Entrez le sommet initiale : "))
        self.sommet_final=int(input("Entrez le sommet final : "))
        self.cout_arete=int(input("Entrez le cout de l'arete : "))
        return (self.sommet_initial, self.sommet_final, self.cout_arete)
        
class Graphe:
    def __init__(self):
        self.nombre_sommet=0
        self.liste_aretes=[
        [1,2,3],[1,4,6],[1,10,9],
        [2,3,2],[2,4,4],[2,10,9],[2,9,9],
        [3,4,2],[3,5,9],[3,9,8],
        [4,5,9],
        [5,6,4],[5,7,5],[5,9,7],
        [6,7,1],[6,8,4],
        [7,8,3],[7,9,9],
        [8,9,10],[8,10,10],
        [9,10,8]]
    def saisie_graphe(self):
        self.nombre_sommet=int(input("Entrez le nombre d'aretes de votre graphe : "))
        enter=0
        for i in range(self.nombre_sommet):
            enter=arete.saisie_arete()
            self.liste_aretes.append(enter)
        return self.liste_aretes
    def tri_par_cout(self):
        liste_aretes=self.liste_aretes
        liste_aretes= sorted(liste_aretes, key= lambda x: x[2])
        print(liste_aretes)
        return liste_aretes

    def ajout_arbre_couvant(self):
        listes_triees = self.tri_par_cout()
        arbre_couvant = []

        for arete in listes_triees:
            if len(arbre_couvant) == 0:
                arbre_couvant.append(arete)
            else:
                cycle = False
                for edge in arbre_couvant:
                    if (arete[0] == edge[0] and arete[1] == edge[1]) or (arete[0] == edge[1] and arete[1] == edge[0]):
                        cycle = True
                        break
                    if self.detect_cycle(arete, arbre_couvant):
                        cycle = True
                        break
                if not cycle:
                    arbre_couvant.append(arete)

        print("Arbre couvrant minimal (Kruskal) :", arbre_couvant)

    def detect_cycle(self, arete, arbre_couvant):
        sommets_visites = set()
        for edge in arbre_couvant:
            sommets_visites.add(edge[0])
            sommets_visites.add(edge[1])

        visited = set()
        queue = [arete[0]]

        while queue:
            sommet = queue.pop(0)
            if sommet == arete[1]:
                return True
            visited.add(sommet)
            for edge in arbre_couvant:
                if edge[0] == sommet and edge[1] not in visited:
                    queue.append(edge[1])
                elif edge[1] == sommet and edge[0] not in visited:
                    queue.append(edge[0])

        return False

    def adjacence(self):
        liste_matrice=[]
        for i in range(self.nombre_sommet):
            initialisation_ligne=[]
            for j in range(self.nombre_sommet):
                initialisation_ligne.append(0)
            liste_matrice.append(initialisation_ligne)
        for i in range(self.nombre_sommet):
            liste_temp=[self.liste_aretes[i][0],self.liste_aretes[i][1]]
            if liste_matrice[liste_temp[0]-1][liste_temp[1]-1] == 0 and liste_matrice[liste_temp[1]-1][liste_temp[0]-1] == 0 :
                liste_matrice[liste_temp[0]-1][liste_temp[1]-1]=1
                liste_matrice[liste_temp[1]-1][liste_temp[0]-1]=1
        return liste_matrice
    def afficher_matrice(self):
        liste_matrice=self.adjacence()
        iteration=len(liste_matrice)
        print("")
        for i in range(iteration):
            for j in range(iteration):
                print(liste_matrice[i][j], end=" ")
            print("")


#M=graphe.adjacence()
#print(M)
#graphe.afficher_matrice()

arete=Arete()
graphe=Graphe()
graphe.ajout_arbre_couvant()
M=graphe.adjacence()
graphe.afficher_matrice()


