items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "blue"

category = -1
if ruleKey == "type":
    category = 0
elif ruleKey == "color":
    category = 1
else:
    category = 2
count = 0
for i in range(len(items)):
    if items[i][category] == ruleValue:
        count += 1
print(count)