tmp = int(input())
N = input()
N_list = list(map(int, str(N)))

result = 0
for i in N_list:
    result += i
    
print(result)