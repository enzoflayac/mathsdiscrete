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
    return L

print("Entrez la matrice booléenne M1 : ")
m1=entree_matrice()
print("Entrez la matrice booléenne M2 : ")
m2=entree_matrice()

def produit (M1,M2):
    L=[]
    Listtemp=[]
    coordonne2=0
    for i in range (taille):
        for j in range (taille):
            for k in range (taille):
                coordonne=M1[i][k]*M2[k][j]
                coordonne2+=coordonne
            Listtemp.append(coordonne2)
            coordonne2=0

        
        L.append(Listtemp)
        Listtemp=[]
    return L

print("produit m1 m2 : ", produit(m1,m2))

def somme(M1,M2):
    L=[]
    listtemp=[]
    coordonées1 = 0
    coordonées2 = 0
    for i in range(taille):
        for j in range(taille):
            coordonées1 = M1[i][j]
            coordonées2 = M2[i][j]
            coordonées = coordonées1 + coordonées2
            listtemp.append(coordonées)
        L.append(listtemp)
        listtemp=[]
    return L

print("somme m1 m2 : ", somme(m1, m2))

def egal(M1,M2):
    egal=True
    for i in range(taille):
        for j in range(taille):
            if M1[i][j]!=M2[i][j]:
                egal=False
    return egal

print("égal :",egal(m1,m2))

def matriceidentité():
    L=[]
    listtemp=[]
    for i in range(taille):
        for j in range(taille):
            if i==j:
                listtemp.append(1)
            else:
                listtemp.append(0)
        L.append(listtemp)
        listtemp=[]
    return L

def puissance (M,n):
    truc=M
    for i in range (n-1):
        truc = produit(M,truc)
    return truc


def matricetransitive(g):
    mt=somme(matriceidentité(),g)
    condition=[matriceidentité(),g]
    i=2
    while egal(condition[-1], condition[-2])==False:
        mt=somme(mt,puissance(g,i))
        i+=1
        print(mt)
        condition.append(mt)
    return mt

print(matricetransitive(m1))