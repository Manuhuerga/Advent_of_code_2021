#   https://adventofcode.com/2015/day/10

#1
#11
#21
#1211
#111221
#312211
#from matplotlib import pyplot as plt

result = []
s = '21'
i = 0
while i < len(s):
    count = 1

    while  i+1 < len(s) and s[i] == s[i+1]:
        i += 1
        count+=1
    result.append(str(count) + s[i])
    i += 1

print(''.join(result))


def lookandsay(_str):
    
    _str = _str + ' '
    count = 1
    ans = ''
    storage = _str[0]

    for s in _str[1:]:

        if s == storage:
            count += 1
        else:
            ans += str(count) + storage   #13  11 12
            storage = s #3
            count = 1

    return(ans)

input = '312'
_len = []

for _ in range(50):
    ans = (lookandsay(input))
    input = ans
    _len.append(len(input))

print (len(ans))

arr = list(range(50))

plt.plot(arr,_len)
#plt.show()

