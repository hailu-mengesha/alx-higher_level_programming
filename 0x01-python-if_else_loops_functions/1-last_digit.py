#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
print("Last digit of " + number + " is " + number[-1],end = "")
if int(number[-1]) > 5:
	print(" and is greater than 5")
elif int(number[-1]) == 0:
	print(" and is 0")
elif int(number[-1]) < 6 and not 0:
	print(" and is less than 6 and not 0")
