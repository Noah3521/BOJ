def hansu(N) :
    han = 0

    for i in range(1, N+1):
        if i < 100: 
         han += 1
        else :
            #print(f"i = {i} / {(i//100)} - {((i//10))%10} == {((i//10))%10} - {(i%10)}")
            if (i//100) - ((i//10))%10 == ((i//10))%10 - (i%10) :
             han +=1
    return han


N = int(input())
result  = hansu(N)
print(result)

