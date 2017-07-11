from __future__ import print_function
print('Input number of rows:')
b = input()
print('Input number of columns:')
c = input()
if(c>3 and b>=3):
	for i in range(0,b):
		a = str()
		for j in range(0,c):
			if( i == 0 or i == (b-1)):
				if(j != 0 or j !=(b-2)):
						a = a+'*'
				else:
						a = a+' '
			elif(i == ((b/2)-1)):
				if(j != 0):
						a = a+' '
				else:
						a = a+'*'
			elif(i == (b/2)):
				if(j > (c/2)-1 or j == 0):
						a = a+'*'
				else:
						a = a+' '
			else:
				if(j==0 or j == (c-1)):
						a = a+'*'
				else:
						a = a+' '
		print(a)
else:
	print('Not possible!!')