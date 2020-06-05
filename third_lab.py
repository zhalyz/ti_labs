#!/usr/bin/python3

import numpy as np
from random import randint


def unzip(C):

    A = C[:, :, 0]
    B = C[:, :, 1]
    return A, B


def nashEq(A, B): return ((np.amax(A, 0) == A) & (np.amax(B.T, 0) == B.T).T)


def optimaPareto(A, B):

    optimalList = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            optimaMatrix = (A[i][j] <= A)
            optimaMatrix[i][j] = False
            if True in optimaMatrix:
                if not True in ((B[i, j] <= B) & optimaMatrix):
                    optimalList.append((i, j))
            else:
                optimalList.append((i, j))
    return optimalList


def gameOne(game):

    print(game)
    A, B = unzip(game)
    nash = nashEq(A, B)
    nash = list(zip(*np.nonzero(nash)))
    print('Равновесие Нэша:')
    for x, y in nash:
        print('x={} y={} v={}'.format(x, y, game[x, y]))
    print()
    pareto = optimaPareto(A, B)
    print('Оптимальность Парето:')
    for x, y in pareto:
        print('x={} y={} v={}'.format(x, y, game[x, y]))
    print()
    print('Пересечение множеств:')
    inter = set(nash) & set(pareto)
    for x, y in inter:
        print('x={} y={} v={}'.format(x, y, game[x, y]))
    print()


def mix(A, B):

    e1 = np.ones(A.shape[0])
    v1 = 1 / np.dot(np.dot(e1, np.linalg.inv(A)), e1)
    v2 = 1 / np.dot(np.dot(e1, np.linalg.inv(B)), e1)
    y = np.dot(np.dot(v1, np.linalg.inv(A)), e1)
    x = np.dot(np.dot(v2, e1), np.linalg.inv(B))
    return np.around(x, 3), np.around(y, 3), np.around((v1, v2), 3)


def dominantStrategy(A):

    temp = A[0] <= A[1]
    temp2 = A[0] >= A[1]
    equil = A[0] == A[1]
    if equil.sum() == 2:
        return False
    if temp.sum() == 2 or temp2.sum() == 2:
        return True
    else:
        return False


def gameTwo(game):

    print('Матрица по варианту')
    print(game)
    A, B = unzip(game)
    nash = nashEq(A, B)
    nash = list(zip(*np.nonzero(nash)))
    if dominantStrategy(A) or dominantStrategy(B):
        print('В игре по крайней мере один игрок имеет строго доминирующую стратегию.')
        print('Следовательно смешанное расширение имеют единвтсвенную ситуацию равновесия по Нэшу.')
        print('Равновесие Нэша:')
        print(nash)
    if len(nash) == 0:
        if (A[0] != A[1]).sum() == 2 and (B[0] != B[1]).sum() == 2:
            x, y, v = mix(A, B)
            print('Игра не имеет ситуации равновесия по Нэшу в чистых стратегиях.')
            print('Вполне смешанная ситуация равновесия:x={} y={} v1={} v2={}'.format(
                x, y, v[0], v[1]))
        else:
            print('Error, singular matrix')
    if len(nash) == 2:
        if (A[0] != A[1]).sum() == 2 and (B[0] != B[1]).sum() == 2:
            print('Равновесие Нэша:')
            for x, y in nash:
                print('x={} y={} v={}'.format(x, y, game[x, y]))
            print()

            print('Игра имеет две ситуации равновесия по Нэшу в чистых стратегиях:')
            x, y, v = mix(A, B)

            print('x={} y={} v1={} v2={}'.format(x, y, v[0], v[1]))
        else:
            print('Error, singular matrix')


def main():
    eps1 = 0.3
    eps2 = 0.7
    cross = np.array([[(1, 1), (1-eps1, 2)], [(2, 1-eps2), (0, 0)]])
    family = np.array([[(4, 1), (0, 0)], [(0, 0), (1, 4)]])
    prison = np.array([[(-5, -5), (0, -10)], [(-10, 0), (-1, -1)]])
    randomMatrix = np.array([[(randint(-50, 50), randint(-50, 50)) for x in range(10)]
                             for y in range(10)])
    names = ['Перекресток', 'МЖ', 'Заключенные', 'Случайная матрица']
    for name, game in zip(names, (cross, family, prison, randomMatrix)):
        print(name)
        gameOne(game)
    game = np.array([[(3, 8), (2, 4)], [(1, 3), (12, 5)]])
    gameTwo(game)


if __name__ == "__main__":
    main()
