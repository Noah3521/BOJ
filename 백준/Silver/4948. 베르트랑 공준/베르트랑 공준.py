import sys, math
input = sys.stdin.readline

# 시간초과 해결법 : 먼저 123456*2만큼의 수를 소수판별한 후 선택한 범위의 값 확인
mx = 246912
prime = [True for _ in range(mx+1)]
prime[0], prime[1] = False, False
for i in range(2, int(math.sqrt(mx))+1):
    if prime[i] == True:
        j = 2
        while i * j <= mx:
            prime[i*j]=False
            j+=1


N = -1
while True:
    N = int(input())    
    if N==0:
        break
    cnt = 0
    for i in range(N+1, 2*N+1):
        if prime[i]:
            cnt+=1
    print(cnt)
