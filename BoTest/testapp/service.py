import math
import random

def quad(a:float, b:float, c:float):
    d = b**2 - 4*a*c
    res1 = None
    res2 = None
    if d>0:
        res1 = (-b + math.sqrt(d))/(2*a)
        res2 = (-b - math.sqrt(d))/(2*a)
    elif d==0:
        res1 = -b/(2*a)
    result = list()
    result.append(res1)
    result.append(res2)
    return result


def check_float(string):
    a= '1234567890.-'
    for i in string:
        if i not in a:
            return False
    return True


def getColor():
    p = random.random()
    if p<=0.5:
        return 'blue'
    elif 0.5<p<0.8:
        return 'green'
    elif 0.8<=p<1:
        return 'red'
