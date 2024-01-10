class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setX(self, a):
        self.__x = a

    def setY(self, b):
        self.__y = b

    def __str__(self):
        return 'Point({}, {})'.format(self.__x, self.__y)


class Rectangle(Point):
    def __init__(self, x, y, lg, ln):
        super().__init__(x, y)
        self.lg = lg
        self.ln = ln

    def getlg(self):
        return self.lg

    def getln(self):
        return self.ln

    def setlg(self, llg):
        self.lg = llg

    def setln(self, lln):
        self.ln = lln

    def aire(self):
        return self.lg * self.ln

    def __str__(self):
        return f"Rectangle({super().__str__()}, Longueur: {self.lg}, Largeur: {self.ln})"


class Parallelepipede(Rectangle):
    def __init__(self, x, y, lg, ln, lh):
        super().__init__(x, y, lg, ln)
        self.lh = lh

    def getlh(self):
        return self.lh

    def setlh(self, llh):
        self.lh = llh

    def aire(self):
        return 2 * (self.ln * self.lg + self.lg * self.lh + self.lh * self.ln)

    def volume(self):
        return self.lg * self.ln * self.lh

    def __str__(self):
        return f"Parallelepipede({super().__str__()}, Hauteur: {self.lh}, Volume: {self.volume()})"


# Exemple d'utilisation
parallelepiped = Parallelepipede(1, 2, 5, 3, 4)
print(parallelepiped)
print(f"Aire du parallelepiped: {parallelepiped.aire()}")
print(f"Volume du parallelepiped: {parallelepiped.volume()}")
