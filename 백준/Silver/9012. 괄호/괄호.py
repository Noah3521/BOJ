T = int(input())

for i in range(T):
    vps = input()

    stack = []

    res = ''

    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else :
                res = 'NO'

    # print("res :",res)
    # print("stack :",stack)

    if res == '' and not stack:
        print('YES')
    else:
        print('NO')