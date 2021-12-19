from itertools import accumulate

def input_files(filename: str):
    with open(filename, 'r') as f:
        data = f.read()
    return list(map(int,data.split(',')))


input = input_files('Day_7\input.txt')

input = sorted(input)

def part1(input):
    fuel =0 
    fuel_list_status = []

    for i in range(0,input[-1]):
        for _in in input:
            fuel += abs (i - _in) 
        fuel_list_status.append(fuel)
        fuel = 0

    return (sorted(fuel_list_status))[0]


def part2(input):
    fuel =0 
    fuel_list_status = []

    for i in range(0,input[-1]):
        for _in in input:
            fuel += (abs(_in - i)*(abs(_in - i)+1)//2)
        
        fuel_list_status.append(fuel)
        fuel = 0
        
    return (sorted(fuel_list_status))[0]

print (part2(input))
