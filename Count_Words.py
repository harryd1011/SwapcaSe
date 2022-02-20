# ID: 20CE028, Name:Harsh Dubey
# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. 
#     The output order should correspond with the input order of appearance of the word. 
#     See the sample input/output for clarification.
from collections import Counter,OrderedDict
class OrderedCounter(Counter,OrderedDict):
    pass
word_array= [] 
# array to store the number of words entered.
n= int(input("Number of words:")) 
print("Words:")
for i in range(n):
    word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
    print(word_ctr[word],end=' ')
