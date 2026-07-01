import random

count = 0

while count != 3:

    n = random.randint(100,999)

    if(n % 5 == 0):
        print(n)
        count += 1