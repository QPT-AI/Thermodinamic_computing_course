# Lesson 3.1 — Heat, work and entropy at the trajectory level

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define work and heat for a single Langevin trajectory (Sekimoto's stochastic energetics).
- Verify the first law per trajectory: $\Delta V = W + Q$.
- Interpret the work distribution and the stochastic entropy $s = -k_B\ln p(x,t)$.

## Prerequisites
- Lesson 1.1: first and second laws.
- Lessons 2.2–2.3: Langevin and Fokker–Planck.

## Narrated script

### [00:06.3] Introduction — `manim:S01`

**ES:** La termodinámica clásica habla de promedios: calor y trabajo de un gas con diez a la veintitrés moléculas. Pero un pbit, una molécula o un nodo de un chip termodinámico son sistemas pequeños, donde cada realización es distinta. La termodinámica estocástica, desarrollada por Sekimoto y Seifert, define calor, trabajo y entropía para una sola trayectoria. Es el lenguaje para medir la energía de un cómputo ruidoso.

**EN:** Classical thermodynamics talks about averages: heat and work of a gas with ten to the twenty-three molecules. But a pbit, a molecule or a node of a thermodynamic chip are small systems, where every realization is different. Stochastic thermodynamics, developed by Sekimoto and Seifert, defines heat, work and entropy for a single trajectory. It is the language for measuring the energy of a noisy computation.

### [00:34.2] Intuition — `manim:S02`

**ES:** Imagina una partícula en una trampa que movemos con una mano. Cuando la mano mueve la trampa, cambia la energía potencial de la partícula: eso es trabajo, energía que nosotros inyectamos. Cuando la partícula se mueve por sí sola dentro de la trampa, empujada por el baño, su energía cambia porque intercambia energía con el fluido: eso es calor. La contabilidad es la de siempre, pero hecha paso a paso sobre una única trayectoria ruidosa.

**EN:** Imagine a particle in a trap that we move with our hand. When the hand moves the trap, the particle's potential energy changes: that is work, energy we inject. When the particle moves on its own within the trap, pushed by the bath, its energy changes because it exchanges energy with the fluid: that is heat. The bookkeeping is the usual one, but done step by step along a single noisy trajectory.

### [01:02.8] Definitions — `manim:S03`

**ES:** Formalmente, con una energía V(x, λ) controlada por un parámetro λ(t), el trabajo es el cambio de energía por mover el parámetro con la partícula quieta: dW = ∂_λ V dλ. El calor recibido es el cambio de energía por el movimiento de la partícula con el parámetro fijo: dQ = ∂_x V ∘ dx, con la regla del punto medio de Stratonovich. Sumando, dV = dW + dQ: la primera ley se cumple en cada trayectoria, no solo en promedio.

**EN:** Formally, with an energy V(x, λ) controlled by a parameter λ(t), work is the change in energy from moving the parameter with the particle held still: dW = ∂_λ V dλ. The heat received is the change in energy from the particle's motion with the parameter fixed: dQ = ∂_x V ∘ dx, with Stratonovich's midpoint rule. Adding up, dV = dW + dQ: the first law holds on every trajectory, not just on average.

### [01:39.4] Visual explanation — `manim:S04`

**ES:** Arrastremos una trampa armónica a velocidad constante. Arriba ves la trampa en movimiento y la partícula que la sigue con retraso. Abajo, tres contadores a lo largo de la misma trayectoria: el trabajo acumulado, el calor acumulado y el cambio de energía potencial. El trabajo crece en promedio porque la partícula se queda atrás y la mano debe tirar de ella. El calor es mayormente negativo: la partícula entrega energía al fluido. Y en todo instante el cambio de energía es exactamente la suma de ambos.

**EN:** Let's drag a harmonic trap at constant speed. At the top you see the moving trap and the particle following it with a lag. Below, three counters along the same trajectory: accumulated work, accumulated heat and the change in potential energy. Work grows on average because the particle lags behind and the hand must pull it. Heat is mostly negative: the particle hands energy to the fluid. And at every instant the change in energy is exactly the sum of both.

### [02:11.9] Work distribution — `manim:S05`

**ES:** Repitamos el experimento veinte mil veces. El trabajo varía de una realización a otra y forma una distribución gaussiana. Su media es positiva, como exige la segunda ley, porque la energía libre no cambia al trasladar la trampa. Pero fíjate en la cola izquierda: en alrededor del quince por ciento de las realizaciones el trabajo es negativo. El baño, por azar, empujó la partícula a nuestro favor. Eso no viola la segunda ley: la segunda ley es una afirmación sobre promedios, y en sistemas pequeños las violaciones individuales son frecuentes.

**EN:** Let's repeat the experiment twenty thousand times. Work varies from one realization to another and forms a Gaussian distribution. Its mean is positive, as the second law demands, because the free energy does not change when the trap is translated. But look at the left tail: in about fifteen percent of realizations the work is negative. The bath, by chance, pushed the particle in our favor. That does not violate the second law: the second law is a statement about averages, and in small systems individual violations are common.

### [02:46.7] Stochastic entropy — `manim:S06`

**ES:** También la entropía se define por trayectoria. La entropía del sistema es s = −k_B ln p(x, t), evaluada en el punto donde está la partícula; su promedio es la entropía de Gibbs. La entropía del medio cambia como menos el calor recibido dividido por T. La entropía total producida en una trayectoria es la suma de ambas. Su promedio nunca es negativo, pero trayectorias individuales pueden reducirla. La próxima lección cuantifica exactamente cuán frecuentes son esas reducciones.

**EN:** Entropy is also defined per trajectory. The system entropy is s = −k_B ln p(x, t), evaluated where the particle is; its average is the Gibbs entropy. The entropy of the medium changes as minus the heat received divided by T. The total entropy produced along a trajectory is the sum of both. Its average is never negative, but individual trajectories can reduce it. The next lesson quantifies exactly how frequent those reductions are.

### [03:20.5] Numerical example — `manim:S07`

**ES:** Con rigidez uno, fricción uno, k_B T igual a uno, velocidad uno y duración tres, la teoría da un trabajo medio de tres menos uno menos e^(−3), unos dos coma cero cinco, y una varianza del doble de la media, cuatro coma uno. La simulación da dos coma cero cuatro y cuatro coma cero nueve. La probabilidad de trabajo negativo predicha es quince coma seis por ciento, y la medida es quince coma cinco.

**EN:** With stiffness one, friction one, k_B T equal to one, speed one and duration three, theory gives a mean work of three minus one minus e^(−3), about 2.05, and a variance twice the mean, 4.1. The simulation gives 2.04 and 4.09. The predicted probability of negative work is 15.6 percent, and the measured one 15.5.

### [03:50.3] Applications — `slide`

**ES:** Esto importa para el cómputo. Un borrado individual puede costar menos que la cota de Landauer; solo el promedio está acotado. La energía de una operación en un pbit es una variable aleatoria con media y varianza. Y en el laboratorio cuatro arrastrarás una trampa para estimar diferencias de energía libre a partir del trabajo.

**EN:** This matters for computing. An individual erasure can cost less than the Landauer bound; only the average is bounded. The energy of an operation on a pbit is a random variable with mean and variance. And in lab four you will drag a trap to estimate free-energy differences from work.

### [04:11.2] Connections — `slide`

**ES:** La primera ley de la lección uno punto uno se vuelve una identidad por trayectoria. La entropía estocástica usa la densidad de Fokker y Planck. Y las próximas lecciones convertirán la distribución del trabajo en leyes exactas.

**EN:** The first law of lesson 1.1 becomes a per-trajectory identity. Stochastic entropy uses the Fokker–Planck density. And the next lessons will turn the work distribution into exact laws.

### [04:26.2] Common mistakes — `slide`

**ES:** Errores comunes: confundir las convenciones de signo. Usar la regla de Itô para el calor, cuando se necesita la del punto medio. Creer que un trabajo negativo viola la segunda ley. Y confundir trabajo con cambio de energía.

**EN:** Common mistakes: mixing up the sign conventions. Using the Itô rule for heat, when the midpoint rule is needed. Believing a negative work violates the second law. And confusing work with the change in energy.

### [04:41.2] Summary — `manim:S11`

**ES:** En resumen: el trabajo es el cambio de energía por mover el control, y el calor, el cambio por el movimiento de la partícula. La primera ley vale trayectoria por trayectoria. El trabajo fluctúa: su media respeta la segunda ley, pero las realizaciones individuales pueden ser negativas.

**EN:** In summary: work is the change in energy from moving the control, and heat, the change from the particle's motion. The first law holds trajectory by trajectory. Work fluctuates: its mean respects the second law, but individual realizations can be negative.

### [04:59.9] Self-assessment — `slide`

**ES:** Para practicar: escribe el trabajo y el calor en una trampa armónica móvil. Explica por qué el calor usa Stratonovich. Predice qué ocurre al duplicar la velocidad. Y calcula el promedio de la entropía estocástica.

**EN:** To practice: write the work and heat in a moving harmonic trap. Explain why heat uses Stratonovich. Predict what happens when the speed doubles. And compute the average of the stochastic entropy.

## Key equations
- $$dW = \frac{\partial V}{\partial\lambda}\,d\lambda,\qquad dQ = \frac{\partial V}{\partial x}\circ dx,\qquad dV = dW + dQ$$ — Sekimoto's stochastic energetics: first law per trajectory.
- $$\langle W\rangle = \gamma v^2\big[t - \tau(1 - e^{-t/\tau})\big],\quad \mathrm{Var}(W) = 2k_BT\langle W\rangle$$ — Dragged harmonic trap ($\tau = \gamma/\kappa$): Gaussian work.
- $$s(t) = -k_B\ln p(x_t, t),\qquad \Delta s_{\text{med}} = -Q/T$$ — Stochastic entropy of the system and of the medium.

## Summary
- Work: change in $V$ due to the control; heat: due to the motion ($\circ$ Stratonovich).
- First law per trajectory: $\Delta V = W + Q$.
- $W$ fluctuates: $\langle W\rangle \ge \Delta F$, but there are trajectories with $W < \Delta F$.
- Stochastic entropy $-k_B\ln p$; total production $\ge 0$ on average.

## Further reading
- [11] U. Seifert, Stochastic thermodynamics, fluctuation theorems and molecular machines, 2012.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics, chs. 4–5.
- Video V8: From Stochastic Thermodynamics to Thermodynamic Inference — U. Seifert.
