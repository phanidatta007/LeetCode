nums = [8,1,2,2,3]
a = len(nums)
lst = []
for i in range(a):
    count = 0
    for j in range(a):
        if nums[i] > nums[j]:
            count += 1
    lst.append(count)
print(lst)


