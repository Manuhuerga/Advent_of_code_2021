#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


def input_files(filename : str) -> str:
    data,op = open(filename).read().split('\n\n')
    data = [[int(data) for data in d.split(',')] for d in data.split('\n')]
    op =  [[line[11], int(line[13:])] for line in op.split('\n')]
    for i in range(len(op)):
        if op[i][0] == 'y':
            op[i][0] = 0
        else:
            op[i][0]= op[i][1]
            op[i].pop()
            op[i].append(0)
        
    return data,op


data,op = input_files('input.txt')


def dots(data, op):
    aux_list = []
    for o in op:
        dx, dy = o
        s = set()
        for d in data:
            d = tuple(d)
            x, y = d
            if dy != 0 and y > dy:
                y = dy - abs(y - dy)
                s.add((x, y))
            elif dx != 0 and x > dx:
                x = dx - abs(x - dx)
                s.add((x, y))
            else:
                s.add(d)
        aux_list.append(s)
        data = s
    return aux_list

print(len(dots(data,op)[0]))

def make_string(data):
    s = ""
    x_min = min(data, key = lambda x : x[0])[0]
    y_min = min(data, key = lambda x : x[1])[1]
    x_max = max(data, key=lambda x : x[0])[0]
    y_max = max(data, key=lambda x : x[1])[1]
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            if (j, i) in data:
                s += "#"
            else: s += "."
        s += "\n"
    return s

print(make_string(dots(data, op)[-1]))
