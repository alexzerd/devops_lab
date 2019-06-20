
directions = input("Input directions in capital letters\n")

x = 0
y = 0

length = len(directions)

for i in range(length):

    if directions[i] == 'U':

        y += 1

    elif directions[i] == 'D':

        y -= 1

    elif directions[i] == 'R':

        x += 1

    else:

        x -= 1

if (x == 0) and (y == 0):

    print("true")

else:

    print("false")
