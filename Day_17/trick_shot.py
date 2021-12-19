#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# target area: x=265..287, y=-103..-58
from itertools import product

# xmin, xmax, ymin, ymax = 265,287,-103,-58
# yvel = -ymin - 1
# y = 0
# while yvel:
#     y += yvel
#     yvel -= 1
# print(y)

def check_velocity_valid(dx, dy, data): #0,-1000 , 1,-999 , 2,-998
    tminx, tmaxx, tminy, tmaxy = data   
    pos_x, pos_y = 0, 0
    while pos_x <= tmaxx and pos_y >= tminy: #0<287  ,  0> -103  
        pos_x, pos_y = pos_x+dx, pos_y+dy # pos_x, pos_y = 0, -1000 -- 1, -999
        dx, dy  = max(0, dx-1), dy-1   #dx,dy = 0,-1001
        if tminx <= pos_x <= tmaxx and tminy <= pos_y <= tmaxy:
            return True
    return False

def highest_y(y):
    return (y+1) * y // 2

data = 265,287,-103,-58
velocities = [vy for vx, vy in product(range(1000), range(-1000, 1000)) if check_velocity_valid(vx, vy, data)]
print(highest_y(max(velocities)))
print(len(velocities))