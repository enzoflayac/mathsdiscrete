

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
        self.liste_aretes=[]

    def saisie_graphe(self):
        self.nombre_sommet=int(input("Entrez le nombre de sommet de votre graphe : "))
        enter=0
        for i in range(self.nombre_sommet):
            enter=arete.saisie_arete()
            self.liste_aretes.append(enter)
        return self.liste_aretes
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
arete=Arete()
graphe=Graphe()

print(graphe.saisie_graphe())
print(graphe.adjacence())
graphe.afficher_matrice()
