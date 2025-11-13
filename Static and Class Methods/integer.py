roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }

class Integer:

    def __init__(self, value:int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, roman_num):
        int_value = 0

        for i in range(len(roman_num)):
            if roman_num[i] in roman_numerals:
                if i + 1 < len(roman_num) and roman_numerals[roman_num[i]] < roman_numerals[roman_num[i + 1]]:
                    int_value -= roman_numerals[roman_num[i]]
                else:
                    int_value += roman_numerals[roman_num[i]]
        return cls(int_value)

    @classmethod
    def from_string(cls, string):
        if not isinstance(string, str):
            return "wrong type"
        try:
            return cls(int(string))
        except ValueError:
            return "wrong type"