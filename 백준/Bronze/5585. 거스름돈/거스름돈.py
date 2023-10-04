li = [500, 100, 50, 10, 5, 1]

cash = 1000 - int(input())

# print('받을 총 금액: ', cash)

count = 0

for i in li :
    while cash >= i :
        count += 1
        # print(i,'원 1개 추가:', count)
        cash -= i

print(count)