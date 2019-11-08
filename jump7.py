for i in range(100):
	a = i+1
	if a % 7 != 0 and a % 10 != 7 and int(a/10) != 7:
		print(a)
