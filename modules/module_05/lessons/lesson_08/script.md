# Lesson 5.8 — Energy accounting in heterogeneous systems

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Split the energy of a TSU + GPU/XPU + FPGA system into fabric, I/O and digital glue.
- Build an explicit cost model for one sample and find the dominant term.
- Label every energy number as measured, simulated, projected or estimated.

## Prerequisites
- Lesson 5.3: Z1 specifications and the energy bound per update.
- Lesson 5.7: hardware abstractions.

## Narrated script

### [00:06.0] Introduction — `manim:S01`

**ES:** En la lección cinco punto tres calculamos que el Z1 gasta como mucho setenta y cuatro femtojulios por actualización. Pero un chip nunca trabaja solo: alguien tiene que enviarle los parámetros, leer sus muestras y hacer el cómputo digital que lo rodea. La energía del sistema completo puede ser muy distinta de la del chip. Hoy aprendemos a contarla.

**EN:** In lesson 5.3 we computed that the Z1 spends at most seventy-four femtojoules per update. But a chip never works alone: someone has to send it the parameters, read its samples and do the digital computation around it. The energy of the full system can be very different from that of the chip. Today we learn to count it.

### [00:27.8] Three buckets — `manim:S02`

**ES:** Dividimos la energía en tres partes. El tejido: las actualizaciones de los pbits dentro del chip. La entrada y salida: los bits que cruzan la frontera del chip, como sesgos que entran y estados que salen. Y el pegamento digital: el cómputo en la CPU, la GPU o la FPGA que prepara los sesgos, controla el muestreo y procesa las muestras. La energía total es la suma de las tres.

**EN:** We split the energy into three parts. The fabric: the pbit updates inside the chip. Input and output: the bits that cross the chip boundary, such as biases going in and states coming out. And the digital glue: the computation on the CPU, GPU or FPGA that prepares the biases, controls sampling and processes the samples. The total energy is the sum of the three.

### [00:53.6] Reference costs — `manim:S03`

**ES:** Necesitamos costos de referencia, y debemos decir de dónde salen. Según las estimaciones de Horowitz para un proceso de cuarenta y cinco nanómetros, una multiplicación en coma flotante de treinta y dos bits cuesta tres coma siete picojulios, una suma cero coma nueve, y una multiplicación entera de ocho bits apenas cero coma dos. Leer treinta y dos bits de la memoria DRAM cuesta unos seiscientos cuarenta picojulios: mover datos cuesta mucho más que operar con ellos. Para la comunicación fuera del chip supondremos diez picojulios por bit, una estimación.

**EN:** We need reference costs, and we must say where they come from. According to Horowitz's estimates for a forty-five nanometer process, a thirty-two-bit floating-point multiply costs 3.7 picojoules, an add 0.9, and an eight-bit integer multiply only 0.2. Reading thirty-two bits from DRAM costs about six hundred forty picojoules: moving data costs much more than operating on it. For off-chip communication we will assume ten picojoules per bit, an estimate.

### [01:29.6] One sample, counted — `manim:S04`

**ES:** Contemos una muestra en el Z1 con mil barridos. El tejido: doscientos sesenta y nueve mil pbits por mil barridos por setenta y cuatro femtojulios, unos veinte microjulios. La entrada y salida: ocho bits de sesgo que entran y un bit de estado que sale por pbit, a diez picojulios por bit, unos veinticuatro microjulios. El pegamento: si una red digital calcula cada sesgo con cien multiplicaciones y sumas en coma flotante, son ciento veinticuatro microjulios. El total es de ciento sesenta y ocho, y el tejido es apenas el doce por ciento.

**EN:** Let's count one sample on the Z1 with a thousand sweeps. The fabric: two hundred sixty-nine thousand pbits times a thousand sweeps times seventy-four femtojoules, about twenty microjoules. Input and output: eight bias bits going in and one state bit coming out per pbit, at ten picojoules per bit, about twenty-four microjoules. The glue: if a digital network computes each bias with a hundred floating-point multiply-adds, that is one hundred twenty-four microjoules. The total is one hundred sixty-eight, and the fabric is only twelve percent.

### [02:06.5] Reducing the overhead — `manim:S05`

**ES:** ¿Cómo se reduce lo que no es tejido? Primero, con pegamento de baja precisión: con aritmética entera de ocho bits, el pegamento baja a seis microjulios, y el tejido pasa a ser el cuarenta por ciento del total. Segundo, amortizando la entrada y salida: con más barridos por lectura, el tejido iguala a la entrada y salida alrededor de mil doscientos barridos. Tercero, leyendo resúmenes en lugar de estados completos. Y finalmente, el objetivo de largo plazo: eliminar el pegamento digital con más funciones dentro del chip.

**EN:** How do we reduce what is not fabric? First, with low-precision glue: with eight-bit integer arithmetic, the glue drops to six microjoules, and the fabric becomes forty percent of the total. Second, by amortizing input and output: with more sweeps per readout, the fabric equals input and output at around twelve hundred sweeps. Third, by reading summaries instead of full states. And finally, the long-term goal: removing the digital glue with more functions inside the chip.

### [02:40.1] Labeling the evidence — `manim:S06`

**ES:** Cada número de energía debe llevar una etiqueta. Medido, si salió de un instrumento sobre un dispositivo real. Simulado, si salió de un modelo físico. Proyectado, si extrapola un diseño que aún no existe. Y estimado, si es un cálculo de orden de magnitud como el de hoy. En este curso, los setenta y cuatro femtojulios son una cota derivada de especificaciones, los costos de Horowitz son estimaciones, y la comparación final es un estimado: nunca lo presentes como una medición.

**EN:** Every energy number must carry a label. Measured, if it came from an instrument on a real device. Simulated, if it came from a physical model. Projected, if it extrapolates a design that does not exist yet. And estimated, if it is an order-of-magnitude calculation like today's. In this course, the seventy-four femtojoules are a bound derived from specifications, Horowitz's costs are estimates, and the final comparison is an estimate: never present it as a measurement.

### [03:12.1] Applications — `slide`

**ES:** En la práctica, antes de cualquier afirmación se escribe la suma de los tres términos, se reporta la energía por muestra con el número de barridos y la precisión del pegamento, y se compara con una línea base digital en la misma tarea y con la misma calidad. En el proyecto final, cada cifra llevará su etiqueta.

**EN:** In practice, before any claim one writes the sum of the three terms, reports the energy per sample with the number of sweeps and the glue precision, and compares with a digital baseline on the same task and at the same quality. In the final project, every figure will carry its label.

### [03:31.3] Common mistakes — `slide`

**ES:** Errores comunes: citar la energía del tejido como si fuera la del sistema. Ignorar la red digital que calcula los sesgos. Comparar energías con calidades o tareas distintas. Y presentar una proyección o un estimado como si fuera una medición.

**EN:** Common mistakes: quoting the fabric energy as if it were the system's. Ignoring the digital network that computes the biases. Comparing energies at different qualities or tasks. And presenting a projection or an estimate as if it were a measurement.

### [03:47.8] Summary — `manim:S09`

**ES:** En resumen: la energía de un sistema heterogéneo es tejido más entrada y salida más pegamento digital. En nuestro ejemplo el tejido era solo el doce por ciento, y subía al cuarenta con pegamento de ocho bits. Cada número debe decir si es medido, simulado, proyectado o estimado.

**EN:** In summary: the energy of a heterogeneous system is fabric plus input and output plus digital glue. In our example the fabric was only twelve percent, rising to forty with eight-bit glue. Every number must say whether it is measured, simulated, projected or estimated.

### [04:07.2] Self-assessment — `slide`

**ES:** Para practicar: calcula la energía del tejido con diez mil barridos. Encuentra cuántos barridos igualan tejido y entrada y salida. Compara el pegamento con ocho bits enteros y con coma flotante. Y etiqueta correctamente los setenta y cuatro femtojulios.

**EN:** To practice: compute the fabric energy with ten thousand sweeps. Find how many sweeps make fabric equal to input and output. Compare the glue with eight-bit integers and with floating point. And correctly label the seventy-four femtojoules.

## Key equations
- $$E_{\text{total}} = \underbrace{N K e_{\text{upd}}}_{\text{fabric}} + \underbrace{N b\, e_{\text{bit}}}_{\text{I/O}} + \underbrace{N m\, e_{\text{MAC}}}_{\text{glue}}$$ — Per-sample cost model: $N$ pbits, $K$ sweeps, $b$ bits crossing per pbit, $m$ MACs per bias.
- $$K^\ast = \frac{b\, e_{\text{bit}}}{e_{\text{upd}}} \approx \frac{9 \cdot 10\ \text{pJ}}{74\ \text{fJ}} \approx 1.2\times10^3$$ — Sweeps at which fabric energy equals I/O energy [E].
- $$\text{fp32 MAC} \approx 4.6\ \text{pJ},\quad \text{int8 MAC} \approx 0.23\ \text{pJ},\quad \text{DRAM 32 b} \approx 640\ \text{pJ}$$ — Reference costs at 45 nm (Horowitz 2014) [E].

## Summary
- E_total = fabric + I/O + digital glue.
- Z1 example, 1000 sweeps: 20 + 24 + 124 µJ; fabric 12 % [E].
- int8 glue: fabric 40 %; amortize I/O past K* ≈ 1200 sweeps.
- Tag every number: [M] measured, [S] simulated, [P] projected, [E] estimated.

## Further reading
- M. Horowitz, Computing's energy problem (and what we can do about it), ISSCC 2014.
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, 2026.
