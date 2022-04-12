import numpy as np
from scipy.optimize import fmin_slsqp

nmax = 20

def proj(u, v):
    return (np.dot(u,v)/np.dot(u,u))*u

def gram_schmidt(v1, v2, v3):
    u1 = v1
    u2 = v2 - proj(u1,v2)
    u3 = v3 - proj(u1,v3) - proj(u2,v3)
    u1 = u1/np.linalg.norm(u1)
    u2 = u2/np.linalg.norm(u2)
    u3 = u3/np.linalg.norm(u3)
    return u1, u2, u3

def f(x):
    ones = np.ones(nmax)
    x1 = x[0:nmax]
    x2 = x[nmax:]
    ones, u1, u2 = gram_schmidt(ones, x1, x2)

    res = 0.0
    for i in range(nmax):
        for j in range(nmax):
            res += (np.abs(u1[i]-u1[j])-np.abs(u2[i]-u2[j]))**2
    print(res-4.0)
    return res

def c1(x):
    return -1.0*np.abs(x[0:nmax].mean())

def c2(x):
    return -1.0*np.abs(x[nmax:].mean())

np.random.seed(42)
x0 = np.random.randn(nmax*2).astype('float64')
xopt, fopt, func_calls, imode, smode = fmin_slsqp(f, x0, ieqcons=[c1,c2], acc=1.0e-9, iter=100000, full_output=True)
#print(xopt, fopt)
ones = np.ones(nmax)
x1 = xopt[0:nmax]
x2 = xopt[nmax:]
ones, u1, u2 = gram_schmidt(ones, x1, x2)
print("x = np.array([%s])"%(", ".join(["%12.10f"%n for n in u1])))
print("y = np.array([%s])"%(", ".join(["%12.10f"%n for n in u2])))
