a,b = map(int, input().split())

ra = 0
rb = 0
ra += a%10*100
ra += a//10%10*10
ra += a//100

rb += b%10*100
rb += b//10%10*10
rb += b//100

if ra > rb:
    print(ra)
else :
    print(rb)