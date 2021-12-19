f = open('input.txt', 'r')

#list_forward = [int(i.replace("forward ", "")) for i in f if 'forward' in i]
#list_up = [int(i.replace("up ", "")) for i in f if 'up' in i]
#list_down = [int(i.replace("down ", "")) for i in f if 'down' in i]


x,y = [0,0]
objetive = 0

for i in f:
    if 'forward' in i:
        x = int(i.replace("forward ", "")) + x
        y = objetive * int(i.replace("forward ", "")) + y
    elif 'down' in i:
        objetive = int(i.replace("down ", "")) + objetive
    else: 
        objetive = -int(i.replace("up ", "")) + objetive

print (x * y)

f.close()