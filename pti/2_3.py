def medal(x):
	total = 3*x[0] + 2*x[1] + 1*x[2]
	return total
def compare(v,w):
	if v != w:
		if v>w:
			return 'A'
		else: 
			return 'B'
	else:
		if a[0] > b[0]:
			return 'A'
		elif a[0] < b[0]:
			return 'B'
		else:
			if a[1] > b[1]:
				return 'A'
			elif a[1] < b[1]:
				return 'B'
			else:
				if a[2] > b[2]:
					return 'A'
				elif a[2] < b[2]:
					return 'B'
				else:
					return 'SAME'


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

v = medal(a)
w = medal(b)

print(compare(v,w))