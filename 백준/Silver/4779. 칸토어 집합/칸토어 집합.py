while True:
    try:
        n = int(input())

        for i in range(pow(3, n)):
            tmp  = i
            flag = tmp%2==0
            for j in range(n-1):
                tmp//=3
                flag = flag and tmp%2==0
            if flag:
                print("-", end = '')
            else :
                print(end = ' ')
        print()
    except EOFError:
        break