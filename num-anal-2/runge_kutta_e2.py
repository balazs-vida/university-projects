import numpy as np
from printSoln import *

# number of iterations
ITER = 500

# error bound
EPS = 1.0e-2

def adaptive_runge_kutta_2_3(f, x, y, x_stop, h, EPS):
    """
    Adaptive third-order Runge--Kutta method, with embedded second-order method 
    Task: to solve the following first-order initial value problem numerically:
        y' = f(x, y(x)), where y = (y[0], y[1], ..., y[n-1])
    
    args:
        f -- given function, which returns the f(x, y) = (y[0], y[1], ..., y[n-1]) array
        x -- beginning of interval
        y -- initial values
        x_stop -- end of interval
        h -- initial step size (trial value of the x-increment)
        EPS -- error bound
    
    returns:
        X -- values of x (array)
        Y -- returned y-values (array)
        
    """
    def runge_kutta_3(f, x, y, h):
        """
        Third-order, four-stage Runge--Kutta method with FSAL (First Same As Last)
        property (ie. three function evaluation per step needed)
        
        args:
            f, x, y, h -- as above
            
        returns:
            dy -- increment of y in the next step
            e -- local error
        
        """
        # Bogacki--Shampine parameters
        a = np.array([0, 1/2, 3/4, 1])
        b1 = np.array([1/2])
        b2 = np.array([0, 3/4])
        b3 = np.array([2/9, 1/3, 4/9])
        
        # coeff's of the third-order formula
        c = np.array([2/9, 1/3, 4/9, 0])
        
        # coeff's of the second-order (embedded) formula
        d = np.array([7/24, 1/4, 1/3, 1/8])
        
        n = len(y)
        k = np.zeros((4,n), dtype=np.float64)
        
        # numerical approx.
        k[0] = h * f(x, y)
        k[1] = h * f(x + a[1] * h, y + b1[0] * k[0])
        k[2] = h * f(x + a[2] * h, y + b2[0] * k[0] + b2[1] * k[1])
        k[3] = h * f(x + a[3] * h, y + b3[0] * k[0] + b3[1] * k[1] + b3[2] * k[2])
    

        E = np.zeros(n)
        dy = np.zeros(n)
        
        # calculating the local error
        # by taking the difference between 3rd and 2nd order approximation
        for i in range(4):
            dy += (c[i] * k[i])
            E += (c[i] - d[i]) * k[i]
        e = np.sqrt(np.sum(E**2) / n) 
        
        return dy, e
    
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    stopper = 0

    for i in range(ITER):
        dy, e = runge_kutta_3(f, x, y, h)
        
        # if local error is within error bound
        if e <= EPS:
            x += h
            y = y + dy
            X.append(x)
            Y.append(y)
            # having reached the end of interval, we stop
            if stopper == 1:
                break
        
        # adaptive adjustment of next step size (h_next)
        if e != 0.0:
            h_next = 0.9 * h * (EPS / e) ** (1/3)
        else:
            h_next = h
            
#        # alternative strategy for adjusting h_next:
#        h_next = 0.9 * h * (EPS / e) ** (1/3)
#        if abs(h_next) <= 0.1 * abs(h):
#            h_next = 0.1 * h
#        
        # if next step is last
        if (0 < h) == (x_stop <= (x + h_next)):
            h_next = x_stop - x
            stopper = 1
            
        h = h_next

    return np.array(X), np.array(Y)


######################
#    
# References:
#    L. Gergó: Numerikus módszerek [Numerical methods], ELTE, 2010.
#    J. Kiusalaas: Numerical methods in engineering with Python 3, CUP, 2013.
#    P. Bogacki, L. F. Shampine: A 3(2) Pair of Runge--Kutta Formulas. Appl. Math. Leit. Vol. 2, No. 4, pp. 321--325, 1989.
#    
###################### 
