# Code I wrote teaching my cousin about 
# while loops in Python.

userInput = 3

while True:
	print("menu")
	print("1 Celsius, 2 Farenheit, 3 exit")
	#don't forget to cast inputs if you want anything other than a string
	userInput = int(input("Enter Choice: "))
	if userInput == 1:
		print("Celsius is for communists")
		print(".")
	elif userInput == 2:
		print("Good job patriot")
		print(".")
	elif userInput == 3:
		print("exiting")
		print(".")
		break

exit()
