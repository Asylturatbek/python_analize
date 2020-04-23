import random
some = random.randint(0,5)
x = 10
while x>=0:
	print(some)
	x-=1
	some = (some+1) % 5