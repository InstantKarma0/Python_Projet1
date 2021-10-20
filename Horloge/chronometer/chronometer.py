from time import time,sleep
from random import randint

def chronoStart():
    start = round(time() * 10000) // 100
    laps = []
    stop = False
    
    now = int()
    diff = int()
    
    while stop == False:
        now = (round(time() * 10000) // 100) - start
        print(formatedTime(now))
        sleep(0.05)
        


def formatedTime(i):
    """Return the time on a format MM:ss:cs from a int
    
    Keyword Arguments:\n
    i -- time in centiseconde
    
    Return a String"""
    
    ANSI_RESET = "\u001B[0m"
    tb = ["\u001B[30m",
    "\u001B[31m",
    "\u001B[32m",
    "\u001B[33m",
    "\u001B[34m",
    "\u001B[35m",
    "\u001B[36m",
    "\u001B[37m",]
    
    cs = i % 100
    
    secondes = (i // 100) % 60
    
    minu = i // 6000
    
    if cs < 10:
        cs = "0" + str(cs)
    if secondes < 10:
        secondes = "0" + str(secondes)
    if minu < 10:
        minu = "0" + str(minu)
        
    return tb[randint(0,len(tb)-1)] + "{}:{}.{}".format(minu, secondes, cs) + ANSI_RESET
    
    
if __name__ == "__main__":
    chronoStart()