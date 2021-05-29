# -*- coding: utf-8 -*-
import itertools 

i = 0
j = 0

for i in itertools.count():
    i += 1
    if i%3 == 0:
        j += 1
    if j> 99:
        break

