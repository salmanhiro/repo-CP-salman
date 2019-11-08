def string(st,n):
	out = ""
	dc = st*n
	count = 0
	for i in range(n):
		out = out + st[i%(len(st))]
		if out[i] == 'a':
			count = count+1
	return count

n = int(input())
st = str(input())

#print(out)
print(string(st,n))