def isStar(i, j):
    if i < 1 or j < 1:
        return False
    if(i%3==1 and j%3==1):
        return True
    return isStar(i//3, j//3);

N = int(input())
for i in range(N):
    for j in range(N):
        if isStar(i, j):
            print(end = ' ')
        else :
            print('*', end = '')
    print()