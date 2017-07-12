def add(a,b):
	q = a+b
	return q;
def subs(a,b):
	q = a-b
	return q;
def muls(a,b):
	q = a*b
	return q;
def divs(a,b):
	q = a/b
	return q;
i=1
while (i!=0):
	print('Enter operation code:\n Addition--> 1 \n Substraction --> 2 \n Multiplication --> 3 \n Division --> 4 \n Exit --> 5')
	c = input()
	if(c == 5):
		print('Good bye!')
		i = 0
		break
	print('Enter First number:')
	a = float(input())
	print('Enter Second number:')
	b = float(input())
	if (c == 1):
		print('Ans:'+ str(add(a,b)))
	elif(c == 2):
		print('Ans:' + str(subs(a,b)))
	elif(c == 3):
		print('Ans:' + str(muls(a,b)))
	elif(c == 4):
		if(b==0):
			print('Division by 0 not possible')
		else:	
			print('Ans:'+str(divs(a,b)))
	else:
		print('Check input!')
		
	

