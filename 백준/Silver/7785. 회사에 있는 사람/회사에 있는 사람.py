N = int(input())

st = set()

for i in range(N):
    s = list(input().split())
    if s[1]=='enter':
        st.add(s[0])
    else :
        if s[0] in st:
            st.remove(s[0])

for i in reversed(sorted(list(st))):
    print(i)