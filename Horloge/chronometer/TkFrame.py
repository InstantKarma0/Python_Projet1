import tkinter as tk
from util.formatedString import formatedTime as formatedTime
from time import sleep, time

class ChronoFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.laps = []
        self.stop = True
        self.currentTime = "00:00.01"
        self.start = 0


        self.currentTime = tk.Label(self, textvariable=self.currentTime)
        self.currentTime.pack()

        self.startButton = tk.Button(self, text="Start", command=self.chronoStart)
        self.startButton.pack()

        self.endButton = tk.Button(self, text="Stop", command=self.chronoStop)
        self.endButton.pack()



    def chronoStart(self):
        if self.start == 0:
            self.start = round(time() * 100)

        self.stop = False
        self.updateTime()
        
    def chronoStop(self):
        self.stop = True
    
    def updateTime(self):
        if self.stop == False:
            now = (round(time() * 100)) - self.start
            self.currentTime = formatedTime(now)
            
            sleep(0.5)
            self.updateTime()




if __name__ == "__main__":
    app = ChronoFrame()
    app.mainloop()