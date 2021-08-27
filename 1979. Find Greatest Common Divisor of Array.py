nums = [30,50]
a = min(nums)
b = max(nums)
temp = []
for i in range(a+1):
    if i == 0:
        temp.append(i)
    elif a % i == 0 and b % i == 0:
        temp.append(i)
c = max(temp)
print(c)