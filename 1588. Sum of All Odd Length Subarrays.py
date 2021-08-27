arr = [1, 4, 2, 5, 3]

b = 0
for x in range(len(arr)):
    for i in range(x, len(arr)):
        a = arr[x:i + 1]
        if len(a) % 2 == 1:
            b = b + sum(a)
print(b)
