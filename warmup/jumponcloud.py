def jump(c,n):

	count = 0
	i = 0
	while i < (n-1):
	    if ((i+2) >= n) or (c[i+2] == 1):  #cant 2 
	        i = i+1
	        count = count+1
	    else:
	        i = i+2
	        count = count + 1
	return count

n = int(input())
c = list(map(int, input().rstrip().split()))
print(jump(c,n))