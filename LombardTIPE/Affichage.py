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
        for j in range(3,6):
            for i in range(4,25):
                x = 3* a * j
                y = 3 * b * i
                circle = self.canvas.create_oval([x - a,y - b,x + a,y + b],outline='red',fill='red')
                bo = Boule(circle,x,y)
                self.boules.append(bo)

        self.physique = Physique()
        self.physique.bouboules = self.boules
        obstacles = []
        a = 20
        b = 1000
        y = 500
        x = 1000 - a / 2
        rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
        obstacle = Obstacle(rectangle,x - a,y,a,b,'v')
        obstacles.append(obstacle)

        a = 20
        b = 1000
        y = 500
        x = a / 2
        rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
        obstacle = Obstacle(rectangle,x + a,y,a,b,'v')
        obstacles.append(obstacle)
        self.physique.obstacles = obstacles

        
        a = 1000
        b = 20
        x = 500
        y = b / 2
        rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
        obstacle = Obstacle(rectangle,x,y + b,a,b,'h')
        obstacles.append(obstacle)

        a = 1000
        b = 20
        x = a / 2
        y = 800 - b / 2
        rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
        obstacle = Obstacle(rectangle,x,y - b,a,b,'h')
        obstacles.append(obstacle)

        a = 50
        b = 50
        x = 450
        y = 300
        rectangle = self.canvas.create_rectangle([x - a,y - b,x + a,y + b],outline='black',fill='white')
        obstacle = Obstacle(rectangle,x,y,a,b,'obs')
        obstacles.append(obstacle)

        a = 50
        b = 50
        x = 650
        y = 350
        coin1 = self.canvas.create_oval([x - a,y - b,x + a,y + b],outline='black',fill='gold')
        obsc1 = Obstacle(coin1,x,y,a,b,"atr")
        obstacles.append(obsc1)
        self.canvas.tag_lower(coin1)
        self.physique.obstacles = obstacles



    def update(self):
        for boule in self.boules:
            if not boule.Off:
                dx,dy = self.physique.deplacer_boule(boule)
                self.canvas.move(boule.circle,dx,dy)
                if boule.Off:
                    self.canvas.itemconfig(boule.circle,fill="blue")
        self.master.after(100,self.update)
