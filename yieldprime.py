# -*- coding: utf-8 -*-

import math
import time


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
           number = yield number
        # time.sleep(1)
        number += 1


def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)

    # can't send non-None value to a just-started generator
    prime_generator.send(None) 

    for power in range(iterations):
        print(prime_generator.send(base ** power))


print_successive_primes(12, 10)
