class vowels:
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
    def __init__(self, some_string):
        self.some_string = some_string
        self.current = -1
        self.vowels = [el for el in self.some_string if el.lower() in vowels.vowels_list]

    def __iter__(self):
        return self

    # def __next__(self):
    #     self.current += 1
    #     if self.current >= len(self.some_string):
    #         raise StopIteration
    #     if self.some_string[self.current].lower() in self.vowels:
    #         return self.some_string[self.current]
    #     else:
    #         return self.__next__()

    def __next__(self):
        self.current += 1
        if self.current >= len(self.vowels):
            raise StopIteration
        else:
            return self.vowels[self.current]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
