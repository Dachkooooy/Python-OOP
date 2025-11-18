class sequence_repeat:
    def __init__(self, sequence:list, number:int):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.number:
            idx = self.current_index % len(self.sequence)
            self.current_index += 1
            return self.sequence[idx]
        raise StopIteration

# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
