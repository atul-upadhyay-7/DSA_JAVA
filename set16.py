# AIM: A program that calculates the factorial of a number
h=int(input("\n")) 
fact=1
for i in range(1,h+1):
    fact=fact*i
print("factor of",h,"is",fact)
