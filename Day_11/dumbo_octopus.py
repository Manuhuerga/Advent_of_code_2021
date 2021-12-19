#!/usr/bin/env python3
import numpy as np

mat = np.genfromtxt('input.txt', delimiter=1)

total = 0
step = 0
while np.any(mat):
    step += 1
    mat += 1
    flashing = np.argwhere(mat > 9)  #retorna los indices que son mayores a 9

    while len(flashing):
        for x, y in flashing:
            box = np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2]

            mat[box] += mat[box] > 0
            mat[x,y] = 0

        flashing = np.argwhere(mat > 9)

    total += np.count_nonzero(mat == 0)

    if step == 100:
        print(f'Part 1: {total}')

print(f'Part 2: {step}')

