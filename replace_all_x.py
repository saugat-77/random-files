
def string_func(string_1):
    if 'x' in string_1 :
        position = string_1.find('x')
        # print(position)
        
        if position +1 == ' ' and position -1 == ' ':
            final_string=string_1.replace('x', 'ecks') 
            return final_string
            # print(final_string)
            # print('test 1')
        
        elif position == 0:
            final_string=string_1.replace('x', 'z') 
            return final_string
            # print(final_string)
            # print('test 2')


        else :
            final_string=string_1.replace('x', 'cks')
            return final_string
            # print(final_string)
            # print('test 3')
    else:
        print('no x in string')

input_string=input('enter a string: ')
string_1=input_string.lower()

print(string_func(string_1))