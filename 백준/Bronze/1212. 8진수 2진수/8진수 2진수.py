value = int(input()) # 8진수

value = int(str(value), 8)
value = bin(value)
print(value.split('0b')[1])