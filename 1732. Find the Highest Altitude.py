gain = [-4,-3,-2,-1,4,3,2]
net_gain = [0]

for i in range(len(gain)):
    net_gain.append(net_gain[i] + gain[i])
print(max(net_gain))
