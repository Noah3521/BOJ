input = input()

"""
1:1 2:2 3:3 4:4 5:5
1:2 2:3 3:4 4:5
1:3 2:4 3:5 
1:4 2:5
1:5
"""

li = []
for i in range(0,len(input)+1):
    for j in range(0,i):
        # print(j,i,end=' ')
        # print(input[j:i])
        li.append(input[j:i])

print(len(set(li)))