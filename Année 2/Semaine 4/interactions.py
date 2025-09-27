#!/usr/bin/env python3

"""
Exercice 1 :
- Déplacer toute l'interaction utilisateur dans une classe `UI`.
- Aucun `print`/`input` en dehors de la classe.
- Le code hors classe ne fait que créer l'UI et appeler ses méthodes.

Exercice 2 :
- Ajouter un paramètre de constructeur `silent` pour désactiver toute sortie console.
  * En mode silencieux: aucun affichage; les entrées sont lues sans prompt.
"""

from typing import Optional


class UI:
    def __init__(self, silent: bool = False) -> None:
        """Initialise l'interface.

        Args:
            silent: Si True, supprime tout affichage console.
        """
        self.silent = silent

    # --- Méthodes d'aide privées ---
    def _print(self, msg: str) -> None:
        if not self.silent:
            print(msg)

    def _input(self, prompt: Optional[str] = None) -> str:
        """Lit une entrée utilisateur.
        - En mode normal, affiche le prompt (via _print) puis lit l'entrée.
        - En mode silencieux, ne produit aucune sortie et lit directement.
        """
        if not self.silent and prompt:
            self._print(prompt)
            return input()
        return input()

    # --- API publique ---
    def ask_name(self) -> str:
        """Demande et retourne un nom non vide."""
        name: Optional[str] = None
        while not name:
            name = self._input('Quel est votre nom ?')
            if name is not None:
                name = name.strip()
        return name  # type: ignore[return-value]

    def greet(self, name: str) -> None:
        self._print(f'Bienvenue, {name}!')

    def ask_hobby(self) -> str:
        """Demande et retourne un passe-temps non vide."""
        hobby: Optional[str] = None
        while not hobby:
            hobby = self._input('Quel est votre passe-temps préféré ?')
            if hobby is not None:
                hobby = hobby.strip()
        return hobby  # type: ignore[return-value]

    def praise_hobby(self, hobby: str) -> None:
        self._print(f'{hobby}, quelle bonne idée !')


# --- Utilisation (aucun print/input direct en dehors de UI) ---
if __name__ == '__main__':
    # Pour activer le mode silencieux, passez silent=True
    ui = UI(silent=False)

    # Exemple d'enchaînement conforme aux consignes :
    # 1) On récupère des valeurs via l'UI
    name = ui.ask_name()
    # 2) On re-passe ces valeurs à d'autres méthodes de l'UI
    ui.greet(name)

    hobby = ui.ask_hobby()
    ui.praise_hobby(hobby)
