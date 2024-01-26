print_list = []
n = int(input())
mmd = ["*"]
for i in range( 2 , (n + 1)):
    mmd.append(".")
counter = 0
while True:
    direction = input()
    if direction == "END":
        break
    elif direction == "B":
        print_list.append(mmd)
        mmd = []
        for i in range( 1 , (n + 1)):
            mmd.append(".")
        mmd[counter] = "*"
    if counter < (n - 1):
        if direction == "R":
            counter += 1
            mmd[counter] = "*" 
    if counter > 0:
        if direction == "L":
            if counter == 0:
                counter = counter + 1
            counter -= 1
            mmd[counter] = "*"
print_list.append(mmd)
for k in range(0, (len(print_list))):
    print(' '.join(print_list[k]))
if counter != (n - 1):
    print("There's no way out!")