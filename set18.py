# AIM: A program that sorts a list of numbers in ascending or descending order
def sort_list():
    if order == "A":
        sl = sorted(list1)
    elif order == "D":
        sl = sorted(list1, reverse=True)
    else:
        print("Invalid")
        return
    print(sl)


list1 = input("enter the list elements\n").split()
list1 = [int(n) for n in list1]
order = input("enter A for ascending or D for descending\n").upper()

sort_list()

