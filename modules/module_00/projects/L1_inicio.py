"""L1 — Calentamiento con JAX: aleatoriedad y cadenas de Markov. Código de inicio.

Ejecutar:  python L1_inicio.py
Completa las secciones marcadas con TODO. Las pruebas al final deben pasar.
"""
import time

import jax
import jax.numpy as jnp
import numpy as np


# ----------------------------------------------------------------- Tarea 1: Bernoulli y entropía
def entropia_bernoulli(p):
    p = jnp.clip(p, 1e-12, 1 - 1e-12)
    return -(p * jnp.log2(p) + (1 - p) * jnp.log2(1 - p))


@jax.jit
def muestras_bernoulli(key, p, n=10**6):
    return jax.random.bernoulli(key, p, (n,))


def tarea1():
    key = jax.random.PRNGKey(0)
    for p in (0.1, 0.5, 0.9):
        key, sub = jax.random.split(key)
        x = muestras_bernoulli(sub, p).block_until_ready()
        t0 = time.perf_counter()
        x = muestras_bernoulli(sub, p).block_until_ready()
        dt = time.perf_counter() - t0
        p_hat = float(jnp.mean(x))
        print(f"p={p}: p_hat={p_hat:.4f}  H_emp={float(entropia_bernoulli(p_hat)):.4f}  "
              f"H_teo={float(entropia_bernoulli(p)):.4f}  tiempo={dt*1e3:.2f} ms [M]")


# ----------------------------------------------------------------- Tarea 2: cadenas de Markov
def cadena_reversible(K, key):
    """Pesos simétricos aleatorios -> P reversible y su pi exacta."""
    W = jax.random.uniform(key, (K, K))
    W = (W + W.T) / 2
    P = W / W.sum(axis=1, keepdims=True)
    pi = W.sum(axis=1) / W.sum()
    return np.array(P), np.array(pi)


def estacionaria_potencias(P, n=10_000):
    p = np.ones(len(P)) / len(P)
    for _ in range(n):
        p = p @ P
    return p


def estacionaria_espectral(P):
    # TODO: vector propio izquierdo con valor propio 1 (np.linalg.eig sobre P.T), normalizado a suma 1
    raise NotImplementedError


def tarea2_3():
    P3 = np.array([[2 / 3, 1 / 3, 0.0], [1 / 4, 1 / 2, 1 / 4], [0.0, 1 / 3, 2 / 3]])
    P50, pi50 = cadena_reversible(50, jax.random.PRNGKey(1))
    for nombre, P in (("3 estados", P3), ("50 estados", P50)):
        pi_pot = estacionaria_potencias(P)
        # TODO: comparar con estacionaria_espectral(P); verificar balance detallado pi_i P_ij = pi_j P_ji
        # TODO: brecha espectral y gráfica log ||p_n - pi||_1 frente a lambda_*^n (matplotlib)
        print(nombre, "pi (potencias) =", np.round(pi_pot[:5], 4), "...")


# ----------------------------------------------------------------- pruebas
def pruebas():
    assert abs(float(entropia_bernoulli(0.5)) - 1.0) < 1e-9
    P3 = np.array([[2 / 3, 1 / 3, 0.0], [1 / 4, 1 / 2, 1 / 4], [0.0, 1 / 3, 2 / 3]])
    assert np.allclose(estacionaria_potencias(P3), [0.3, 0.4, 0.3], atol=1e-10)
    print("pruebas básicas: OK")


if __name__ == "__main__":
    pruebas()
    tarea1()
    tarea2_3()
