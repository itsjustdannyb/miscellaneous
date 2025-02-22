# leetcode question -  square root
import time

def sqrt_(number):
    if (number <= 0):
        return 0
    for i in range(number):
        # check if product of loop index is greater than number
        if (i * i > number):
            return i - 1

if __name__ == "__main__":
    start = time.time()
    number = int(input("number: "))
    # number = 25000000000
    print(sqrt_(number))
    stop = time.time()
    print("time taken:", stop-start)