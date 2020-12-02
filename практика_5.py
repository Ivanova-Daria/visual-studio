
from package1 import *
x = float(input("Ширина комнаты: "))
y = float(input("Длинна комнаты: "))
z = float(input("Высота комнаты: "))
r1 = Room.Room(x, y, z) 
r1.square() #общая  площадь квартиры

r1.addWD(1, 1)  #площадь окна
r1.addWD(1, 1) #площадь окна
r1.addWD(1, 2) #площадь двери
print("Площадь оклеиваемой поверхности =", r1.workSurface())
print("Понадобиться", r1.roll(int(input("Ширина рулона:")),int(input("Длинна рулона:"))),"рулонов")

