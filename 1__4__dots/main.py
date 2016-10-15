import random
import math


# генерация точек со случайными координатами
file = open('dots.txt', 'w')
num = 10
x, y = 0, 0
for i in range(num):
    random.seed(version=2)
    x = random.randint(-20, 20) + random.random()
    y = random.randint(-20, 20) + random.random()
    file.write(str(round(x, 4)) + ' ' + str(round(y, 4)) + '\n')
file.close()


# списки для координат из файла
dot_x = []
dot_y = []
file = open('dots2.txt', 'r')  # либо dots.txt

# чтение из файла
for line in file:
    n1, n2 = line.split(' ')
    dot_x.append(float(n1))
    dot_y.append(float(n2))
file.close()

print("точки: ")
print("x: ", dot_x)
print("y: ", dot_y)

# список для расстояний м/у точками
distance = []
l = len(dot_x)
for i in range(l):
    for j in range(i, l, 1):  # начать с i-той, чтобы не вычислять уже вычисленное
        if i != j:
            distance.append(math.sqrt(math.pow((dot_x[i] - dot_x[j]), 2.0) + math.pow((dot_y[i] - dot_y[j]), 2.0)))
print("расст.: ",  distance)
min = min(distance)
print('минимальное расст.: ' + str(min))
max = max(distance)
print('максимальное расст.: ' + str(max))

#  для проверки - расстояния для точек из файла dots2.txt вычисленные вручную
print(math.sqrt(2), math.sqrt(13), math.sqrt(29), math.sqrt(5), math.sqrt(17), math.sqrt(10))