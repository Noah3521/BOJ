def fibo1(n, count):
    if(n==1 or n==2):
        return 1
    return fibo1(n-1, count) + fibo1(n-2, count)

def fibo2(n, li, count) :
    if n==1 or n==2:
        return li[n]
    for i in range(3, n+1):
        count+=1
        li[i] = li[i-1] + li[i-2]
    return count

n = int(input())

li = [1 for _ in range(n+1)]

print(fibo1(n, 0), fibo2(n, li, 0))