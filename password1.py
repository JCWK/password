password = "a123456"
i = 3
while i > 0:
	i = i - 1
	pw = input("Please enter your password: ")
	if pw == password:
		print("Password correct")
		break
	else:
		print("Password wrong")
		if i > 0:
		    print("You have", i, "chances left")
		else:
		    print("Please wait 15mins and try again")
