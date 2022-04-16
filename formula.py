
def quadratic_equation (a, b,c):

    from math import sqrt

    d = b**2 - 4*a*c

    if d == 0:
        return -b / (2*a)

    elif d > 0:
        return (-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a)

    else:
        return None
    
    






