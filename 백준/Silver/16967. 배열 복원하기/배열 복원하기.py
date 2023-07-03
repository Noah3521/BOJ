# H, W, X, Y = map(int, input().split())

# li = [[0 for _ in range(W)]for _ in range(H)]

# for i in range(H):
#     tmp = list(map(int, input().split()))
#     for j in range(len(tmp)):
#         li[i][j] = tmp[j]


# li2 = [[0 for _ in range(W+Y)]for _ in range(H+X)]

# print(li)

# for i in range(H):
#     for j in range(W):
#         li2[i][j] = li[i][j]

# for i in range(X+H):
#     for j in range(Y+W):
#         try:
#             li2[i+X][j+Y] += li[i][j]
#         except:
#             pass

# print("\n\n복원 전 배열")
# for i in range(X+H):
#     for j in range(Y+W):
#         print(li2[i][j], end = ' ')
#     print()

H, W, X, Y = map(int, input().split())

li2 = [[0 for _ in range(W+Y)]for _ in range(H+X)]

for i in range(H+X):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        li2[i][j] = tmp[j]

for i in range(X+H):
    for j in range(Y+W):
        try:
            li2[i+X][j+Y] -= li2[i][j]
        except:
            pass

# print("\n\n복원 후 배열")
for i in range(H):
    for j in range(W):
        print(li2[i][j], end = ' ')
    print()
