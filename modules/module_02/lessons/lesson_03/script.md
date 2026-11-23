# Lesson 2.3 — The Fokker–Planck equation

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Go from Langevin trajectories to the evolution of the density: $\partial_t p = -\partial_x J$, $J = \mu f p - D\partial_x p$.
- Interpret the probability current and find stationary solutions.
- Distinguish equilibrium ($J = 0$, Boltzmann) from non-equilibrium steady states ($J \neq 0$).

## Prerequisites
- Lesson 2.2: overdamped Langevin and the Einstein relation.
- Partial derivatives; continuity equation.

## Narrated script

### [00:05.0] Introduction — `manim:S01`

**ES:** Una sola trayectoria de Langevin es impredecible. Pero si soltamos miles de partículas, su densidad evoluciona de forma perfectamente determinista. La ecuación que gobierna esa densidad es la de Fokker y Planck. Es el puente entre la física de una partícula ruidosa y la estadística de su distribución, y es la herramienta para demostrar que un chip termodinámico termina muestreando la distribución correcta.

**EN:** A single Langevin trajectory is unpredictable. But if we release thousands of particles, their density evolves in a perfectly deterministic way. The equation governing that density is the Fokker–Planck equation. It is the bridge between the physics of one noisy particle and the statistics of its distribution, and it is the tool to prove that a thermodynamic chip ends up sampling the right distribution.

### [00:30.6] Intuition — `manim:S02`

**ES:** Piensa en una gota de tinta en agua. Cada molécula de tinta hace su propio movimiento browniano, pero la mancha, como un todo, se ensancha de manera suave y predecible. Si además hay una corriente en el agua, la mancha se desplaza mientras se ensancha. Fokker y Planck es exactamente eso: un término de arrastre, que mueve la densidad siguiendo la fuerza, y un término de difusión, que la ensancha.

**EN:** Think of a drop of ink in water. Each ink molecule does its own Brownian motion, but the blot as a whole spreads smoothly and predictably. If there is also a current in the water, the blot drifts while it spreads. Fokker–Planck is exactly that: a drift term, which moves the density along the force, and a diffusion term, which spreads it.

### [00:56.1] The equation — `manim:S03`

**ES:** Para la ecuación de Langevin sobreamortiguada, la densidad p(x, t) obedece ∂p/∂t = −∂J/∂x, donde la corriente de probabilidad es J = μ f p − D ∂p/∂x. El primer término es el arrastre: la probabilidad viaja con velocidad μ f. El segundo es la difusión: la probabilidad fluye de donde hay más hacia donde hay menos. Es una ecuación de continuidad: la probabilidad no se crea ni se destruye, solo se mueve.

**EN:** For the overdamped Langevin equation, the density p(x, t) obeys ∂p/∂t = −∂J/∂x, where the probability current is J = μ f p − D ∂p/∂x. The first term is drift: probability travels with velocity μ f. The second is diffusion: probability flows from where there is more to where there is less. It is a continuity equation: probability is neither created nor destroyed, it only moves.

### [01:30.0] Visual explanation — `manim:S04`

**ES:** Comparemos. Las barras verdes son el histograma de cuatro mil partículas de Langevin que empiezan todas en el mismo punto, en el pozo de la derecha. La curva amarilla es la solución numérica de la ecuación de Fokker y Planck, sin ningún ruido. Coinciden en todo momento. Primero la densidad se ensancha dentro del pozo; luego, lentamente, la probabilidad cruza la barrera y llena el otro pozo hasta alcanzar la distribución de Boltzmann.

**EN:** Let's compare. The green bars are the histogram of four thousand Langevin particles that all start at the same point, in the right well. The amber curve is the numerical solution of the Fokker–Planck equation, with no noise at all. They match at every moment. First the density spreads within the well; then, slowly, probability crosses the barrier and fills the other well until it reaches the Boltzmann distribution.

### [01:58.4] Stationary solution — `manim:S05`

**ES:** En el estado estacionario, la densidad no cambia, así que la corriente es constante. En una dimensión, con la densidad yendo a cero en los extremos, la corriente debe ser cero. Entonces el arrastre equilibra exactamente la difusión: μ f p = D ∂p/∂x. Con f = −V' y la relación de Einstein, la solución es p ∝ e^(−V/k_B T). Aquí está la demostración prometida: la dinámica de Langevin con el ruido correcto tiene como estado estacionario la distribución de Boltzmann.

**EN:** In the stationary state, the density does not change, so the current is constant. In one dimension, with the density going to zero at the ends, the current must be zero. Then drift exactly balances diffusion: μ f p = D ∂p/∂x. With f = −V' and the Einstein relation, the solution is p ∝ e^(−V/k_B T). Here is the promised proof: Langevin dynamics with the right noise has the Boltzmann distribution as its stationary state.

### [02:33.1] Out of equilibrium — `manim:S06`

**ES:** Pero no todo estado estacionario es equilibrio. Pon una partícula en un anillo con un potencial ondulado y empújala con una fuerza constante que la hace girar. La densidad deja de cambiar, pero la corriente no es cero: hay un flujo neto de probabilidad dando vueltas. Es un estado estacionario fuera del equilibrio. La distribución ya no es la de Boltzmann, y el sistema disipa calor continuamente. Estos estados son los protagonistas de la unidad tres.

**EN:** But not every stationary state is equilibrium. Put a particle on a ring with a wavy potential and push it with a constant force that makes it go around. The density stops changing, but the current is not zero: there is a net flow of probability circulating. It is a non-equilibrium steady state. The distribution is no longer Boltzmann, and the system dissipates heat continuously. These states are the protagonists of unit three.

### [03:01.5] Numerical example — `manim:S07`

**ES:** Para un potencial cuadrático la ecuación se resuelve exactamente. Si la partícula empieza en x₀, la densidad es gaussiana en todo instante, con media x₀ e^(−t/τ) y varianza (k_B T/κ)(1 − e^(−2t/τ)), con τ = 1/(μκ). La media relaja con tiempo τ y la varianza con la mitad. Con x₀ = 2, κ = 1 y k_B T = 0,25, en t = τ la media vale cero coma setenta y cuatro y la varianza cero coma dos dos.

**EN:** For a quadratic potential the equation is solved exactly. If the particle starts at x₀, the density is Gaussian at every instant, with mean x₀ e^(−t/τ) and variance (k_B T/κ)(1 − e^(−2t/τ)), with τ = 1/(μκ). The mean relaxes with time τ and the variance with half of it. With x₀ = 2, κ = 1 and k_B T = 0.25, at t = τ the mean is 0.74 and the variance 0.22.

### [03:37.6] Applications — `slide`

**ES:** Fokker y Planck nos da la garantía de que un dispositivo de Langevin muestrea la distribución correcta, y su espectro nos dice cuánto tarda. Los modelos de difusión de la unidad nueve son, en el fondo, ecuaciones de Fokker y Planck recorridas hacia adelante y hacia atrás. Y en la unidad tres la corriente de probabilidad nos dará la producción de entropía.

**EN:** Fokker–Planck gives us the guarantee that a Langevin device samples the right distribution, and its spectrum tells us how long it takes. The diffusion models of unit nine are, at bottom, Fokker–Planck equations run forward and backward. And in unit three the probability current will give us entropy production.

### [04:00.1] Connections — `slide`

**ES:** Fokker y Planck es la versión continua de la evolución de distribuciones en una cadena de Markov. Su caso exactamente soluble es el proceso de Ornstein y Uhlenbeck. Su análogo para saltos discretos es la ecuación maestra. Y la producción de entropía se escribe con la corriente.

**EN:** Fokker–Planck is the continuous version of the evolution of distributions in a Markov chain. Its exactly solvable case is the Ornstein–Uhlenbeck process. Its analog for discrete jumps is the master equation. And entropy production is written with the current.

### [04:18.0] Common mistakes — `slide`

**ES:** Errores comunes: confundir estacionario con equilibrio. Olvidar las condiciones de frontera. Ignorar que con ruido dependiente del estado la ecuación depende de la interpretación. Y pensar que una sola trayectoria sigue la ecuación, cuando la ecuación es para la densidad.

**EN:** Common mistakes: confusing stationary with equilibrium. Forgetting the boundary conditions. Ignoring that with state-dependent noise the equation depends on the interpretation. And thinking a single trajectory follows the equation, when the equation is for the density.

### [04:35.6] Summary — `manim:S11`

**ES:** En resumen: la densidad de un proceso de Langevin obedece ∂p/∂t = −∂J/∂x, con una corriente que combina arrastre y difusión. En el equilibrio la corriente es cero y la solución es la de Boltzmann. Si la corriente no se anula, tenemos un estado estacionario fuera del equilibrio que disipa.

**EN:** In summary: the density of a Langevin process obeys ∂p/∂t = −∂J/∂x, with a current combining drift and diffusion. At equilibrium the current is zero and the solution is Boltzmann. If the current does not vanish, we have a non-equilibrium steady state that dissipates.

### [04:56.5] Self-assessment — `slide`

**ES:** Para practicar: escribe la ecuación para un potencial cuadrático, demuestra que Boltzmann anula la corriente, calcula la solución gaussiana en otro instante, y explica por qué una fuerza constante en un anillo no puede llevar al equilibrio.

**EN:** To practice: write the equation for a quadratic potential, prove that Boltzmann makes the current vanish, compute the Gaussian solution at another instant, and explain why a constant force on a ring cannot lead to equilibrium.

## Key equations
- $$\partial_t p = -\partial_x J,\qquad J = \mu f(x)\,p - D\,\partial_x p$$ — Fokker–Planck as a continuity equation with drift and diffusion.
- $$J = 0,\ f = -V',\ D = \mu k_BT\ \Rightarrow\ p_{\text{eq}} \propto e^{-V/k_BT}$$ — Equilibrium state: zero current and the Boltzmann distribution.
- $$p(x,t) = \mathcal N\!\Big(x_0e^{-t/\tau},\ \tfrac{k_BT}{\kappa}\big(1-e^{-2t/\tau}\big)\Big)$$ — Exact solution for the quadratic potential, $\tau = 1/(\mu\kappa)$.

## Summary
- Density: $\partial_t p = -\partial_x J$, $J$ = drift − diffusion.
- Equilibrium: $J = 0$ ⇒ Boltzmann (with the Einstein relation).
- NESS: $\partial_t p = 0$ with $J \neq 0$; it dissipates heat.
- OU: exact Gaussian solution; the mean relaxes in $\tau$, the variance in $\tau/2$.

## Further reading
- [1] Gardiner, Handbook of Stochastic Methods; H. Risken, The Fokker–Planck Equation.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics, ch. 3.
- [45] Song et al., Score-based generative modeling through SDEs, 2021.
