rectangles = [[5,8],[3,9],[5,12],[16,5]]
maxlength = []

for i in range(len(rectangles)):
    maxlength.append(min(rectangles[i]))

length = max(maxlength)
count = 0
for i in range(len(maxlength)):
    if length == maxlength[i]:
        count += 1
print(count)
