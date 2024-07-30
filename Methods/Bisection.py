import math as mt

def fun(x):
    #mt.pow(x, 3) - (3 * x) + 1
    #-2 + (x * (mt.log(x)))
    return mt.pow(mt.e, x) - x - 2

def iteration(x, y, error):
    return ((mt.log(y - x) - mt.log(error)) / 2) + 1

def bisection(x, y):
    error = mt.pow(10, -2)
    it = round(iteration(x, y, error))

    for i in range(it):
        m = (x + y) / 2

        fx = fun(x)
        fy = fun(y)
        fm = fun(m)

        fxx = '+' if fx > 0 else '-' if fx < 0 else '0'
        fyy = '+' if fy > 0 else '-' if fy < 0 else '0'
        fmm = '+' if fm > 0 else '-' if fm < 0 else '0'

        print(f"| {i} | {x} | {y} | {m} | {fxx} | {fyy} | {fmm}")

        if fx * fm < 0:  
            y = m
        else:  
            x = m



    


