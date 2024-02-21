# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
        for i in range(self.nombre_sommet):
            for j in range(self.nombre_sommet):
                if self.liste_aretes[i][j]

    
    
arete=Arete()
graphe=Graphe()
print(graphe.saisie_graphe())
        