#!/usr/bin/env python3

import customset

cs=customset.StringSet()
cs.add('hola')

try:
    cs.add(12)
    print("This should not be printed")
except ValueError:
    pass
cs.add("")
print(cs)

print(cs.pop())
print(cs)
