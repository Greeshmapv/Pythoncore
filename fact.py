try:
    num = int(input("Enter the number: "))
    if num == 0:
        print("Factorial of zero is 1")
        i = 1
        fact = 1
        while i <= num:
            fact = fact * i
            i += 1
        print("Factorial of", num, "=", fact)
    elif num > 0:
        i = 1
        fact = 1
        while i <= num:
            fact = fact * i
            i += 1
        print("Factorial of", num, "=", fact)
    else:
        raise ValueError("There is no factorial for negative numbers")
except ValueError as ve:
    print(ve)
except:
    raise
