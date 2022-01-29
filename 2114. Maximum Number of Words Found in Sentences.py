def countNumberOfWords(sentence):
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            count += 1
    count += 1
    return count

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
counts = []

for sentence in sentences:
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            count += 1
    count += 1
    counts.append(count)
print(counts)