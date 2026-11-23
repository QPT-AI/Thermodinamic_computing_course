"""L3 — El solucionador lineal Ornstein–Uhlenbeck. Código de inicio (JAX).

dx = -(A x - b) dt + sqrt(2/beta) dW   ⇒   x_inf ~ N(A^{-1} b, beta^{-1} A^{-1})
Ejecutar: python L3_inicio.py
"""
import time

import jax
import jax.numpy as jnp
import numpy as np


def wishart(key, d, factor=2):
    """A = G G^T / (factor d) + 0.1 I con G de d x (factor d): SPD, κ moderado."""
    G = jax.random.normal(key, (d, factor * d))
    return G @ G.T / (factor * d) + 0.1 * jnp.eye(d)


def ou_solver(key, A, b, beta=1.0, dt=None, T=200.0, burn=20.0):
    lmax = float(jnp.linalg.eigvalsh(A)[-1])
    dt = dt or 0.1 / lmax           # muy por debajo del límite 2/λmax (sesgo ≈ λΔt/2)
    n, nb = int(T / dt), int(burn / dt)
    s = jnp.sqrt(2 * dt / beta)

    def paso(carry, k):
        x, suma, suma2 = carry
        x = x - (A @ x - b) * dt + s * jax.random.normal(k, b.shape)
        return (x, suma + x, suma2 + jnp.outer(x, x)), None

    claves = jax.random.split(key, n)
    (x, _, _), _ = jax.lax.scan(paso, (jnp.zeros_like(b), jnp.zeros_like(b), jnp.zeros((b.size, b.size))), claves[:nb])
    (x, suma, suma2), _ = jax.lax.scan(paso, (x, jnp.zeros_like(b), jnp.zeros((b.size, b.size))), claves[nb:])
    m = n - nb
    media = suma / m
    cov = suma2 / m - jnp.outer(media, media)
    return media, beta * cov, dt


if __name__ == "__main__":
    key = jax.random.PRNGKey(0)
    for d in (10, 50):
        kA, kb, ks = jax.random.split(jax.random.fold_in(key, d), 3)
        A = wishart(kA, d)
        b = jax.random.normal(kb, (d,))
        x_ref = jnp.linalg.solve(A, b)
        t0 = time.perf_counter()
        x_ou, Ainv_ou, dt = ou_solver(ks, A, b)
        x_ou.block_until_ready()
        ev = jnp.linalg.eigvalsh(A)
        err = float(jnp.linalg.norm(x_ou - x_ref) / jnp.linalg.norm(x_ref))
        err_inv = float(jnp.linalg.norm(Ainv_ou - jnp.linalg.inv(A)) / jnp.linalg.norm(jnp.linalg.inv(A)))
        print(f"d={d:3d} κ={float(ev[-1]/ev[0]):6.1f} dt={dt:.4f}  err(A^-1 b)={err:.3f}  err(A^-1)={err_inv:.3f}  "
              f"t={time.perf_counter()-t0:.1f}s [S]")
    # TODO 1: error frente a T (integración) y frente a d; comparar escalado lineal vs cuadrático.
    # TODO 2: verificar Δt < 2/λmax; mostrar inestabilidad con Δt = 2.1/λmax.
    # TODO 3: comparar tiempo de pared con CG (jax.scipy.sparse.linalg.cg) y Cholesky.
    # RETO: dinámica subamortiguada; convergencia frente a κ.
