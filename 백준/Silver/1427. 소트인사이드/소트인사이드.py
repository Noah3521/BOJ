n = int(input())
li_n = list(map(int, str(n)))

li_n.sort(reverse=True)
for i in li_n:
    print(i, end="")