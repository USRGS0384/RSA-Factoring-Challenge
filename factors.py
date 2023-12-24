#!/usr/bin/python3
"""Module that factorize as many numbers as possible
 into a product of two smaller numbers."""

import sys 
import time

def factorize(num):
    """Takes a number as input

    args:
    num: input integers.
    Return: A tuple of two factors if the number is not a
        prime
    None if the number is prime"""

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return(i, num//i)
        return None

    if _name_ == "_main_":

        """reads the input file."""

        if len(sys.argv) != 2:
            print("usage: factors <file">)
            exit()
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as f:
        lines = f.readlines()
    except FileNotFoundError:
    print("file not found")
    exit()

    start_time = time.time()
    """loops over each line (that shound contian one each number)
   if the factorize returns a tuple of factors.
   it prints the factorizationin the desired forms"""

   for line in line:
       num = int(line.strip())
       factors = factorize (num)
       if factors:
           print(f"{num}={factors[0]}*{factors[1]}")

           """if the elapsed time exceeded 5 seconds, the program
           exits with an error message"""

           if time.time() - start_time>5:
               print("Time limit exceeded")
               exit()
