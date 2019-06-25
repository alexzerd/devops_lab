def conclusion(str):

    x, y = count_position(str)
    print(x == 0 and y == 0)

    return x == 0 and y == 0


def count_position(dir):

    x = 0
    y = 0

    length = len(dir)

    for i in range(length):
        if dir[i] == 'U':
            y += 1
        elif dir[i] == 'D':
            y -= 1
        elif dir[i] == 'R':
            x += 1
        else:
            x -= 1

    return x, y


if __name__ == "__main__":
    directions = input("Input directions: ")
    conclusion(directions)
