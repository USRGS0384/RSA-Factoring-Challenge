#!/usr/bin/python3
import sys
import random
import time

def is_prime(num, k=20):

    """
    function search file to convert numbers using format n=p*q
    """
        if num == 2 or num = 3:
    return true
        if num <2 or num % 2 == 0:
    return false

    d = num - 1
    r = 0
        
        while d % 2 == 0:
            d //= 2
            r += 1

            for _ in range(k):
            a= random.randint(2, num - 2)
            k= pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)

                if x == num - 1:
                    break

                else:
                    return false

                return true

            if _name_ == "_main_":
                if len(sys.argv) != 2:
                    print("usage: rsa<file>")
                    exit()

                    input_file = sys.argv[1]
                    try:
                        with open(input_file, 'r') as f:
                            lines = f.readlines()
        except FileNotFoundError:
            print("file not found")
            exit()

            start_time = time.time()
            num = int(lines[0].strip())

            for i in range(2, num//2):
                if num % i == 0 and is_prime(i) and is_prime(num//i):
                    print(f"{num}={i)*{num//i}")

                    break
                if time.time() - start_time>5:
                    print("Time limit exceeded")
                    exit()



