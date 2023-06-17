N = int(input())
F = int(input())

for i in range(100):
    s = str(N//100) + str("%02d" % i)
    if int(s)%F==0:
        print("%02d"%i)
        break