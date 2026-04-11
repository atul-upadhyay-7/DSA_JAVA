# AIM: A program that converts a given number from one base to another.
def decimal_others(value, choice):
	if choice == 1:
		return value
	elif choice == 2:
		return format(value, "b")
	elif choice == 3:
		return format(value, "o")
	elif choice == 4:
		return format(value, "x")
	else:
		return "Invalid Option"


def binary_others(value, choice):
	decimal_value = int(value, 2)
	if choice == 1:
		return decimal_value
	elif choice == 2:
		return value
	elif choice == 3:
		return format(decimal_value, "o")
	elif choice == 4:
		return format(decimal_value, "x")
	else:
		return "Invalid Option"


def octal_others(value, choice):
	decimal_value = int(value, 8)
	if choice == 1:
		return decimal_value
	elif choice == 2:
		return format(decimal_value, "b")
	elif choice == 3:
		return value
	elif choice == 4:
		return format(decimal_value, "x")
	else:
		return "Invalid Option"


def hex_others(value, choice):
	decimal_value = int(value, 16)
	if choice == 1:
		return decimal_value
	elif choice == 2:
		return format(decimal_value, "b")
	elif choice == 3:
		return format(decimal_value, "o")
	elif choice == 4:
		return value
	else:
		return "Invalid Option"


print("Enter source base:")
print("1. Decimal")
print("2. Binary")
print("3. Octal")
print("4. Hexadecimal")
source = int(input())

value = input("Enter the number: ").strip()

print("Convert to:")
print("1. Decimal")
print("2. Binary")
print("3. Octal")
print("4. Hexadecimal")
choice = int(input())

if source == 1:
	result = decimal_others(int(value), choice)
elif source == 2:
	result = binary_others(value, choice)
elif source == 3:
	result = octal_others(value, choice)
elif source == 4:
	result = hex_others(value, choice)
else:
	result = "Invalid source base"

print("Converted value:", result)
