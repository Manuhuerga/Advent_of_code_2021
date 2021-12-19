#!/usr/bin/env python3

import numpy as np
from collections import Counter
from skimage import measure

def input_files(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
        lines = [[int(data) for data in d] for d in data]
    return lines

    
    
def part1():  
    data = input_files('input.txt')

    aux_list= []
    for d in range(len(data)):
        for i in range(len(data[0])):
            if i not in [0,len(data[0])-1]:
                if data[d][i] < data[d][i+1] and data[d][i] < data[d][i-1]:
                    if d not in [0,len(data)-1]:
                        if data[d][i] < data[d+1][i] and data[d][i] < data[d-1][i]:
                            aux_list.append(data[d][i])
                    else:
                        if d == 0:
                            if data[d][i] < data[d+1][i]:
                                aux_list.append(data[d][i])
                        else:
                            if data[d][i] < data[d-1][i]:
                                aux_list.append(data[d][i])
            else:
                if i==0:                    
                    if data[d][i] < data[d][i+1]:
                        if d not in [0,len(data)-1]:
                            if data[d][i] < data[d+1][i] and data[d][i] < data[d-1][i]:
                                aux_list.append(data[d][i])
                        else:
                            if d == 0:
                                if data[d][i] < data[d+1][i]:
                                    aux_list.append(data[d][i])
                            else:
                                if data[d][i] < data[d-1][i]:
                                    aux_list.append(data[d][i])

                else:
                    if data[d][i] < data[d][i-1]:
                        if d not in [0,len(data)-1]:
                            if data[d][i] < data[d+1][i] and data[d][i] < data[d-1][i]:
                                aux_list.append(data[d][i])
                        else:
                            if d == 0:
                                if data[d][i] < data[d+1][i]:
                                    aux_list.append(data[d][i])
                            else:
                                if data[d][i] < data[d-1][i]:
                                    aux_list.append(data[d][i])         
    
    return(sum(aux_list) + len(aux_list))



def part2():

    def fill_hmap(row, col, count):
        if data[row][col] != 9:
            count += 1 
            data[row][col] = 9 
            count = fill_hmap(row, col+1, count)
            count = fill_hmap(row, col-1, count)
            count = fill_hmap(row+1, col, count)
            count = fill_hmap(row-1, col, count)
        return count

    data = input_files('input.txt')

    for i in range(len(data)):
        data[i].append(9)
        data[i].insert(0, 9)

    nines = [9] * (len(data[0]))
    data.append(nines)
    data.insert(0, nines)



    aux_list = []
    for d in range(1, len(data)-1):
        for i in range(1, len(data[0])-1):
            b = fill_hmap(d, i, 0)
            if b: 
                aux_list.append(b)

    aux_list.sort()
    return (aux_list[-1] * aux_list[-2] * aux_list[-3])

print(f'Part 1: ',part1())
print(f"Part 2: ",part2())