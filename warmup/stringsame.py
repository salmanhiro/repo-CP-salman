def res(string):
	return [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
result = []

number = int(input())

for e in range(number):
	n = int(input())
	string1 = str(input())
	string2 = str(input())
	s1 = res(string1[:n])
	s2 = res(string2[:n])
	a = []
	b = []

	for l in range(len(s1)):
		if len(s1[l]) >= 2:
			a.append(s1[l])
		if len(s2[l]) >= 2:
			b.append(s2[l])

	same = False
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				same = True


	if same == True:
		result.append('YES')
	else:
		result.append('NO')


for m in range(len(result)):
	print(result[m])

