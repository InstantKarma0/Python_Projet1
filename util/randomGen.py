from random import randint

def randomInt(borneSup, borneInf=0):
    """Return a random Integer beetween both end points

    Keyword arguments:\n
    borneSup -- lower end point.

    Optional Keyword arguments:\n
    borneInf -- upper end point. (default 0).

    Return an Integer"""
    return randint(borneInf, borneSup)
