# Lesson 4.3 — MCMC: Metropolis–Hastings and Gibbs

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build Markov chains with stationary distribution $p \propto e^{-\beta E}$: Metropolis–Hastings and Gibbs.
- Verify detailed balance for both, and why Gibbs needs only the Markov blanket.
- Parallelize with block and chromatic Gibbs; see why updating every spin at once fails.

## Prerequisites
- Lesson 0.5: Markov chains and detailed balance.
- Lessons 4.1–4.2: graphical models and Ising.

## Narrated script

### [00:06.6] Introduction — `manim:S01`

**ES:** Ya sabemos que no podemos calcular la función de partición de un modelo grande. La salida es muestrear: construir una cadena de Markov cuya distribución estacionaria sea exactamente la de Boltzmann, y dejarla correr. Ese es el método de Monte Carlo por cadenas de Markov. En esta lección veremos sus dos recetas clásicas y cómo paralelizarlas, que es exactamente lo que hace un chip de pbits.

**EN:** We already know we cannot compute the partition function of a large model. The way out is to sample: build a Markov chain whose stationary distribution is exactly the Boltzmann distribution, and let it run. That is the Markov chain Monte Carlo method. In this lesson we will see its two classic recipes and how to parallelize them, which is exactly what a pbit chip does.

### [00:31.4] Metropolis–Hastings — `manim:S02`

**ES:** Metropolis propone un cambio, por ejemplo voltear un espín, y calcula el cambio de energía ΔE. Si la energía baja, acepta siempre. Si sube, acepta con probabilidad e^(−βΔE). Con esa regla, el flujo de probabilidad entre dos estados es igual en ambos sentidos: se cumple el balance detallado con la distribución de Boltzmann. Lo bueno es que solo necesitamos diferencias de energía, nunca la función de partición.

**EN:** Metropolis proposes a change, for example flipping a spin, and computes the energy change ΔE. If the energy goes down, it always accepts. If it goes up, it accepts with probability e^(−βΔE). With that rule, the probability flow between two states is equal in both directions: detailed balance holds with the Boltzmann distribution. The nice part is that we only need energy differences, never the partition function.

### [01:00.0] Gibbs sampling — `manim:S03`

**ES:** El muestreo de Gibbs toma una variable y la vuelve a sortear desde su distribución condicional, dadas todas las demás. Por la manta de Markov, esa condicional solo depende de los vecinos. Para un espín de Ising es P(s_i = +1) = σ(2βu_i), una sigmoide del campo local. No hay rechazos: cada paso produce una muestra nueva de esa variable. Y la sigmoide del campo local es exactamente lo que implementa un pbit.

**EN:** Gibbs sampling takes one variable and redraws it from its conditional distribution, given all the others. By the Markov blanket, that conditional depends only on the neighbors. For an Ising spin it is P(s_i = +1) = σ(2βu_i), a sigmoid of the local field. There are no rejections: each step produces a new sample of that variable. And the sigmoid of the local field is exactly what a pbit implements.

### [01:30.1] Chromatic Gibbs — `manim:S04`

**ES:** Actualizar los espines uno por uno es lento. ¿Podemos actualizar muchos a la vez? Sí, siempre que no sean vecinos: sus condicionales no dependen unas de otras. Coloreamos el grafo de modo que ningún par de vecinos comparta color, y actualizamos todos los nodos de un color en paralelo. En una red cuadrada bastan dos colores, como un tablero de ajedrez. Ese es el Gibbs cromático, y así funciona un chip de pbits.

**EN:** Updating spins one by one is slow. Can we update many at once? Yes, as long as they are not neighbors: their conditionals do not depend on each other. We color the graph so that no two neighbors share a color, and update all nodes of one color in parallel. On a square lattice two colors suffice, like a chessboard. That is chromatic Gibbs, and that is how a pbit chip works.

### [01:57.3] Why not all at once — `manim:S05`

**ES:** ¿Y si actualizamos todos los espines simultáneamente? Cada uno usaría el valor viejo de sus vecinos, que también están cambiando. La cadena resultante ya no tiene a Boltzmann como distribución estacionaria. A temperatura tres, el Gibbs cromático da una energía media por espín de menos cero coma ocho dos, y Metropolis, menos cero coma siete nueve. La actualización totalmente paralela da cero coma cero dos: completamente equivocada.

**EN:** And if we update all spins simultaneously? Each would use the old value of its neighbors, which are also changing. The resulting chain no longer has Boltzmann as its stationary distribution. At temperature three, chromatic Gibbs gives a mean energy per spin of −0.82, and Metropolis, −0.79. The fully parallel update gives 0.02: completely wrong.

### [02:25.1] Numerical example — `manim:S06`

**ES:** Un ejemplo de aceptación de Metropolis. En una red cuadrada a temperatura tres, voltear un espín rodeado de cuatro vecinos alineados aumenta la energía en ocho. La probabilidad de aceptar es e^(−8/3), unos siete por ciento. El mismo espín, con Gibbs, termina en contra de sus vecinos con probabilidad σ(−8/3), unos seis coma cinco por ciento. Las dos cadenas difieren en los pasos, pero coinciden en la distribución.

**EN:** An example of Metropolis acceptance. On a square lattice at temperature three, flipping a spin surrounded by four aligned neighbors raises the energy by eight. The acceptance probability is e^(−8/3), about seven percent. The same spin, with Gibbs, ends up against its neighbors with probability σ(−8/3), about 6.5 percent. The two chains differ in their steps, but agree on the distribution.

### [02:54.9] Applications — `slide`

**ES:** Los chips de pbits implementan Gibbs cromático en hardware, con un color por fase de reloj. THRML hace Gibbs por bloques sobre grafos de factores en GPU. Y como el grafo tiene grado acotado, bastan pocos colores, lo que permite un paralelismo masivo. En el laboratorio cinco lo programarás en JAX.

**EN:** Pbit chips implement chromatic Gibbs in hardware, one color per clock phase. THRML does block Gibbs over factor graphs on GPU. And since the graph has bounded degree, few colors suffice, which allows massive parallelism. In lab five you will program it in JAX.

### [03:16.1] Common mistakes — `slide`

**ES:** Errores frecuentes: actualizar vecinos a la vez. Usar una propuesta no simétrica sin la corrección de Hastings. Olvidar el factor dos en la sigmoide. Y confundir una distribución estacionaria correcta con una mezcla rápida, que es el tema de la próxima lección.

**EN:** Frequent mistakes: updating neighbors at the same time. Using a non-symmetric proposal without the Hastings correction. Forgetting the factor of two in the sigmoid. And confusing a correct stationary distribution with fast mixing, which is the topic of the next lesson.

### [03:33.7] Summary — `manim:S09`

**ES:** En resumen: Metropolis acepta cambios con probabilidad min(1, e^(−βΔE)), y Gibbs resortea cada variable desde su condicional. Ambos cumplen balance detallado con Boltzmann y solo usan información local. Colorear el grafo permite actualizar en paralelo sin romper la distribución.

**EN:** In summary: Metropolis accepts changes with probability min(1, e^(−βΔE)), and Gibbs redraws each variable from its conditional. Both satisfy detailed balance with Boltzmann and use only local information. Coloring the graph allows parallel updates without breaking the distribution.

### [03:54.6] Self-assessment — `slide`

**ES:** Para practicar: demuestra el balance detallado de Metropolis. Deriva la condicional de Gibbs para Ising. Cuenta los colores de una red triangular. Y explica por qué falla la actualización totalmente paralela.

**EN:** To practice: prove detailed balance for Metropolis. Derive the Gibbs conditional for Ising. Count the colors of a triangular lattice. And explain why the fully parallel update fails.

## Key equations
- $$A(s \to s') = \min\big(1,\ e^{-\beta[E(s') - E(s)]}\big)$$ — Metropolis acceptance (symmetric proposal).
- $$P(s_i = +1 \mid s_{-i}) = \sigma(2\beta u_i),\qquad u_i = \sum_j J_{ij}s_j + h_i$$ — Gibbs conditional for an Ising spin.
- $$\pi(s)\,P(s \to s') = \pi(s')\,P(s' \to s)$$ — Detailed balance: both samplers satisfy it with $\pi \propto e^{-\beta E}$.

## Summary
- MCMC: chains with stationary distribution $e^{-\beta E}/Z$; no $Z$ needed.
- Metropolis: accept with $\min(1, e^{-\beta\Delta E})$; Gibbs: redraw from the conditional.
- Chromatic Gibbs: one color class in parallel; 2 colors on a square lattice.
- Updating neighbors simultaneously breaks the stationary distribution.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- [3] Levin, Peres and Wilmer, Markov Chains and Mixing Times.
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, 2022.
