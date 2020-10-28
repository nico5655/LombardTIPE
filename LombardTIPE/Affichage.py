from tkinter import *
from Boule import Boule, Obstacle
from Calcul import Physique

class Affichage(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.pack(fill=BOTH,expand=1)
        self.boules = []
        a = 10
        b = 10
        self.canvas = Canvas(self,height=1000,width=1000)
        self.canvas.grid()
        for i in range(5,15):
            x = 2 * a * i
            y = 2 * b * i
            circle = self.canvas.create_oval([x - a,y - b,x + a,y + b],outline='red',fill='red')
            bo = Boule(circle,x,y)
            self.boules.append(bo)
        self.physique = Physique()
        self.physique.bouboules = self.boules
        obstacles = []
        for i in range(10):
            a = 20
            b = 100
            y = b * i + b / 2
            x = 800 - a / 2
            rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
            obstacle = Obstacle(rectangle,x - a,y,a,b)
            obstacles.append(obstacle)

        for i in range(10):
            a = 20
            b = 100
            y = b * i + b / 2
            x = a / 2
            rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
            obstacle = Obstacle(rectangle,x - a,y,a,b)
            obstacles.append(obstacle)
        self.physique.obstacles = obstacles

        
        for i in range(10):
            a = 100
            b = 20
            x = a * i + a / 2
            y = b / 2
            rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
            obstacle = Obstacle(rectangle,x - a,y,a,b)
            obstacles.append(obstacle)

        for i in range(10):
            a = 100
            b = 20
            x = a * i + a / 2
            y = 800-b / 2
            rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
            obstacle = Obstacle(rectangle,x - a,y,a,b)
            obstacles.append(obstacle)
        self.physique.obstacles = obstacles



    def update(self):
        for boule in self.boules:
            dx,dy = self.physique.deplacer_boule(boule)
            self.canvas.move(boule.circle,dx,dy)
        self.master.after(50,self.update)
