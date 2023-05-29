N = 3
for i in range(N):
    li = list(map(int, input().split()))
    
    cnt = li.count(0)

    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    else :
        print('E')
    
    