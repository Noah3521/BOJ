H = [int(input()) for _ in range(9)]

H.sort()

N = sum(H) - 100

# print(N)
# print(H)
for i in range(len(H)):
    for j in range(i+1, len(H)):
        if(H[i] + H[j] == N):
                remove1 = H[i]
                remove2 = H[j]
                break
H.remove(remove1)
H.remove(remove2)

for i in H:
     print(i)