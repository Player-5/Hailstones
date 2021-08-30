#!/usr/bin/env python3

class hailstone_number:

    def __init__(self, num):

        if not isinstance(num, int):
            raise TypeError(f"Object type int excpected not {type(num)}.")
        if num < 1:
            raise ValueError(f"int value must be greater then 0.")

        self.start_num = num
        self.num = num
        self.steps = 0
        self.max = num
        self.lst = []
        self.lst.append(num)

    def __even(self):
        self.num /= 2

    def __odd(self):
        self.num = (3 * self.num) + 1

    def __print(self):
        print(f"Number: {self.start_num}")
        print(f"Steps: {self.steps}")
        print(f"Numbers: {self.lst}")
        print(f"Max: {self.max}")

    def calculate(self):

        while self.num != 1:

            if self.num % 2 == 0:
                self.__even()
            else:
                self.__odd()

            if self.num > self.max:
                self.max = self.num

            self.lst.append(self.num)
            self.steps += 1
        self.__print()

if __name__ == "__main__":
    import sys

    def get_num():

        if len(sys.argv) != 2:
            raise ValueError("Argument not given")
        return int(sys.argv[1])

    def run():
        number = hailstone_number(get_num())
        number.calculate()
        
    run()
