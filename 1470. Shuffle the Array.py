def shuffle(nums, n):

    nums1 = []
    nums2 = []
    result = []
    for i in range(n):
        nums1.append(nums[i])
    for i in range(n,len(nums)):
        nums2.append(nums[i])
    for i in range(n):
        result.append(nums1[i])
        result.append(nums2[i])
    return result
nums = [2,5,1,3,4,7]
n = 3
a = shuffle(nums,n)
print(a)
