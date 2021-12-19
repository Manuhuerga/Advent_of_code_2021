def input_files(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
        lines = [[["".join(sorted(d)) for d in data.split()] for data in d.split(" | ")] for d in data]
    return lines


def part1():

    count = 0
    aux_list = []
    lista = input_files('input.txt')

    for index in range(len(lista)):
        for l in lista[index][1]:
            if len(l) in [2,3,4,7]:
                aux_list.append(l)

    return len(aux_list)


def find_number(nums):
    '''
    Function not used, because it useless :(
    '''
    my_dic =   {'abcdeg': 0, 'ab': 1, 'acdfg': 2, 'abcdf': 3,
                'abef': 4, 'bcdef': 5, 'bcdefg': 6, 'abd': 7,
                'abcdefg': 8, 'abcdef': 9}
    
    my_list= [my_dic[i] for i in nums if i in my_dic]
    return "".join([str(_) for _ in my_list])


def find_nums(nums):
    '''
    This function determinated the values from 0 to 9 for each
    string in input.txt 
    :return : list of string each string represent a value from 0 to 9
    : n0 = 0 , etc
    '''
    n1 = [x for x in nums if len(x) == 2][0]
    n4 = [x for x in nums if len(x) == 4][0]
    n7 = [x for x in nums if len(x) == 3][0]
    n8 = [x for x in nums if len(x) == 7][0]
    n9 = [x for x in nums if len(x) == 6 and all(y in x for y in n4)][0]
    n0 = [x for x in nums if len(x) == 6 and x != n9 and all(y in x for y in n1)][0]
    n6 = [x for x in nums if len(x) == 6 and x != n9 and x != n0][0]
    n3 = [x for x in nums if len(x) == 5 and all(y in x for y in n1)][0]
    n5 = [x for x in nums if len(x) == 5 and x != n3 and all(y in n9 for y in x)][0]
    n2 = [x for x in nums if len(x) == 5 and x != n3 and x != n5][0]
    return [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]


def part2():

    nums = 0
    aux =0
    lista = input_files('input.txt')

    for index in range(len(lista)):
        nums = find_nums(lista[index][0])
        aux += int("".join([str(nums.index(x)) for x in lista[index][1]]))

    return aux

print(f'Part 1: ',part1())
print(f'Part 2: ',part2())
