tuple=[(1, 3, 5, 6), (3, 2, 5, 7), (2, 1, 3, 8), (6, 4, 2, 1)]
output = sorted(tuple, key=lambda x: x[-1])
print(output)