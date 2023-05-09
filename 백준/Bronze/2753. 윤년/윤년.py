year = int(input())
isLeap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if isLeap :
    print(1)
else :
    print(0)