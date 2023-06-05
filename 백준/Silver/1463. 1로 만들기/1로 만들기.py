# 1 -> 0
# 2 -> 1
# 3 -> 1
# 4 -> 2
# 5 -> 3
# 6 -> 2
# 7 -> 3
# 8 -> 3
# 9 -> 2
# 10-> 3
def sol(N):
    if N > 6: dp = [0 for _ in range(N+1)]
    else :
        dp = [0 for _ in range(6+1)]
        dp[1] = 0
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 3
        dp[6] = 2
        print(dp[N])
        return
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 3
    dp[6] = 2

    # print(dp)
    for i in range(6+1, N+1):
        tmp = [100000 for _ in range(3)]
        tmp[0] = dp[i-1] + 1
        if i%2==0:
            tmp[1] = dp[i//2] + 1
        if i%3==0:
            tmp[2] = dp[i//3] + 1
        dp[i] = min(tmp)
        # print('tmp :', tmp)
        

    print(dp[N])

sol(int(input()))