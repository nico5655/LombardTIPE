from tkinter import *
from Affichage import Affichage

tk=Tk()
tk.geometry("1000x1000")
affichage=Affichage(tk)
affichage.update()
tk.mainloop()