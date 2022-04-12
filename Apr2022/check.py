import numpy as np

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

def f(x,y):
    ones = np.ones(nmax)
    x1 = x
    x2 = y
    ones, u1, u2 = gram_schmidt(ones, x1, x2)

    res = 0.0
    for i in range(nmax):
        for j in range(nmax):
            res += (np.abs(u1[i]-u1[j])-np.abs(u2[i]-u2[j]))**2
    return res

x = np.loadtxt("x.dat")
y = np.loadtxt("y.dat")

print("x.x = %e"%(np.dot(x,x)))
print("y.y = %e"%(np.dot(y,y)))
print("x.y = %e"%(np.dot(x,y)))
print("sum(x) = %e"%(np.sum(x)))
print("sum(y) = %e"%(np.sum(y)))
print("f(x,y) = %e"%(f(x,y)))
print("f(x,y)-4.0 = %e"%(f(x,y)-4.0))

print("x = [%s]"%(", ".join(["%12.10f"%n for n in x])))
print("y = [%s]"%(", ".join(["%12.10f"%n for n in y])))
