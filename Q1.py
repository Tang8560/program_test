# -*- coding: utf-8 -*-

import random
import numpy as np


class Compute(object):
    
    def Compute_data(self):     
        data20 = []  
        for i in range(20):
            data = self.Generate_random()
            data20.append(data)
        mean_data = np.mean(data20)
        max_data = max(data20)
        min_data = min(data20)
        
        return mean_data, max_data, min_data
            
    def Generate_random(self):
        result = random.randint(1,100)
        return result
    
C = Compute()
mean_data, max_data, min_data = C.Compute_data()
    

    


        
        
