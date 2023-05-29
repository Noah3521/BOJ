N = int(input())
li = list(map(int, input().split()))

li.sort()
print(li[0]*li[len(li)-1])