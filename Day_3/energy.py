f = open('input.txt', 'r')

list = [i.replace("\n", "") for i in f]
m = list.copy()

gamma_list = []
epsilon_list = []
oxigen = []
oxigen_2 = []
Co2 = []
acum = 0 

def dec(binary):
     return sum((2**c) * v for c,v in enumerate(binary))

def neg(binary):
    list = []
    for i in binary:
        if i:
            list.append(0)
        else:
            list.append(1)  
    return list

def part2(list,m):
    for i in range(len(list[0])):
    	zero = 0
    	one = 0
    	for j in range(len(list)):
    		zero += list[j][i] == '0'
    		one += list[j][i] == '1'
    	if zero > one:
    		o2 = '0'
    	elif one > zero:
    		o2 = '1'
    	else:
    		o2 = '1'
    	if len(list) > 1:
    		nextL = []
    		for j in range(len(list)):
    			if list[j][i] == o2:
    				nextL.append(list[j])
    		list = nextL

    	zero = 0
    	one = 0
    	for j in range(len(m)):
    		zero += m[j][i] == '0'
    		one += m[j][i] == '1'
    	if zero > one:
    		co2 = '1'
    	elif one > zero:
    		co2 = '0'
    	else:
    		co2 = '0'
    	if len(m) > 1:
    		nextM = []
    		for j in range(len(m)):
    			if m[j][i] == co2:
    				nextM.append(m[j])
    		m = nextM

    finO2 = int(list[0], 2)
    finCO2 = int(m[0], 2)
    print(finO2 * finCO2)




            

def part1(list):
    acum = 0
    for i in range(len(list[0])):
        for j in range(len(list)): 
            if int(list[j][i]):
                acum += 1  
        
        if acum > len(list)/2:
            gamma_list.append(1)
            epsilon_list.append(0)
        else:
            gamma_list.append(0)
            epsilon_list.append(1)


part1(list)
gamma = dec(gamma_list[::-1])
epsilon = dec(epsilon_list[::-1])


part2(list,m)