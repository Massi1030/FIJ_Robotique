#on a au depart, un npmbre aleatoire qui est choisi
# apres, le jeu nous demande e taper un nombre entre 0 et 100
# si la reponsse est inferieur au nombre aleatoire
# il doit afficher "le nombre est plus grand"
#si la reponsse est superieur au nombre aleatoire
# il doit afficher "le nombre est plus petit"
# et sinon, vous avez gange
# ici, on importe une librairie qui contient
# des fonctions aleatoires
# initialise nos variables nbAleatoir et trouver
# nb aleatoire sera generer par l'ordinateur
# trouver est un boolean qui est egale a Faux
# Tant que trouver est egale a Faux on continue
# on converti le nombre taper au clavier en int
# on compare notre reponse avec le nb aleatoire
# on passe trouver a vrai pour arreter la boucle





import random

nbAleatoire = random.randrange(0,100)
trouver = False

while trouver == False :
    print("tape un nombre entre 0 et 100")
    reponse =  int(input())

    if reponse < nbAleatoire :
        print("le nombre est plus grand")
    elif reponse > nbAleatoire :
        print("le nombre est plus petit")
    else:
        print("Gagne !")
        trouver = True
