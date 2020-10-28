from Boule import Force

class Physique:
    def __init__(self, *args, **kwargs):
        self.bouboules = []#pour les forces
        self.obstacles = []
        return super().__init__(*args, **kwargs)

    def ForceTotale(self,boule):
        Ftotale = Force()
        for bo in self.bouboules:
            Ftotale = Ftotale.add(self.force_repulsion(bo,boule))
        for ob in self.obstacles:
            Ftotale = Ftotale.add(self.force_obstacle_boule(ob,boule))
        return Ftotale.add(self.ForceGlobale(boule))

    def ForceGlobale(self,boule):
        x = 10 - 0.1 * boule.VX
        y = 20-0.1 * boule.VY
        return Force(x,y)

    def force_repulsion(self,boule1,boule2):#répulsion exercée par boule1 sur boule2
        if boule1 == boule2:#la boule n'agit pas sur elle-même.
            return Force()
        fx = 1 / (boule1.X - boule2.X)
        fy = 1 / (boule1.Y - boule2.Y)
        return Force(5*fx,5*fy)

    def force_obstacle_boule(self,obstacle,boule):
        fx = 1 / (obstacle.X - boule.X)
        fy = 1 / (obstacle.Y - boule.Y)
        return Force(- 6 * ((fx) ** 2) * (boule.VX), - 6 * ((fy) ** 2) * (boule.VY))

    def deplacer_boule(self,boule):

        #paramètres
        dt = 0.05
        m = 0.1

        F = self.ForceTotale(boule)

        #accélération
        ax = F.X / m
        ay = F.Y / m

        #vitesse
        boule.VX += ax * dt
        boule.VY += ay * dt

        #position
        dx = boule.VX * dt
        dy = boule.VY * dt
        boule.X = boule.X + dx
        boule.Y = boule.Y + dy

        return dx,dy