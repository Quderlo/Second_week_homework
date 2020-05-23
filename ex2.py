def fun(x, y):
	if (type(x) != str or type(y) != str):
		return 0
	elif (x == y):
		return 1
	elif (len(x) > len(y)):
		return 2
	elif (y == 'learn'):
		return 3



x = input()
y = input()
print(fun(x, y))