import sys
import math

def checksnt (number):
    snumber = int(math.sqrt(number))
    for i in range (1, snumber):
        if (number % i == 0):
            return False

    return True

number = int(input('Please input number:'))
if checksnt(number):
    print "%s la so nguyen to." % number
else:
    print "%s khong la so nguyen to." % number
