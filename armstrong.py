import sys
a = sys.argv[1]
a1 = len(a)
a = int(a)
a4 = a
a3 = 0
while(a1>=0):
	a2 = a4/(10**(a1-1))
	a4 = a4 - a2*10**(a1-1)
	a3 = a3 + a2**3
	a1 = a1-1
if(a == a3):
	print(str(a) + ' is a armstrong number.')
else:
	print(str(a) + ' is not a armstrong number.')