def diskon(k):
	if k[0]/k[1] > k[2]/k[3]:
		return 'A'
	elif k[0]/k[1] == k[2]/k[3]:
		return 'SAME'
	else:
		return 'B'


k = list(map(int, input().rstrip().split()))
result = diskon(k)
print(result)