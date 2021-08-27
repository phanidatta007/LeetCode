nums = [4,2,5,9,7,4,8]
nums.sort()
n = len(nums)
a = nums[n-1] * nums[n-2]
b = nums[0] * nums[1]
maximum = a-b
print(maximum)

