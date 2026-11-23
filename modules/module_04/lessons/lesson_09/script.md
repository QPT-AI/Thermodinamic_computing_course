# Lesson 4.9 — Mean-field theory

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Derive the self-consistent equations $m_i = \tanh\big(\beta(\sum_j J_{ij}m_j + h_i)\big)$.
- Solve them graphically and by iteration; compare $T_c^{\text{MF}} = zJ$ with the exact 2D result.
- Read mean field as a deterministic tanh layer: from sampling to neural networks.

## Prerequisites
- Lesson 4.5: pbits, $\mathbb E[s] = \tanh(\beta u)$.
- Lesson 4.2: 2D Ising and $T_c$.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** Muestrear es caro. ¿Y si, en lugar de seguir cada espín fluctuante, siguiéramos solo su valor medio? Esa es la idea del campo medio: reemplazar las fluctuaciones de los vecinos por su promedio. El resultado es un sistema de ecuaciones deterministas que cualquier procesador resuelve rápido. Y su forma es exactamente la de una red neuronal con activación tangente.

**EN:** Sampling is expensive. What if, instead of following each fluctuating spin, we followed only its mean value? That is the idea of mean field: replace the neighbors' fluctuations by their average. The result is a system of deterministic equations that any processor solves quickly. And its form is exactly that of a neural network with tanh activation.

### [00:28.3] The approximation — `manim:S02`

**ES:** Un pbit con entrada u_i tiene media tanh(βu_i). Pero la entrada depende de los vecinos, que fluctúan. El campo medio reemplaza cada vecino por su media, s_j → m_j, y obtiene las ecuaciones autoconsistentes m_i = tanh(β(Σ_j J_ij m_j + h_i)). Despreciamos las correlaciones entre vecinos: es exacto cuando cada espín tiene muchísimos vecinos débiles.

**EN:** A pbit with input u_i has mean tanh(βu_i). But the input depends on the neighbors, which fluctuate. Mean field replaces each neighbor by its mean, s_j → m_j, and obtains the self-consistent equations m_i = tanh(β(Σ_j J_ij m_j + h_i)). We neglect correlations between neighbors: it is exact when each spin has very many weak neighbors.

### [00:59.6] Graphical solution — `manim:S03`

**ES:** En una red uniforme con z vecinos, todos los espines tienen la misma media y la ecuación es m = tanh(βzJ m). La solución es la intersección de la recta y = m con la curva tangente. Si la pendiente en el origen, βzJ, es menor que uno, la única solución es cero: desorden. Si es mayor, aparecen dos soluciones simétricas: el sistema se magnetiza. La transición ocurre en T_c = zJ.

**EN:** On a uniform lattice with z neighbors, all spins have the same mean and the equation is m = tanh(βzJ m). The solution is the intersection of the line y = m with the tanh curve. If the slope at the origin, βzJ, is less than one, the only solution is zero: disorder. If it is greater, two symmetric solutions appear: the system magnetizes. The transition happens at T_c = zJ.

### [01:30.3] Mean field vs exact — `manim:S04`

**ES:** Para la red cuadrada, con cuatro vecinos, el campo medio predice T_c = 4. El valor exacto de Onsager es dos coma dos siete. El campo medio sobreestima el orden, porque ignora las fluctuaciones que lo destruyen. A temperatura dos predice una magnetización de cero coma nueve seis, frente a cero coma nueve uno exacto. Y a temperatura tres predice cero coma siete ocho, cuando en realidad el sistema ya está desordenado.

**EN:** For the square lattice, with four neighbors, mean field predicts T_c = 4. The exact Onsager value is 2.27. Mean field overestimates order, because it ignores the fluctuations that destroy it. At temperature two it predicts a magnetization of 0.96, versus 0.91 exact. And at temperature three it predicts 0.78, when in reality the system is already disordered.

### [01:59.0] From sampling to tanh layers — `manim:S05`

**ES:** Resolvamos las ecuaciones por iteración: m ← tanh(β(J m + h)). Cada iteración es una capa de una red neuronal: una matriz, un sesgo y una activación tangente. Con T = 2, partiendo de cero coma cinco, la iteración converge a cero coma nueve cinco siete en unas cinco capas. Así, una red de pbits que muestrea y una red neuronal determinista son dos caras del mismo modelo: una fluctúa, la otra promedia.

**EN:** Let's solve the equations by iteration: m ← tanh(β(J m + h)). Each iteration is a neural network layer: a matrix, a bias and a tanh activation. With T = 2, starting from 0.5, the iteration converges to 0.957 in about five layers. So a pbit network that samples and a deterministic neural network are two faces of the same model: one fluctuates, the other averages.

### [02:30.0] Variational view — `manim:S06`

**ES:** Hay una justificación más profunda. El campo medio busca, entre todas las distribuciones que factorizan espín por espín, la que minimiza la energía libre variacional, o lo que es igual, la divergencia KL con la distribución de Boltzmann. Por la desigualdad de Gibbs y Bogoliubov, esa energía libre es siempre una cota superior de la verdadera. Es la misma idea de la inferencia variacional en aprendizaje automático.

**EN:** There is a deeper justification. Mean field searches, among all distributions that factorize spin by spin, for the one that minimizes the variational free energy, or equivalently, the KL divergence to the Boltzmann distribution. By the Gibbs–Bogoliubov inequality, that free energy is always an upper bound on the true one. It is the same idea as variational inference in machine learning.

### [02:56.4] Applications — `slide`

**ES:** El campo medio da una aproximación rápida de la fase del modelo para entrenar máquinas de Boltzmann, y explica las unidades tangente que construiremos con pbits en la unidad diez. La propagación de creencias y las correcciones TAP lo refinan. Es exacto con interacciones de alcance infinito y pobre cerca de la transición en pocas dimensiones.

**EN:** Mean field gives a fast approximation of the model phase for training Boltzmann machines, and explains the tanh units we will build from pbits in unit ten. Belief propagation and TAP corrections refine it. It is exact with infinite-range interactions and poor near the transition in low dimensions.

### [03:17.8] Common mistakes — `slide`

**ES:** Errores comunes: confiar en la temperatura crítica del campo medio en dos dimensiones. Tomar la solución cero por debajo de la transición, que es inestable. Olvidar que ignora las correlaciones. E iterar sin amortiguamiento, lo que puede oscilar.

**EN:** Common mistakes: trusting the mean-field critical temperature in two dimensions. Taking the zero solution below the transition, which is unstable. Forgetting that it ignores correlations. And iterating without damping, which can oscillate.

### [03:34.2] Summary — `manim:S09`

**ES:** En resumen: el campo medio reemplaza a los vecinos por sus medias y obtiene m_i = tanh(β(Σ J_ij m_j + h_i)). Predice una transición en T_c = zJ, que sobreestima el orden. Iterarlo es aplicar capas tangente: el puente entre muestrear con pbits y calcular con redes neuronales.

**EN:** In summary: mean field replaces the neighbors by their means and gets m_i = tanh(β(Σ J_ij m_j + h_i)). It predicts a transition at T_c = zJ, which overestimates order. Iterating it means applying tanh layers: the bridge between sampling with pbits and computing with neural networks.

### [03:56.8] Self-assessment — `slide`

**ES:** Para practicar: resuelve la ecuación autoconsistente. Deriva el comportamiento cerca de la transición. Calcula la temperatura crítica de la red triangular. Y explica por qué el campo medio es exacto con alcance infinito.

**EN:** To practice: solve the self-consistent equation. Derive the behavior near the transition. Compute the critical temperature of the triangular lattice. And explain why mean field is exact with infinite range.

## Key equations
- $$m_i = \tanh\Big(\beta\big(\textstyle\sum_j J_{ij}m_j + h_i\big)\Big)$$ — Naive mean-field self-consistent equations.
- $$m = \tanh(\beta zJ\,m),\qquad T_c^{\text{MF}} = zJ/k_B$$ — Uniform lattice with $z$ neighbors; 2D square: $T_c^{\text{MF}} = 4$ vs exact 2.27.
- $$F_{\text{MF}} = \langle E\rangle_q - T S(q) \ge F,\quad q(s) = \prod_i q_i(s_i)$$ — Variational (Gibbs–Bogoliubov) bound with a factorized distribution.

## Summary
- Neighbors → their means: $m = \tanh(\beta(Jm + h))$.
- Graphical solution; transition at $T_c = zJ$ (overestimates order).
- Iteration = tanh layers: pbits sample, neural networks average.
- Variational: minimizes KL over factorized distributions; $F_{\text{MF}} \ge F$.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- M. Opper and D. Saad (eds.), Advanced Mean Field Methods, MIT Press, 2001.
- [18] J. Kaiser and S. Datta, Probabilistic computing with p-bits, 2021.
