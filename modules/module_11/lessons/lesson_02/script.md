# Lesson 11.2 — Torx: stochastic differentiable programming

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define parametrized stochastic circuits (PSCs): typed wires, local stochastic gates, circuit composition.
- Derive the logarithmic parameter-shift identity and compare gradient estimators.
- Explain generator-derived gates (PIsing) and why tiling them on edges is not Gibbs sampling.

## Prerequisites
- Lesson 11.1: THRML and block Gibbs.
- Lesson 2.8: continuous-time Markov jump processes.

## Narrated script

### [00:06.2] Introduction — `manim:S01`

**ES:** THRML simula muestreo por bloques. Pero muchos algoritmos son más generales: cadenas de transiciones estocásticas con parámetros que queremos entrenar, como un modelo de difusión o un paseo aleatorio. En agosto de dos mil veintiséis, Extropic publicó los circuitos estocásticos parametrizados y torx, una biblioteca en JAX para construirlos, ejecutarlos y derivarlos. La idea es la misma que la de los circuitos cuánticos: un lenguaje de compuertas cercano a lo que el hardware hace de forma nativa.

**EN:** THRML simulates block sampling. But many algorithms are more general: chains of stochastic transitions with parameters we want to train, like a diffusion model or a random walk. In August twenty twenty-six, Extropic published parametrized stochastic circuits and torx, a JAX library to build, execute and differentiate them. The idea is the same as with quantum circuits: a gate language close to what the hardware does natively.

### [00:38.9] Stochastic gates — `manim:S02`

**ES:** Un circuito tiene cables con tipo: binarios, categóricos o continuos. Cada compuerta es una matriz estocástica local con parámetros. La más simple es el NOT probabilístico, PNOT: invierte un pbit con probabilidad p. Es una mezcla de la identidad y del NOT. El intercambio probabilístico y el NOT controlado probabilístico siguen la misma receta. El circuito completo es el producto de sus compuertas aplicado a la distribución de entrada.

**EN:** A circuit has typed wires: binary, categorical or continuous. Each gate is a local stochastic matrix with parameters. The simplest is the probabilistic NOT, PNOT: it flips a pbit with probability p. It is a mixture of the identity and the NOT. The probabilistic swap and the probabilistic controlled NOT follow the same recipe. The complete circuit is the product of its gates applied to the input distribution.

### [01:08.9] Training a circuit — `manim:S03`

**ES:** Reproducimos el primer ejemplo del artículo con nuestra propia implementación mínima en NumPy, escrita a partir de sus definiciones. Un PNOT, un intercambio y un NOT controlado actúan sobre dos pbits que empiezan en cero cero. Queremos la distribución mitad cero cero, mitad uno uno, correlación perfecta. Tras tres mil pasos de Adam, la pérdida baja de cero coma tres tres a dos por diez a la menos cinco, y la distribución final es cero coma cuatro nueve ocho en cada estado correlacionado.

**EN:** We reproduce the paper's first example with our own minimal NumPy implementation, written from its definitions. A PNOT, a swap and a controlled NOT act on two pbits starting at zero zero. We want the distribution half zero zero, half one one, perfect correlation. After three thousand Adam steps, the loss falls from 0.33 to 2·10⁻⁵, and the final distribution is 0.498 in each correlated state.

### [01:41.3] Gradients from circuit runs — `manim:S04`

**ES:** En hardware no tenemos la distribución exacta, solo muestras. Para las compuertas de mezcla con p = σ(θ), la derivada de la compuerta es la diferencia de dos compuertas de la misma familia: la original y otra con un parámetro desplazado, cuyo valor de p es el cuadrado del original. Verificamos la identidad con error de diez a la menos once. El gradiente se estima con la diferencia de dos promedios de ejecuciones del circuito: es la regla de desplazamiento de parámetro.

**EN:** In hardware we do not have the exact distribution, only samples. For mixture gates with p = σ(θ), the derivative of the gate is the difference of two gates of the same family: the original and another with a shifted parameter, whose value of p is the square of the original. We verify the identity with an error of ten to the minus eleven. The gradient is estimated with the difference of two averages of circuit runs: it is the parameter-shift rule.

### [02:11.6] Two estimators — `manim:S05`

**ES:** Comparamos con REINFORCE, el estimador de función de puntuación, que usa la trayectoria interna del circuito. Con mil ejecuciones, ambos son insesgados: el gradiente exacto es menos cero coma cero cuatro dos ocho, y los promedios coinciden. En este ejemplo, REINFORCE tuvo menos varianza. La ventaja del desplazamiento de parámetro es otra: solo necesita ejecutar el circuito y leer la salida, sin observar los estados intermedios, que en un chip no siempre son accesibles.

**EN:** We compare with REINFORCE, the score-function estimator, which uses the circuit's internal trajectory. With a thousand runs, both are unbiased: the exact gradient is −0.0428, and the averages agree. In this example, REINFORCE had lower variance. The advantage of the parameter shift is different: it only needs to run the circuit and read the output, without observing intermediate states, which on a chip are not always accessible.

### [02:42.2] Generator-derived gates — `manim:S06`

**ES:** Otra familia de compuertas sale de exponenciar una matriz de tasas. PIsing aplica durante un tiempo la dinámica de Glauber de dos espines acoplados. Desde la distribución uniforme, con acoplamiento uno y beta dos, a tiempo cinco alcanza la distribución de Boltzmann: cero coma cuatro nueve uno en los estados alineados. Pero cuidado: aplicar PIsing arista por arista en un anillo de ocho espines no muestrea el Ising del anillo. En nuestro caso queda a una distancia de variación total de cero coma ocho cuatro, mientras que Gibbs cromático es exacto. El artículo encuentra el mismo efecto.

**EN:** Another family of gates comes from exponentiating a rate matrix. PIsing applies for a time the Glauber dynamics of two coupled spins. From the uniform distribution, with coupling one and beta two, at time five it reaches the Boltzmann distribution: 0.491 in the aligned states. But careful: applying PIsing edge by edge on a ring of eight spins does not sample the ring's Ising model. In our case it stays at a total variation distance of 0.84, while chromatic Gibbs is exact. The paper finds the same effect.

### [03:19.9] Applications — `slide`

**ES:** Los circuitos estocásticos sirven para paseos aleatorios, difusión discreta, redes estocásticas sobre grafos y difusión con saltos. El mismo circuito corre con aleatoriedad de software o de hardware: el artículo usa pbits del chip X0 y obtiene estimaciones consistentes con la referencia. Y al compilar, usa compuertas de Gibbs nativas, no PIsing por aristas.

**EN:** Stochastic circuits are useful for random walks, discrete diffusion, stochastic networks on graphs and jump diffusion. The same circuit runs with software or hardware randomness: the paper uses pbits from the X0 chip and obtains estimates consistent with the baseline. And when compiling, use native Gibbs gates, not edge-tiled PIsing.

### [03:44.6] Common mistakes — `slide`

**ES:** Errores comunes: suponer que componer equilibrios locales da el equilibrio global. Usar REINFORCE cuando los estados internos no se pueden observar. Llevar las probabilidades a cero o uno, donde la puntuación diverge. E ignorar el error de calibración de los pbits reales, de alrededor del cinco por ciento.

**EN:** Common mistakes: assuming that composing local equilibria gives the global equilibrium. Using REINFORCE when the internal states cannot be observed. Pushing probabilities to zero or one, where the score diverges. And ignoring the calibration error of real pbits, around five percent.

### [04:04.8] Summary — `manim:S09`

**ES:** En resumen, un circuito estocástico parametrizado compone compuertas locales con tipo, y torx lo construye, ejecuta y deriva. La identidad de desplazamiento convierte la derivada en la diferencia de dos ejecuciones, útil cuando solo vemos la salida. Las compuertas derivadas de generadores, como PIsing, son potentes, pero componerlas por aristas no da el equilibrio global.

**EN:** In summary, a parametrized stochastic circuit composes typed local gates, and torx builds, executes and differentiates it. The shift identity turns the derivative into the difference of two runs, useful when we only see the output. Generator-derived gates, like PIsing, are powerful, but composing them edge by edge does not give the global equilibrium.

### [04:29.7] Self-assessment — `slide`

**ES:** Para practicar: escribe la matriz del PNOT. Demuestra la relación del parámetro desplazado. Explica por qué el desplazamiento de parámetro conviene al hardware. Y explica por qué PIsing por aristas no es Gibbs.

**EN:** To practice: write the PNOT matrix. Prove the relation of the shifted parameter. Explain why the parameter shift suits hardware. And explain why edge-tiled PIsing is not Gibbs.

## Key equations
- $$\mathrm{PNOT}(p) = \begin{pmatrix}1-p & p\\ p & 1-p\end{pmatrix},\qquad G(\theta) = (1-\sigma(\theta))\,I + \sigma(\theta)\,B$$ — Sigmoid-mixture gates.
- $$\partial_\theta G = G(\theta) - G(\theta^-),\quad \theta^- = -\ln\big((1+e^{-\theta})^2 - 1\big)$$ — Logarithmic parameter-shift identity (verified to 1e-11) [S].
- $$\mathrm{PIsing}(\theta) = e^{\Delta t\,Q},\quad Q_{ab} = \sigma\big(-\beta(E(s_a) - E(s_b))\big)$$ — Generator-derived Glauber gate.

## Summary
- PSC: typed wires + local parametrized stochastic gates; torx (JAX).
- Training toy circuit: loss 0.33 → 2·10⁻⁵ [S].
- Parameter shift: gradient from two circuit runs; unbiased like REINFORCE [S].
- Edge-tiled PIsing ≠ Gibbs: TV 0.84 (our ring) vs exact chromatic Gibbs [S].

## Further reading
- G. Verdon et al., A framework for stochastic differentiable programming, arXiv:2608.01612 (2026).
- Extropic, torx examples (torx/ in this repository), 2026.
- R. J. Williams, Simple statistical gradient-following algorithms (REINFORCE), Machine Learning 8, 229 (1992).
