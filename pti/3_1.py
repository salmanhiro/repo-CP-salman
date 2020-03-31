def med(k):
	y = []
	for i in range(len(k)):
		if k[i]>=s:
			y.append(k[i])
	summation = 0
	for j in range(len(y)):
		summation = summation + y[j]
	mean = summation/len(y)
	return mean



k = list(map(int, input().rstrip().split()))
s = int(input())

print(med(k))