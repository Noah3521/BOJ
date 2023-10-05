n = int(input())

total = 0

count = 0



for i in range(1, 4294967295+1) :
    if total + i > n :
        break
    count += 1
    total += i

    
# print(total)
print(count)