#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint 
import sys
from collections import defaultdict
from math import inf 
import heapq
sys.setrecursionlimit(3000)

def input_files(filename : str) -> str:
    data = open(filename).read().split('\n')
    data = [[int(data) for data in d ] for d in data]
    D2 = [[(data[j%len(data)][i%len(data)] + int(i/len(data)) + int(j/len(data)) -1) % 9 + 1 for i in range(len(data) * 5)] for j in range(len(data) * 5)]

    return D2

data = input_files('input.txt')

#pprint.pprint(data)
my_dict = {}

def search(r,c):
    if (r,c) in my_dict:
        return my_dict[(r,c)]
    if r<0 or r>=len(data) or c<0 or c>=len(data[r]):
        return 1e9
    if r==len(data)-1 and c==len(data[r])-1:
        return data[r][c]

    ans = data[r][c] + min(search(r+1,c), search(r, c+1))
    
    my_dict[(r,c)] = ans
    return ans

print(search(0,0)-data[0][0])

def shortestPath(data):
    risk = defaultdict(lambda : inf, {(0,0):0})
    visited = defaultdict(lambda : False)
    heapq.heappush(Q := [], (0, (0,0)))
    while Q:
        x = heapq.heappop(Q)[1]
        visited[x] = True
        for n in [p for p in [(x[0]-1,x[1]), (x[0]+1,x[1]), (x[0],x[1]-1), (x[0],x[1]+1)] if p[0] in range(len(data)) and p[1] in range(len(data))]:
            if not visited[n]:    
                newRisk = risk[x] + data[n[0]][n[1]]
                if risk[n] > newRisk:
                    risk[n] = newRisk
                    heapq.heappush(Q, (newRisk, n))
    return risk[(len(data)-1, len(data)-1)]

print("Part 2:", shortestPath(data))
