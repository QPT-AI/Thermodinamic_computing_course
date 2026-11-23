# Lesson 5.3 — Extropic's TSUs

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe the thermodynamic sampling unit (TSU) and its primitives: pbit, pdit, pmode, pmog.
- Place the X0, XTR-0 and Z1 systems; compute rates and energy bounds from Z1's stated figures.
- Understand the host loop CPU + FPGA + chip and per-pbit calibration.

## Prerequisites
- Lessons 4.3, 4.5: chromatic Gibbs and pbits.
- Lesson 5.2: physical and digital pbits.

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** Extropic llama unidad de muestreo termodinámico, o TSU, a un chip que ejecuta muestreo de Gibbs en hardware sobre un grafo de variables aleatorias. Su programa es una energía, y su salida son muestras. En esta lección recorremos sus piezas: las primitivas aleatorias, los chips de prueba X0 y XTR-0, y el chip Z1, con más de doscientos sesenta mil pbits.

**EN:** Extropic calls a thermodynamic sampling unit, or TSU, a chip that runs Gibbs sampling in hardware over a graph of random variables. Its program is an energy, and its output is samples. In this lesson we go through its pieces: the random primitives, the X0 and XTR-0 test chips, and the Z1 chip, with more than two hundred sixty thousand pbits.

### [00:29.9] Four primitives — `manim:S02`

**ES:** El TSU no solo tiene pbits. Un pbit muestrea un bit con probabilidad sigmoide. Un pdit muestrea una variable categórica de varios valores, con probabilidades softmax. Un pmode muestrea una variable continua gaussiana, y un pmog, una mezcla de gaussianas. Con estas cuatro piezas se construyen modelos discretos, continuos e híbridos, siempre con condicionales locales.

**EN:** The TSU does not only have pbits. A pbit samples a bit with sigmoid probability. A pdit samples a categorical variable with several values, with softmax probabilities. A pmode samples a continuous Gaussian variable, and a pmog, a mixture of Gaussians. With these four pieces one builds discrete, continuous and hybrid models, always with local conditionals.

### [00:55.6] X0 and XTR-0 — `manim:S03`

**ES:** Los primeros chips, X0 y XTR-0, sirvieron para validar las primitivas. Usan muestreadores CMOS en régimen subumbral, donde el ruido de los transistores es grande y útil. Como cada dispositivo es algo distinto, cada pbit se calibra: según el pensum, con optimización bayesiana se alcanza un error de probabilidad de alrededor del cinco por ciento. El sistema completo es un bucle: una CPU define el problema, un FPGA traduce y lee, y el chip muestrea.

**EN:** The first chips, X0 and XTR-0, served to validate the primitives. They use CMOS samplers in the subthreshold regime, where transistor noise is large and useful. Since each device is somewhat different, each pbit is calibrated: according to the syllabus, Bayesian optimization reaches a probability error of about five percent. The complete system is a loop: a CPU defines the problem, an FPGA translates and reads, and the chip samples.

### [01:27.3] The Z1 chip — `manim:S04`

**ES:** El chip Z1 tiene doscientos sesenta y nueve mil quinientos sesenta y ocho pbits, cada uno con dieciséis acoplamientos a sus vecinos. Funciona a más de cincuenta megahercios y consume menos de un vatio. Eso da más de diez billones de actualizaciones por segundo, y como máximo setenta y cuatro femtojulios por actualización. Se ofrece en tarjetas M.2 y PCIe, y en sistemas de clúster que apuntan a mil millones de pbits.

**EN:** The Z1 chip has two hundred sixty-nine thousand five hundred sixty-eight pbits, each with sixteen couplings to its neighbors. It runs at more than fifty megahertz and consumes under one watt. That gives more than ten trillion updates per second, and at most seventy-four femtojoules per update. It comes in M.2 and PCIe cards, and in cluster systems aiming at a billion pbits.

### [01:54.8] Programming a TSU — `manim:S05`

**ES:** Programar un TSU es escribir una energía sobre su grafo fijo. Se cargan los acoplamientos y los campos en los registros de cada pbit, se fija una temperatura efectiva, y se deja correr Gibbs cromático. Algunas variables se pueden fijar como evidencia, igual que en la lógica invertible. Cada cierto número de barridos se leen muestras. Si el modelo no cabe en un grafo de grado dieciséis, hay que embeberlo, como veremos en la lección cinco punto siete.

**EN:** Programming a TSU means writing an energy over its fixed graph. The couplings and fields are loaded into each pbit's registers, an effective temperature is set, and chromatic Gibbs runs. Some variables can be clamped as evidence, just like in invertible logic. Every so many sweeps, samples are read out. If the model does not fit in a degree-sixteen graph, it has to be embedded, as we will see in lesson 5.7.

### [02:23.3] Numerical example — `manim:S06`

**ES:** Hagamos cuentas con las cifras declaradas. Doscientos sesenta y nueve mil pbits a cincuenta megahercios son unos uno coma tres por diez a la trece actualizaciones por segundo. Con un vatio, la energía por actualización es como máximo 7,4 × 10⁻¹⁴ J. Comparado con el límite de Landauer, es unos veintiséis millones de veces más, pero comparado con una actualización digital estimada de setenta picojulios, es unas mil veces menos.

**EN:** Let's run the numbers with the stated figures. Two hundred sixty-nine thousand pbits at fifty megahertz are about 1.3 × 10¹³ updates per second. With one watt, the energy per update is at most 7.4 × 10⁻¹⁴ J. Compared with the Landauer limit, that is about twenty-six million times more, but compared with an estimated seventy-picojoule digital update, it is about a thousand times less.

### [02:53.3] Applications — `slide`

**ES:** En el curso usaremos THRML para simular programas de TSU en GPU, construiremos modelos de eliminación de ruido que el TSU muestrea en la unidad nueve, y veremos la arquitectura Z1T para modelos de lenguaje en la unidad diez. En el laboratorio ocho construirás un grafo de grado dieciséis, lo colorearás y estimarás las actualizaciones por segundo.

**EN:** In the course we will use THRML to simulate TSU programs on GPU, build denoising models sampled by the TSU in unit nine, and see the Z1T architecture for language models in unit ten. In lab eight you will build a degree-sixteen graph, color it and estimate updates per second.

### [03:17.0] Common mistakes — `slide`

**ES:** Cuidado: la cifra de setenta y cuatro femtojulios es una cota derivada de la potencia y la frecuencia declaradas, no una medición. El grafo del Z1 es fijo, de grado dieciséis. La calibración deja un error del orden del cinco por ciento. Y la energía por actualización no incluye la entrada, la salida ni el anfitrión.

**EN:** Careful: the seventy-four-femtojoule figure is a bound derived from the stated power and frequency, not a measurement. The Z1 graph is fixed, of degree sixteen. Calibration leaves an error on the order of five percent. And the energy per update does not include input, output or the host.

### [03:38.1] Summary — `manim:S09`

**ES:** En resumen: un TSU ejecuta Gibbs cromático en hardware sobre un grafo fijo, con cuatro primitivas: pbit, pdit, pmode y pmog. X0 y XTR-0 validaron los muestreadores subumbral y su calibración. Z1 escala a doscientos sesenta y nueve mil pbits de grado dieciséis, con una cota de setenta y cuatro femtojulios por actualización.

**EN:** In summary: a TSU runs chromatic Gibbs in hardware over a fixed graph, with four primitives: pbit, pdit, pmode and pmog. X0 and XTR-0 validated the subthreshold samplers and their calibration. Z1 scales to two hundred sixty-nine thousand degree-sixteen pbits, with a bound of seventy-four femtojoules per update.

### [04:02.9] Self-assessment — `slide`

**ES:** Para practicar: calcula las actualizaciones por segundo del Z1. Elige la primitiva para una etiqueta de diez clases y para la intensidad de un píxel. Calcula los barridos por segundo con cuatro colores. Y explica por qué cada pbit necesita su propia calibración.

**EN:** To practice: compute Z1's updates per second. Choose the primitive for a ten-class label and for a pixel intensity. Compute the sweeps per second with four colors. And explain why each pbit needs its own calibration.

## Key equations
- $$R = 269\,568 \times 50\ \text{MHz} \approx 1.35\times10^{13}\ \text{updates/s}$$ — Z1 update rate from its stated figures.
- $$e_{\text{update}} \le \frac{1\ \text{W}}{R} \approx 7.4\times10^{-14}\ \text{J}$$ — Upper bound on the energy per update.
- $$p(x_i = k\mid\cdot) = \frac{e^{\beta u_{ik}}}{\sum_{k'} e^{\beta u_{ik'}}}\ (\text{pdit}),\qquad x_i\mid\cdot \sim \mathcal N(\mu_i, \sigma_i^2)\ (\text{pmode})$$ — Conditionals of the categorical and Gaussian primitives.

## Summary
- TSU = hardware chromatic Gibbs over a fixed graph; program = energy.
- Primitives: pbit, pdit (softmax), pmode (Gaussian), pmog (mixture).
- X0/XTR-0: subthreshold CMOS samplers; per-pbit calibration (~5 %).
- Z1: 269,568 pbits, degree 16, >50 MHz, <1 W ⇒ ≤ 7.4 × 10⁻¹⁴ J/update.

## Further reading
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- Video V1: From One to One Billion (Torx, Thermalizers, Z1) — Extropic.
