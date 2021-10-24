from tkinter import *

root = Tk("Horloge")


button_leave = Button(root, text="Fermer", command=root.quit)
button_leave.pack()
root.mainloop()