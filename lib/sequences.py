#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []

    if length <= 0:
        print(fibonacci_list) 
        return
    elif length >= 1:
        fibonacci_list.append(0)  
    if length >= 2:
        fibonacci_list.append(1)  

    a, b = 0, 1

    for _ in range(2, length):
        a, b = b, a + b  
        fibonacci_list.append(b)

    # Print the list
    print(fibonacci_list)

