import re
import threading
from time import sleep, time

verif = False
def _ajustement_ (toSplit):
    toSplit = temps.split(':')
    #On split le format afin d'avoir les heures/minutes/secondes de manière disctincte
    for x in range(len(toSplit)) :
        toSplit[x] = int(toSplit[x])
    #On change le type des entrées en int afin de faire, si nécessaie, des opérations dessus

    if toSplit[2] >= 60:
        toSplit[1] += toSplit[2]//60
        toSplit[2] = toSplit[2]%60

    if toSplit[1] >= 60:
        toSplit[0] += toSplit[1]//60
        toSplit[1] = toSplit[1]%60
    #On affine ce que l'utilisateur à entré
    print (toSplit)
    return toSplit

def compteur (Tab) :
    tabCompteur = _ajustement_(Tab)
    total= tabCompteur[0]*3600+tabCompteur[1]*60+tabCompteur[2]
    return total

while not verif:
    temps = input('Combien de temps voulez vous mettre ? (hh:mm:ss)')
    verif = re.search('^[0-9]*:[0-9]*:[0-9]*$', temps)
#Demande et vérification de l'entrée utilisateur

difference = compteur(temps)
print (difference)

start = time()
h = difference // 3600
difference = difference % 3600
m = difference // 60
difference = difference % 60
s = difference


for y in range(400):
    end = time()
    sleep(1)
    print(round(difference - (end - start)))
    print("{}:{}.{}".format(h, m, s))


    
