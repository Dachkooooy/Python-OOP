class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data.pop(-1)

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return "[" + ', '.join(reversed(self.data)) + "]"

my_info = Stack()
print(my_info.push("1"))
print(my_info.push("2"))
print(my_info.push("3"))
print(my_info)
print(my_info.pop())
print(my_info.top())
print(my_info.is_empty())
