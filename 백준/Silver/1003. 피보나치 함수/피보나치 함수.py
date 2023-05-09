def fibo(n):
    if li[n]!=0:
        return li[n]
    if n==1 or n==2:
        li[n]=1
        return li[n]
    else:
        li[n]=fibo(n-1)+fibo(n-2)
        return li[n]

li=[0]*41

for i in range(int(input())):
    n=int(input())
    if n==0:
        print(1,0)
    else :
        fibo(n)
        print(f"{li[n-1]} {li[n]}")