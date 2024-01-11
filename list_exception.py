def mylist_operation(my_list,index):
    try:
        print("the element is:",my_list[index])
    except IndexError:
        raise Exception("there is no value")


limit=int(input("enter the limit to insert:"))
my_list=[]
for i in range(limit):
     num=int(input("enter the numbers:"))
     my_list.append(num)
index=int(input("enter the index you want to access"))
mylist_operation(my_list,index)