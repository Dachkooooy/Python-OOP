def print_top(n):
    for row in range(n + 1):
       print(f"{' '*(n-row)}{'* ' * row}")


def print_bottom(n):
    for row in range(1, n):
        print(f"{' '* row}{'* ' * (n-row)}")


def print_rhombus(n):
    print_top(n)
    print_bottom(n)


n = int(input())
print_rhombus(n)