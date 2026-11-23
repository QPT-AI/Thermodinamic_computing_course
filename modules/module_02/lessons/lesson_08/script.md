# Lesson 2.8 — Continuous-time Markov jump processes

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe a jump process by its rate matrix $Q$ and the master equation $\dot p = pQ$.
- Simulate exact trajectories with the Gillespie algorithm.
- Compute first-passage times and their variability.

## Prerequisites
- Lesson 0.5: discrete-time Markov chains.
- Exponential and Poisson distributions.

## Narrated script

### [00:06.0] Introduction — `manim:S01`

**ES:** No todo sistema ruidoso se mueve de forma continua. Un pbit salta entre menos uno y más uno; una molécula se fabrica o se degrada; un electrón entra o sale de una isla. Son procesos de saltos en tiempo continuo: el estado es discreto, pero los saltos ocurren en instantes aleatorios. Son el lenguaje de los circuitos brownianos y de las redes de reacciones químicas que veremos en la unidad cinco.

**EN:** Not every noisy system moves continuously. A pbit jumps between minus one and plus one; a molecule is produced or degraded; an electron enters or leaves an island. These are continuous-time jump processes: the state is discrete, but the jumps happen at random instants. They are the language of Brownian circuits and of the chemical reaction networks we will see in unit five.

### [00:32.3] Intuition — `manim:S02`

**ES:** Piensa en un pbit como una moneda que, de vez en cuando, se voltea sola. Desde el estado menos uno salta a más uno con una tasa k₊, es decir, con probabilidad k₊ dt en cada intervalo diminuto dt. Desde más uno vuelve con tasa k₋. El tiempo de espera en cada estado es exponencial y sin memoria. A largo plazo, la fracción de tiempo en el estado más uno es k₊/(k₊ + k₋).

**EN:** Think of a pbit as a coin that, every now and then, flips itself. From state minus one it jumps to plus one with rate k₊, that is, with probability k₊ dt in each tiny interval dt. From plus one it returns with rate k₋. The waiting time in each state is exponential and memoryless. In the long run, the fraction of time in state plus one is k₊/(k₊ + k₋).

### [00:59.9] Master equation — `manim:S03`

**ES:** Para la distribución completa, cada estado gana probabilidad por los saltos que llegan y la pierde por los que salen. Eso es la ecuación maestra: dp_i/dt = Σ_j (p_j Q_ji − p_i Q_ij). En forma matricial, ṗ = p Q, donde Q es la matriz de tasas, con filas que suman cero. Es la versión en tiempo continuo de p_{n+1} = p_n P, y su solución es p(t) = p(0) e^(Qt). Las barras muestran cómo la distribución relaja hacia el estado estacionario.

**EN:** For the full distribution, each state gains probability from incoming jumps and loses it through outgoing ones. That is the master equation: dp_i/dt = Σ_j (p_j Q_ji − p_i Q_ij). In matrix form, ṗ = p Q, where Q is the rate matrix, whose rows sum to zero. It is the continuous-time version of p_{n+1} = p_n P, and its solution is p(t) = p(0) e^(Qt). The bars show how the distribution relaxes toward the stationary state.

### [01:36.3] Gillespie algorithm — `manim:S04`

**ES:** ¿Cómo se simula una trayectoria sin discretizar el tiempo? Gillespie propuso dos sorteos por evento. Primero, el tiempo hasta el próximo salto, exponencial con tasa igual a la suma de todas las tasas de salida. Segundo, cuál salto ocurre, con probabilidad proporcional a su tasa. Es exacto: no hay paso de tiempo ni sesgo. La animación lo aplica a una molécula que se produce con tasa k y se degrada con tasa γ n. El histograma del número de moléculas converge a una distribución de Poisson con media k/γ.

**EN:** How do we simulate a trajectory without discretizing time? Gillespie proposed two draws per event. First, the time to the next jump, exponential with rate equal to the sum of all exit rates. Second, which jump happens, with probability proportional to its rate. It is exact: there is no time step and no bias. The animation applies it to a molecule produced at rate k and degraded at rate γ n. The histogram of the number of molecules converges to a Poisson distribution with mean k/γ.

### [02:11.3] First-passage times — `manim:S05`

**ES:** Muchas preguntas de cómputo son de primer paso: ¿cuánto tarda el sistema en llegar por primera vez a un estado? Por ejemplo, cuánto tarda un circuito browniano en completar un cálculo. Si el cálculo requiere N saltos sucesivos, cada uno con tasa k, el tiempo total es la suma de N exponenciales: su media es N/k y su varianza N/k². La precisión relativa mejora como uno sobre raíz de N. Los histogramas de Gillespie se estrechan a medida que N crece. En la unidad tres veremos que esa precisión tiene un costo en producción de entropía.

**EN:** Many computing questions are first-passage questions: how long does the system take to reach a state for the first time? For example, how long a Brownian circuit takes to complete a computation. If the computation requires N successive jumps, each with rate k, the total time is a sum of N exponentials: its mean is N/k and its variance N/k². The relative precision improves as one over root N. The Gillespie histograms narrow as N grows. In unit three we will see that this precision costs entropy production.

### [02:48.2] Numerical example — `manim:S06`

**ES:** Producción con tasa diez por segundo y degradación de una por segundo por molécula: el número medio en estado estacionario es diez, con varianza también diez. Para el pbit con k₊ = 3 y k₋ = 1 por microsegundo, la probabilidad de más uno es tres cuartos, y la autocorrelación decae con tasa k₊ + k₋, cuatro por microsegundo: un tiempo de correlación de doscientos cincuenta nanosegundos.

**EN:** Production at rate ten per second and degradation of one per second per molecule: the mean number at steady state is ten, with variance also ten. For the pbit with k₊ = 3 and k₋ = 1 per microsecond, the probability of plus one is three quarters, and the autocorrelation decays with rate k₊ + k₋, four per microsecond: a correlation time of two hundred fifty nanoseconds.

### [03:16.2] Applications — `slide`

**ES:** Los procesos de saltos describen la actualización de pbits en un chip, los circuitos brownianos de tokens cuyo tiempo de cómputo es un tiempo de primer paso, y las redes de reacciones químicas. En la unidad tres los usaremos para enunciar relaciones de incertidumbre termodinámica.

**EN:** Jump processes describe pbit updates on a chip, Brownian token circuits whose computation time is a first-passage time, and chemical reaction networks. In unit three we will use them to state thermodynamic uncertainty relations.

### [03:33.3] Common mistakes — `slide`

**ES:** Errores frecuentes: confundir una tasa con una probabilidad. Olvidar que las filas de la matriz de tasas suman cero. Discretizar el tiempo cuando Gillespie es exacto. Y reportar solo el tiempo medio de primer paso, sin su variabilidad.

**EN:** Frequent mistakes: confusing a rate with a probability. Forgetting that the rows of the rate matrix sum to zero. Discretizing time when Gillespie is exact. And reporting only the mean first-passage time, without its variability.

### [03:49.5] Summary — `manim:S09`

**ES:** En resumen: un proceso de saltos se describe con tasas; la distribución obedece la ecuación maestra ṗ = p Q. Gillespie simula trayectorias exactas con dos sorteos por evento. Y los tiempos de primer paso, con su media y su varianza, miden cuánto tarda y qué tan preciso es un cómputo estocástico.

**EN:** In summary: a jump process is described by rates; the distribution obeys the master equation ṗ = p Q. Gillespie simulates exact trajectories with two draws per event. And first-passage times, with their mean and variance, measure how long a stochastic computation takes and how precise it is.

### [04:10.7] Self-assessment — `slide`

**ES:** Para practicar: resuelve la ecuación maestra del pbit, demuestra que la distribución de Poisson es estacionaria, calcula media y varianza de un tiempo de primer paso, y describe los dos sorteos del algoritmo de Gillespie.

**EN:** To practice: solve the pbit master equation, prove that the Poisson distribution is stationary, compute the mean and variance of a first-passage time, and describe the two draws of the Gillespie algorithm.

## Key equations
- $$\dot p_i = \sum_j \big(p_j Q_{ji} - p_i Q_{ij}\big),\quad \dot p = pQ,\quad \sum_j Q_{ij} = 0$$ — Master equation and rate matrix.
- $$\tau \sim \mathrm{Exp}(R),\quad R = \sum_j Q_{ij};\qquad P(i\to j) = Q_{ij}/R$$ — Gillespie's two draws.
- $$\langle\tau_N\rangle = N/k,\quad \mathrm{Var}(\tau_N) = N/k^2$$ — First passage after $N$ successive jumps of rate $k$.

## Summary
- Jumps with rates; memoryless exponential waiting times.
- Master equation $\dot p = pQ$; solution $p(0)e^{Qt}$.
- Gillespie: exact simulation, two draws per event.
- First passage: mean and variance measure the time and precision of a computation.

## Further reading
- [1] Gardiner, Handbook of Stochastic Methods (master equation).
- [26] Y. Utsumi et al., Computation time and thermodynamic uncertainty relation of Brownian circuits, 2022.
- [27] P. Raux, C. Goupil and G. Verley, Thermodynamic circuits for chemical reaction networks, 2025.
