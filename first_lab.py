#!/usr/bin/python3

def init():
    raw_table = input('table 3x3 plz\n').split(' ')
    matrix = [[0 for x in range(3)] for y in range(3)]
    z = 0
    for x in range(3):
        for y in range(3):
            matrix[x][y]=int(raw_table[z])
            z+=1

    return matrix

def magic(table):
    a = 0
    b = 0
    an = 0
    bn = 0
    masA = [0 for i in range(3)]
    masB = [0 for i in range(3)]
    constKb = 0
    constKa = 100
    epselen = 100
    shag = 1
    print('k   A   B   x1  x2  x3    y1  y2  y3     v\     v/     e')
    while epselen > 0.1:
        a = an
        b = bn
        
        for i in range(3):
            masA[i] = masA[i] + table[a][i]
            masB[i] = masB[i] + table[i][b]
            
        for z in range(0,3):
            if masB[a] < masB[z]:
                an = z

            if masA[b] > masA[z]:
                bn = z
        
        kB = masA[bn]/(shag)
        kA = masB[an]/(shag)
        if kB > constKb:
            print(shag)
            constKb = kB

        if kA < constKa:
            print('!!!= ',shag)
            constKa = kA

          print(shag,' ', a+1,' ',b+1,' ',masB,'  ', masA,' ', masB[an],'/',shag,'  ',masA[bn],'/',shag,' ',epselen)
        shag+=1
            
if __name__ == "__main__":
    table = init()
    print(table)
    print()
    magic(table)
