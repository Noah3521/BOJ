N = int(input())
for i in range(int(N/2), N) :
    if i + sum(map(int, str(i))) == N : 
        print(i)
        break
else :
    print(0)