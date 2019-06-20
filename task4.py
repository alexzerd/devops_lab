
print("Input mat parameters")

n = int(input())

m = int(input())

number_of_elms = 1

center = (n-1)/2

for i in range(n):

    if i < center:

        print(((m - number_of_elms * 3) // 2) * "-", end='')
        print(number_of_elms * ".|.", end='')
        print(((m - number_of_elms * 3) // 2) * "-")
        number_of_elms += 2

    elif i == center:

        print(((m - 7) // 2) * "-", end='')
        print("WELCOME", end='')
        print(((m - 7) // 2) * "-")
        number_of_elms -= 2

    else:

        print(((m - number_of_elms * 3) // 2) * "-", end='')
        print(number_of_elms * ".|.", end='')
        print(((m - number_of_elms * 3) // 2) * "-")
        number_of_elms -= 2
