def runningSum(nums):
    ans = []
    x = 0
    for i in nums:
        x = x + i
        ans.append(x)
    return ans