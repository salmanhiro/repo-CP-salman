def nim(k):
	if (k%2) == 0:
		if k <=100:
			return 2
		elif k <=200:
			return 4
		elif k <=300:
			return 6
		elif k <= 400:
			return 8
		else: return 9
	else:
		if k <=100:
			return 1
		elif k <=200:
			return 3
		elif k <=300:
			return 5
		elif k <= 400:
			return 7
		else: return 9


k = int(input())
print(nim(k))