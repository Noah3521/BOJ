n = int(input())

f = 1

for i in range(1, n+1) :
    f*=i

answer = 0

for i in reversed(str(f)) :
    if i!='0' :
        break
    answer += 1

print(answer)