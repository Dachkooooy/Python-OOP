def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1

for el in squares(3):
    print(el)