#!/usr/bin/env python3

concat = __import__('1-concat').concat

str1 = 'hello'
str2 = 'ahmed'
print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
