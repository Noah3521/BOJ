N = int(input())

#  ===== 피보나치 수 정렬 미리 생성 =====
fibo = [0 for _ in range(N+1)]

for i in range(N+1):
    if i==0:
        fibo[0] = 0
        continue
    elif i<2:
        fibo[i] = 1
        continue
    fibo[i] = fibo[i-1] + fibo[i-2]

# ===== 입력받아서 해당 인덱스 출력 =====

print(fibo[N])