encoded = [1,2,3]
first = 1

arr = [first]
a = len(encoded)

for i in range(a):
    arr.append(0)
    arr[i+1] = encoded[i] ^ arr[i]

print(arr)