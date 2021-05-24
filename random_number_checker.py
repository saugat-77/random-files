import random
import sys

x=random.randint(1,10)

def random_number(num):
    if (x==num):
        print("wise guess")
    elif (num>x):
        print('go lower')
        
    else:
        print("guess higher")

while True:        

    user_input=int(input("enter a random number from (1,10): "))
    random_number(user_input)
    if user_input==x:
        sys.exit()
