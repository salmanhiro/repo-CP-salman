def compare(a,b):
	same = []
	for i,j in ((a,b) for a in range(len_a) for b in range(len_b)):
			if a[i] == b[j]:
				same.append(a[i])
	return same




len_a = int(input())
a = list(map(int, input().rstrip().split()))
len_b = int(input())
b = list(map(int, input().rstrip().split()))

print(*compare(a,b))