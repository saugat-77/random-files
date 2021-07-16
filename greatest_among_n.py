lst=[]
x=0
number_of_elements=int(input("enter number of list items: "))

for i in range(0,number_of_elements):
    x=x+1
    print("the", x, " element is:")
    list_numbers=int(input())
    lst.append(list_numbers)
    
n=0
big_number=0
for i in range(0,number_of_elements):
    x=lst[n]

    if (x>big_number):
        big_number=x
    else:
        big_number=big_number
   
    n=n+1

print("the list is :", lst)

print("greatest number in list is: ", big_number)