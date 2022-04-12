import numpy as onp
import jax.numpy as jnp
import jax

jax.config.update("jax_enable_x64", True)

nmax = 20

@jax.jit
def proj(u, v):
    return (jnp.dot(u,v)/jnp.dot(u,u))*u

@jax.jit
def gram_schmidt(v1, v2, v3):
    u1 = v1
    u2 = v2 - proj(u1,v2)
    u3 = v3 - proj(u1,v3) - proj(u2,v3)
    u1 = u1/jnp.linalg.norm(u1)
    u2 = u2/jnp.linalg.norm(u2)
    u3 = u3/jnp.linalg.norm(u3)
    return u1, u2, u3

@jax.jit
def f(x):
    ones = jnp.ones(nmax)
    x1 = x[:,0].ravel()
    x2 = x[:,1].ravel()
    ones, u1, u2 = gram_schmidt(ones, x1, x2)

    res = 0.0
    for i in range(nmax):
        for j in range(nmax):
            res += (jnp.abs(u1[i]-u1[j])-jnp.abs(u2[i]-u2[j]))**2
    return res

x = jax.random.uniform(jax.random.PRNGKey(42), shape=(nmax,2), dtype='float64', minval=-1.0, maxval=1.0)
print(x)
for n in range(1000000):
    x = x - 1.0e-3*jax.jacfwd(f)(x)
    print(f(x)-4.0)
    if f(x)-4.0 < 1.0e-8:
        break
print(x.T)
