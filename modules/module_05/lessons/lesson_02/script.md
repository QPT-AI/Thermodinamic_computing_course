# Lesson 5.2 — p-bits: MTJ and CMOS

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain how a low-barrier magnetic tunnel junction becomes a pbit: retention $\tau = \tau_0 e^{\Delta/k_BT}$ with $\Delta \sim k_BT$.
- Describe digital (CMOS/FPGA) pbits: RNG, lookup table for tanh, comparator.
- Place p-computers and sparse Ising machines: graph coloring, parallel updates, flips per second.

## Prerequisites
- Lesson 4.5: the pbit and its hardware rule.
- Lesson 3.7: Arrhenius retention.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** En la unidad cuatro el pbit fue una abstracción: un espín que vale más uno con probabilidad sigmoide. Ahora veamos cómo se construye. Hay dos caminos. Uno es físico: un imán diminuto tan inestable que el calor lo voltea solo. El otro es digital: un generador aleatorio, una tabla y un comparador en un FPGA. Ambos llevan a los p-computadores.

**EN:** In unit four the pbit was an abstraction: a spin that equals plus one with sigmoid probability. Now let's see how it is built. There are two paths. One is physical: a magnet so tiny and unstable that heat flips it on its own. The other is digital: a random generator, a table and a comparator on an FPGA. Both lead to p-computers.

### [00:30.0] Magnetic tunnel junction — `manim:S02`

**ES:** Una unión túnel magnética tiene dos capas magnéticas separadas por un aislante. Si las magnetizaciones son paralelas, la resistencia es baja; si son antiparalelas, alta. En una memoria magnética, la capa libre tiene una barrera de unas cuarenta k_B T para que no se voltee en años. En un pbit hacemos lo contrario: una capa libre con barrera del orden de k_B T, que el ruido térmico voltea en nanosegundos. Leemos la resistencia, y su voltaje es un bit aleatorio.

**EN:** A magnetic tunnel junction has two magnetic layers separated by an insulator. If the magnetizations are parallel, the resistance is low; if antiparallel, high. In a magnetic memory, the free layer has a barrier of about forty k_B T so that it does not flip for years. In a pbit we do the opposite: a free layer with a barrier on the order of k_B T, which thermal noise flips within nanoseconds. We read the resistance, and its voltage is a random bit.

### [01:01.4] Retention and speed — `manim:S03`

**ES:** El tiempo medio entre volteos sigue la ley de Néel y Arrhenius, τ = τ₀ e^(Δ/k_B T), con τ₀ del orden de un nanosegundo. Con una barrera de cuarenta k_B T, el imán se queda quieto unos siete años: es una memoria. Con veinte, medio segundo. Con una sola k_B T, menos de tres nanosegundos: es un pbit. El mismo dispositivo pasa de memoria a generador aleatorio cambiando solo la altura de la barrera.

**EN:** The mean time between flips follows the Néel–Arrhenius law, τ = τ₀ e^(Δ/k_B T), with τ₀ on the order of a nanosecond. With a barrier of forty k_B T, the magnet stays put for about seven years: it is a memory. With twenty, half a second. With a single k_B T, less than three nanoseconds: it is a pbit. The same device goes from memory to random generator just by changing the barrier height.

### [01:31.1] Tuning the probability — `manim:S04`

**ES:** Para que sea un pbit, la entrada debe controlar la probabilidad. Una corriente o un voltaje inclina el pozo doble: favorece un estado sobre el otro. La fracción de tiempo en el estado alto sigue una sigmoide de la entrada. En el circuito típico, la unión se conecta a un transistor y a un inversor: la entrada es el voltaje de compuerta y la salida es un bit que fluctúa con la probabilidad deseada. Las tasas de salto, y por lo tanto la velocidad, se mantienen en nanosegundos.

**EN:** To be a pbit, the input must control the probability. A current or voltage tilts the double well: it favors one state over the other. The fraction of time in the high state follows a sigmoid of the input. In the typical circuit, the junction is connected to a transistor and an inverter: the input is the gate voltage and the output is a bit that fluctuates with the desired probability. The jump rates, and therefore the speed, stay in the nanoseconds.

### [02:01.5] CMOS and FPGA pbits — `manim:S05`

**ES:** El camino digital emula el mismo comportamiento con circuitos estándar. Un generador pseudoaleatorio produce un número, una tabla guarda la tangente hiperbólica, y un comparador decide el signo, exactamente la regla que vimos en la lección cuatro punto cinco. No ahorra la energía de la aleatoriedad, pero se puede construir hoy en un FPGA, con cientos de miles de pbits y la conectividad que queramos. Es la plataforma con la que se desarrollaron los p-computadores.

**EN:** The digital path emulates the same behavior with standard circuits. A pseudorandom generator produces a number, a table stores the hyperbolic tangent, and a comparator decides the sign, exactly the rule we saw in lesson 4.5. It does not save the energy of randomness, but it can be built today on an FPGA, with hundreds of thousands of pbits and whatever connectivity we want. It is the platform on which p-computers were developed.

### [02:31.0] Sparse Ising machines — `manim:S06`

**ES:** Un p-computador conecta muchos pbits según un grafo y los actualiza con Gibbs cromático. La clave de su velocidad es la dispersión: si cada pbit tiene pocos vecinos, el grafo se colorea con pocos colores, y en cada fase de reloj se actualizan en paralelo todos los pbits de un color. Las máquinas de Ising dispersas en FPGA alcanzan miles de millones de volteos por segundo, varios órdenes de magnitud más que una CPU recorriendo los espines uno por uno.

**EN:** A p-computer connects many pbits according to a graph and updates them with chromatic Gibbs. The key to its speed is sparsity: if each pbit has few neighbors, the graph is colored with few colors, and in each clock phase all pbits of one color update in parallel. Sparse Ising machines on FPGA reach billions of flips per second, several orders of magnitude more than a CPU going through the spins one by one.

### [03:01.4] Applications — `slide`

**ES:** Las uniones túnel estocásticas dan volteos en nanosegundos y probabilidad ajustable, aunque cada dispositivo es algo distinto y hay que calibrarlos. Los p-computadores en FPGA ya resuelven problemas de optimización, de muestreo y de lógica invertible. En el laboratorio ocho simularás circuitos de pbits y medirás su curva de transferencia.

**EN:** Stochastic tunnel junctions give nanosecond flips and tunable probability, although each device is somewhat different and they must be calibrated. FPGA p-computers already solve optimization, sampling and invertible-logic problems. In lab eight you will simulate pbit circuits and measure their transfer curve.

### [03:24.2] Common mistakes — `slide`

**ES:** Errores comunes: usar una unión de memoria, que nunca se voltea. Ignorar la variabilidad entre dispositivos. Actualizar vecinos en la misma fase. Y contar volteos por segundo sin comprobar que la distribución muestreada es la correcta.

**EN:** Common mistakes: using a memory junction, which never flips. Ignoring device-to-device variability. Updating neighbors in the same phase. And counting flips per second without checking that the sampled distribution is correct.

### [03:39.8] Summary — `manim:S09`

**ES:** En resumen: una unión túnel magnética con barrera del orden de k_B T es un pbit físico que fluctúa en nanosegundos, y una entrada que inclina su pozo ajusta la probabilidad. Un pbit digital combina generador, tabla y comparador. Conectados en grafos dispersos y coloreados, forman p-computadores rápidos.

**EN:** In summary: a magnetic tunnel junction with a barrier on the order of k_B T is a physical pbit that fluctuates within nanoseconds, and an input that tilts its well tunes the probability. A digital pbit combines a generator, a table and a comparator. Connected in sparse, colored graphs, they form fast p-computers.

### [04:00.8] Self-assessment — `slide`

**ES:** Para practicar: calcula la barrera para un tiempo de volteo dado. Compara las barreras de un pbit y de una memoria. Cuenta los colores de una red cuadrada. Y explica en qué gasta energía un pbit digital que uno magnético no.

**EN:** To practice: compute the barrier for a given flip time. Compare the barriers of a pbit and a memory. Count the colors of a square lattice. And explain what a digital pbit spends energy on that a magnetic one does not.

## Key equations
- $$\tau = \tau_0\,e^{\Delta/k_BT},\qquad \tau_0 \sim 1\ \text{ns}$$ — Néel–Arrhenius mean flip time of a nanomagnet with barrier $\Delta$.
- $$\Delta = 40\,k_BT \Rightarrow \tau \approx 7\ \text{years};\qquad \Delta = k_BT \Rightarrow \tau \approx 2.7\ \text{ns}$$ — Memory vs pbit regimes of the same device.
- $$s = \mathrm{sgn}\big(\mathrm{LUT}_{\tanh}(u) - \mathrm{RNG}\big)$$ — Digital (CMOS/FPGA) pbit.

## Summary
- Stochastic MTJ: $\Delta \sim k_BT$, ns flips; tilt tunes a sigmoid probability.
- Same device: memory at $\Delta \approx 40\,k_BT$, pbit at $\Delta \sim k_BT$.
- Digital pbit: RNG + tanh LUT + comparator (FPGA).
- p-computers: sparse graphs, coloring, parallel updates.

## Further reading
- [17] K. Y. Camsari, B. M. Sutton and S. Datta, p-bits for probabilistic spin logic, Appl. Phys. Rev. 6, 011305 (2019).
- [18] J. Kaiser and S. Datta, Probabilistic computing with p-bits, Appl. Phys. Lett. 119, 150503 (2021).
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, Nat. Electron. 5, 460 (2022).
