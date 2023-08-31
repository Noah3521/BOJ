n=int(input())
li = []
for i in range(n):
    li.append(int(input()))
stack = []
cnt = 0
answer = ''

for i in range(1, n+1):
    stack.append(i)
    answer += '+\n'
    while stack and stack[-1] == li[cnt]: 
        answer += '-\n'
        stack.pop()
        cnt += 1

if stack : print('NO')
else     : print(answer) 


# stack.append(1)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(2)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(3)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(4)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break        
#     print(stack.pop()) 
#     cnt += 1
# stack.append(5)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(6)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(7)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
# stack.append(8)
# while stack[-1] == li[cnt]: 
#     if len(li) <= cnt: break
#     print(stack.pop()) 
#     cnt += 1
