class take_skip:
    def __init__(self, step:int, count:int):
        self.step = step
        self.count = count
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.count:
            raise StopIteration
        else:
            value = self.current * self.step
            return value

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
