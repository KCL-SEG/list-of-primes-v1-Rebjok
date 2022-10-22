"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import is_
import math


def primes(number_of_primes):
    list = [2]
    track = 1
    number = 3

    while track < number_of_primes:

        is_prime = True
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                is_prime = False

        if is_prime:
            list.append(number)
            track += 1

        number += 2
    return list
