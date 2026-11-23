# Lesson 6.5 — Timing models

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build an end-to-end timing model: digital-to-analog loading, analog dynamics, analog-to-digital readout.
- Explain why the $O(d^2)$ compilation step often dominates when the analog core is fast.
- Amortize loading over many right-hand sides.

## Prerequisites
- Lessons 6.1 and 6.4: protocol times and complexity.
- Lesson 5.8: energy accounting (same three-part logic).

## Narrated script

### [00:04.4] Introduction — `manim:S01`

**ES:** La complejidad de la lección anterior contaba solo la evolución analógica. Pero la matriz vive en un computador digital, y la solución debe volver a él. Un modelo de tiempo honesto suma tres partes: cargar el problema, dejar evolucionar al sistema y leer el resultado. Hoy veremos que la primera parte, la compilación, suele ser la más cara.

**EN:** The complexity in the previous lesson counted only the analog evolution. But the matrix lives in a digital computer, and the solution must return to it. An honest timing model adds three parts: loading the problem, letting the system evolve and reading the result. Today we will see that the first part, compilation, is often the most expensive.

### [00:26.9] Three stages — `manim:S02`

**ES:** Primero, la compilación: cada uno de los d² elementos de A pasa por un convertidor digital analógico, un DAC, para fijar un acoplamiento. Segundo, la dinámica analógica: equilibrar y promediar, un tiempo proporcional a d por el tiempo de relajación. Tercero, la lectura: los d valores de la solución pasan por un convertidor analógico digital, un ADC. La compilación crece como d²; los métodos digitales no la necesitan, porque la matriz ya está en su memoria.

**EN:** First, compilation: each of the d² entries of A goes through a digital-to-analog converter, a DAC, to set a coupling. Second, the analog dynamics: equilibrate and average, a time proportional to d times the relaxation time. Third, readout: the d values of the solution go through an analog-to-digital converter, an ADC. Compilation grows as d²; digital methods do not need it, because the matrix is already in their memory.

### [00:59.7] RC time constants — `manim:S03`

**ES:** ¿Qué fija el tiempo de relajación en un circuito? La constante RC, resistencia por capacitancia. Con un microsegundo, el núcleo analógico es lento comparado con la carga. Con diez nanosegundos, típico de un circuito integrado pequeño, la dinámica es cien veces más rápida. Paradójicamente, cuanto más rápido es el núcleo analógico, más pesa la parte digital.

**EN:** What sets the relaxation time in a circuit? The RC constant, resistance times capacitance. With one microsecond, the analog core is slow compared with loading. With ten nanoseconds, typical of a small integrated circuit, the dynamics is a hundred times faster. Paradoxically, the faster the analog core, the more the digital part weighs.

### [01:24.3] A worked model — `manim:S04`

**ES:** Hagamos números con supuestos explícitos: mil millones de valores por segundo en los convertidores, y una dinámica de veinte tiempos de relajación por dimensión, escala que sale de la simulación de la lección seis punto uno. Con dimensión mil y RC de un microsegundo, cargar toma un milisegundo y la dinámica veinte: la carga es el cinco por ciento. Con diez nanosegundos, la dinámica baja a dos décimas de milisegundo y la carga pasa a ser el ochenta y tres por ciento. El cruce ocurre en una dimensión de veinte mil en el primer caso, y de solo doscientos en el segundo.

**EN:** Let's run numbers with explicit assumptions: a billion values per second in the converters, and dynamics of twenty relaxation times per dimension, a scale taken from the simulation in lesson 6.1. With dimension one thousand and an RC of one microsecond, loading takes one millisecond and the dynamics twenty: loading is five percent. With ten nanoseconds, the dynamics drops to two tenths of a millisecond and loading becomes eighty-three percent. The crossover occurs at a dimension of twenty thousand in the first case, and of only two hundred in the second.

### [02:00.2] Amortization — `manim:S05`

**ES:** La solución clásica es amortizar. Si la matriz no cambia y hay que resolver muchos sistemas con distintos lados derechos, se carga una sola vez y luego cada solución cuesta solo la dinámica y la lectura. Con cien lados derechos, en el caso rápido, el tiempo por solución baja de uno coma dos milisegundos a cero coma dos uno, y la carga pasa a ser menos del cinco por ciento. Al revés, en un método de Newton donde la matriz cambia en cada paso, la compilación se paga siempre.

**EN:** The classic solution is to amortize. If the matrix does not change and many systems with different right-hand sides must be solved, it is loaded once and then each solution costs only the dynamics and the readout. With a hundred right-hand sides, in the fast case, the time per solution drops from 1.2 milliseconds to 0.21, and loading becomes less than five percent. Conversely, in a Newton method where the matrix changes at every step, compilation is always paid.

### [02:30.9] What the paper found — `manim:S06`

**ES:** Aifer y colaboradores construyeron un modelo de tiempo completo, con todas las operaciones digitales, de conversión y analógicas, y lo compararon con gradiente conjugado y Cholesky en una GPU. En dimensión cien, el método termodinámico pierde. En dimensiones de mil y cinco mil se vuelve competitivo, sobre todo al principio, cuando basta una solución aproximada. Y advierten que su modelo aún no incluye la imprecisión analógica.

**EN:** Aifer and colleagues built a complete timing model, with all digital, conversion and analog operations, and compared it with conjugate gradient and Cholesky on a GPU. In dimension one hundred, the thermodynamic method loses. In dimensions of a thousand and five thousand it becomes competitive, especially early on, when an approximate solution is enough. And they warn that their model does not yet include analog imprecision.

### [02:59.2] Applications — `slide`

**ES:** Para diseñar alrededor de la compilación: reutilizar la matriz con muchos lados derechos, actualizar solo partes de baja dimensión en vez de recargar todo, usar bancos paralelos de convertidores y memoria de acoplamientos en el chip. En el laboratorio nueve añadirás un modelo de tiempo y encontrarás el cruce.

**EN:** To design around compilation: reuse the matrix with many right-hand sides, update only low-dimensional parts instead of reloading everything, use parallel banks of converters and on-chip coupling memory. In lab nine you will add a timing model and find the crossover.

### [03:18.9] Common mistakes — `slide`

**ES:** Errores comunes: reportar solo el tiempo analógico. Suponer que un núcleo más rápido siempre ayuda de extremo a extremo. Olvidar que la línea base digital no paga transferencia. Y recargar toda la matriz cuando solo cambió el lado derecho.

**EN:** Common mistakes: reporting only the analog time. Assuming a faster core always helps end to end. Forgetting that the digital baseline pays no transfer. And reloading the whole matrix when only the right-hand side changed.

### [03:34.9] Summary — `manim:S09`

**ES:** En resumen: el tiempo total es carga más dinámica más lectura. La carga crece como d² y domina cuando el núcleo analógico es rápido; en nuestro modelo, el cruce está en d* = 20 τ_r B. Amortizar sobre muchos lados derechos lo resuelve.

**EN:** In summary: total time is loading plus dynamics plus readout. Loading grows as d² and dominates when the analog core is fast; in our model, the crossover is at d* = 20 τ_r B. Amortizing over many right-hand sides solves it.

### [03:53.2] Self-assessment — `slide`

**ES:** Para practicar: escribe el tiempo total en función de la dimensión. Encuentra el cruce. Calcula el tiempo por solución con varios lados derechos. Y explica por qué un núcleo más rápido hace dominar la compilación.

**EN:** To practice: write the total time as a function of the dimension. Find the crossover. Compute the time per solution with several right-hand sides. And explain why a faster core makes compilation dominate.

## Key equations
- $$T(d) = \underbrace{\frac{d^2}{B_{\text{DAC}}}}_{\text{compile}} + \underbrace{c\,d\,\tau_r}_{\text{analog}} + \underbrace{\frac{d}{B_{\text{ADC}}}}_{\text{readout}},\qquad \tau_r = RC$$ — End-to-end timing model for $Ax = b$ (here $c = 20$, $B = 10^9$ values/s) [E].
- $$d^\ast = c\,\tau_r\,B_{\text{DAC}}:\quad 2\times10^4\ (\tau_r = 1\ \mu\text{s}),\ \ 200\ (\tau_r = 10\ \text{ns})$$ — Dimension above which compilation dominates.
- $$\frac{T_K}{K} = \frac{d^2}{K B_{\text{DAC}}} + c\,d\,\tau_r + \frac{d}{B_{\text{ADC}}}$$ — Amortized time per solve with $K$ right-hand sides.

## Summary
- T = compile (d²) + analog (∝ d τ_r) + readout (d).
- d = 1000: loading 5 % (RC = 1 µs) vs 83 % (RC = 10 ns) [E].
- Faster analog core ⇒ compilation dominates; crossover d* = c τ_r B.
- Amortize over K right-hand sides: 1.2 → 0.21 ms per solve (K = 100).

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
- [29] M. Aifer et al., Solving the compute crisis with physics-based ASICs, 2025.
