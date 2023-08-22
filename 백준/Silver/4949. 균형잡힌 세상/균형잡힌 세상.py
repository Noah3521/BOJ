
def f(row):
    st = []
    answer = 'yes'
    for i in row :
        if i == '(' or i == '[':
            st.append(i)
        if i==')':
            if st and st[-1] == '(':
                st.pop()
            else :
                answer = 'no'
        if i==']':
            if st and st[-1] == '[':
                st.pop()
            else :
                answer = 'no'

    if st :
        answer = 'no'

    print(answer)

while True:
    row = input()
    if row == '.':
        break
    else :
        f(row)