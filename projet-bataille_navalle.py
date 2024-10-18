def stock_initial():
    """
    Établit le stock de bateaux par joueur.
    Sortie : un dictionnaire avec le nombre de bateaux par taille
    """
    #initialisation du stock de bateau
    return {2: 1, 3: 2, 4: 1, 5: 1}

def verif_bateau(grille, taille, orientation, coordonnee):
    """
    Vérifie si un bateau peut être placé
    Entrée :
        grille : un tableau de tableau de jeu
        taille : taille du bateau
        orientation : un booleen qui défini l'orientation du bateau
        coordonnee : position de départ pour placer un bateau
    Sortie :True si le bateau peut être placé, sinon False
    """
    #transformation des coordonnés pour parcourir le tableau
    col = int(coordonnee[1:].upper()) - 1
    ligne = ord(coordonnee[0]) - 65
    
    # Vérif de la taille
    if orientation:  
        if col + taille > 10:
            return False  # Le bateau ne passe pas
        for i in range(taille):
            if grille[ligne][col + i] != ".":  # Vérif pour placer si case libre
                return False
    else:  
        if ligne + taille > 10:
            return False  # Le bateau ne passe pas
        for i in range(taille):
            if grille[ligne + i][col] != ".":  # Vérif pour placer si case libre
                return False

    return True

def placer_bateau(grille, stock, taille, orientation, coordonnee):
    """
    Permet de placer un bateau sur la grille.
    Entrée :
        grille : un tableau de tableau de jeu
        taille : taille du bateau
        orientation : un booleen qui défini l'orientation du bateau
        coordonnee : position de départ pour placer un bateau
    Sortie :True si le bateau peut être placé, sinon False
    """
    col = int(coordonnee[1:].upper()) - 1
    ligne = ord(coordonnee[0]) - 65
    #verif du stock
    if stock[taille] <= 0:
        raise ValueError(f"Il n'y a plus de bateau de taille {taille} à placer.")
    #cas où le bateau n'est pas plaçable
    if not verif_bateau(grille, taille, orientation, coordonnee):
        raise ValueError("Impossible de placer le bateau, vérifie la position et l'orientation.")
    #place le bateau en parcourant le tableau selon la taille
    for i in range(taille):
        if orientation:  
            grille[ligne][col + i] = " O"
        else:  
            grille[ligne + i][col] = " O"
    stock[taille] -= 1

def affiche_tab(tableau, joueur):
    """
    Affiche le tableau d'un joueur.
    
    Entrée:
    tableau: La carte du jeu.
    joueur: Le numero du joueur ("P1" ou "P2").
    Sortie: le tableau affiché
    """
    lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    colonnes = [str(i + 1) for i in range(10)]  

    # Affichage du haut de la carte 
    print("    1   2   3   4   5   6   7   8   9  10")
    
    for i in range(10):
        print(f"{lignes[i]}  ", end="") 
        for j in range(10):
            print(f"{tableau[i][j]:>2}", end="  ")
        print() 



def create_game():
    """
    Crée la partie en établissant une grille vide par joueur.
    """
    tableau_p1 = []
    tableau_p2 = []
    stock_p1 = stock_initial()
    stock_p2 = stock_initial()
    for i in range(10):  
        ligne_p1 = []  
        for j in range(10):
            ligne_p1.append(".")  
        tableau_p1.append(ligne_p1)  

    
    for i in range(10):
        ligne_p2 = []
        for j in range(10):
            ligne_p2.append(".")
        tableau_p2.append(ligne_p2)

    affiche_tab(tableau_p1, "P1")
    affiche_tab(tableau_p2, "P2")
    return tableau_p1, tableau_p2, stock_p1, stock_p2




#test pour la pres
tableau_p1, tableau_p2, stock_p1, stock_p2 = create_game()
#affiche_tab(tableau_p1, "P1")
#affiche_tab(tableau_p2, "P2")

print(verif_bateau(tableau_p1, 3, True, "A1"))
placer_bateau(tableau_p1, stock_p1, 3, True, "A1")
#verif_bateau(tableau_p1, 3, True, "A1")
affiche_tab(tableau_p1, "P1")
#placer_bateau(tableau_p1, stock_p1, 3, True, "A1")
placer_bateau(tableau_p1, stock_p1, 2, False, "B1")
#placer_bateau(tableau_p1, stock_p1, 2, True, "B5")
#placer_bateau(tableau_p1, stock_p1, 5, True, "D8")

affiche_tab(tableau_p1, "P1")


#verif_bateau(tableau_p2, 3, True, "A1")
placer_bateau(tableau_p2, stock_p2, 3, True, "A1")
#verif_bateau(tableau_p2, 3, True, "A1")
#placer_bateau(tableau_p2, stock_p2, 3, True, "A1")
placer_bateau(tableau_p2, stock_p2, 2, True, "B5")
#placer_bateau(tableau_p2, stock_p2, 2, True, "B5")
#placer_bateau(tableau_p2, stock_p2, 5, True, "D8")

affiche_tab(tableau_p2, "P2")