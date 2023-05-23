N = int(input())
n = 665
cnt = 0

while cnt != N:
    n += 1
    if str(n).count("666") != 0:
        cnt += 1

print(n)