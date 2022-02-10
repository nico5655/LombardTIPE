
class Boule:
    def __init__(self,circle,x=0,y=0, off=False, *args, **kwargs):
        self.circle=circle
        self.X=x
        self.Y=y
        self.VX=0
        self.VY=0
        self.Off=off
    

class Force:
    def __init__(self,x=0.,y=0.):
        self.X=x
        self.Y=y

    def add(self,force):
        x = self.X + force.X
        y = self.X + force.Y
        return Force(x,y)

    def multiply(self,scalar):
        return Force(scalar*self.X,scalar*self.Y)


class Obstacle:
    def __init__(self,rectangle,x,y,a,b,orient):
        self.X=x
        self.Y=y
        self.A=a
        self.B=b
        self.Orient=orient
        self.rectangle=rectangle
