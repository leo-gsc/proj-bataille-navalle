def stock_initial():
    """
    Établit le stock de bateaux par joueur.
    Sortie : un dictionnaire avec le nombre de bateaux par taille
    """
    #initialisation du stock de bateau
    return {2: 1, 3: 2, 4: 1, 5: 1}

def verif_bateau(carte, taille, orientation, coordonnee):
    """
    Vérifie si un bateau peut être placé
    Entrée :
        carte : un tableau de tableau de jeu
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
            if carte[ligne][col + i] != ".":  # Vérif pour placer si case libre
                return False
    else:  
        if ligne + taille > 10:
            return False  # Le bateau ne passe pas
        for i in range(taille):
            if carte[ligne + i][col] != ".":  # Vérif pour placer si case libre
                return False

    return True

def placer_bateau(carte, stock, taille, orientation, coordonnee):
    """
    Permet de placer un bateau sur la grille.
    Entrée :
        carte : un tableau de tableau de jeu
        taille : taille du bateau
        orientation : un booleen qui défini l'orientation du bateau
        coordonnee : position de départ pour placer un bateau
    Sortie :True si le bateau peut être placé, sinon False
    """
    col = int(coordonnee[1:].upper()) - 1
    ligne = ord(coordonnee[0]) - 65
    #verif du stock
    if stock[taille] <= 0:
        raise ValueError(f"plus de bateau de {taille} à placer.")
    #cas où le bateau n'est pas plaçable
    if not verif_bateau(carte, taille, orientation, coordonnee):
        raise ValueError("il doit y avoir un soucis de placement")
    #place le bateau en parcourant le tableau selon la taille
    for i in range(taille):
        if orientation:  
            carte[ligne][col + i] = " O"
        else:  
            carte[ligne + i][col] = " O"
    stock[taille] -= 1



def attaque(carte_averse, coordonnee, score):
    """permet d'attauqer les bateaux adverses
    Entrées: grille_adverse, la carte de l'adversaire
             coordonnée, le point qui va être attaqué
    Sortie: "Touché" si un bateau est atteint, "coulé" sinon
    """
    col = int(coordonnee[1:].upper()) - 1  
    ligne = ord(coordonnee[0]) - 65  
    #verif si case déjà attaquée
    if carte_averse[ligne][col] == " X":
        print("Cette case a déjà été attaquée!")
        return score
    #verif pour savoir si on touche ou non
    if carte_averse[ligne][col] == " O":
        score += 1
        if score == 17:
            print("Gagné!")
        carte_averse[ligne][col] = " X" 
        print("Touché")
    else:
        carte_averse[ligne][col] = " X" 
        print("Raté")
    return score
    
    
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
    score_p1 = 0
    score_p2 = 0
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
    return tableau_p1, tableau_p2, stock_p1, stock_p2, score_p1, score_p2




#test pour la pres
tableau_p1, tableau_p2, stock_p1, stock_p2, score_p1, score_p2 = create_game()
#affiche_tab(tableau_p1, "P1")
#affiche_tab(tableau_p2, "P2")

#print(verif_bateau(tableau_p1, 3, True, "A1"))
placer_bateau(tableau_p1, stock_p1, 3, True, "A1")
#verif_bateau(tableau_p1, 3, True, "A1")
#affiche_tab(tableau_p1, "P1")
#placer_bateau(tableau_p1, stock_p1, 3, True, "A1")
placer_bateau(tableau_p1, stock_p1, 3, True, "A6")
placer_bateau(tableau_p1, stock_p1, 2, False, "B1")
placer_bateau(tableau_p1, stock_p1, 4, True, "E3")
placer_bateau(tableau_p1, stock_p1, 5, True, "D4")
#placer_bateau(tableau_p1, stock_p1, 2, True, "B5")
#placer_bateau(tableau_p1, stock_p1, 5, True, "D8")

affiche_tab(tableau_p1, "P1")


#verif_bateau(tableau_p2, 3, True, "A1")
placer_bateau(tableau_p2, stock_p2, 3, True, "A1")
#verif_bateau(tableau_p2, 3, True, "A1")
#placer_bateau(tableau_p2, stock_p2, 3, True, "A1")
placer_bateau(tableau_p2, stock_p2, 2, True, "B5")
placer_bateau(tableau_p2, stock_p2, 3, False, "G6")
placer_bateau(tableau_p2, stock_p2, 4, True, "E3")
placer_bateau(tableau_p2, stock_p2, 5, True, "D4")
#placer_bateau(tableau_p2, stock_p2, 2, True, "B5")
#placer_bateau(tableau_p2, stock_p2, 5, True, "D8")

#affiche_tab(tableau_p2, "P2")

score_p1 = attaque(tableau_p2, "A1", score_p1)
score_p2 = attaque(tableau_p1, "E1", score_p2)

score_p1 = attaque(tableau_p2, "A1", score_p1)
#affiche_tab(tableau_p2, "P2")
#affiche_tab(tableau_p1, "P1")
score_p2 = attaque(tableau_p1, "A1", score_p2)
#score_p2 = attaque(tableau_p1, "B1", score_p2)
#score_p2 = attaque(tableau_p1, "C1", score_p2)
#score_p2 = attaque(tableau_p1, "A2", score_p2)
#score_p2 = attaque(tableau_p1, "A3", score_p2)
#score_p2 = attaque(tableau_p1, "A6", score_p2)
#score_p2 = attaque(tableau_p1, "A7", score_p2)
#score_p2 = attaque(tableau_p1, "A8", score_p2)
#score_p2 = attaque(tableau_p1, "D4", score_p2)
#score_p2 = attaque(tableau_p1, "D5", score_p2)
#score_p2 = attaque(tableau_p1, "D6", score_p2)
#score_p2 = attaque(tableau_p1, "D7", score_p2)
#score_p2 = attaque(tableau_p1, "D8", score_p2)
#score_p2 = attaque(tableau_p1, "E3", score_p2)
#score_p2 = attaque(tableau_p1, "E4", score_p2)
#score_p2 = attaque(tableau_p1, "E5", score_p2)
#attaque(tableau_p1, "E6", score_p2)
#affiche_tab(tableau_p1, "P2")
print(score_p2)