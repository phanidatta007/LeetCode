allowed = "ab"
words = ["ab","bd","aaab","baa","badab"]
count = 0

def isBuilt(allowed, word):
    for i in range(len(word)):
        if word[i] not in allowed:
            return False

    return True

for word in words:
    if isBuilt(allowed, word):
        count += 1
print(count)