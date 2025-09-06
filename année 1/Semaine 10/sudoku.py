import tkinter as tk
import random

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")  # Titre vide
        self.taille = 9
        self.sous_taille = 3
        self.grille_complete = [[0 for _ in range(self.taille)] for _ in range(self.taille)]  # Solution
        self.grille_joueur = [[0 for _ in range(self.taille)] for _ in range(self.taille)]  # Grille du joueur
        self.cases = [[None for _ in range(self.taille)] for _ in range(self.taille)]
        self.generer_grille()
        self.creer_interface()

    def est_valide(self, ligne, col, num, grille):
        """Vérifie si un nombre peut être placé dans une case donnée."""
        for x in range(self.taille):
            if grille[ligne][x] == num:
                return False
        for x in range(self.taille):
            if grille[x][col] == num:
                return False
        debut_ligne = ligne - ligne % self.sous_taille
        debut_col = col - col % self.sous_taille
        for i in range(debut_ligne, debut_ligne + self.sous_taille):
            for j in range(debut_col, debut_col + self.sous_taille):
                if grille[i][j] == num:
                    return False
        return True

    def remplir_grille(self, grille):
        """Remplit la grille de manière récursive pour générer un Sudoku complet."""
        for ligne in range(self.taille):
            for col in range(self.taille):
                if grille[ligne][col] == 0:
                    nums = list(range(1, self.taille + 1))
                    random.shuffle(nums)
                    for num in nums:
                        if self.est_valide(ligne, col, num, grille):
                            grille[ligne][col] = num
                            if self.remplir_grille(grille):
                                return True
                            grille[ligne][col] = 0
                    return False
        return True

    def generer_grille(self):
        """Génère une grille complète et crée un puzzle."""
        self.remplir_grille(self.grille_complete)

        # Copie de la grille complète pour le joueur
        self.grille_joueur = [row[:] for row in self.grille_complete]

        # Supprime des cases pour créer un puzzle
        nb_cases_a_supprimer = 40  # Ajustez selon la difficulté
        cases_supprimees = 0
        while cases_supprimees < nb_cases_a_supprimer:
            ligne = random.randint(0, self.taille - 1)
            col = random.randint(0, self.taille - 1)
            if self.grille_joueur[ligne][col] != 0:
                self.grille_joueur[ligne][col] = 0
                cases_supprimees += 1

    def creer_interface(self):
        """Crée une interface graphique."""
        self.frame = tk.Frame(self.root, bg="#F7F9FC")
        self.frame.pack(pady=20)

        for ligne in range(self.taille):
            for col in range(self.taille):
                case = tk.Entry(
                    self.frame,
                    width=2,
                    font=("Arial", 18),  # Police Arial
                    justify="center",
                    relief="flat",  # Enlève le cadre des cases
                    highlightthickness=1  # Bordure de 1 pixel
                )
                case.grid(row=ligne, column=col, padx=0, pady=0)

                # Si la case est remplie, on l'affiche
                if self.grille_joueur[ligne][col] != 0:
                    case.insert(0, str(self.grille_joueur[ligne][col]))
                    # Assurez-vous que les chiffres déjà remplis restent visibles avec la couleur appropriée
                    if self.grille_joueur[ligne][col] == self.grille_complete[ligne][col]:
                        case.config(fg="#63C956")  # Vert (99, 201, 86)
                    else:
                        case.config(fg="#EC6B60")  # Rouge (236, 107, 96)

                    case.config(state="disabled", disabledbackground="#FFFFFF", disabledforeground="#000000")  # Clair
                else:
                    case.bind("<KeyRelease>", lambda e, r=ligne, c=col: self.valider_au_fur_et_a_mesure(r, c))

                self.cases[ligne][col] = case

    def valider_au_fur_et_a_mesure(self, ligne, col):
        """Valide automatiquement une case lorsque l'utilisateur saisit un chiffre."""
        valeur = self.cases[ligne][col].get()
        if valeur.isdigit() and 1 <= int(valeur) <= 9:
            valeur = int(valeur)
            if self.grille_complete[ligne][col] == valeur:
                self.cases[ligne][col].config(fg="#63C956")  # Vert (99, 201, 86)
            else:
                self.cases[ligne][col].config(fg="#EC6B60")  # Rouge (236, 107, 96)
            self.grille_joueur[ligne][col] = valeur
        else:
            self.grille_joueur[ligne][col] = 0
            self.cases[ligne][col].config(fg="black")  # Réinitialise la couleur à noir si la case est vide ou invalide

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()