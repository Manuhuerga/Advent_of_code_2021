f = open('input.txt', 'r')
data = f.read().splitlines()


input_numbers = map(int, data[0].split(','))

boards = []
acum = 0

for l in data[1:]:
	if not l:
		boards.append([])
		continue
	boards[-1].append(list(map(int, l.split())))

def part1(input_numbers, boards):
    for input in input_numbers:
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                for k in range(5):
                    if input in boards[i][j]:
                        boards[i][j][k] = 'X'
                    for v in range(len(boards)):                    
                        if ['X','X','X','X','X'] in boards[v]:
                            return(boards[v])

