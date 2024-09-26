#!/usr/bin/env python3
# Author: Arnie Lloyd Sarmiento
# Author ID: asarmiento6@myseneca.ca
# Date Created: 2024/09/25

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
