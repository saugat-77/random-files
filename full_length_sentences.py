
def func(sentence):
    
    new_list=[]
    y=sentence.split(' ')

    res = len(max(y, key = len))

    for i in y:

        if (len(i)== res or len(i)>res ):
            new_list=new_list + [i]
        else:
            len_i=res-len(i)
            j=i[0]*len_i
            new_string=j+i

            new_list=new_list + [new_string]
    sentence_1 = ' '.join(new_list)
    return sentence_1

sentence=input('enter a sentence: ')
print(func(sentence))