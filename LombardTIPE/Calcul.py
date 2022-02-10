from Boule import Force

class Physique:
    def __init__(self, *args, **kwargs):
        self.bouboules = []#pour les forces
        self.obstacles = []
        self.mspeed = 100
        return super().__init__(*args, **kwargs)

    def ForceTotale(self,boule):
        Ftotale = Force()
        for bo in self.bouboules:
            if not bo.Off:
                Ftotale = Ftotale.add(self.force_repulsion(bo,boule))
        for ob in self.obstacles:
            if ob.Orient == "obs" or ob.Orient == "atr":
                f = self.force_obstacle_boule(ob,boule)
                Ftotale = Ftotale.add(f)
        return Ftotale.add(self.ForceGlobale(boule))

    def ForceGlobale(self,boule):
        x = - 0.1 * boule.VX
        y = - 0.1 * boule.VY
        return Force(x,y)

    def force_obstacle_boule(self,obstacle,boule):
        fx = -obstacle.X + boule.X
        fy = -obstacle.Y + boule.Y
        fa = (fx ** 2 + fy ** 2) ** (1 / 2)
        
        f = Force(fx,fy)
        f = f.multiply(1 / fa)
        if fa > 50:
            fa = fa - 50
        f = f.multiply(10000 / (fa) ** (2))
        if obstacle.Orient == "atr":
            f = f.multiply(-100)
            fa = (fx ** 2 + fy ** 2) ** (1 / 2)
            if fa < 40:
                boule.Off = True
                self.bouboules.remove(boule)
        return f

    def force_repulsion(self,boule1,boule2):#répulsion exercée par boule1 sur boule2
        if boule1 == boule2:#la boule n'agit pas sur elle-même.
            return Force()
        fx = boule1.X - boule2.X
        fy = boule1.Y - boule2.Y
        fa = (fx ** 2 + fy ** 2) ** (1 / 2)

        f = Force(fx,fy)
        f = f.multiply(1 / fa)
        if fa > 20:
            fa = fa - 20
        elif fa > 10:
            fa = fa - 10
        elif fa > 5:
            fa = 1
        else:
            fa=0.1
        f = f.multiply(25 / (fa ** 2))
        return f


    def deplacer_boule(self,boule):
        #paramètres
        dt = 0.1
        m = 0.1

        F = self.ForceTotale(boule)

        #accélération
        ax = F.X / m
        ay = F.Y / m

        #vitesse
        boule.VX += ax * dt
        boule.VY += ay * dt

        if abs(boule.VX) > self.mspeed:
            boule.VX = (boule.VX / abs(boule.VX)) * self.mspeed
        if abs(boule.VY) > self.mspeed:
            boule.VY = (boule.VY / abs(boule.VY)) * self.mspeed

        #position
        dx = boule.VX * dt
        dy = boule.VY * dt

       # for bo in self.bouboules:
        #    if boule != bo:
         #       fx = boule.X + dx - bo.X
          #      fy = boule.Y + dy - bo.Y
           #     fa = (fx ** 2 + fy ** 2) ** (1 / 2)
            #    if fa < 10:
             #       boule.VX = -boule.VX
              #      boule.VY = -boule.VY
               #     dx = -dx
                #    dy = -dy

        for ob in self.obstacles:
            deltaX = (ob.X - (boule.X))
            delta2X = deltaX - dx
            if (ob.X - (boule.X)) * (ob.X - (boule.X + dx)) < 0 and ob.Orient == 'v':
                dx = -dx
                boule.VX = -boule.VX
            if (ob.Y - (boule.Y)) * (ob.Y - (boule.Y + dy)) < 0 and ob.Orient == 'h':
                dy = -dy
                boule.VY = -boule.VY


        boule.X = boule.X + dx
        boule.Y = boule.Y + dy
        return dx,dy