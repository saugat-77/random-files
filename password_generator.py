import string
import random

pass_len=int(input('enter your password length: ' ))
s1=string.ascii_lowercase   #sabai lowercase haru
# print(s1)
s2=string.ascii_uppercase
# print(s2)
s3=string.digits
# print(s3)
s4=string.punctuation
# print(s4)

s=[]        
#extend list ma element append garcha
s.extend(list(s1))   
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

print()
print("".join(random.sample(s, pass_len)))  #random join garcha
print()