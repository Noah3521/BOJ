N, M = map(int ,input().split())

st = set()

for i in range(N):
    s = input()
    st.add(s)

count = 0
for i in range(M):
    s = input()
    if s in st:
        count += 1

print(count)