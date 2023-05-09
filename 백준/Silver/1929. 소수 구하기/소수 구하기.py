import sys, math
input = sys.stdin.readline

mx = 1000000
prime = [True for _ in range(mx+1)]
prime[0], prime[1] = False, False
for i in range(2, int(math.sqrt(mx))+1):
    if prime[i] == True:
        j = 2
        while i * j <= mx:
            prime[i*j]=False
            j+=1

N, M = map(int, input().split())

for i in range(N, M+1):
    if prime[i]:
        print(i)