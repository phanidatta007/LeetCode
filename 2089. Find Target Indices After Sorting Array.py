nums = [1,2,5,2,3]
target = 5
nums1 = sorted(nums)
lst = []
for i in range(len(nums1)):
    if nums1[i] == target:
       lst.append(i)
lst.sort()
print(lst)