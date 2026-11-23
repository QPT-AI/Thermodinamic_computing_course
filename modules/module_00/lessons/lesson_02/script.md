# Lesson 0.2 — A map of computing paradigms

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Place the classical, thermodynamic, quantum, neuromorphic, analog and reversible paradigms by their computing primitive.
- Compare energy scales: signal energy versus $k_B T$ and versus $\hbar\omega$.
- Distinguish the three fluctuation regimes: suppressed, harnessed thermal, and quantum.

## Prerequisites
- Lesson 0.1: switching energy and the energy wall.
- Basic notions of probability and the exponential.

## Narrated script

### [00:05.0] Introduction — `manim:S01`

**ES:** Clásico, cuántico, neuromórfico, analógico, reversible, termodinámico. Hay muchas formas de computar, y cada una aprovecha la física de una manera distinta. En esta lección construiremos un mapa para ubicarlas. La pregunta que organiza el mapa es simple: ¿qué hace cada paradigma con las fluctuaciones?

**EN:** Classical, quantum, neuromorphic, analog, reversible, thermodynamic. There are many ways to compute, and each one exploits physics differently. In this lesson we will build a map to place them. The question that organizes the map is simple: what does each paradigm do with fluctuations?

### [00:25.7] Intuition — `manim:S02`

**ES:** Supón que necesitas lanzar una moneda justa un millón de veces. Un computador digital no puede lanzar monedas: las simula con un generador pseudoaleatorio, una larga cadena de operaciones deterministas. Un sistema físico pequeño, en cambio, ya está temblando por el calor. Una partícula en un pozo doble con una barrera baja salta sola de un lado a otro. Basta con mirarla para obtener bits aleatorios. El paradigma digital gasta energía para eliminar el ruido y luego más energía para fabricar azar. El paradigma termodinámico usa el ruido directamente.

**EN:** Suppose you need to flip a fair coin a million times. A digital computer cannot flip coins: it simulates them with a pseudorandom generator, a long chain of deterministic operations. A small physical system, by contrast, is already jiggling from heat. A particle in a double well with a low barrier hops from side to side on its own. Just looking at it gives random bits. The digital paradigm spends energy to remove noise and then more energy to manufacture randomness. The thermodynamic paradigm uses the noise directly.

### [01:01.9] Visual explanation — `manim:S03`

**ES:** La variable que decide todo es la altura de la barrera comparada con la energía térmica k_B T. La probabilidad de un salto espontáneo escala como e^(−E_b/k_B T). Con una barrera de una o dos veces k_B T, la partícula salta constantemente: tenemos un bit probabilístico. Si subimos la barrera, los saltos se vuelven raros. Con unas cuarenta veces k_B T, la probabilidad de error cae por debajo de una en diez mil billones por intento: tenemos un bit digital. El mismo dispositivo puede ser determinista o aleatorio según cuánta energía le pongamos a la barrera.

**EN:** The variable that decides everything is the barrier height compared with the thermal energy k_B T. The probability of a spontaneous hop scales as e^(−E_b/k_B T). With a barrier of one or two k_B T, the particle hops constantly: we have a probabilistic bit. If we raise the barrier, hops become rare. At about forty k_B T, the error probability falls below one in ten quadrillion per attempt: we have a digital bit. The same device can be deterministic or random depending on how much energy we put into the barrier.

### [01:40.7] Formal theory — `manim:S04`

**ES:** Podemos dibujar un mapa con dos cocientes adimensionales. En el eje horizontal, la energía de la señal dividida por k_B T. En el eje vertical, la energía de un cuanto, ħω, dividida por k_B T. Abajo a la derecha, con señales mucho mayores que el ruido térmico, vive el cómputo digital clásico: las fluctuaciones se suprimen. Abajo a la izquierda, con señales del orden de k_B T, vive el cómputo termodinámico: las fluctuaciones térmicas se aprovechan. Arriba, cuando el cuanto de energía supera a la energía térmica, dominan las fluctuaciones cuánticas: es el territorio del cómputo cuántico. Estos son los tres dominios de fluctuación.

**EN:** We can draw a map with two dimensionless ratios. On the horizontal axis, the signal energy divided by k_B T. On the vertical axis, the energy of a quantum, ħω, divided by k_B T. Bottom right, with signals much larger than thermal noise, lives classical digital computing: fluctuations are suppressed. Bottom left, with signals on the order of k_B T, lives thermodynamic computing: thermal fluctuations are harnessed. At the top, when the energy quantum exceeds the thermal energy, quantum fluctuations dominate: the territory of quantum computing. These are the three fluctuation regimes.

### [02:23.7] Numerical example — `manim:S05`

**ES:** Pongamos números. A trescientos kelvin, k_B T vale unos 4,14 × 10⁻²¹ J, o veintiséis milielectronvoltios. Un cúbit superconductor típico opera cerca de cinco gigahercios. Su cuanto, h f, dividido por k_B, equivale a una temperatura de solo cero coma veinticuatro kelvin. Para que el ruido térmico no destruya el estado cuántico, hay que enfriar muy por debajo de eso, a decenas de milikelvin. El cómputo termodinámico, en cambio, funciona a temperatura ambiente, porque el ruido es su materia prima.

**EN:** Let's put in numbers. At three hundred kelvin, k_B T is about 4.14 × 10⁻²¹ J, or twenty-six millielectronvolts. A typical superconducting qubit operates near five gigahertz. Its quantum, h f, divided by k_B, corresponds to a temperature of only 0.24 kelvin. For thermal noise not to destroy the quantum state, it must be cooled far below that, to tens of millikelvin. Thermodynamic computing, instead, works at room temperature, because noise is its raw material.

### [02:59.7] The six paradigms — `manim:S06`

**ES:** Ahora ubiquemos cada paradigma por su primitiva. El cómputo clásico ejecuta lógica booleana determinista. El analógico deja que magnitudes continuas, como voltajes y corrientes, resuelvan ecuaciones al evolucionar. El reversible usa compuertas que no borran información para acercarse al límite de Landauer. El neuromórfico imita al cerebro, con eventos esparcidos y memoria junto al cómputo. El cuántico manipula amplitudes con evoluciones unitarias y mide al final. Y el termodinámico deja que un sistema físico se relaje hacia una distribución de Boltzmann, y lee muestras de ella.

**EN:** Now let's place each paradigm by its primitive. Classical computing executes deterministic Boolean logic. Analog computing lets continuous quantities, like voltages and currents, solve equations as they evolve. Reversible computing uses gates that do not erase information to approach the Landauer limit. Neuromorphic computing mimics the brain, with sparse events and memory next to compute. Quantum computing manipulates amplitudes with unitary evolution and measures at the end. And thermodynamic computing lets a physical system relax toward a Boltzmann distribution, and reads samples from it.

### [03:37.6] Applications — `slide`

**ES:** Ningún paradigma gana en todo. El digital sigue siendo imbatible cuando necesitamos exactitud y control. El termodinámico apunta a tareas que ya son probabilísticas: muestrear de modelos basados en energía, generar con difusión, resolver sistemas lineales por equilibración. El cuántico brilla en problemas con estructura de interferencia, como la factorización. Y en la práctica los sistemas serán heterogéneos, combinando varios de estos paradigmas en un mismo computador.

**EN:** No paradigm wins at everything. Digital remains unbeatable when we need exactness and control. Thermodynamic targets tasks that are already probabilistic: sampling energy-based models, generating with diffusion, solving linear systems by equilibration. Quantum shines on problems with interference structure, such as factoring. And in practice systems will be heterogeneous, combining several of these paradigms in one computer.

### [04:08.4] Connections — `slide`

**ES:** Volveremos a este mapa muchas veces. En la unidad uno estudiaremos la termodinámica de la información. En la unidad cuatro veremos el pbit, la primitiva del cómputo termodinámico discreto. En la unidad cinco conoceremos el hardware real. Y en la unidad siete compararemos de frente un algoritmo de difusión con el algoritmo cuántico de Shor.

**EN:** We will come back to this map many times. In unit one we will study the thermodynamics of information. In unit four we will see the pbit, the primitive of discrete thermodynamic computing. In unit five we will meet real hardware. And in unit seven we will compare a diffusion algorithm head to head with Shor's quantum algorithm.

### [04:31.1] Common mistakes — `slide`

**ES:** Cuidado con cuatro confusiones. El cómputo termodinámico no es cuántico a temperatura ambiente: no hay superposición ni interferencia, solo fluctuaciones térmicas clásicas. Tampoco es lo mismo que el analógico, que puede ser completamente determinista. No es lo mismo que el reversible, que se ocupa de no borrar. Y el ruido no siempre es malo: cuando la tarea es muestrear, el ruido es justamente lo que necesitamos.

**EN:** Watch out for four confusions. Thermodynamic computing is not quantum at room temperature: there is no superposition or interference, only classical thermal fluctuations. Nor is it the same as analog, which can be completely deterministic. It is not the same as reversible computing, which is about not erasing. And noise is not always bad: when the task is sampling, noise is exactly what we need.

### [04:58.3] Summary — `manim:S10`

**ES:** En resumen: cada paradigma se define por su primitiva y por lo que hace con las fluctuaciones. El digital las suprime con barreras de decenas de k_B T. El termodinámico las aprovecha con barreras del orden de k_B T. El cuántico requiere que el cuanto de energía supere a la energía térmica. La pregunta del curso es cuándo aprovechar el ruido ahorra energía de verdad.

**EN:** In summary: each paradigm is defined by its primitive and by what it does with fluctuations. Digital suppresses them with barriers of tens of k_B T. Thermodynamic harnesses them with barriers on the order of k_B T. Quantum requires the energy quantum to exceed the thermal energy. The question of the course is when harnessing noise truly saves energy.

### [05:21.7] Self-assessment — `slide`

**ES:** Para practicar: calcula la barrera necesaria para una tasa de error de uno en mil millones. Encuentra la temperatura equivalente del cuanto de un oscilador de diez gigahercios. Clasifica tres sistemas en el mapa de paradigmas. Y explica por qué el muestreo es la tarea natural del cómputo termodinámico.

**EN:** To practice: compute the barrier needed for an error rate of one in a billion. Find the equivalent temperature of the quantum of a ten-gigahertz oscillator. Classify three systems on the paradigm map. And explain why sampling is the natural task of thermodynamic computing.

## Key equations
- $$P_{\text{hop}} \propto e^{-E_b/k_B T}$$ — Arrhenius/Kramers law: probability that thermal noise crosses a barrier $E_b$.
- $$k_B T \big|_{300\,\text{K}} \approx 4.14\times10^{-21}\,\text{J} \approx 25.9\,\text{meV}$$ — Thermal energy scale at room temperature.
- $$\hbar\omega \gg k_B T \iff T \ll h f / k_B$$ — Condition for quantum fluctuations to dominate over thermal ones.

## Summary
- Each paradigm is characterized by its primitive and by what it does with fluctuations.
- Digital: $E_b \gtrsim 40\,k_B T$ (fluctuations suppressed).
- Thermodynamic: $E_b \sim k_B T$ (thermal fluctuations harnessed, room temperature).
- Quantum: $\hbar\omega \gg k_B T$ (cryogenics, amplitude interference).

## Further reading
- [6] T. Conte et al., Thermodynamic Computing (CCC workshop report), 2019.
- [28] P. J. Coles et al., Thermodynamic AI and the fluctuation frontier, 2023.
- [4] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, 2010.
- Video V2: Thermodynamic AI and the Fluctuation Frontier — P. Coles.
