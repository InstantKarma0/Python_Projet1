from time import time, sleep


class Chronometer():
    def __init__(self):
        self._laps = []
        self._stop = False
        self.currentTime = "00:00.:00"



    def chronoStart(self):
        start = round(time() * 100)
        now = 0
        
        while not self._stop:
            print("oui")
            now = (round(time() * 100)) - start
            self.currentTime = self.formatedTime(now)
            sleep(0.05)
        
    def chronoStop(self):
        self._stop = True


    def formatedTime(self,i):
        """Return the time on a format MM:ss:cs from a int
        
        Keyword Arguments:\n
        i -- time in centiseconde
        
        Return a String"""
        
        cs = i % 100
        
        secondes = (i // 100) % 60
        
        minu = i // 6000
        
        if cs < 10:
            cs = "0" + str(cs)
        if secondes < 10:
            secondes = "0" + str(secondes)
        if minu < 10:
            minu = "0" + str(minu)
            
        return "{}:{}.{}".format(minu, secondes, cs)
    





    #                   GETTER SETTER

    #   self.stop

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, bool):
        self._stop = bool

    #   self.laps

    @property
    def laps(self):
        return self._laps

    @laps.setter
    def laps(self, newList):
        self._laps = newList



if __name__ == "__main__":
    chrono = Chronometer()
    chrono.chronoStart()