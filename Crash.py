import os
path = os.getcwd( )
for i in range(1, 100000000000000000000000001):
	os.mkdir(path + f"\\{ i  }")
