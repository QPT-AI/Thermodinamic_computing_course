# Lesson 0.5 — Markov chains

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe a Markov chain by its transition matrix and evolve distributions: $p_{n+1} = p_n P$.
- Compute the stationary distribution $\pi P = \pi$ and check detailed balance.
- Relate the spectral gap to the mixing time: $\|p_n - \pi\|_1 \lesssim C\,|\lambda_2|^n$.

## Prerequisites
- Lesson 0.3: categorical variables.
- Lesson 0.4: eigenvalues and eigenvectors.

## Narrated script

### [00:04.3] Introduction — `manim:S01`

**ES:** Un muestreador de Gibbs, un chip de pbits o una partícula que salta entre pozos tienen algo en común: su siguiente estado depende solo del estado actual, y de nada más del pasado. Eso es una cadena de Markov. Las cadenas de Markov son el motor matemático del muestreo. En esta lección veremos cómo una cadena olvida su punto de partida, a qué distribución llega y qué tan rápido lo hace.

**EN:** A Gibbs sampler, a pbit chip or a particle hopping between wells have something in common: their next state depends only on the current state, and on nothing else from the past. That is a Markov chain. Markov chains are the mathematical engine of sampling. In this lesson we will see how a chain forgets its starting point, which distribution it reaches and how fast.

### [00:28.8] Intuition — `manim:S02`

**ES:** Imagina un caminante en un grafo de tres estados. En cada paso tira un dado cargado que depende solo del nodo donde está, y salta según el resultado. Las flechas indican las probabilidades de transición: desde el estado uno, por ejemplo, se queda con probabilidad dos tercios y pasa al dos con probabilidad un tercio. Si contamos cuántas veces visita cada estado, las fracciones se estabilizan: tres décimos, cuatro décimos y tres décimos. Ese es el comportamiento a largo plazo de la cadena.

**EN:** Imagine a walker on a three-state graph. At each step it rolls a loaded die that depends only on the node it is at, and jumps according to the result. The arrows show the transition probabilities: from state one, for example, it stays with probability two thirds and moves to two with probability one third. If we count how often it visits each state, the fractions settle: three tenths, four tenths and three tenths. That is the long-run behavior of the chain.

### [01:00.6] Evolving distributions — `manim:S03`

**ES:** En lugar de seguir a un solo caminante, sigamos la distribución de probabilidad completa. Es un vector fila p_n, y un paso de la cadena es multiplicarlo por la matriz de transición: p_{n+1} = p_n P. Empecemos con toda la probabilidad en el estado uno. Las barras cambian paso a paso y se acercan a la distribución estacionaria. Si empezamos en el estado tres, o en una mezcla cualquiera, llegamos al mismo destino. La cadena olvida de dónde vino.

**EN:** Instead of following a single walker, let's follow the whole probability distribution. It is a row vector p_n, and one step of the chain multiplies it by the transition matrix: p_{n+1} = p_n P. Let's start with all the probability in state one. The bars change step by step and approach the stationary distribution. If we start in state three, or in any mixture, we reach the same destination. The chain forgets where it came from.

### [01:32.8] Stationary distribution — `manim:S04`

**ES:** La distribución de llegada no cambia al aplicar un paso más: π P = π. Es un vector propio por la izquierda de la matriz de transición, con valor propio uno. Para una cadena irreducible y aperiódica, es decir, que puede ir de cualquier estado a cualquier otro y no oscila con un período fijo, esa distribución existe, es única, y la cadena converge a ella desde cualquier inicio.

**EN:** The limiting distribution does not change when one more step is applied: π P = π. It is a left eigenvector of the transition matrix, with eigenvalue one. For an irreducible and aperiodic chain, that is, one that can go from any state to any other and does not oscillate with a fixed period, that distribution exists, is unique, and the chain converges to it from any start.

### [01:57.9] Detailed balance — `manim:S05`

**ES:** Hay una condición más fuerte que la estacionariedad: el balance detallado, π_i P_ij = π_j P_ji. Significa que, en equilibrio, el flujo de probabilidad de i a j es igual al flujo de j a i en cada arista. En nuestra cadena los flujos se compensan arista por arista. Ahora mira una cadena que gira en un ciclo: su distribución estacionaria es uniforme, pero hay una corriente neta circulando. Es estacionaria, pero no cumple balance detallado. Las cadenas que cumplen balance detallado se llaman reversibles, y describen sistemas en equilibrio termodinámico. Si el balance detallado se cumple, la estacionariedad se sigue automáticamente.

**EN:** There is a stronger condition than stationarity: detailed balance, π_i P_ij = π_j P_ji. It means that, at equilibrium, the probability flow from i to j equals the flow from j to i on every edge. In our chain the flows cancel edge by edge. Now look at a chain that rotates around a cycle: its stationary distribution is uniform, but a net current circulates. It is stationary, but it does not satisfy detailed balance. Chains that satisfy detailed balance are called reversible, and they describe systems in thermodynamic equilibrium. If detailed balance holds, stationarity follows automatically.

### [02:41.6] Spectral gap and mixing — `manim:S06`

**ES:** ¿Qué tan rápido se olvida el inicio? La respuesta está en los otros valores propios. El más grande siempre es uno. El segundo en valor absoluto, λ₂, controla la velocidad: la distancia a la estacionaria decae como ∣λ₂∣ⁿ. En escala logarítmica, la distancia cae en línea recta, con pendiente igual al logaritmo de λ₂. La brecha espectral es uno menos λ₂, y el tiempo de mezcla crece como su inverso. Cadenas con brecha pequeña tardan mucho en olvidar; en los modelos de Ising cerca de la temperatura crítica la brecha se cierra y el muestreo se vuelve lento.

**EN:** How fast is the start forgotten? The answer lies in the other eigenvalues. The largest is always one. The second largest in absolute value, λ₂, controls the speed: the distance to stationarity decays as ∣λ₂∣ⁿ. On a log scale, the distance falls in a straight line, with slope equal to the log of λ₂. The spectral gap is one minus λ₂, and the mixing time grows as its inverse. Chains with a small gap take a long time to forget; in Ising models near the critical temperature the gap closes and sampling becomes slow.

### [03:19.8] Numerical example — `manim:S07`

**ES:** Verifiquemos con nuestra cadena. Resolvemos π P = π con la suma igual a uno, y obtenemos tres décimos, cuatro décimos y tres décimos. Comprobemos balance detallado entre los estados uno y dos: tres décimos por un tercio da un décimo, y cuatro décimos por un cuarto también da un décimo. Los valores propios de la matriz son uno, dos tercios y un sexto. La brecha espectral es un tercio, así que cada paso reduce la distancia a la estacionaria aproximadamente a dos tercios.

**EN:** Let's check with our chain. We solve π P = π with the sum equal to one, and get three tenths, four tenths and three tenths. Let's check detailed balance between states one and two: three tenths times one third gives one tenth, and four tenths times one quarter also gives one tenth. The eigenvalues of the matrix are one, two thirds and one sixth. The spectral gap is one third, so each step shrinks the distance to stationarity to about two thirds.

### [03:52.7] Applications — `slide`

**ES:** Las cadenas de Markov aparecen por todas partes en el curso. Gibbs y Metropolis son cadenas diseñadas para que su distribución estacionaria sea la de Boltzmann. Un chip de pbits es una cadena de Markov física, y su brecha espectral decide cuántos barridos hacen falta. En el laboratorio uno construirás cadenas de tres y de cincuenta estados, y medirás la convergencia contra la predicción espectral.

**EN:** Markov chains show up everywhere in the course. Gibbs and Metropolis are chains designed so that their stationary distribution is the Boltzmann distribution. A pbit chip is a physical Markov chain, and its spectral gap decides how many sweeps are needed. In lab one you will build chains with three and fifty states, and measure convergence against the spectral prediction.

### [04:18.1] Connections — `slide`

**ES:** En la próxima lección veremos que, en un ciclo, los vectores propios son ondas de Fourier. En la unidad uno la distribución estacionaria será la de Boltzmann. La ecuación de Fokker y Planck es la versión continua de lo que vimos hoy. Y en la unidad cuatro mediremos en la práctica qué tan correlacionadas están las muestras.

**EN:** In the next lesson we will see that, on a cycle, the eigenvectors are Fourier waves. In unit one the stationary distribution will be the Boltzmann distribution. The Fokker–Planck equation is the continuous version of what we saw today. And in unit four we will measure in practice how correlated the samples are.

### [04:38.3] Common mistakes — `slide`

**ES:** Cuidado con las convenciones: si la distribución es un vector fila, se multiplica por la izquierda y las filas de la matriz suman uno. Recuerda que estacionaria no implica balance detallado. Una cadena periódica puede tener distribución estacionaria y aun así no converger. Y la velocidad la decide el valor absoluto del segundo valor propio: uno cercano a menos uno también frena la mezcla.

**EN:** Watch the conventions: if the distribution is a row vector, it multiplies from the left and the rows of the matrix sum to one. Remember that stationary does not imply detailed balance. A periodic chain can have a stationary distribution and still not converge. And the speed is decided by the absolute value of the second eigenvalue: one near minus one also slows mixing.

### [05:03.7] Summary — `manim:S11`

**ES:** En resumen: una cadena de Markov se describe con su matriz de transición, y las distribuciones evolucionan como p_{n+1} = p_n P. La estacionaria cumple π P = π, y el balance detallado describe el equilibrio. La brecha espectral fija la velocidad con que la cadena olvida su inicio.

**EN:** In summary: a Markov chain is described by its transition matrix, and distributions evolve as p_{n+1} = p_n P. The stationary distribution satisfies π P = π, and detailed balance describes equilibrium. The spectral gap sets how fast the chain forgets its start.

### [05:25.0] Self-assessment — `slide`

**ES:** Para practicar: demuestra que el balance detallado implica estacionariedad. Encuentra la estacionaria de una cadena de dos estados y su segundo valor propio. Calcula cuántos pasos hacen falta para llegar a una distancia de una millonésima. Y construye una cadena con estacionaria uniforme que no cumpla balance detallado.

**EN:** To practice: prove that detailed balance implies stationarity. Find the stationary distribution of a two-state chain and its second eigenvalue. Compute how many steps are needed to reach a distance of one millionth. And build a chain with a uniform stationary distribution that violates detailed balance.

## Key equations
- $$p_{n+1} = p_n P,\quad \sum_j P_{ij} = 1$$ — Evolution of the distribution (row vector) under a row-stochastic matrix.
- $$\pi P = \pi$$ — Stationary distribution: left eigenvector with eigenvalue 1.
- $$\pi_i P_{ij} = \pi_j P_{ji}$$ — Detailed balance: equal flows on every edge; it implies stationarity.
- $$\|p_n - \pi\|_1 \lesssim C\,|\lambda_2|^n,\quad t_{\text{mix}} \sim \frac{1}{1-|\lambda_2|}\ln\frac{1}{\varepsilon}$$ — The spectral gap controls the mixing speed.

## Summary
- Markov: the future depends only on the present; $p_{n+1} = p_n P$.
- Stationary $\pi P = \pi$; unique and attracting if the chain is irreducible and aperiodic.
- Detailed balance $\pi_i P_{ij} = \pi_j P_{ji}$: equilibrium without net currents.
- Spectral gap $1 - |\lambda_2|$: mixing time $\sim$ its inverse.

## Further reading
- [3] D. A. Levin, Y. Peres and E. L. Wilmer, Markov Chains and Mixing Times, AMS, 2009 (chs. 1, 4, 12).
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- Video V10: Spectral Graph Theory — L. Trevisan (supplementary).
