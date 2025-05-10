def count_vowels( word):
    read= list(word)
    vowels= ['a','e','i','o','u']
    count =0
    for i in read:
        if i in vowels:
            count +=1
    return count

# read= "Markaeio"
# see=list(read)
# vowels= ['a','e','i','o','u']
# count=0
# for i in see:
#     if i in vowels:
#         count+=1
# print(count)
# print(see)

see= count_vowels("eenbiop")
print(see)