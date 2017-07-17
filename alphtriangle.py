a = input('Enter number of rows in the alphabet triangle')
if(a>7):
	print('Error: alphabet does not have enough characters')
else:
	s = str()
	for i in range(0,a+1):
		for j in range(0,i):
			s = s+chr(65+i*(i-1)/2+j)
		print(s)
		s = str()		