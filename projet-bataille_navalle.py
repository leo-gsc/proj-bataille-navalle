def stock_initial():
    """
    établi le stock de bateau par joueurs
    sortie: un dictionnaire avec le nombre de bateau par taille
    """
    return {2: 1, 3: 2, 4: 1, 5: 1}

def placer_bateau(grille, taille, orientation, coordonnee):
    """
    permet de placer un bateau
    """
    if #en gros faudrait que si le bateau n'est pas disponible il est impossible de le placer
    #renvoie une erreur
    if orientation == True:
        for i in grille:




def create_game():
    """
    permet de créer la partie en établissant une grille par joueurs
    """
    stock_p1 = stock_initial()
    stock_p2 = stock_initial()
    tableau = []
    lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    for i in range(10):
        ligne = []
        for j in range(10):
            valeur = f"{lignes[i]}{j+1}"
            ligne.append(valeur)
        tableau.append(ligne)

    print("P1 1  2  3  4  5  6  7  8  9  10")
    for i in range(10):
        print(lignes[i], end=" ")
        for j in range(10):
            print(tableau[i][j], end=" ")
        print()


    tableau2 = []
    lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    for i in range(10):
        ligne = []
        for j in range(10):
            valeur = f"{lignes[i]}{j+1}"
            ligne.append(valeur)
        tableau2.append(ligne)

    print("P2 1  2  3  4  5  6  7  8  9  10")
    for i in range(10):
        print(lignes[i], end=" ")
        for j in range(10):
            print(tableau2[i][j], end=" ")
        print()








