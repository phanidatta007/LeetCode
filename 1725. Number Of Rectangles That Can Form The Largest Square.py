rectangles = [[5,8],[3,9],[5,12],[16,5]]
squares = []
maxlength = []

for i in range(len(rectangles)):
    val = [min(rectangles[i]),min(rectangles[i])]
    squares.append(val)

for i in range(len(squares)):
    val1 = max(squares[i])
    maxlength.append(val1)

length = max(maxlength)
count = 0
for i in range(len(maxlength)):
    if length == maxlength[i]:
        count += 1
print(count)
