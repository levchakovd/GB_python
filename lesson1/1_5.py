#5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in - 3 - 6 - 2 - 1
import math


print('Сейчас узнаем расстояние между двумя точками А и В')
ax = int(input('Введите Координату Х точки А '))
ay = int(input('Введите Координату Y точки А '))
bx = int(input('Введите Координату Х точки B '))
by = int(input('Введите Координату Y точки B '))

print(round(math.sqrt((bx-ax)**2+(by-ay)**2),3))