import numpy as np
def func(x):
    if(x<0.5):
        temp=float(x*np.arctan(x))
        return temp
    else:
        temp=float(np.sin(1/x))
        return temp
