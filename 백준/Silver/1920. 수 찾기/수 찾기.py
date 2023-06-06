import sys
input = sys.stdin.readline

def isN(st, N):
    if N in st :
        return 1
    else :
        return 0
    
N = int(input())
NL = set(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))
for i in ML:
    print(isN(NL, i))