#!/usr/bin/env python3
# coding: utf-8

"""
A python3 module used to calculate hailstone Numbers, testing if they terminate
into 4, 2, 1. and recording relevent data about the proccese.
"""

class hailstone:
    """
    A class to calculate and store relevent data on hailstone numbers

    Parameters
    ----------
    num : int
        The number which all calculations will start from

    Attributes
    ----------
    start_num : int
        stored in memory to recall the origin point

    num : int
        the working number which all calculations will be preformed on

    steps : int
        An integers used to count the number of steps unitl complition

    max : int
        the highest vaule reached during calculations, defaults to start_num

    lst : list
        A list of integers that were reached before terminateing to 1
    """

    def __init__(self, num):

        # checking the num to make sure it's an int and greater then 0
        if not isinstance(num, int):
            raise TypeError(f"Object type int excpected. not {type(num)}.")
        if num < 1:
            raise ValueError(f"Integer value must be greater then 0.")

        # assigning attributes to class instance
        self.start_num = num

        self.num = self.max = self.start_num

        self.steps = 0

        self.lst = [self.start_num]

    def print(self):
        """
        Used to output the data collected to the user through the command line

        Parameters
        ----------
        Null

        Raises
        ------
        Null

        Returns
        -------
        Null
        """
        print(f"Number: {self.start_num}")
        print(f"Steps: {self.steps}")
        print(f"Numbers: {self.lst}")
        print(f"Max: {self.max}")

    def calculate(self):
        """
        The main method of the class used to determine which calculation to perform

        Parameters
        ----------
        Null

        Raises
        ------
        Null

        Returns
        -------
        Null
        """
        # loops until num terminates at 1
        while self.num != 1:

            # checks whether num is even or odd
            self.num = self.num / 2 if self.num % 2 == 0 else (3 * self.num) + 1

            # checks if num has surpassed current max
            if self.num > self.max:
                self.max = self.num

            # adds num to lst and increments steps counter
            self.lst.append(self.num)
            self.steps += 1

        # when finished output data to user
        self.print()

if __name__ == "__main__":

    import sys

    # checks if enough arguments have been passed through
    if len(sys.argv) < 2:
        raise ValueError("Correct number of argument not given.")

    # creates list of arguments
    args = list(map(int, sys.argv[1:]))

    # turns args into hailstone(s) and runs .calculate() on all of them
    list(map(hailstone.calculate, list(map(hailstone, args))))
