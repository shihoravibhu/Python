# (A) Write a Python program to perform the following task using random a module: 
# 1) Generate a 6-digit random secure OTP. 
# 2) Random integer between 0 and 100, with a step of 3. 
# 3) Generate a random String of length 5. 
# 4) Pick a random character from a given String.

import random

print(random.randint(100000,999999))

print(random.randrange(0,101,3))

s = "hey"

print(random.choice(s))