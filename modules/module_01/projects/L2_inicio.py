"""L2 — El límite de Landauer: borrar un bit en un pozo doble. Código de inicio (JAX).

Modelo: partícula sobreamortiguada, k_B T = 1, movilidad 1:
    dx = -dV/dx(x, t) dt + sqrt(2) dW,     V(x, t) = Eb (x^4 - 2 s(t) x^2) + c(t) x
Protocolo (fracción u del tiempo total tau): bajar barrera s:1->0 | inclinar c:0->cmax | subir s:0->1 | quitar c.
Trabajo de Sekimoto: W = sum_t [V(x_t, t+dt) - V(x_t, t)].
Ejecutar:  python L2_inicio.py
"""
import jax
import jax.numpy as jnp
import numpy as np

EB, CMAX = 8.0, 8.0
FASES = jnp.array([0.0, 0.3, 0.6, 0.9, 1.0])


def horario(u):
    s = jnp.interp(u, FASES, jnp.array([1.0, 0.0, 0.0, 1.0, 1.0]))
    c = jnp.interp(u, FASES, jnp.array([0.0, 0.0, CMAX, CMAX, 0.0]))
    return s, c


def V(x, s, c):
    return EB * (x ** 4 - 2 * s * x ** 2) + c * x


def dV(x, s, c):
    return EB * (4 * x ** 3 - 4 * s * x) + c


def equilibrio_inicial(key, n):
    """Muestras de exp(-V(x,1,0)) por muestreo de una rejilla fina (exacto hasta la discretización)."""
    xs = jnp.linspace(-2, 2, 8001)
    p = jnp.exp(-V(xs, 1.0, 0.0))
    return jax.random.choice(key, xs, (n,), p=p / p.sum())


def borrar(key, tau, n=4000, dt=1e-3):
    pasos = int(tau / dt)
    k0, k1 = jax.random.split(key)
    x0 = equilibrio_inicial(k0, n)
    ruido = jax.random.normal(k1, (pasos, n))

    def paso(estado, entrada):
        x, W = estado
        k, xi = entrada
        s, c = horario(k / pasos)
        s2, c2 = horario((k + 1) / pasos)
        W = W + V(x, s2, c2) - V(x, s, c)                  # trabajo (Sekimoto)
        x = x - dV(x, s2, c2) * dt + jnp.sqrt(2 * dt) * xi  # Euler-Maruyama
        return (x, W), None

    (x, W), _ = jax.lax.scan(paso, (x0, jnp.zeros(n)), (jnp.arange(pasos), ruido))
    return x, W


if __name__ == "__main__":
    key = jax.random.PRNGKey(0)
    print(f"cota de Landauer: ln 2 = {np.log(2):.4f} k_B T")
    for i, tau in enumerate([1.0, 5.0, 20.0]):
        x, W = borrar(jax.random.fold_in(key, i), tau)
        print(f"tau={tau:5.1f}  <W>={float(W.mean()):.3f} ± {float(W.std()/np.sqrt(W.size)):.3f} k_BT   "
              f"P(x<0)={float((x < 0).mean()):.4f}   [S]")
    # TODO 1: histograma de W para cada tau (matplotlib).
    # TODO 2: <W>(tau) para tau en {1,2,5,10,20,50,100}; ajuste ln2 + a/tau con los puntos lentos.
    # TODO 3: explicar la disipación en exceso y el efecto de la tasa de fallo para tau grande.
    # RETO: máquina de Szilard (medir el lado, inclinar según la medición, extraer trabajo, borrar el registro).
