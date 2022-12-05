def max_profit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            pricediff = prices[j] - prices[i]
            if pricediff > max_profit:
                max_profit = pricediff
    return max_profit


print(max_profit([6,1,9,3,6,3,1]))