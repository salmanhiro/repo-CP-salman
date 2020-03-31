def countvalley(n,s):
	ele = 0
	count = 0
	for i in range(n):
		if s[i] == 'U':
			ele = ele + 1
			if ele == 0:
				count = count + 1
		else:
			ele = ele - 1

	return count





n = int(input())
s = input()
result = countvalley(n,s)
print(result)