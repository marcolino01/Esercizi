i : int = 0

assert i == 0 , f"the value must be equal to 0 instead is {i}"


def check_sqrt(func, input, result):
    
    n = func(input)

    assert n == result, f"error the expected value is {result}, your functions retutn {n}"


def constant(input):

    return -1

from math import sqrt

check_sqrt(sqrt, 4, 2)
check_sqrt(sqrt, 9, 3)


import unittest



class Calculations:

    def __init__(self, a : float, b : float) -> float:
        self.a : int = a
        self.b : float = b

    def get_sum(self):

        return self.a + self.b
    
    def get_difference(self):

        return self.a - self.b
    
    def get_product(self):

        return self.a * self.b
    
    def get_quotient(self):

        return self.a / self.b
    
    
    

