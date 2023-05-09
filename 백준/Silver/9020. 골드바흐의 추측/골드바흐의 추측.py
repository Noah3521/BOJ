import sys, math
input = sys.stdin.readline

mx = 10001
prime = [True for _ in range(mx+1)]
prime[0], prime[1] = False, False
for i in range(2, int(math.sqrt(mx))+1):
    if prime[i] == True:
        j = 2
        while i * j <= mx:
            prime[i*j]=False
            j+=1

for _ in range(int(input())):
    n = int(input())
    if n==4:
        print(2,2)
    else:
        a=n//2
        b=a
        while not (prime[a] and prime[b]):
            a-=1
            b+=1
        print(a, b)
