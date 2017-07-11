import sys

a = sys.argv[1]
if(len(a)>=6 or len(a)<= 16):
	print('Password length is valid')
	if(any(i.islower() for i in a)):
		print('Password has a lower character')
		if(any(i.isupper() for i in a)):
			print('Password has a upper character')
			if(any(i.isalnum() for i in a)):
				print('Password has a number')
				chars = set('$#@')
				if any((c in chars) for c in a):
					print('Password has a special character')
					print('Password is valid!!')
				else:
					print('Password has no special character')
			else:
				print('Password has no number')
		else:
			print('Password has no upper case character')
	else:
		print('Password has no lower character')
else:
	print('Password length is invalid')
					