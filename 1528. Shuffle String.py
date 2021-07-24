s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]

temp = [0]*len(s)
shffld_str = ""
for i in range(len(s)):
    temp[indices[i]] = s[i]
for i in range(len(s)):
    shffld_str = shffld_str + temp[i]
print(shffld_str)
