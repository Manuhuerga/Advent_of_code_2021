import numpy as np
filename = 'input.txt'

arr  = []

def extract_data(filename):

    with open(filename) as f:
        data = f.read().splitlines()

    for d in data:
        p1,p2 = d.split(' -> ') 
        p1,p2 = sorted([p1,p2])

        p1 = p1.split(',')
        p2 = p2.split(',')

        p1 = list(map(int,p1))
        p2 = list(map(int,p2))

        p1,p2 = sorted([p1,p2])

        x1,y1 = p1
        x2,y2 = p2

        arr.append([x1,y1,x2,y2])

    return arr



def part1(arr):
    _map= np.zeros((1000,1000))
    for a in arr:
        x1,y1,x2,y2 = a
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    _map[x][y] += 1

    acum = 0
    for i in _map:
        for j in i:
            if j>1:
                acum +=1

    print(acum)


def part2(arr):
    _map= np.zeros((1000,1000))
    for a in arr:
        x1,y1,x2,y2 = a
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    _map[x][y] += 1
        else:
            if x1 <= x2 and y1 <= y2:
                for i in range(x2-x1 + 1):
                    _map[x1+i][y1+i] += 1
            else:
                for i in range(x2-x1 + 1):
                    _map[x1+i][y1-i] += 1

    acum = 0
    for i in _map:
        for j in i:
            if j>1:
                acum +=1

    print(acum)

arr = extract_data(filename)
part1(arr)
part2(arr)