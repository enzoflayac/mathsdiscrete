M1=[[1,3,1],[2,3,1],[1,2,1]]
M2=[[2,3,1],[1,3,1],[1,2,1]]
taille=3

taille= int(input(" Quel est le nombre de colones de vos matrices carrées ?"))

def entree_matrice():
    L=[]
    Listtemp=[]
    for J in range (taille):
        for i in range (taille):
            coordonne=int(input(f"\nentrez la coordonnée n°{i+1} de la ligne {J+1} :"))
            Listtemp.append(coordonne)
        
        L.append(Listtemp)
        Listtemp=[]
    print(L)

M1=entree_matrice()
M2=entree_matrice()


def produit (M1,M2):
    L=[]
    Listtemp=[]
    coordonne2=0
    for i in range (taille):
        for j in range (taille):
            for k in range (taille):
                coordonne=M1[i][k]*M2[k][j]
                print(coordonne)
                coordonne2+=coordonne
            print("\n",coordonne2)
            Listtemp.append(coordonne2)
            coordonne2=0

        
        L.append(Listtemp)
        Listtemp=[]
    return L


print("Le produit en M1 et M2 est :", produit(M1,M2))

def puissance (M,n):
    truc=M
    for i in range (n-1):
        truc = produit(M,truc)
    return truc

print("test de la puissance :",puissance(entree_matrice(),2))

def nbchemins(M,n,i,j):
    return puissance(M,n)[i-1][j-1]
print("Entrez la matrice pour le nombre de chemins :")
m=entree_matrice()
n=int(input("Entrez le nombre de chemins n : "))
i=int(input("Entrez le premier sommet i : "))
j=int(input("Entrez le sommet j : "))
print("nbchemins = ", nbchemins(m,n,i,j))