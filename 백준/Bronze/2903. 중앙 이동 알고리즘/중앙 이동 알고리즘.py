n = int(input())

st = 3

for i in range(1, n):
    st += 2 ** (i)
print(st**2) 