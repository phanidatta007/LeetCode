def isPalindrome(word):
    word1 = ""
    for i in range(-1,-len(word)-1,-1):
        word1 = word1 + word[i]

    if word == word1:
        return True
    else:
        return False
words = ["abc","car","ada","racecar","cool"]
for i in range(len(words)):
    ans = isPalindrome(words[i])
    if ans == True:
        print(words[i])
        break
