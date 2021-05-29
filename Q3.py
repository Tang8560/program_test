# -*- coding: utf-8 -*-

import time

LUX_MIN = 10
LUX_MAX = 100


class Main():
    def __init__(self):
        
        value = []       
        while True:
            test = self.detect()
            if test >= LUX_MIN and test <= LUX_MAX:
                value.append(test)
                if len(value) >= 3:
                    break
            else: value = [] 
                
    def detect(self):
        value = GetLuc()
        time.sleep(1)
        return value
