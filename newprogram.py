try:
    integer=int(input("enter the integer number:"))
    print(integer)
except ValueError:
    raise Exception("This is not a integer number")