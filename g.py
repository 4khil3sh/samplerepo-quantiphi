from __future__ import print_function
for i in range(0,7):
	a = str()
	for j in range(0,5):
		if( i == 0 or i == 6):
			if(j == 1 or j ==2 or j ==3):
						a = a+'*'
			else:
						a = a+' '
		elif(i == 2):
			if(j != 0):
						a = a+' '
			else:
						a = a+'*'
		elif(i == 3):
			if(j != 1):
						a = a+'*'
			else:
						a = a+' '
		else:
			if(j==0 or j == 4):
						a = a+'*'
			else:
						a = a+' '
	print(a)