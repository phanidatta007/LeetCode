s = "What is the solution to this problem"
k = 4

temp = ""
arr = []
for i in range(len(s)):
    if s[i] == " ":
        arr.append(temp)
        temp = ""
        continue
    temp = temp + s[i]
arr.append(temp)
print(arr)
ans = ""
for i in range(k-1):
    ans = ans + arr[i] + " "
ans = ans + arr[k-1]
print(ans)
