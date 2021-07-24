nums = [65,44,72,15]
lst = []
n = len(nums)
i = 0
while i <= (n-2)/2:
    freq, val = nums[2*i],nums[(2*i)+1]
    for j in range(freq):
        lst.append(val)
    i += 1
    print(freq,val)
print(lst)
