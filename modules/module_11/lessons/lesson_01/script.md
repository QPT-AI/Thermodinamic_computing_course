# Lesson 11.1 — THRML: simulating TSUs on GPUs

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe THRML's abstractions: nodes, blocks, factors, conditional samplers, sampling programs and schedules.
- Run block Gibbs on an Ising model with THRML and verify it against exact enumeration.
- Measure GPU throughput in flips per nanosecond and compare it with an FPGA and with Z1's specification.

## Prerequisites
- Lesson 4.3: MCMC, Metropolis–Hastings and Gibbs.
- Lesson 10.7: the Z1 chip.

## Narrated script

### [00:06.9] Introduction — `manim:S01`

**ES:** Antes de tener un chip, hay que poder programarlo. THRML es la biblioteca de Extropic para simular computadores probabilísticos en GPU. Está construida sobre JAX y sirve de andamio para implementar algoritmos de muestreo por bloques sobre modelos gráficos dispersos y heterogéneos, como los que corre su hardware. Hoy la usamos de verdad: comprobamos su exactitud y medimos su velocidad.

**EN:** Before having a chip, one must be able to program it. THRML is Extropic's library for simulating probabilistic computers on GPUs. It is built on JAX and serves as a scaffold for implementing block sampling algorithms on sparse, heterogeneous graphical models, like those its hardware runs. Today we use it for real: we check its exactness and measure its speed.

### [00:32.3] Factor graphs — `manim:S02`

**ES:** El punto de partida es un modelo basado en energía factorizado: la energía es una suma de factores, cada uno sobre unas pocas variables cercanas. Para muestrear se usa Gibbs: cada variable se actualiza según su distribución condicionada a sus vecinas. Como la condicional solo depende de los factores que tocan a esa variable, la actualización es local, justo lo que un chip puede hacer con cableado corto.

**EN:** The starting point is a factorized energy-based model: the energy is a sum of factors, each over a few nearby variables. Sampling uses Gibbs: each variable is updated according to its distribution conditioned on its neighbors. Since the conditional only depends on the factors touching that variable, the update is local, exactly what a chip can do with short wiring.

### [00:58.1] THRML's building blocks — `manim:S03`

**ES:** THRML organiza esto en piezas. Los nodos representan variables de distintos tipos: espines, categóricas, continuas. Los bloques agrupan nodos que no interactúan entre sí y pueden actualizarse a la vez, por ejemplo los dos colores de una rejilla. Los factores definen la energía, y los muestreadores condicionales dicen cómo actualizar cada tipo de nodo. Un programa de muestreo junta todo, y un calendario fija el calentamiento, el número de muestras y los barridos entre muestras.

**EN:** THRML organizes this into pieces. Nodes represent variables of different types: spins, categorical, continuous. Blocks group nodes that do not interact with each other and can be updated at once, for example the two colors of a grid. Factors define the energy, and conditional samplers say how to update each type of node. A sampling program puts everything together, and a schedule sets the warm-up, the number of samples and the sweeps between samples.

### [01:30.3] Is it exact? — `manim:S04`

**ES:** Lo comprobamos con una rejilla de cuatro por cuatro, dieciséis espines con acoplamientos y campos al azar, donde podemos enumerar los sesenta y cinco mil quinientos treinta y seis estados. Con veinte mil cadenas y dos colores, tras un barrido el error máximo en las magnetizaciones es cero coma cuatro; tras diez, cero coma cero cuatro; tras treinta, cero coma cero uno, el piso estadístico de las cadenas. El muestreador converge a la distribución correcta.

**EN:** We check it with a four-by-four grid, sixteen spins with random couplings and fields, where we can enumerate all sixty-five thousand five hundred thirty-six states. With twenty thousand chains and two colors, after one sweep the maximum error in the magnetizations is 0.4; after ten, 0.04; after thirty, 0.01, the statistical floor of the chains. The sampler converges to the correct distribution.

### [01:60.0] How fast is a GPU? — `manim:S05`

**ES:** Ahora la velocidad. Simulamos una rejilla de doscientos sesenta y dos mil espines, del tamaño de un chip Z1, en una GPU de consumo. Obtenemos entre cinco coma ocho y siete coma cinco giros por nanosegundo, según el número de cadenas. Una FPGA que cablea el problema logra unos sesenta. Y la especificación de Z1, doscientos sesenta y nueve mil pbits a cincuenta megahercios, implica unos trece mil quinientos, casi dos mil veces más que nuestra GPU.

**EN:** Now the speed. We simulate a grid of two hundred sixty-two thousand spins, the size of a Z1 chip, on a consumer GPU. We get between 5.8 and 7.5 flips per nanosecond, depending on the number of chains. An FPGA that hard-wires the problem achieves about sixty. And the Z1 specification, two hundred sixty-nine thousand pbits at fifty megahertz, implies about thirteen thousand five hundred, almost two thousand times more than our GPU.

### [02:31.0] What THRML is for — `manim:S06`

**ES:** THRML no pretende competir en velocidad con el chip. Sirve para diseñar y depurar algoritmos antes de tener hardware, para entrenar modelos basados en energía con divergencia contrastiva, y para validar que un programa muestrea lo que debe. Sus programas usan las mismas abstracciones que el hardware: bloques, condicionales locales y calendarios, de modo que lo que funciona en la simulación se puede trasladar al chip.

**EN:** THRML does not try to compete in speed with the chip. It is for designing and debugging algorithms before having hardware, for training energy-based models with contrastive divergence, and for validating that a program samples what it should. Its programs use the same abstractions as the hardware: blocks, local conditionals and schedules, so that what works in simulation can be carried over to the chip.

### [02:57.9] Applications — `slide`

**ES:** Usa THRML para prototipar muestreadores por bloques, entrenar modelos basados en energía con fases fijada y libre, validar primero contra enumeración exacta en grafos pequeños, y escalar con muchas cadenas y varios dispositivos.

**EN:** Use THRML to prototype block samplers, train energy-based models with clamped and free phases, validate first against exact enumeration on small graphs, and scale with many chains and several devices.

### [03:13.9] Common mistakes — `slide`

**ES:** Errores comunes: poner nodos que interactúan en el mismo bloque. Usar pocos barridos de calentamiento. Comparar giros por nanosegundo sin declarar tamaños. Y saltarse la comprobación exacta en un grafo pequeño.

**EN:** Common mistakes: putting interacting nodes in the same block. Using few warm-up sweeps. Comparing flips per nanosecond without declaring sizes. And skipping the exact check on a small graph.

### [03:28.5] Summary — `manim:S09`

**ES:** En resumen, THRML simula en GPU el muestreo por bloques que corre el hardware, con nodos, bloques, factores, condicionales y calendarios. Lo verificamos contra la enumeración exacta, con error en el piso estadístico tras treinta barridos. En velocidad, una GPU de consumo da unos siete giros por nanosegundo, frente a trece mil quinientos que implica Z1: la simulación es para diseñar, no para producir.

**EN:** In summary, THRML simulates on GPU the block sampling the hardware runs, with nodes, blocks, factors, conditionals and schedules. We verified it against exact enumeration, with error at the statistical floor after thirty sweeps. In speed, a consumer GPU gives about seven flips per nanosecond, against thirteen thousand five hundred implied by Z1: simulation is for designing, not for production.

### [03:56.9] Self-assessment — `slide`

**ES:** Para practicar: explica por qué los nodos del mismo color se actualizan en paralelo. Calcula el piso estadístico. Calcula los giros por nanosegundo de Z1. Y di qué especifica un calendario de muestreo.

**EN:** To practice: explain why same-color nodes are updated in parallel. Compute the statistical floor. Compute Z1's flips per nanosecond. And say what a sampling schedule specifies.

## Key equations
- $$\mathcal E(x) = \sum_{\psi\in S}\psi(x_{\psi}),\qquad P(x_i\mid x_{nb(i)}) \propto e^{-\mathcal E_i(x_i, x_{nb(i)})}$$ — Factorized EBM and local Gibbs conditional.
- $$\max_i\,|\hat m_i - m_i|\colon 0.40\ (1) \to 0.042\ (10) \to 0.009\ (30\ \text{sweeps})$$ — THRML vs exact enumeration, 4×4 Ising, 20 000 chains [S].
- $$269\,568\times 50\ \text{MHz} \approx 1.35\times10^{4}\ \text{flips/ns}\ \text{vs}\ 7.5\ (\text{GPU})$$ — Z1 specification vs measured consumer GPU.

## Summary
- THRML: JAX scaffold for block sampling on sparse heterogeneous PGMs.
- Nodes, blocks, factors, conditional samplers, programs, schedules.
- Exact check (4×4): error at the statistical floor by 30 sweeps [S].
- 262k spins: 5.8–7.5 flips/ns (RTX 2070S) vs ~60 FPGA vs ~13 500 Z1 spec.

## Further reading
- Extropic, THRML documentation and examples (thrml/ in this repository), 2025.
- Extropic, An efficient probabilistic hardware architecture for diffusion-like models, arXiv:2510.23972 (2025).
- N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, arXiv:2303.10728 (2023).
