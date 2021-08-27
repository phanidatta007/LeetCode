word1 = ["abc","d","defg"]
word2 = ["abcddefg"]
temp1 = ""
temp2 = ""
for i in range(len(word1)):
    temp1 = temp1 + word1[i]
print(temp1)
for i in range(len(word2)):
    temp2 = temp2 + word2[i]
print(temp2)
if temp1 == temp2:
    print(True)
else:
    print(False)