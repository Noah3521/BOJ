import sys
input = sys.stdin.readline

N = int(input())

dict = {
    0:[10],
    1:[1],
    2:[2,4,8,6],
    3:[3,9,7,1],
    4:[4,6],
    5:[5],
    6:[6],
    7:[7,9,3,1],
    8:[8,4,2,6],  
    9:[9,1] 
}

for i in range(N):
    a, b = map(int, input().split())
    a%=10
    print(dict[a][b%len(dict[a])-1])