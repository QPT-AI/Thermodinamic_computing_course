# Lesson 1.2 — Statistical mechanics and the Boltzmann distribution

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Derive the Boltzmann distribution $p(x) = e^{-\beta E(x)}/Z$ from contact with a heat bath.
- Interpret the partition function $Z$: normalization, $F = -k_BT\ln Z$ and $\langle E\rangle = -\partial_\beta \ln Z$.
- See how temperature controls the shape of the distribution over an energy landscape.

## Prerequisites
- Lesson 1.1: entropy $S = k_B\ln\Omega$ and free energy.
- Lesson 0.3: probability distributions.

## Narrated script

### [00:06.3] Introduction — `manim:S01`

**ES:** Si este curso tuviera una sola fórmula, sería esta: la probabilidad de un estado es proporcional a la exponencial de menos su energía dividida por k_B T. Un chip termodinámico recibe una función de energía y devuelve muestras de esa distribución. En esta lección veremos de dónde sale, qué papel juega la temperatura y por qué el número que la normaliza, la función de partición, contiene toda la termodinámica.

**EN:** If this course had a single formula, it would be this: the probability of a state is proportional to the exponential of minus its energy divided by k_B T. A thermodynamic chip receives an energy function and returns samples from that distribution. In this lesson we will see where it comes from, what role temperature plays, and why the number that normalizes it, the partition function, contains all of thermodynamics.

### [00:32.8] Intuition — `manim:S02`

**ES:** Piensa en un sistema pequeño en contacto con un baño enorme. La energía total está fija. Cada unidad de energía que tiene el sistema se la quita al baño, y el baño, al perder energía, pierde microestados. Como la entropía del baño crece linealmente con su energía, con pendiente uno sobre T, su número de microestados cae exponencialmente: cada vez que el sistema toma una porción E de energía, el número de formas de arreglar el baño se multiplica por e^(−E/k_B T). Las barras muestran ese conteo. La probabilidad de un estado del sistema es proporcional al número de microestados que le deja al baño. Esa es la distribución de Boltzmann.

**EN:** Think of a small system in contact with a huge bath. The total energy is fixed. Every unit of energy the system holds is taken from the bath, and the bath, by losing energy, loses microstates. Since the bath's entropy grows linearly with its energy, with slope one over T, its number of microstates falls exponentially: every time the system takes a portion E of energy, the number of ways to arrange the bath is multiplied by e^(−E/k_B T). The bars show that count. The probability of a system state is proportional to the number of microstates it leaves the bath. That is the Boltzmann distribution.

### [01:15.1] Visual explanation — `manim:S03`

**ES:** Ahora tomemos un paisaje de energía con dos valles de distinta profundidad. La curva verde es la distribución de Boltzmann. A temperatura alta, la exponencial es casi plana y el sistema explora todo el paisaje. Al enfriar, la probabilidad se concentra en los valles. Y a temperatura muy baja, casi toda la probabilidad cae en el valle más profundo, el mínimo global. La temperatura es una perilla entre explorar y optimizar. Esta misma idea es la base del recocido simulado.

**EN:** Now take an energy landscape with two valleys of different depth. The green curve is the Boltzmann distribution. At high temperature, the exponential is almost flat and the system explores the whole landscape. As it cools, probability concentrates in the valleys. And at very low temperature, almost all the probability falls into the deepest valley, the global minimum. Temperature is a knob between exploring and optimizing. This same idea underlies simulated annealing.

### [01:46.3] Partition function — `manim:S04`

**ES:** Para que las probabilidades sumen uno dividimos por Z, la suma de e^(−βE) sobre todos los estados, con β igual a 1/k_B T. Z parece un simple normalizador, pero codifica toda la termodinámica. La energía libre es F = −k_B T ln Z. La energía media es menos la derivada del logaritmo de Z respecto a β. Y la varianza de la energía es la segunda derivada. El problema es que Z suma sobre todos los estados: para cien espines hay dos elevado a cien términos. Por eso, en lugar de calcular Z, muestreamos.

**EN:** For the probabilities to sum to one we divide by Z, the sum of e^(−βE) over all states, with β equal to 1/k_B T. Z looks like a mere normalizer, but it encodes all of thermodynamics. The free energy is F = −k_B T ln Z. The mean energy is minus the derivative of the log of Z with respect to β. And the variance of the energy is the second derivative. The problem is that Z sums over all states: for a hundred spins there are two to the hundred terms. That is why, instead of computing Z, we sample.

### [02:25.1] Maximum-entropy derivation — `manim:S05`

**ES:** Hay otra derivación elegante. Busquemos la distribución con la máxima entropía de Shannon que tenga una energía media fija. Con multiplicadores de Lagrange, uno para la normalización y otro para la energía, la condición de óptimo da que el logaritmo de p es lineal en la energía. Es decir, p es exponencial en la energía, y el multiplicador es exactamente β. La distribución de Boltzmann es la menos comprometida con todo lo que no sabemos, excepto la energía media.

**EN:** There is another elegant derivation. Let's look for the distribution with maximum Shannon entropy that has a fixed mean energy. With Lagrange multipliers, one for normalization and one for energy, the optimality condition says the log of p is linear in the energy. That is, p is exponential in the energy, and the multiplier is exactly β. The Boltzmann distribution is the least committed to everything we don't know, except the mean energy.

### [02:54.7] Numerical example — `manim:S06`

**ES:** Un sistema de tres niveles con energías cero, uno y dos, medidas en unidades de k_B T. Los pesos de Boltzmann son uno, e^(−1) y e^(−2): uno, cero coma tres seis ocho y cero coma uno tres cinco. La función de partición es su suma, uno coma cinco cero tres. Las probabilidades son cero coma seis seis cinco, cero coma dos cuatro cinco y cero coma cero nueve. La energía media es cero coma cuatro dos cinco, y la energía libre es menos el logaritmo de uno coma cinco cero tres, unos menos cero coma cuatro uno.

**EN:** A three-level system with energies zero, one and two, in units of k_B T. The Boltzmann weights are one, e^(−1) and e^(−2): 1, 0.368 and 0.135. The partition function is their sum, 1.503. The probabilities are 0.665, 0.245 and 0.09. The mean energy is 0.425, and the free energy is minus the log of 1.503, about −0.41.

### [03:31.6] Applications — `slide`

**ES:** Esta distribución es el lenguaje de programación del cómputo termodinámico. Un chip recibe los parámetros de una energía y devuelve muestras. En aprendizaje automático, los modelos basados en energía aprenden esa energía a partir de datos. En optimización, bajar la temperatura concentra la distribución en el mínimo global. Y con una energía cuadrática, la distribución de Boltzmann es una gaussiana cuya media resuelve un sistema lineal.

**EN:** This distribution is the programming language of thermodynamic computing. A chip receives the parameters of an energy and returns samples. In machine learning, energy-based models learn that energy from data. In optimization, lowering the temperature concentrates the distribution on the global minimum. And with a quadratic energy, the Boltzmann distribution is a Gaussian whose mean solves a linear system.

### [03:59.6] Connections — `slide`

**ES:** En la próxima lección conectaremos esta distribución con la entropía de Gibbs. En la unidad dos veremos que es el estado estacionario de la dinámica de Langevin. Y en la unidad cuatro la aplicaremos al modelo de Ising y al pbit, que es la distribución de Boltzmann de un solo espín.

**EN:** In the next lesson we will connect this distribution with Gibbs entropy. In unit two we will see that it is the stationary state of Langevin dynamics. And in unit four we will apply it to the Ising model and to the pbit, which is the Boltzmann distribution of a single spin.

### [04:17.4] Common mistakes — `slide`

**ES:** Atención: la fórmula da la probabilidad de un microestado; para un macroestado hay que multiplicar por su número de microestados. Sumar una constante a la energía no cambia las probabilidades. Beta es uno sobre k_B T, no uno sobre T. Y la distribución describe equilibrio con un baño: fuera del equilibrio necesitaremos otras herramientas.

**EN:** Careful: the formula gives the probability of a microstate; for a macrostate you must multiply by its number of microstates. Adding a constant to the energy does not change the probabilities. Beta is one over k_B T, not one over T. And the distribution describes equilibrium with a bath: out of equilibrium we will need other tools.

### [04:40.0] Summary — `manim:S10`

**ES:** En resumen: un sistema en contacto con un baño visita cada estado con probabilidad e^(−βE)/Z, porque eso maximiza los microestados del baño, o equivalentemente la entropía con energía media fija. La temperatura controla la forma de la distribución, y la función de partición contiene la energía libre y todos los momentos de la energía.

**EN:** In summary: a system in contact with a bath visits each state with probability e^(−βE)/Z, because that maximizes the bath's microstates, or equivalently the entropy at fixed mean energy. Temperature controls the shape of the distribution, and the partition function contains the free energy and all the moments of the energy.

### [05:02.7] Self-assessment — `slide`

**ES:** Para practicar: resuelve el sistema de dos niveles. Demuestra las fórmulas de la energía media y su varianza. Cuenta los términos de la función de partición para cien espines y para el chip Z1. Y aplica Boltzmann a un resorte para obtener el teorema de equipartición.

**EN:** To practice: solve the two-level system. Prove the formulas for the mean energy and its variance. Count the terms of the partition function for a hundred spins and for the Z1 chip. And apply Boltzmann to a spring to obtain the equipartition theorem.

## Key equations
- $$p(x) = \frac{e^{-\beta E(x)}}{Z},\quad Z = \sum_x e^{-\beta E(x)},\quad \beta = \frac{1}{k_BT}$$ — Boltzmann distribution (canonical ensemble) and partition function.
- $$F = -k_BT\ln Z,\quad \langle E\rangle = -\partial_\beta \ln Z,\quad \mathrm{Var}(E) = \partial_\beta^2\ln Z$$ — Thermodynamics follows from derivatives of $\ln Z$.
- $$\max_p\Big\{-\sum p\ln p\ :\ \sum p = 1,\ \sum pE = \bar E\Big\} \Rightarrow p \propto e^{-\beta E}$$ — Boltzmann as the maximum-entropy distribution at fixed mean energy.

## Summary
- $p(x) = e^{-\beta E(x)}/Z$: probability of a microstate in contact with a bath.
- High $T$ explores; low $T$ concentrates on the global minimum.
- $Z$ normalizes and generates the thermodynamics: $F = -k_BT\ln Z$; computing it is intractable, so we sample.
- Equivalent to maximum entropy at fixed mean energy.

## Further reading
- [2] L. Peliti and S. Pigolotti, Stochastic Thermodynamics, chs. 1–2.
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods (section 2).
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
