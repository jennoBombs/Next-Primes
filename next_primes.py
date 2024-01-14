#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Jennifer Reisinger"
__email__ = "jhubbard3@students.columbiabasin.edu"
__date__ = "Spring 2022"
__version__ = "0.1"

# libraries
import sys
import numpy as np


# script arguments
script_name = sys.argv[0]
script_arguments = sys.argv[1:]
start_number = int(script_arguments[0])
generate_prime_count = int(script_arguments[1])

# set default variables
i = 0
primes = []

# the isPrime method checks the start_number to see if it is prime
def isPrime(start_number):
    if (start_number % 2 == 0):
        return False
    # the np arange method checks for factors
    for i in np.arange(3, int(start_number**0.5 + 1), 2):
        if (start_number % i == 0):
            return False
    return True

# loop
while True:
    # increment the counter
    start_number += 1
    # is it prime?
    if (isPrime(start_number)) is True:
        primes.append(start_number)
        i += 1
        # if the count is good, then exit
        if (i == generate_prime_count):
            break

# print the results per the requirements
#R5
print('Prime Numbers:', primes)