
f = open('input_sonar.txt', 'r')

list = [int(i.replace("\n", "")) for i in f]


def part1 (list):
    
    count = 0    

    for i in range(len(list)):

        if i == 0:
            print (str(list[0]) + ' (N/A - no previous measurement)')
            band = 1

        else:
            if list[i]<list[i-1] and band == 1:
                print (str(list[i]) + ' (decreased)')

            else:
                print (str(list[i]) + ' (increased)')
                count = count +1

    return count

def part1_noprint (list):

    return len([i for i in range(len(list)) if list[i]>list[i-1]])


def part2(list):

    acum = 0
    aux_list = []

    for j in range(len(list)):
        for i in range(3):
            acum = acum + list[i+j-4]
        aux_list.append(acum)
        acum = 0

    return aux_list


