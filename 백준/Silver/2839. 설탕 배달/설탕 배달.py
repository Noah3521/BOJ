n = int(input())

res = 0

res = n // 5
r = n % 5

if r == 0:
    pass
elif r == 1 and res >= 1:
    res -= 1
    res += 2

elif r == 2 and res >= 2:
    res -= 2
    res += 4

elif r == 3 and res >= 0:
    res += 1

elif r == 4 and res >= 1:
    res -= 1
    res += 3
else :
    res = -1

print(res)