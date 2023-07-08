li=[]
n=int(input())
for i in range(n):
    li.append(input())

s = "daf"
c=[]
for i in range(len(li[0])):
    for j in range(n):
        # print("li[j][i] :", li[j][i])
        if j!=0 and li[j][i]!=tmp:
            c.append(i)
            break
        tmp = li[j][i]

idx=0
for i in range(len(li[0])):
    # print('c :', c[idx], i)
    if idx<len(c) and c[idx]==i:
        print('?',end='')
        idx+=1
        continue
    print(li[0][i], end ='')