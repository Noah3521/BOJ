from itertools import combinations, permutations

def f(n):
    li = []
    for i in range(1, n+1):
        if n%i==0:
            li.append(i)
    # print(li)
    combi = []
    for i in range(2, len(li) + 1):
        combi += list(combinations(li, i))
    
    li.remove(n)
    if sum(li) == n:
        print(n, end = ' = ')
        for i in range(len(li)):
            if i == len(li)-1:
                print(li[i])
            else :
                print(li[i], end = ' + ')
    else :
        print(n, 'is NOT perfect.')


                
while(True):
    n = int(input())
    if n==-1:
        break
    f(n)