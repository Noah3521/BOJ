C = int(input())
total = 0
sm = list()
bak_li = list()
bak_cnt = list()
cnt = 0
for i in range(C):
  li1 = list(map(int, input().split()))
  bak_li.append(li1)
  for j in li1[1:]:
    total += j
  sm.append(total/li1[0])
  total = 0


for i in range(C) :
  for j in bak_li[i][1:]:
    if j > sm[i] :
      cnt += 1
  bak_cnt.append(cnt)
  cnt = 0

for i in range(C):
  N = bak_li[i][0]
  result = bak_cnt[i]/N*100
  print(f"{result:.3f}%")

# print(bak_li)
# print(sm)
# print(bak_cnt)