# 쿼터 25
# 다임 10
# 니켈 5
# 페니 1


N = int(input())
for i in range(N):
    n = int(input())
    print(n // 25, end = ' ')
    print((n % 25) // 10, end = ' ')
    print(((n % 25) % 10) // 5, end = ' ') 
    print((((n % 25) % 10) % 5 ) // 1)