nums = [0,1,2,3,4]
index = [0,1,2,2,1]

target = []
l = 0
for i in range(len(index)):
    if l == index[i]:
        target.append(nums[i])
    else:
        target.insert(index[i],nums[i])
    l += 1
print(target)