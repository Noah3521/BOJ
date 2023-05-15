n, b = input().split()  # 입력값 N과 B를 받음
b = int(b)  # B를 정수형으로 변환
result = 0  # 결과값 초기화
k = 1  # 자릿수를 표현하는 변수 초기화

for digit in reversed(n):  # N의 각 자리 숫자에 대해 뒤에서부터 처리
    if digit.isdigit():  # 숫자인 경우에만 처리
        result += int(digit) * k  # 결과값에 현재 자리 숫자를 곱한 후 더함
    else:  # 알파벳인 경우에는 아스키 코드를 이용하여 숫자로 변환한 후 처리
        result += (ord(digit) - ord('A') + 10) * k  # 결과값에 현재 자리 숫자를 곱한 후 더함
        # print((ord(digit) - ord('A') + 10))
    k *= b  # 자릿수 변수를 업데이트

print(result)  # 결과값 1