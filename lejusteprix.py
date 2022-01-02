#le juste prix

#
# code pour start la game 
#
start = str(input("Commencer la partie ? (tappez ok pour commencer) : "))


while start != "ok":
    start = str(input("Commencer la partie ? (tappez ok pour commencer) : "))

#
#codage du jeu
#  

import random

mystere = random.randint(0,100)

nb1 = int(input("Devinez le nombre mystère : "))

while mystere != nb1 :
    if mystere < nb1 :
        print("Trop grand !")
        nb1 = int(input("Devinez le nombre mystère : "))
    if mystere > nb1 : 
        print("Trop petit !")
        nb1 = int(input("Devinez le nombre mystère : "))
    else :
        print("Bravo vous avez trouvé le nombre mystere !")