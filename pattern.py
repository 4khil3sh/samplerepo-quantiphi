
for i in range(0,10):
	if(i<=5):
		a=str()
		for j in range(0,i):
			a = a+'*'
		print(a)
	else:	
		a=str()
		for j in range(0,10-i):
			a = a+'*'
		print(a)
		 