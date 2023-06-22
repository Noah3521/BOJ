n = input()

# 입력된 이진수가 유효한지 확인
if all(char in '01' for char in n):
    # 2진수 -> 10진수 변환
    d = int(n, 2)
    # 10진수 -> 8진수 변환
    print(oct(d)[2:])
else:
    print("유효한 이진수를 입력해주세요.")
