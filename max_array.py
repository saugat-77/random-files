inp_arr=[]
total_number=int(input('total length of array ? '))
for i in range(total_number):
    inp_num=int(input('enter array element: '))
    inp_arr += [inp_num]

seen = set()
duplicate_array = []

for x in inp_arr:
    if x in seen:
        duplicate_array.append(x)
    else:
        seen.add(x)
    
new_list=list(set(duplicate_array))
# print(list(new_list))

duplicate_array.extend(new_list)
for i in duplicate_array:
    inp_arr.remove(i)
inp_arr.sort(reverse=True)
# print('original list= ',inp_arr )
print("maxm element= " ,inp_arr[0])
# print("duplicate array= ", duplicate_array)
# print("seen= ", seen)

