#AIM: A program that generates a random password of specified length.
import string
import random
def generate(n):
	c = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(c) for _ in range(n))
	return password
n = int(input("enter the length of the password\n"))
r = generate(n)
print(r)
