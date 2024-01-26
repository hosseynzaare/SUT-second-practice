def changebase(n, base=10, to=10):
    n = int(str(n),base)
    positive = n >= 0

    if to == 10:
        return str(n)
    n = abs(n)
    num = []
    handle_digit = lambda i: str(i) if i < 10 else chr(i+55)
    while n > 0:
        num.insert(0, handle_digit(n % to))
        n = n // to

    return ''.join(num) if positive else '-' + ''.join(num)

sumMaghsum = []
oldbasee = []

while True:
    inputt = entry , basee = map(int, input().split())
    if basee <= 9 and basee >= 2:
        list = [] 
        list2 = []
        s_maghsum = []
        for i in range(1, (entry + 1)):
            if (entry % i) == 0:
                list.append(i)
        maghsum = sum(list)
        oldbasee.append(basee)
        s_maghsum.append(maghsum)

    else:
        s_maghsum = []
        oldbasee.append(basee)

    
    for j in s_maghsum:
        if entry != -1 and basee != -1:
            b = int(changebase(j, 10, basee))
            list2.append(b)

            sumMaghsum.append(list2[0])
    if  entry == -1 and basee == -1:
        oldbasee.pop()
        z = 0
        for x in oldbasee:
            if x > 9 or x < 2 :
                print("invalid base!")
                z = 1
                exit()
            break
        
        if z == 0:
            summ = sum(sumMaghsum)
            print(summ)
            break