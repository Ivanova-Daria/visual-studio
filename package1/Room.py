class Win_Door:
     def __init__(self, x, y):
          self.square = x * y



class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []
    def square(self):
        self.square = 2 * self.height * (self.width + self.lenght)
        return self.square
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square
    def roll(self,rw,rl):
      n = self.workSurface()/(rw*rl)
      if n>round(n):
           return round(n)+1
      else:
           return round(n)




