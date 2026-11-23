# Lesson 4.4 — Sampling diagnostics

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Diagnose an MCMC run: burn-in, integrated autocorrelation time and effective sample size.
- Recognize critical slowing down near $T_c$.
- Use simulated annealing for optimization and parallel tempering to cross barriers.

## Prerequisites
- Lesson 2.6: ergodicity and autocorrelation.
- Lessons 4.2–4.3: Ising model and Gibbs sampling.

## Narrated script

### [00:04.9] Introduction — `manim:S01`

**ES:** Un muestreador correcto puede ser inútil si es lento. La cadena tiene la distribución estacionaria correcta, pero ¿cuándo llegó a ella, y cuántas muestras realmente independientes nos dio? En esta lección aprendemos a diagnosticar una corrida y dos trucos clásicos para acelerarla: el recocido y el tempering paralelo.

**EN:** A correct sampler can be useless if it is slow. The chain has the right stationary distribution, but when did it get there, and how many truly independent samples did it give us? In this lesson we learn to diagnose a run and two classic tricks to speed it up: annealing and parallel tempering.

### [00:25.5] Burn-in — `manim:S02`

**ES:** Toda cadena empieza en un estado arbitrario. Las primeras muestras recuerdan ese inicio y no representan la distribución estacionaria. A esa fase se le llama calentamiento, y se descarta. Un diagnóstico práctico es lanzar varias cadenas desde inicios distintos: cuando sus promedios se superponen, el calentamiento terminó.

**EN:** Every chain starts in an arbitrary state. The first samples remember that start and do not represent the stationary distribution. That phase is called burn-in, and it is discarded. A practical diagnostic is to launch several chains from different starts: when their averages overlap, burn-in is over.

### [00:46.7] Autocorrelation and ESS — `manim:S03`

**ES:** Después del calentamiento, las muestras consecutivas siguen correlacionadas. Como en la lección dos punto seis, el tiempo de autocorrelación integrado dice cada cuántos barridos obtenemos una muestra nueva. El tamaño efectivo de muestra es el número de barridos dividido por ese tiempo. En una red de dieciséis por dieciséis a temperatura tres coma cinco, el tiempo es de unos ocho barridos, y treinta y ocho mil barridos valen como cuatro mil quinientas muestras independientes.

**EN:** After burn-in, consecutive samples are still correlated. As in lesson 2.6, the integrated autocorrelation time says every how many sweeps we get a new sample. The effective sample size is the number of sweeps divided by that time. On a sixteen-by-sixteen lattice at temperature 3.5, that time is about eight sweeps, and thirty-eight thousand sweeps are worth about forty-five hundred independent samples.

### [01:15.9] Critical slowing down — `manim:S04`

**ES:** Ahora acerquémonos a la temperatura crítica. A dos coma ocho, el tiempo de autocorrelación de la magnetización sube a unos treinta y tres barridos. En dos coma dos siete se dispara a más de dos mil, y los mismos treinta y ocho mil barridos valen apenas diecisiete muestras independientes. Es la desaceleración crítica: los dominios grandes tardan mucho en reorganizarse con actualizaciones locales. Cerca de una transición de fase, el muestreo local se vuelve muy caro.

**EN:** Now let's approach the critical temperature. At 2.8, the autocorrelation time of the magnetization rises to about thirty-three sweeps. At 2.27 it shoots up to more than two thousand, and the same thirty-eight thousand sweeps are worth barely seventeen independent samples. This is critical slowing down: large domains take a long time to reorganize with local updates. Near a phase transition, local sampling becomes very expensive.

### [01:45.5] Simulated annealing — `manim:S05`

**ES:** Si lo que buscamos es el mínimo de la energía, podemos aprovechar la temperatura. El recocido simulado empieza caliente, donde la cadena explora libremente, y enfría poco a poco hasta casi cero, donde la distribución se concentra en los mínimos. En un vidrio de espín de dieciséis por dieciséis, un enfriamiento de diez barridos termina en una energía de menos uno coma dos cinco por espín; con diez mil barridos llega a menos uno coma tres siete. Enfriar más despacio da mejores mínimos, con rendimientos decrecientes.

**EN:** If what we want is the minimum of the energy, we can exploit temperature. Simulated annealing starts hot, where the chain explores freely, and cools gradually to almost zero, where the distribution concentrates on the minima. On a sixteen-by-sixteen spin glass, a ten-sweep cooling ends at an energy of −1.25 per spin; with ten thousand sweeps it reaches −1.37. Cooling more slowly gives better minima, with diminishing returns.

### [02:19.2] Parallel tempering — `manim:S06`

**ES:** El tempering paralelo corre varias réplicas a temperaturas distintas al mismo tiempo. De vez en cuando propone intercambiar las configuraciones de dos réplicas vecinas, y acepta con probabilidad min(1, e^((β_i − β_j)(E_i − E_j))). Así, una configuración atrapada en la réplica fría puede subir a la caliente, cruzar la barrera y volver. Con β cero coma cinco y cero coma seis, y una diferencia de energía de veinte, el intercambio se acepta con probabilidad e^(−2), un trece por ciento.

**EN:** Parallel tempering runs several replicas at different temperatures at the same time. Every so often it proposes swapping the configurations of two neighboring replicas, and accepts with probability min(1, e^((β_i − β_j)(E_i − E_j))). That way, a configuration stuck in the cold replica can climb to the hot one, cross the barrier and come back. With β of 0.5 and 0.6, and an energy difference of twenty, the swap is accepted with probability e^(−2), about thirteen percent.

### [02:54.2] Applications — `slide`

**ES:** En la práctica, siempre reporta el tiempo de autocorrelación y el tamaño efectivo, no solo el número de barridos. La energía de un chip por muestra independiente es la energía por barrido multiplicada por ese tiempo. Y en optimización con hardware de pbits, el calendario de recocido debe ir despacio cerca de la temperatura crítica.

**EN:** In practice, always report the autocorrelation time and the effective sample size, not just the number of sweeps. A chip's energy per independent sample is the energy per sweep times that time. And in optimization with pbit hardware, the annealing schedule must slow down near the critical temperature.

### [03:15.1] Common mistakes — `slide`

**ES:** Errores frecuentes: medir la autocorrelación en un observable rápido mientras uno lento no ha mezclado. Corridas tan cortas que subestiman el propio tiempo de autocorrelación. Enfriar demasiado rápido. Y elegir temperaturas tan separadas que los intercambios nunca se aceptan.

**EN:** Frequent mistakes: measuring the autocorrelation on a fast observable while a slow one has not mixed. Runs so short that the autocorrelation time itself is underestimated. Cooling too fast. And choosing temperatures so far apart that swaps are never accepted.

### [03:33.3] Summary — `manim:S09`

**ES:** En resumen: descarta el calentamiento, mide el tiempo de autocorrelación y reporta el tamaño efectivo de muestra. Cerca de la temperatura crítica, el muestreo local se vuelve muy lento. El recocido simulado usa la temperatura para optimizar, y el tempering paralelo la usa para cruzar barreras.

**EN:** In summary: discard the burn-in, measure the autocorrelation time and report the effective sample size. Near the critical temperature, local sampling becomes very slow. Simulated annealing uses temperature to optimize, and parallel tempering uses it to cross barriers.

### [03:52.7] Self-assessment — `slide`

**ES:** Para practicar: calcula un tamaño efectivo de muestra. Explica la desaceleración crítica. Deriva la aceptación del intercambio. Y diseña una escalera de temperaturas.

**EN:** To practice: compute an effective sample size. Explain critical slowing down. Derive the swap acceptance. And design a temperature ladder.

## Key equations
- $$\tau_{\text{int}} = 1 + 2\sum_{k\ge1}\rho_k,\qquad \mathrm{ESS} = n/\tau_{\text{int}}$$ — Integrated autocorrelation time and effective sample size.
- $$A_{\text{swap}} = \min\big(1,\ e^{(\beta_i - \beta_j)(E_i - E_j)}\big)$$ — Parallel-tempering swap acceptance between replicas $i$ and $j$.
- $$T_k = T_{\min}\,(T_{\max}/T_{\min})^{k/(K-1)}$$ — Geometric temperature ladder with $K$ replicas.

## Summary
- Discard burn-in; check with several chains.
- $\tau_{\text{int}}$ and ESS: 16×16 Ising, $\tau_{\text{int}}(m)$ ≈ 8 (T = 3.5) → >2000 (T = 2.27).
- Simulated annealing: −1.25 (10 sweeps) → −1.37 (10⁴ sweeps) per spin on a ±J glass.
- Parallel tempering: replica swaps cross barriers.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- [3] Levin, Peres and Wilmer, Markov Chains and Mixing Times.
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, 2022.
