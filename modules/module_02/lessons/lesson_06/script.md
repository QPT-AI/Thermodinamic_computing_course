# Lesson 2.6 — Ergodicity

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Distinguish time averages from ensemble averages and recognize when they coincide (ergodicity).
- Compute the autocorrelation and the integrated autocorrelation time $\tau_{\text{int}}$.
- Put correct error bars on averages of correlated samples: $\sigma_{\bar x} \approx \sqrt{\mathrm{Var}(x)\,\tau_{\text{int}}/n}$.

## Prerequisites
- Lesson 0.5: Markov chains and spectral gap.
- Lesson 2.4: Ornstein–Uhlenbeck process.

## Narrated script

### [00:04.1] Introduction — `manim:S01`

**ES:** Un computador termodinámico casi nunca devuelve una muestra aislada: devuelve un promedio de muchas lecturas consecutivas de un mismo sistema. ¿Ese promedio en el tiempo da lo mismo que el promedio sobre muchas copias independientes? ¿Y cuánto confiamos en él? La respuesta tiene dos partes: la ergodicidad y el tiempo de autocorrelación. Sin ellas, nuestras barras de error mienten.

**EN:** A thermodynamic computer almost never returns an isolated sample: it returns an average of many consecutive readings of the same system. Does that time average give the same as the average over many independent copies? And how much do we trust it? The answer has two parts: ergodicity and the autocorrelation time. Without them, our error bars lie.

### [00:28.3] Intuition — `manim:S02`

**ES:** Mira dos partículas en un pozo doble. La de la izquierda tiene una barrera baja: salta de un pozo a otro muchas veces, y su fracción de tiempo en cada pozo converge a un medio, como el ensamble. La de la derecha tiene una barrera enorme: en todo el tiempo que la observamos nunca cruza. Su promedio temporal dice que el sistema está siempre en el pozo derecho, lo cual es falso para el ensamble. En la práctica, un sistema es ergódico si lo observamos durante más tiempo que su tiempo de mezcla.

**EN:** Look at two particles in a double well. The left one has a low barrier: it hops between wells many times, and its fraction of time in each well converges to one half, like the ensemble. The right one has a huge barrier: in all the time we watch it, it never crosses. Its time average says the system is always in the right well, which is false for the ensemble. In practice, a system is ergodic if we observe it for longer than its mixing time.

### [00:59.4] Autocorrelation — `manim:S03`

**ES:** Aunque el sistema sea ergódico, muestras consecutivas no son independientes. La autocorrelación mide cuánto se parece el valor actual al valor de un rato después: ρ(τ) = C(τ)/C(0). Para el proceso de Ornstein y Uhlenbeck decae como una exponencial. La curva medida en la simulación sigue la exponencial teórica, con ruido en la cola. El área bajo la curva, multiplicada por dos, es el tiempo de autocorrelación integrado: cuánto tiempo hay que esperar para obtener una muestra efectivamente nueva.

**EN:** Even if the system is ergodic, consecutive samples are not independent. The autocorrelation measures how much the current value resembles the value a while later: ρ(τ) = C(τ)/C(0). For the Ornstein–Uhlenbeck process it decays as an exponential. The curve measured in the simulation follows the theoretical exponential, with noise in the tail. The area under the curve, times two, is the integrated autocorrelation time: how long you must wait to get an effectively new sample.

### [01:33.6] Effective sample size — `manim:S04`

**ES:** Si tomamos n muestras espaciadas por un paso Δt, y el tiempo de autocorrelación integrado, en pasos, es τ_int, solo tenemos unas n/τ_int muestras independientes: el tamaño efectivo de muestra. Muestrear más rápido que la autocorrelación no aporta información nueva, solo copias. La varianza del promedio es la varianza de una muestra multiplicada por τ_int/n, y no por uno sobre n.

**EN:** If we take n samples spaced by a step Δt, and the integrated autocorrelation time, in steps, is τ_int, we only have about n/τ_int independent samples: the effective sample size. Sampling faster than the autocorrelation adds no new information, only copies. The variance of the average is the variance of one sample times τ_int/n, not times one over n.

### [02:02.2] Error bars — `manim:S05`

**ES:** Comprobémoslo repitiendo el experimento doscientas veces. Cada punto es el promedio de una corrida, con su barra de error. Si ignoramos la correlación, las barras naranjas son demasiado cortas: muchas no contienen el valor verdadero. Con la corrección por el tiempo de autocorrelación, las barras verdes contienen el valor verdadero en la proporción esperada, alrededor del noventa y cinco por ciento para dos sigmas. Una herramienta práctica para estimarlas es el método de bloques: promediar por bloques más largos que la autocorrelación y usar la dispersión de los bloques.

**EN:** Let's check by repeating the experiment two hundred times. Each point is the average of one run, with its error bar. If we ignore the correlation, the orange bars are too short: many do not contain the true value. With the autocorrelation-time correction, the green bars contain the true value in the expected proportion, about ninety-five percent for two sigmas. A practical tool to estimate them is the blocking method: average over blocks longer than the autocorrelation and use the spread of the blocks.

### [02:36.7] Numerical example — `manim:S06`

**ES:** Un proceso de Ornstein y Uhlenbeck con tasa cero coma uno, leído cada cero coma uno unidades de tiempo, tiene autocorrelación e^(−0,01 k) entre lecturas separadas k pasos. Su tiempo integrado es uno más ese número entre uno menos ese número: unos doscientos pasos. Con diez mil lecturas, el tamaño efectivo de muestra es solo de unas cincuenta. La barra de error real es unas catorce veces mayor que la ingenua.

**EN:** An Ornstein–Uhlenbeck process with rate 0.1, read every 0.1 time units, has autocorrelation e^(−0.01 k) between readings k steps apart. Its integrated time is one plus that number over one minus that number: about two hundred steps. With ten thousand readings, the effective sample size is only about fifty. The real error bar is about fourteen times larger than the naive one.

### [03:05.5] Applications — `slide`

**ES:** En hardware esto tiene consecuencias directas. El tiempo que debe integrar el solucionador lineal crece con el tiempo de correlación, que es el inverso del valor propio más pequeño. Leer un chip de pbits más rápido que su tiempo de correlación desperdicia energía de entrada y salida. Cerca de una transición de fase, el tiempo de correlación de Gibbs se dispara. Y en todos los laboratorios, las barras de error deben incluir la autocorrelación.

**EN:** In hardware this has direct consequences. The time the linear solver must integrate grows with the correlation time, which is the inverse of the smallest eigenvalue. Reading a pbit chip faster than its correlation time wastes input and output energy. Near a phase transition, the Gibbs correlation time blows up. And in every lab, error bars must include the autocorrelation.

### [03:33.2] Connections — `slide`

**ES:** El tiempo de autocorrelación está acotado por la brecha espectral de la lección cero punto cinco. La autocorrelación es también la respuesta, por el teorema de fluctuación y disipación. Y en la unidad cuatro la usaremos como diagnóstico de los muestreadores.

**EN:** The autocorrelation time is bounded by the spectral gap from lesson 0.5. The autocorrelation is also the response, by the fluctuation–dissipation theorem. And in unit four we will use it as a diagnostic for samplers.

### [03:49.5] Common mistakes — `slide`

**ES:** Errores frecuentes: usar la fórmula de muestras independientes con datos correlacionados. No descartar el transitorio. Confundir la ergodicidad teórica con la práctica. Y estimar el tiempo integrado sumando toda la cola ruidosa sin truncarla.

**EN:** Frequent mistakes: using the independent-sample formula with correlated data. Not discarding the transient. Confusing theoretical ergodicity with practical ergodicity. And estimating the integrated time by summing the whole noisy tail without truncating it.

### [04:05.4] Summary — `manim:S10`

**ES:** En resumen: un sistema es ergódico en la práctica si lo observamos más tiempo que su tiempo de mezcla. Las muestras consecutivas están correlacionadas, y el tiempo de autocorrelación integrado dice cuántas son realmente independientes. La barra de error correcta es la raíz de la varianza por τ_int sobre n.

**EN:** In summary: a system is ergodic in practice if we observe it for longer than its mixing time. Consecutive samples are correlated, and the integrated autocorrelation time says how many are truly independent. The correct error bar is the square root of the variance times τ_int over n.

### [04:25.3] Self-assessment — `slide`

**ES:** Para practicar: calcula el tiempo integrado de una autocorrelación geométrica. Obtén un tamaño efectivo de muestra. Explica por qué un pozo con barrera de cuarenta k_B T no es ergódico en la práctica. Y describe el método de bloques.

**EN:** To practice: compute the integrated time of a geometric autocorrelation. Get an effective sample size. Explain why a well with a forty k_B T barrier is not ergodic in practice. And describe the blocking method.

## Key equations
- $$\bar x_T = \frac1T\int_0^T x(t)\,dt \to \mathbb E_\pi[x]$$ — Ergodicity: time average = ensemble average.
- $$\tau_{\text{int}} = 1 + 2\sum_{k\ge1}\rho_k,\qquad n_{\text{eff}} = \frac{n}{\tau_{\text{int}}}$$ — Integrated autocorrelation time and effective sample size.
- $$\sigma_{\bar x} \approx \sqrt{\frac{\mathrm{Var}(x)\,\tau_{\text{int}}}{n}}$$ — Error bar of an average of correlated samples.

## Summary
- Practical ergodicity: observe for longer than the mixing time.
- Autocorrelation $\rho(\tau)$; OU: $e^{-a\tau}$.
- $n_{\text{eff}} = n/\tau_{\text{int}}$; reading faster does not help.
- Error bars: $\sqrt{\mathrm{Var}\,\tau_{\text{int}}/n}$ or the blocking method.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods (autocorrelation and errors).
- [3] Levin, Peres and Wilmer, Markov Chains and Mixing Times.
- [30] Aifer et al., Thermodynamic linear algebra (integration time).
