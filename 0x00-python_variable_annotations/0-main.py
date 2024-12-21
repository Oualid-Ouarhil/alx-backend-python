#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.5, 2.5) == 1.5 + 2.5)
print(add.__annotations__)
