def count_change(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]
    return dp[money]

print(count_change(4, [1, 2]))
print(count_change(10, [5, 2, 3]))
print(count_change(0, []))