total = int(input())
var = int(input())

for i in range(var) :
    price, cnt = map(int, input().split())
    total -= price * cnt

if total == 0 :
    print("Yes")
else :
    print("No")