count = 0
for i in range(8):
    li = list(str(input()))
    # print(li)
    for j in range(8):
        if i%2==0:
            if j%2==0:
                if li[j]=='F':
                    # print('횐색입니다')
                    count+=1
        else :
            if j%2!=0:
                if li[j]=='F':
                    # print('횐색입니다')
                    count+=1

# print('answer :', count)
print(count)