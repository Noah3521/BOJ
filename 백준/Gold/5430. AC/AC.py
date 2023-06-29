import re
from collections import deque
import sys

input = sys.stdin.readline

def solution(size, prompt, li):
    flag = False
    r = 0
    for i in prompt: 
        if i=='R':
            r+=1
        if i=='D':
            if not li:
                # print('빈 리스트임')
                flag = True
            else :
                if r%2==0:
                    li.popleft()
                else :
                    li.pop()
    
    # print('-------->', end = '')
    if flag :
        print('error')
    else :
        answer = ""
        answer += '['

        tmp1 = list(reversed(li))
        tmp2 = list(li)
        if len(tmp)!=0:
            if r%2!=0:  # 뒤집을 경우
                for i in range(len(tmp1)) :
                    answer += str(tmp1[i])
                    if(i!=len(tmp1)-1): answer += ','

            else :      # 뒤집지 않을 경우
                for i in range(len(tmp2)):
                    answer += str(tmp2[i])
                    if(i!=len(tmp2)-1): answer += ','

        answer += (']')
        print(answer)
T = int(input())
for i in range(T):
    prompt = list(input())
    size = int(input())
    tmp = input()
    li = list(map(int, re.sub(r'[^0-9]', ' ', tmp).split()))
    li = deque(li)
    solution(size, prompt, li)
