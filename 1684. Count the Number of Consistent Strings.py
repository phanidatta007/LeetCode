allowed = "ab"
words = ["ab","bd","aaab","baa","badab"]
count = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        if allowed == words[j]:
            count += 1
print(count)