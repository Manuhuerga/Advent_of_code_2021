data = open('input.txt').read().splitlines()
data = [d.split('-') for d in data]

my_dict = {}

def make_a_dict(s,d):
    if d != 'start':
        my_dict[s] = my_dict.get(s,[])+[d]

for d in data:
    k,v = d
    make_a_dict(k,v)
    make_a_dict(v,k)
print(my_dict)

def searching(v,b):
    if 'end' in v:
        return [v]
    c = [(value in v and value.islower(),value) for value in my_dict[v[-1]]]

    return [d for x,n in c if not(x&b) for d in searching(v+[n],x|b)]

print("Part 1: ", len(searching(['start'],1)))
print("Part 2: ", len(searching(['start'],0)))