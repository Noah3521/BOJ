N = int(input())
li = list()
adder = 0
result = [0]*N
for i in range(N):
  li.append(input())
for i in range(N):
  for j in range(len(li[i])):
    tmp = li[i][j]
    if tmp == 'O':
      adder += 1
    else :
      adder = 0
    # print("{} + ".format(adder))
    result[i] += adder
  adder = 0

for i in result:
  print(i)