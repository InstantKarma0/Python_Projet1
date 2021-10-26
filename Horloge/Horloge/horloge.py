from time import sleep
from datetime import datetime


def horloge ():
    for x in range (500):
        sleep(1)
        now = datetime.now()
        completeDate = now.strftime("%d/%m/%Y %H:%M:%S")
        print(completeDate)

if __name__ == "__main__":
    horloge()
