def KidsWithCandies(candies, extraCandies):

    highestN = max(candies)
    result = []

    for i in range(len(candies)):
        if candies[i] + extraCandies >= highestN:
            result.append(True)
        else:
            result.append(False)
    return result

candies = [2,3,5,1,3]
extraCandies = 3
a = KidsWithCandies(candies, extraCandies)
print(a)