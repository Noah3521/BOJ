def test(N, M, li):
    li.sort(reverse=True)
    res = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (li[i] + li[j] + li[k]) == M :
                    return li[i] + li[j] + li[k]
                if (li[i] + li[j] + li[k]) <= M :
                    # print(i,'번째',li[i], li[j], li[k])
                    res.append(li[i] + li[j] + li[k])
    return max(res)


N, M = map(int, input().split())
li = list(map(int, input().split()))

# N = 5
# M = 21
# li = [5, 6, 7, 8, 9]

# N = 10
# M = 500
# li = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

print(test(N, M, li))