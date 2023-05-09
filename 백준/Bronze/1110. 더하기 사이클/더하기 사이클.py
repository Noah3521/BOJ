ab1 = int(input())
ab2 = ab1
count = 0
while True : 
    a = ab2 // 10
    b = ab2 % 10
    ab2 = b*10 + (a+b)%10 # 84
    count+=1
    if ab1 == ab2 :
        break
    
print(count)