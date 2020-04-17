for x in range(1,101):
	if x % 7 == 0 or str(x).find('7') != -1:
		continue
	print(x)
