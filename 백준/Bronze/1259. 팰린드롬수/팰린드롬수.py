
while True :
    s = input()

    if(s=='0') : 
        break

    mid = len(s)//2

    # print(s[mid::-1])
    # print(s[mid:])


    if len(s)%2==0 :
        if s[mid-1::-1]==s[mid:] :
            print('yes')
        else :
            print('no')
    else :
        if s[mid::-1]==s[mid:] :
            print('yes')
        else :
            print('no')