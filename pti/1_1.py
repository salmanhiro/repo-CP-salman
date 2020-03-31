def fizzbuzz(i):
	if (i%5 == 0) and (i%7 == 0):
		return ('FizzBuzz')
	elif (i%5 == 0):
		return('Fizz')
	elif (i%7 == 0):
		return('Buzz')
	else:
		return(i)


a = int(input())
b = int(input())
for i in range(a,b):
	print(fizzbuzz(i))




