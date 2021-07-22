def maximumWealth(accounts):
    m = len(accounts)
    n = len(accounts[0])
    wealth = []

    for i in range(m):
        temp = 0
        for j in range(n):
            temp = temp + accounts[i][j]
        wealth.append(temp)
    maxiumum = max(wealth)
    return maxiumum

