#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def input_files(filename : str) -> str:
    data = open(filename).read().split('\n')
    temp = data[0]
    rules = {}
    for d in data[2:]:
        k,v = d.split(" -> ")
        rules[k] = v

    return rules,temp


rules,template = input_files('input_for_testing.txt')
counter_dict = {k: template.count(k) for k in rules.keys()}
print(counter_dict)
for i in range(1):
    new_counter_dict = counter_dict.copy()
    for k, v in counter_dict.items():
        if counter_dict[k]:
            new_counter_dict[k] -= v
            print(new_counter_dict)
            new_counter_dict[k[0] + rules[k]] += v
            print(new_counter_dict)
            new_counter_dict[rules[k] + k[1]] += v
            print(new_counter_dict)
    counter_dict = new_counter_dict

print(counter_dict)
l = {x: 0 for x in set(''.join(counter_dict.keys()))}
print(l)

for k, v in counter_dict.items():
    l[k[0]] += v/2
    l[k[1]] += v/2

print(int(max(l.values()) - min(l.values())) + 1)
