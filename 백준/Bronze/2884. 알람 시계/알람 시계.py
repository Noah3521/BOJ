hh, mm = map(int, input().split())

if mm < 45:
    hh -= 1
    tmp = mm - 45
    mm = 60 + tmp
else :
    mm -= 45

if hh == -1:
    hh = 23
print("{} {}".format(hh, mm))