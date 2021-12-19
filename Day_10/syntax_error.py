def input_files(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def part1():

    data = input_files('input.txt')
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}

    error = []

    for d in data:
        score = 0
        aux_list = []
        for c in d:
            if c not in [")", "]", "}", ">"]:
                aux_list.append(c)
            else:
                if c == pairs[aux_list[-1]]:
                    aux_list.pop()
                else:
                    error.append(values[c])
                    aux_list = []
                    break
    
    return (sum(error))

def part2():

    data = input_files('input.txt')
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    values = {"(": 1 , "[": 2 , "{": 3, "<": 4}
    aux_list2 = []
    score_list= []
    
                                   
    for d in data:
        score = 0
        aux_list = []
        for c in d:
            if c not in [")", "]", "}", ">"]:
                aux_list.append(c)
            else:
                if c == pairs[aux_list[-1]]:
                    aux_list.pop()
                else:
                    aux_list=[]
                    break

        if aux_list:
            aux_list2.append(aux_list[::-1])
    
    score= 0 
    for m in aux_list2:
        for c in m:
            score = (score*5) + values[c]
        score_list.append(score)
        score = 0
    
    return(sorted(score_list)[len(score_list)//2])

print(f"Part 1: ",part1())
print(f"Part 2: ",part2())