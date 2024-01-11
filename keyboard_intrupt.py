def keyboard_intrupt():
    try:
        num=int(input("enter the number:"))
        print(num)
    except KeyboardInterrupt:
        raise Exception("it is a keyboard intrupt error")
    
keyboard_intrupt()