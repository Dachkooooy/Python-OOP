from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        # drug variant za reshenie
        # return sum(args)
        # izpolzvame reduce s cel konsistentnost
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)
