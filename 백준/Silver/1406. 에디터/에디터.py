import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip("\n")

left = deque(s)
right = deque()

for i in range(int(input())) :
    cmd = input().rstrip("\n")

    # left
    if cmd=='L':
        if left:
            right.appendleft(left.pop())
    # right
    elif cmd=='D':
        if right:
            left.append(right.popleft())
    # l del
    elif cmd=='B':
        if left:
            left.pop()
    # l add
    else:
        left.append(cmd.split()[1])

print(''.join(left + right))