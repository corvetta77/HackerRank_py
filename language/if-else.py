#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    weird = "Weird"
    not_weird = "Not Weird"
    if n % 2 == 0:
        if n in range(2, 6):
            print(not_weird)
        else:
            if n in range(6, 21):
                print(weird)
            else:
                print(not_weird)
    else:
        print(weird)
