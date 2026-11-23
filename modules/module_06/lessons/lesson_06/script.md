# Lesson 6.6 — Landscape: inference and beyond

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Sample an exact Gaussian posterior with an OU device (thermodynamic Bayesian inference).
- Solve box-constrained quadratic programs with projected, low-temperature Langevin dynamics.
- Estimate matrix exponentials from equilibrium autocorrelations, and state the idea of thermodynamic parallelism.

## Prerequisites
- Lessons 6.1–6.3: moments of the OU equilibrium.
- Lesson 1.6: Bayesian inference.

## Narrated script

### [00:05.6] Introduction — `manim:S01`

**ES:** Cerramos la unidad con un panorama. El mismo dispositivo de osciladores acoplados sirve para mucho más que sistemas lineales. Veremos tres ejemplos: muestrear distribuciones posteriores bayesianas, resolver programas cuadráticos con restricciones y calcular exponenciales de matrices. Y terminaremos con una idea que intenta explicar de dónde viene la ventaja termodinámica.

**EN:** We close the unit with a landscape. The same device of coupled oscillators is useful for much more than linear systems. We will see three examples: sampling Bayesian posterior distributions, solving constrained quadratic programs and computing matrix exponentials. And we will finish with an idea that tries to explain where the thermodynamic advantage comes from.

### [00:29.5] Bayesian inference — `manim:S02`

**ES:** Con un prior gaussiano y observaciones lineales con ruido gaussiano, la posterior también es gaussiana, con precisión Λ = I + Hᵀ H / σ². Si cargamos Λ como matriz de acoplamientos, el equilibrio del dispositivo es exactamente la posterior: no hay que resolver nada, cada instante del sistema es una muestra. Aifer y colaboradores proponen circuitos para este modelo y para regresión logística bayesiana, y argumentan que el tiempo de muestreo escala solo como el logaritmo de la dimensión.

**EN:** With a Gaussian prior and linear observations with Gaussian noise, the posterior is also Gaussian, with precision Λ = I + Hᵀ H / σ². If we load Λ as the coupling matrix, the equilibrium of the device is exactly the posterior: nothing needs to be solved, every instant of the system is a sample. Aifer and colleagues propose circuits for this model and for Bayesian logistic regression, and argue that the sampling time scales only as the logarithm of the dimension.

### [01:03.6] Posterior simulation — `manim:S03`

**ES:** Lo simulamos en dos dimensiones con tres observaciones. Las muestras del dispositivo reproducen la posterior exacta: las varianzas son cero coma dos siete y cero coma seis cuatro, y las estimadas, cero coma dos ocho y cero coma seis siete. La incertidumbre no se calcula aparte: sale gratis de las fluctuaciones.

**EN:** We simulate it in two dimensions with three observations. The device samples reproduce the exact posterior: the variances are 0.27 and 0.64, and the estimated ones, 0.28 and 0.67. The uncertainty is not computed separately: it comes for free from the fluctuations.

### [01:24.4] Quadratic programming — `manim:S04`

**ES:** Si además hay restricciones de caja, del tipo cada variable entre cero y uno, basta con poner paredes: cuando el sistema choca con una, se queda en el borde. A baja temperatura, el promedio converge al óptimo del programa cuadrático. En nuestro ejemplo, el óptimo es cero coma seis y uno; con k_B T = 0,001 obtenemos cero coma seis cero y cero coma nueve nueve. A temperatura más alta la pared sesga el promedio hacia adentro.

**EN:** If there are also box constraints, such as every variable between zero and one, it is enough to add walls: when the system hits one, it stays at the edge. At low temperature, the average converges to the optimum of the quadratic program. In our example, the optimum is 0.6 and 1; with k_B T = 0.001 we get 0.60 and 0.99. At higher temperature the wall biases the average inward.

### [01:53.6] Matrix exponentials — `manim:S05`

**ES:** El tercer ejemplo usa la dinámica, no solo el equilibrio. En un proceso de Ornstein-Uhlenbeck, la autocorrelación con retardo s es e^(−A s) Σ. Midiendo correlaciones entre el estado actual y el de hace s unidades, y multiplicando por β A, obtenemos la exponencial de la matriz. Con dimensión cinco y una trayectoria de veinte mil unidades, el error relativo es del cinco por ciento. Duffield y colaboradores muestran que esto da una ventaja lineal en la dimensión para simular sistemas dinámicos lineales.

**EN:** The third example uses the dynamics, not only the equilibrium. In an Ornstein-Uhlenbeck process, the autocorrelation at lag s is e^(−A s) Σ. By measuring correlations between the current state and the one s units earlier, and multiplying by β A, we obtain the matrix exponential. With dimension five and a trajectory of twenty thousand units, the relative error is five percent. Duffield and colleagues show that this gives a speedup linear in the dimension for simulating linear dynamical systems.

### [02:27.9] Thermodynamic parallelism — `manim:S06`

**ES:** ¿Por qué aparece siempre una ganancia proporcional a la dimensión? Duffield y colaboradores proponen una hipótesis: el paralelismo termodinámico. El ruido empuja al sistema en todas las direcciones a la vez, así que una sola trayectoria explora todos los modos simultáneamente y estima muchas cantidades en paralelo. El ruido, que en un computador digital es un enemigo, aquí es el recurso que paraleliza. Es una hipótesis, no un teorema, y está entre los problemas abiertos de la unidad once.

**EN:** Why does a gain proportional to the dimension always appear? Duffield and colleagues propose a hypothesis: thermodynamic parallelism. Noise pushes the system in all directions at once, so a single trajectory explores all modes simultaneously and estimates many quantities in parallel. Noise, which in a digital computer is an enemy, is here the resource that parallelizes. It is a hypothesis, not a theorem, and it is among the open problems of unit eleven.

### [02:59.6] Applications — `slide`

**ES:** Estas primitivas tocan la inteligencia artificial en el aprendizaje profundo bayesiano, en la optimización con restricciones, en los modelos de espacio de estados, y en la unidad ocho, donde el gradiente natural usará el mismo núcleo de álgebra lineal.

**EN:** These primitives touch artificial intelligence in Bayesian deep learning, in constrained optimization, in state-space models, and in unit eight, where the natural gradient will use the same linear-algebra core.

### [03:15.8] Common mistakes — `slide`

**ES:** Errores comunes: muestrear la posterior a una temperatura distinta de uno. Resolver un programa cuadrático a temperatura alta. Estimar la exponencial con retardos muy largos, donde la señal se pierde en el ruido. Y tratar el paralelismo termodinámico como un teorema.

**EN:** Common mistakes: sampling the posterior at a temperature other than one. Solving a quadratic program at high temperature. Estimating the exponential with very long lags, where the signal is lost in noise. And treating thermodynamic parallelism as a theorem.

### [03:33.9] Summary — `manim:S09`

**ES:** En resumen: el equilibrio de un dispositivo de osciladores es una posterior bayesiana exacta en el caso gaussiano; con paredes y baja temperatura resuelve programas cuadráticos; y su autocorrelación da exponenciales de matrices. El paralelismo termodinámico es la hipótesis que une estas ventajas.

**EN:** In summary: the equilibrium of an oscillator device is an exact Bayesian posterior in the Gaussian case; with walls and low temperature it solves quadratic programs; and its autocorrelation gives matrix exponentials. Thermodynamic parallelism is the hypothesis that unifies these advantages.

### [03:53.1] Self-assessment — `slide`

**ES:** Para practicar: deduce la posterior gaussiana. Explica por qué la temperatura debe ser uno. Demuestra la fórmula de la autocorrelación. Y explica qué sesga la solución del programa cuadrático a temperatura finita.

**EN:** To practice: derive the Gaussian posterior. Explain why the temperature must be one. Prove the autocorrelation formula. And explain what biases the solution of the quadratic program at finite temperature.

## Key equations
- $$p(x\mid y) = \mathcal N\big(\Lambda^{-1}H^\top y/\sigma^2,\ \Lambda^{-1}\big),\quad \Lambda = I + H^\top H/\sigma^2$$ — Gaussian posterior = OU equilibrium with $A = \Lambda$, $b = H^\top y/\sigma^2$, $\beta = 1$.
- $$\langle x(t+s)\,x(t)^\top\rangle = e^{-As}\,\Sigma = \beta^{-1}e^{-As}A^{-1}\ \Rightarrow\ e^{-As} = \beta\,C(s)\,A$$ — Matrix exponential from the autocorrelation (symmetric $A$).
- $$\min_{0\le x\le 1}\ \tfrac12 x^\top A x - b^\top x:\quad x \leftarrow \Pi_{[0,1]}\big(x - (Ax - b)\,dt + \sqrt{2k_BT\,dt}\,\xi\big)$$ — Box-constrained QP by projected Langevin at low temperature.

## Summary
- Gaussian posterior = OU equilibrium; uncertainty from fluctuations.
- Projected Langevin, low T: box-constrained QP (0.602, 0.994 vs 0.6, 1) [S].
- Autocorrelation ⇒ e^(−As) (5 % error, d = 5) [S].
- Thermodynamic parallelism: noise as a resource (a hypothesis).

## Further reading
- M. Aifer et al., Thermodynamic Bayesian inference, arXiv:2410.01793 (2024).
- S. Duffield et al., Thermodynamic matrix exponentials and thermodynamic parallelism, arXiv:2311.12759 (2023).
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
