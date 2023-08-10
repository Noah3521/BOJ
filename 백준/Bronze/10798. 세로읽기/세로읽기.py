"""
5 X 5 배열 만들어서 입력받기
y를 먼저 증가시키고 x를 증가시키는 방법으로 출력
"""

li = []

maxlen = 0

for i in range(5):
   s = list(input())
   li.append(s)
   if maxlen < len(s) :
      maxlen = len(s)

for i in range(maxlen):
   for j in range(5):
      try:
         print(li[j][i], end='')
      except:
         continue
