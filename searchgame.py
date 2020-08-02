#!/usr/bin/python3
import numpy as np
import math

def fibonacci_sphere(samples=1):

    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        
        radius = math.sqrt(1 - y * y)  # radius at y
        
        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append((x, y, z))

    return points

def genCubePoints(countPoints, a):
    a = 5
    mas = fibonacci_sphere(5)
    

    randomAngle = np.random.uniform(0, 90)

    xRotation = np.array([[1,0,0], [0,math.cos(randomAngle),-math.sin(randomAngle)],
                            [0, math.sin(randomAngle), math.cos(randomAngle)]])
    yRotation = np.array([[math.cos(randomAngle), 0, math.sin(randomAngle)], [0,1,0],
                            [-math.sin(randomAngle), 0, math.cos(randomAngle)]])
    zRotation = np.array([[math.cos(randomAngle),-math.sin(randomAngle), 0], 
                            [math.sin(randomAngle), math.cos(randomAngle), 0],[0, 0, 1]])
    x = []
    y = []
    z = []

    for m in mas:
        x.append(m[0])
        y.append(m[1])
        z.append(m[2])
    

    matrix = xRotation.dot(np.stack([x,y,z]))
    matrix = yRotation.dot(matrix)
    matrix = zRotation.dot(matrix)

    finaleMatrix = np.empty((0,3))

    for j in range(len(matrix[0])):

        tempMatrix = np.stack([matrix[0][j],matrix[1][j],matrix[2][j]])
        maxChoordAbs = np.amax(abs(tempMatrix))
        cubeTempMatrix = tempMatrix.copy()
        for k in range(len(cubeTempMatrix)):
            if abs(cubeTempMatrix[k]) == maxChoordAbs:
                cubeTempMatrix[k] = a/2
            else:
                cubeTempMatrix[k] = (a/2)*cubeTempMatrix[k]/maxChoordAbs
        cubeTempMatrix = [math.copysign(cubeTempMatrix[i],tempMatrix[i]) for i in range(3)]
        finaleMatrix = np.vstack([finaleMatrix, cubeTempMatrix])

    x = []
    y = []
    z = []

    for row in finaleMatrix:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
    
    return finaleMatrix

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

            #print(np.linalg.norm(a-bPoint))
            result = True
            break
    return result


def main():

    countPoints = int(input('Количество точек: '))
    R = float(input('Радиус обнаружения: '))
    a = float(input('Длина ребра куба: '))
    gamesCount = int(input('Количество игр: '))

    """countPoints = 5
    R = 2
    a = 5
    gamesCount = 10"""
    count = 0

    for x in range(gamesCount):

        aPoints = genCubePoints(countPoints, a)
        #aPoints = genPoints(countPoints, a)
        #print(aPoints)

        bPoint = genPoints(1, a)
        
        if checkResult(aPoints, bPoint, R):
            count += 1

    print('Цена игры численным методом: ', count/gamesCount)

    cubeArea = (a ** 2) * 6
    cireckeArea = countPoints * np.pi * (R ** 2)
    print('Цена игры аналитическим методом: ', cireckeArea/cubeArea)


if __name__ == "__main__":
    main()
