s = input()

li = s.split("-")

# print(li)

answer = 0

for i in range(len(li)) :
    
    if li[i].__contains__("+") :
        temp = 0
        for j in li[i].split("+") :
            temp += int(j)
    
        li[i] = temp

temp = li.pop(0)
# if not temp.isdigit() :
temp = int(temp)
answer += temp

if li :
    for i in li :
        if str(type(i))=="<class 'str'>" :
            answer -= int(i)
        else :
            answer -= i


print(answer)