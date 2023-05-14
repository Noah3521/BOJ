T = int(input())
for i in range(T):
    ch = input().split()
    for i in ch:
        print(i[::-1],end=' ')
    print()