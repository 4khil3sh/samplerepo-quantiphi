a = raw_input('Enter the email address: ')
s = str()
for i in range(0,len(a)): 
	if(a[i] != '@'):
		s = s +a[i]
	else:	
		break
print(s)
	 