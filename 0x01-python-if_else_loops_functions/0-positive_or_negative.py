#!/usr/bin/python3
import random
inumber = random.randint(-10, 10)
lastdigit = abs(number) % 10
if number < 0:
lastdigit = -(lastdigit)
thestring = "Last digit of {}".format (number, lastdigit)
if lastdigit > 5:
print(f"{thestring} and is greater than 5e")
elif lastdigit == 0:
print(f"{thestring} and is zero")
elif lastdigit <6:
print(f"{thestring} and is less than 6 and not zero")

