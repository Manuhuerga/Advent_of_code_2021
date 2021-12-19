#input = [[i,n,p,u,t,v,a,l,u,e,s],
#         [[a,b,c,d,e,f,g],
#          [h,i,j,k,l,m,n],
#          [n,o,p,q,r,s,t],
#          [u,v,w,x,y,z,0]
#          [1,2,3,4,5,6,7]]
#          ..........
#           []]


def check(t, m):
	a = [[t[i][j] in m for j in range(5)] for i in range(5)]
	b = [[a[j][i] for j in range(5)] for i in range(5)]
	for i in range(5):
		if sum(a[i]) == 5 or sum(b[i]) == 5:
			return True
	return False

f = open('input.txt', 'r')
data = f.read().splitlines()

input = map(int, data[0].split(','))  #[1,2,3,4,5,.....]

table = []
#data is ['1 2 3 4 5', '23 43 43 54 12', '12 3 5 76 1', ...]
for l in data[1:]:
	if not l:
		table.append([])
		continue
	table[-1].append(list(map(int, l.split())))

#table is [ 
#           [
#            [a11,a12,a13,a14,a15],
#            [a21,a22,a23,a24,a25],
#            [a31,a32,a33,a34,a35],
#            [a41,a42,a43,a44,a45],
#            [a51,a52,a53,a54,a55]
#                                   ]
#                                       ]

m = []
_marker = -1

for _in in input:
	m.append(_in)
	for t in table:
		if check(t, m):
			_marker = 0
			for i in t:
				for j in i:
					if j not in m:
						_marker += j
			_marker = _in * _marker
			break
	if _marker != -1:
            break

print(_marker)