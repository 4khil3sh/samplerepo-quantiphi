import sys
a = sys.argv[1]
print(len(a))
b = a[::-1]
print("Is it a palindrome?")
print(a==b)