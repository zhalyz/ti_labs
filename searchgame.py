#!/usr/bin/python3
import numpy as np


def genPoints(countPoints, a):
    array = np.zeros(3)
    for x in range(countPoints):
        randPlane = np.random.randint(0, 5)
        arrayx = np.random.uniform(-a/2, a/2, size=3)
        if randPlane == 0:
            arrayx[0] = -a/2
        elif randPlane == 1:
            arrayx[0] = a/2
        elif randPlane == 2:
            arrayx[1] = -a/2
        elif randPlane == 3:
            arrayx[1] = a/2
        elif randPlane == 4:
            arrayx[2] = -a/2
        elif randPlane == 5:
            arrayx[2] = a/2
        array = np.vstack([array, arrayx])
    array = np.delete(array, 0, axis=0)
    return array


def checkResult(aPoints, bPoint, R):
    result = False
    for a in aPoints:
        if np.linalg.norm(a-bPoint) <= R:
            result = True
            break
    return result


def main():

    countPoints = int(input('Количество точек: '))
    R = float(input('Радиус обнаружения: '))
    a = float(input('Длина ребра куба: '))
    gamesCount = int(input('Количество игр: '))
    count = 0

    for x in range(gamesCount):
        aPoints = genPoints(countPoints, a)
        bPoint = genPoints(1, a)
        if checkResult(aPoints, bPoint, R):
            count += 1
    print('Цена игры численным методом: ', count/gamesCount)

    cubeArea = (a ** 2) * 6
    cireckeArea = countPoints * np.pi * (R ** 2)
    print('Цена игры аналитическим методом: ', cireckeArea/cubeArea)


if __name__ == "__main__":
    main()
