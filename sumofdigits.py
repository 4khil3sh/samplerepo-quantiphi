a = input('Enter number whose sum of digits is desired:')
b = 0
while(a>0):
	b= b+ a%10
	a = a/10
print(b)