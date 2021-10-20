from re import search as regexSearch
from time import sleep, time

def minuteur():
    """ DOCS DE LA FONCTION """
    
    # Input Cheker
    verif = False
    while not verif:
        # Asking user Input
        temps = input('Combien de temps voulez vous mettre ? (hh:mm:ss)')
        # Regex type (XX:XX:XX) where X is Number beetween 0-9
        verif = regexSearch('^[0-9]*:[0-9]*:[0-9]*$', temps)
    #Demande et vérification de l'entrée utilisateur

    startTime = time()
    currentTime = time()
    totalDuration = compteur(temps)

    print(formatedTime(totalDuration))

    while (totalDuration != round(currentTime - startTime)):
        sleep(1)
        currentTime = time()
        if ((totalDuration) - round(currentTime - startTime)) <= 10:
            print("\u001B[31m" + formatedTime((totalDuration) - round(currentTime - startTime)) + "\u001B[0m")
            continue
        print(formatedTime((totalDuration) - round(currentTime - startTime)))
        
    print("\u001B[31m" + "DRINNNNNNNNNNNNNGGGGGGGGG!" + "\u001B[0m")
        

def formatedTime(time):
    """ Translate a total amount of seconds in a Formated String with the format hh:mm:ss
    
    Keyword Arguments:\n
    time -- Int representing a amount of seconds"""
    
    # Get Hours value
    h = time // 3600
    # Removing Hours from time
    time = time % 3600
    # Get minutes value
    m = time // 60
    # Removing minutes from time
    time = time % 60
    # Get seconds values
    s = time
    
    
    if s < 10:
        s = "0" + str(s)
    if m < 10:
        m = "0" + str(m)
    if h < 10:
        h = "0" + str(h)
    
    #Return the formated string
    return "{}:{}:{}".format(h, m, s)
    

def _ajustement_(temps):
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
    return toSplit

def compteur (Tab) :
    tabCompteur = _ajustement_(Tab)
    total= tabCompteur[0]*3600+tabCompteur[1]*60+tabCompteur[2]
    return total


if __name__ == "__main__":
    minuteur()