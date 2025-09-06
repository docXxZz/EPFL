def probleme_echauffement(a):
    return(a//3-2)
print(probleme_echauffement(55131))


ma_liste = [55131, 114008, 145297, 76135, 50317, 134036, 122136, 97704, 51245, 141732, 120427, 142020, 88166, 55313, 110391, 112436, 78195, 74294, 128984, 68240, 137098, 142016, 83577, 89257, 107744, 67357, 131342, 98247, 137501, 134577, 65696, 84925, 50159, 110319, 91921, 103303, 84505, 84683, 100811, 82626, 66774, 123216, 95151, 88237, 60705, 124319, 102926, 143160, 92780, 64283, 132434, 113935, 84907, 113698, 117240, 129327, 78837, 144841, 138054, 130990, 100191, 141768, 138941, 108165, 62138, 121690, 117305, 90147, 134422, 78031, 121331, 120947, 120235, 138880, 141076, 119480, 66844, 77660, 106364, 99187, 144244, 120483, 77715, 135703, 125521, 123253, 127556, 96458, 91965, 73924, 95176, 87540, 122083, 146013, 67761, 100413, 145994, 149450, 94330, 112824]

nouvelle_liste = []

for valeur in ma_liste:
    somme = 0

    while valeur > 0:
        somme += valeur

        valeur /= 3
        valeur = round(valeur / 3)
        valeur -= 2
        valeur = round(valeur - 2)

    print(f"Somme totale pour cet élément : {somme}")
    nouvelle_liste.append(somme)

print("\nNouvelle liste :")
print(nouvelle_liste)




































class CPU :

    def __init__(self, code: str):
        self.code = nouvelle_liste
        self.indice = 0
        self.registres = [00, 1, 2, 3, ]
        a=0
        b=1
        c=2
        d=3
        add :1
        sub :2
        mul :3
        

    # Appelée à chaque instruction.
    # Retourne True si le programme doit continuer, False si le programme doit s'arrêter.
    def executer_instruction(self) -> bool:
        match self.code[self.indice]:
            case 0x01:
                # ADD
                gauche = self.registres[self.code[self.indice+2]]
                droite = self.registres[self.code[self.indice+3]]
                self.registres[self.code[self.indice+1]] = gauche + droite
                # Les registres font 32 bits:
                self.registres[self.code[self.indice+1]] %= 2**32
                self.indice += 4
        return True # MODIFIEZ-MOI


def probleme_1(entree: str) -> int:
    cpu = CPU(entree) # Vous pouvez ajouter des paramètres à __init__
    while cpu.executer_instruction():
        pass # Executer les instructions en boucle jusqu'à ce que executer_instruction retourne False
    # Mettre ici le code pour calculer la réponse

def probleme_2(entree: str) -> int:
    cpu = CPU() # Vous pouvez ajouter des paramètres à __init__
    while cpu.executer_instruction():
        pass # Executer les instructions en boucle jusqu'à ce que executer_instruction retourne False
    # Mettre ici le code pour calculer la réponse

def probleme_3(entree: str) -> int:
    cpu = CPU() # Vous pouvez ajouter des paramètres à __init__
    while cpu.executer_instruction():
        pass # Executer les instructions en boucle jusqu'à ce que executer_instruction retourne False
    # Mettre ici le code pour calculer la réponse

def probleme_final(entree: str) -> int:
    pass # Mettez votre code ici!

### LOCAL ###

def read_input(filename: str) -> str:
    with open(filename, "r") as f:
      return f.read()

# print(probleme_echauffement(read_input("poids.txt")))
# print(probleme_1(read_input("programme_1.txt")))
# print(probleme_2(read_input("programme_2.txt")))
# print(probleme_3(read_input("programme_3.txt")))
# print(probleme_final(read_input("programme_final.txt")))

### CODEFORCES ###
def read_multiline_input() -> str:
    _ = input() # On ignore le commentaire.
    lines = int(input())
    content = ""
    for i in range(lines):
        content += input() + "\n"
    return content

# Pour valider l'échauffement sur codeforces, décommenter la ligne suivante:
# print(probleme_echauffement(read_multiline_input()))

# Pour le problème 1 sur codeforces (recommenter les autres lignes)
# print(probleme_1(read_multiline_input()))

# Problème 2
# print(probleme_2(read_multiline_input()))

# Problème 3
# print(probleme_3(read_multiline_input()))

# Problème final
# print(probleme_final(read_multiline_input()))
