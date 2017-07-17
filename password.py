def validate(s):
	a = s
	if(len(a)>=6 or len(a)<= 16):
		if(any(i.islower() for i in a)):
			if(any(i.isupper() for i in a)):
				if(any(i.isalnum() for i in a)):
					chars = set('$#@')
					if any((c in chars) for c in a):
						q = 'Valid'
					else:
						q = 'Not Valid'
				else:
					q = 'Not Valid'
			else:
				q = 'Not Valid'
		else:
			q = 'Not Valid'
	else:
		q = 'Not Valid'
	return q;
def main(s):
	print(validate(s))
if __name__ == '__main__':
	s = raw_input('Enter the password: ')
    	main(s)