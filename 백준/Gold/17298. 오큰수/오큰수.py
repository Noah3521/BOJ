N = int(input())
li = list(map(int, input().split()))

# N = 5
# li = [1,8,5,7,9]

# print(li)
stack = []
answer = [-1 for _ in range(N)]

stack.append(0)

for i in range(N):
    if li[stack[-1]] >= li[i] :
        stack.append(i)
        # print("1 stack ",stack)
        # print("1 answer", answer)
    else :
        while stack and li[stack[-1]] < li[i]:
            answer[stack.pop()] = li[i]
        stack.append(i)
        # print("2 stack",stack)
        # print("2 answer", answer)

# print(answer)
for i in answer : 
    print(i, end = ' ')
# answer = 8979-1