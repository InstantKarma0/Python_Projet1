import tkinter as tk
from util.formatedString import formatedTime as formatedTime
from time import sleep, time
from threading import *

class ChronoFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.laps = []
        self.stop = True
        self.currentTime = "00:00.00"
        self.start = 0

        self.thread1 = Thread(target = self.updateTime)
        self.thread1.start()

        self.labelTime = tk.Label(self, text=self.currentTime)
        self.labelTime.pack()

        self.startButton = tk.Button(self, text="Start", command=self.chronoStart)
        self.startButton.pack()

        self.endButton = tk.Button(self, text="Stop", command=self.chronoStop)
        self.endButton.pack()



    def chronoStart(self):
        if self.start == 0:
            self.start = round(time() * 100)

        self.stop = False
        #self.threadingUpdate()
        
    def chronoStop(self):
        print(self.stop)
        if self.stop == False:
            self.endButton["command"] = self.reinitChrono
            self.endButton["text"] = "Reinitialiser"
            
        self.stop = True
        self.start = 0
        
        
        
    def reinitChrono(self):
        print("reinit")
        
        self.currentTime = "00:00.00"
        self.labelTime["text"] = self.currentTime
        self.endButton["command"] = self.chronoStop()
        self.endButton["text"] = "Stop"
            
    def updateTime(self):
        while True:
            
            if self.stop == False:
                now = (round(time() * 100)) - self.start
                self.currentTime = formatedTime(now)
                self.labelTime["text"] = self.currentTime
                
            sleep(0.01)




if __name__ == "__main__":
    app = ChronoFrame()
    app.mainloop()