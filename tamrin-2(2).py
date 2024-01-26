func = input()
sum_list = []
list_lcd = []
list_gcd = []

if func == "sum":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        sum_list.append(b)  
    a = sum(sum_list)
    print(a)
    
elif func == "average":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        sum_list.append(b)  
    a = sum(sum_list)
    length = len(sum_list)
    average = (a / length)
    round = round(average, 2)
    print(round)
    
elif func == "min":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        sum_list.append(b)
    length = len(sum_list)
    min = sum_list[0]
    for i in sum_list:
        if i < min:
            min = i
    print(min)

elif func == "max":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        sum_list.append(b)
    length = len(sum_list)
    max = sum_list[0]
    for i in sum_list:
        if i > max:
            max = i
    print(max)
    
elif func == "lcd":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        list_lcd.append(b)
        length = len(list_lcd)
    list_lcd.sort()
    d = 0
    kmm = list_lcd[d]
    if list_lcd[d] != list_lcd[d + 1]:
        if kmm < list_lcd[d + 1]:
            slm = True
            while slm:
                slm = False
                for i in range(1, 1000):
                    aa = int(kmm) * i
                    w = aa
                    u = int(list_lcd[d + 1])
                    v = (w % u)
                    if v == 0:
                        d += 1
                        kmm = aa
                        if list_lcd[d] != list_lcd[-1]:
                            slm = True
                        break               
            print(kmm)
        
elif func == "gcd":
    while True:
        entry = input()
        if entry == "end":
            break
        b = int(entry)
        list_lcd.append(b)
        length = len(list_lcd)
    list_lcd.sort()
    import functools
    import math
    def gcd(list_lcd):
        gcd = list_lcd[0]
        for num in list_lcd[1:]:
            gcd = math.gcd(gcd, num)
        return gcd
    result = gcd(list_lcd)
    print(result)

else:
    print('Invalid command')