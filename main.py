#!/usr/bin/env python3
# coding: utf-8

"""
A python3 module used to calculate hailstone Numbers, testing if they terminate
into 4, 2, 1. and recording relevent data about the proccese.
"""

class hailstone_number:
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
        self.num = self.start_num
        self.steps = 0
        self.max = self.start_num
        self.lst = []
        self.lst.append(num)

    def __even(self):
        """
        A method to half the num when it is found to be even

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
        self.num /= 2

    def __odd(self):
        """
        A method to increase num by 3n+1 when it is found to be odd

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
        self.num = (3 * self.num) + 1

    def __print(self):
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
            if self.num % 2 == 0:
                self.__even()
            else:
                self.__odd()

            # checks if num has surpassed current max
            if self.num > self.max:
                self.max = self.num

            # adds num to lst and increments steps counter
            self.lst.append(self.num)
            self.steps += 1

        # when finished output data to user
        self.__print()

if __name__ == "__main__":
    import sys

    def get_num():
        """
        Returns a list of arguments provided from the command line.

        Parameters
        ----------
        Null

        Raises
        ------
        Null

        Returns
        -------
        args_lst : (lst)
            an array of integers
        """
        if len(sys.argv) < 2:
            raise ValueError("Correct number of argument not given.")

        return list(map(int, sys.argv[1:]))

    def run():
        """
        Loops over the provided numbers to calculate the hailstone conjecture.

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

        lst = list(map(hailstone_number, get_num()))

        for x in range(len(lst)):
            lst[x].calculate()

    # runs the calculation on the provided integers
    run()
