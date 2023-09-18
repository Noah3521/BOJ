import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

for i in range(int(input())) :
    cmd = input().rstrip('\n')
    
    if cmd=='pop' :
        if queue:
            print(queue.popleft())
        else :
            print(-1)
    elif cmd=='size':
        print(len(queue))    
    elif cmd=='empty':
        if len(queue)==0:
            print(1)
        else :
            print(0)
    elif cmd=='front':
        if queue:
            print(queue[0])
        else :
            print(-1)
    elif cmd=='back':
        if queue: 
            print(queue[-1])
        else :
            print(-1)
    else : #push X
        queue.append(cmd.split()[1])
    