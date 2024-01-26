a = int(input('input your entry '))
for i in range(1, a+1):
    b = 1
    for j in range(1, i+1):
        print(b, ' ', sep='', end='')
        b = b * (i - j) // j
    print()