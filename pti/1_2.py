def write(n):
	k = 1
	while(n>=1):
		for i in range(n):
			 print(k, end = ' ')
		n = n-1
		k = k+1
		
n = int(input())

print(write(n))