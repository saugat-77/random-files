punctuation=['!','.',',',':',';','?']
a=input('enter a string: ')
lista=a.split()
new_lsit   =[]
# print(lista)
for a in lista:
    if '!' in a or '.' in a or ',' in a or ':' in a or ';' in a or '?' in a:
        for i in a:
            if i in punctuation:
                newstr=a.split(i)
                sentence_1 = newstr[0]
                length = len(sentence_1)
                swap=sentence_1[1:length-1]+sentence_1[0]+'arg'+a[length:]    
                new_lsit.append(swap) 
                break
    else:   
        text=a[1:]+a[0]+'arg'
        new_lsit.append(text)
finalstr=" ".join(new_lsit)
print(finalstr)