# AIM: A program that generates a multiplication table for a given number.
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
