# Lesson 4.5 — The pbit as a stochastic neuron

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the pbit: $P(s_i = +1) = \sigma(2\beta u_i)$, $\mathbb E[s_i] = \tanh(\beta u_i)$.
- Implement it with the rule $s_i = \mathrm{sgn}\big(\tanh(\beta u_i) - r\big)$, $r \sim U(-1, 1)$, and verify its statistics.
- See a network of pbits as a Gibbs sampler of an Ising model and as a stochastic neural network.

## Prerequisites
- Lesson 4.3: Gibbs sampling.
- Lesson 2.8: jump processes.

## Narrated script

### [00:05.4] Introduction — `manim:S01`

**ES:** Un bit digital siempre vale lo mismo hasta que alguien lo cambia. Un pbit, o bit probabilístico, fluctúa por sí solo entre menos uno y más uno, y su entrada no fija su valor sino su probabilidad. Es la pieza mínima del cómputo termodinámico discreto: una neurona estocástica que, conectada con otras, muestrea un modelo de Ising.

**EN:** A digital bit always keeps the same value until someone changes it. A pbit, or probabilistic bit, fluctuates on its own between minus one and plus one, and its input sets not its value but its probability. It is the minimal piece of discrete thermodynamic computing: a stochastic neuron that, connected to others, samples an Ising model.

### [00:27.7] Definition — `manim:S02`

**ES:** Un pbit recibe una entrada u y produce un espín s. La probabilidad de que valga más uno es la sigmoide σ(2βu). Su valor medio es la tangente hiperbólica, tanh(βu). Con entrada cero es una moneda justa; con entrada grande y positiva casi siempre vale uno. El parámetro β controla qué tan determinista es: con β infinito, el pbit se vuelve un bit digital con umbral.

**EN:** A pbit receives an input u and produces a spin s. The probability that it equals plus one is the sigmoid σ(2βu). Its mean value is the hyperbolic tangent, tanh(βu). With zero input it is a fair coin; with a large positive input it is almost always one. The parameter β controls how deterministic it is: with infinite β, the pbit becomes a thresholded digital bit.

### [00:55.9] Hardware rule — `manim:S03`

**ES:** ¿Cómo se construye? Una forma muy usada compara la tangente hiperbólica de la entrada con un número aleatorio uniforme entre menos uno y uno, y toma el signo: s = sgn(tanh(βu) − r). La probabilidad de que r quede por debajo de la tangente es exactamente (1 + tanh βu)/2, que es la sigmoide. En la simulación, con u = 0,5, la fracción de unos es cero coma siete tres, igual a σ(1).

**EN:** How is it built? A widely used way compares the hyperbolic tangent of the input with a uniform random number between minus one and one, and takes the sign: s = sgn(tanh(βu) − r). The probability that r falls below the tangent is exactly (1 + tanh βu)/2, which is the sigmoid. In the simulation, with u = 0.5, the fraction of ones is 0.73, equal to σ(1).

### [01:27.8] Networks of pbits — `manim:S04`

**ES:** Ahora conectemos pbits. Si la entrada de cada uno es su campo local, u_i = Σ_j J_ij s_j + h_i, y los actualizamos en el orden de un coloreo del grafo, la red entera hace muestreo de Gibbs del modelo de Ising con esos acoplamientos. Los pbits no calculan la distribución: la habitan. El histograma de los estados visitados reproduce e^(−βE) sin calcular nunca la función de partición.

**EN:** Now let's connect pbits. If each one's input is its local field, u_i = Σ_j J_ij s_j + h_i, and we update them in the order of a graph coloring, the whole network performs Gibbs sampling of the Ising model with those couplings. The pbits do not compute the distribution: they inhabit it. The histogram of visited states reproduces e^(−βE) without ever computing the partition function.

### [01:56.6] Stochastic neuron — `manim:S05`

**ES:** Mira la estructura: suma ponderada de entradas, más un sesgo, pasada por una sigmoide. Es la neurona de una red neuronal, pero con salida aleatoria en lugar de un número. Por eso las redes de pbits son el sustrato natural de las máquinas de Boltzmann. Y si promediamos muchas lecturas, la salida media es tanh(βu): una neurona determinista con activación tangente, que usaremos en la teoría de campo medio.

**EN:** Look at the structure: a weighted sum of inputs, plus a bias, passed through a sigmoid. It is the neuron of a neural network, but with a random output instead of a number. That is why pbit networks are the natural substrate of Boltzmann machines. And if we average many readouts, the mean output is tanh(βu): a deterministic neuron with tanh activation, which we will use in mean-field theory.

### [02:24.5] Numerical example — `manim:S06`

**ES:** Comprobemos con doscientas mil actualizaciones por entrada. Con entrada menos uno, la fracción de unos es cero coma uno dos, como σ(−2). Con cero, un medio. Con cero coma cinco, cero coma siete tres. Con uno coma cinco, cero coma nueve cinco. Y la media del espín sigue a la tangente hiperbólica con tres cifras.

**EN:** Let's check with two hundred thousand updates per input. With input minus one, the fraction of ones is 0.12, like σ(−2). With zero, one half. With 0.5, 0.73. With 1.5, 0.95. And the spin mean follows the hyperbolic tangent to three digits.

### [02:46.7] Applications — `slide`

**ES:** Los pbits se construyen con uniones túnel magnéticas de barrera baja, que fluctúan por el ruido térmico, o con circuitos CMOS que combinan un generador aleatorio, una tabla para la tangente y un comparador. El chip Z1 de Extropic tiene más de doscientos sesenta mil pbits con dieciséis acoplamientos cada uno.

**EN:** Pbits are built with low-barrier magnetic tunnel junctions, which fluctuate from thermal noise, or with CMOS circuits that combine a random generator, a lookup table for the tangent and a comparator. Extropic's Z1 chip has more than two hundred sixty thousand pbits with sixteen couplings each.

### [03:06.9] Common mistakes — `slide`

**ES:** Cuidado con el factor dos en la sigmoide, con actualizar pbits vecinos a la vez, con confundir la media con la probabilidad, y con generadores aleatorios sesgados o correlacionados, que deforman la distribución.

**EN:** Watch out for the factor of two in the sigmoid, for updating neighboring pbits at the same time, for confusing the mean with the probability, and for biased or correlated random generators, which distort the distribution.

### [03:20.7] Summary — `manim:S09`

**ES:** En resumen: un pbit es un espín aleatorio con P(+1) = σ(2βu) y media tanh(βu). Se implementa comparando la tangente con ruido uniforme. Una red de pbits con entradas iguales a los campos locales hace muestreo de Gibbs de un modelo de Ising, y es una red neuronal estocástica.

**EN:** In summary: a pbit is a random spin with P(+1) = σ(2βu) and mean tanh(βu). It is implemented by comparing the tangent with uniform noise. A pbit network whose inputs are the local fields performs Gibbs sampling of an Ising model, and it is a stochastic neural network.

### [03:43.0] Self-assessment — `slide`

**ES:** Para practicar: demuestra la regla de hardware. Calcula la media del espín. Encuentra la entrada que da noventa por ciento de unos. Y calcula la probabilidad de que dos pbits acoplados coincidan.

**EN:** To practice: prove the hardware rule. Compute the spin mean. Find the input that gives ninety percent ones. And compute the probability that two coupled pbits agree.

## Key equations
- $$P(s_i = +1) = \sigma(2\beta u_i),\qquad \mathbb E[s_i] = \tanh(\beta u_i)$$ — pbit statistics given its input $u_i$.
- $$s_i = \mathrm{sgn}\big(\tanh(\beta u_i) - r\big),\quad r \sim U(-1, 1)$$ — Hardware update rule.
- $$u_i = \sum_j J_{ij}s_j + h_i$$ — Input equal to the local field: the network does Gibbs sampling of Ising.

## Summary
- pbit: $P(+1) = \sigma(2\beta u)$, mean $\tanh(\beta u)$; $\beta\to\infty$ gives a digital bit.
- Hardware: compare $\tanh(\beta u)$ with uniform noise.
- Network with $u_i$ = local field ⇒ chromatic Gibbs of Ising.
- Stochastic neuron; its mean is a tanh neuron (mean field).

## Further reading
- [17] K. Y. Camsari, B. M. Sutton and S. Datta, p-bits for probabilistic spin logic, Appl. Phys. Rev. 6, 011305 (2019).
- [18] J. Kaiser and S. Datta, Probabilistic computing with p-bits, 2021.
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
