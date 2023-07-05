x,y,w,h = map(int, input().split())

a,b = 0,0

w,h
x,y

if x > w-x:
    a=w-x
    # print('1',w-x)
else :
    a=x
    # print(x)

if y > h-y:
    b=h-y
    # print('1',h-y)
else :
    b=y
    # print(y)

if a<b:
    # print('answer:',a)
    print(a)
else :
    # print('answer', b)
    print(b)