def product(a,b):
	result = []
	degree = []
	for i,j in ((a,b) for a in range(n_a+1) for b in range(n_b+1)):
		coeff = a[i]*b[j]
		result.append(coeff)
	return result
def degree(n_a,n_b):
	degree = []
	for i,j in ((a,b) for a in range(n_a,-1,-1) for b in range(n_b,-1,-1)):
		deg = i+j
		degree.append(deg)
	return degree

def matching(temp,degri):
	result = []
	for i in range(len(temp)):
		for j in range(len(degri)):
			if (temp[i] == degri[j]):
				if(i!=j):
					summed = prod[i]+prod[j]
					print(prod[i],prod[j])
					result.append(summed)
	return result



n_a = int(input())

a = list(map(int, input().rstrip().split()))

n_b = int(input())

b = list(map(int, input().rstrip().split()))

prod = product(a,b)
degri = degree(n_a,n_b)
temp = degri 
sama = matching(temp,degri)

print(prod)
print(degri)
print(temp)
print(sama)