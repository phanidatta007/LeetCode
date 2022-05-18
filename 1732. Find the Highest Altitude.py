gain = [-5,1,5,0,-7]
net_gain = 0
ans = 0

for i in range(len(gain)):
     net_gain = net_gain + gain[i]
     if net_gain >= ans:
         ans = net_gain
print(ans)