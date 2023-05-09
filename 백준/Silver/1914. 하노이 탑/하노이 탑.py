def hanoi(frm, to, n):
    if n == 1:
        print(f'{frm} {to}')
    else:
        empty = 6 - frm - to
        hanoi(frm, empty, n - 1)
        print(f'{frm} {to}')
        hanoi(empty, to, n - 1)


numberOfDisk = int(input())
startLocation = 1
desLocation = 3
print(pow(2, numberOfDisk)-1)
if numberOfDisk <= 20:
    hanoi(startLocation, desLocation, numberOfDisk)