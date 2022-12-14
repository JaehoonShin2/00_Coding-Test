import sys

n = int(sys.stdin.readline().rstrip())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(1, n):
    #red
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    #green
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    #blue
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
    
print(min(dp[n-1]))