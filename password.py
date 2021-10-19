password = "a123456"
i = 3
while True:
	pw = input("Please enter your password: ")
	if pw == password:
		print("Password correct")
		break
	else:
		i = i - 1
		print("You have", i, "chances left")
		if i == 0:
		    break