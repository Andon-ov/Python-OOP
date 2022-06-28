def get_line(i, n):
    space = n - 1 - i
    star = i + 1
    return ' ' * space + '* ' * star


def make_rhombus(n):
    for i in range(n):
        print(get_line(i, n))

    for i in range(n - 2, -1, -1):
        print(get_line(i, n))


make_rhombus(int(input()))
