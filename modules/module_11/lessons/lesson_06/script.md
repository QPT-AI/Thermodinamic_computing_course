# Lesson 11.6 — Open problems

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Summarize the open problems of thermodynamic AI with the numbers measured in this course.
- Locate where the energy goes, from the vocabulary head down to the thermal scale kT ln 2.
- State what evidence would convince you that a thermodynamic advantage is real, and discuss energy policy.

## Prerequisites
- Units 9–11.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** Llegamos al final del curso con una pregunta guía, qué te convencería de que una ventaja termodinámica es real. A lo largo de las unidades medimos muchas cosas, y cada medida dejó un problema abierto. Hoy los reunimos en cinco frentes: conectividad y calidad, el pegamento digital, la precisión, la teoría, y el impacto energético de la inteligencia artificial en la sociedad.

**EN:** We reach the end of the course with a guiding question, what would convince you that a thermodynamic advantage is real. Across the units we measured many things, and each measurement left an open problem. Today we gather them on five fronts: connectivity and quality, the digital glue, precision, theory, and the energy impact of artificial intelligence on society.

### [00:29.0] Connectivity versus quality — `manim:S02`

**ES:** Primer frente. Los chips tienen grado fijo y los modelos densos funcionan mejor. En nuestro experimento iso-FLOP hubo un grado óptimo intermedio, pero en el caso de estudio la dispersión de grado cuatro costó un tercio de bit por carácter, y Z1T necesitó del orden de diez veces más cómputo de entrenamiento para igualar a GPT-2 small. Abierto: cómo escalan estas pérdidas con el tamaño, y qué arquitecturas las reducen.

**EN:** First front. Chips have fixed degree and dense models work better. In our iso-FLOP experiment there was an optimal intermediate degree, but in the case study degree-four sparsity cost a third of a bit per character, and Z1T needed on the order of ten times more training compute to match GPT-2 small. Open: how these losses scale with size, and which architectures reduce them.

### [00:56.8] Removing the digital glue — `manim:S03`

**ES:** Segundo frente: el pegamento digital. Recorramos la escalera de energía de un token de Z1T. La cabeza de vocabulario cuesta unos ciento treinta y seis microjulios. El trabajo de la FPGA, doscientos ochenta y seis nanojulios, cuatrocientas setenta y siete veces menos. El muestreo en el chip, ocho coma siete cuatro nanojulios, treinta y tres veces menos. Cada peldaño es un problema abierto: la ventaja del sustrato solo aparece si se eliminan los de arriba.

**EN:** Second front: the digital glue. Let's walk down the energy ladder of a Z1T token. The vocabulary head costs about one hundred thirty-six microjoules. The FPGA work, two hundred eighty-six nanojoules, four hundred seventy-seven times less. Sampling on the chip, 8.74 nanojoules, thirty-three times less. Each step is an open problem: the substrate's advantage only appears if the ones above are removed.

### [01:27.7] Precision and physics — `manim:S04`

**ES:** Tercer frente: la precisión. Cada bit efectivo cuesta cuatro veces más muestras; el ruido de las entradas sesga la salida de las unidades tangente; y los pbits reales tienen un error de calibración de alrededor del cinco por ciento. Abierto: cuántos bits necesita de verdad un modelo de lenguaje, si el entrenamiento puede absorber el ruido y la deriva del dispositivo, y cómo calibrar millones de pbits sin pagar con energía digital.

**EN:** Third front: precision. Each effective bit costs four times more samples; input noise biases the output of tangent units; and real pbits have a calibration error of about five percent. Open: how many bits a language model really needs, whether training can absorb the device's noise and drift, and how to calibrate millions of pbits without paying in digital energy.

### [01:55.5] Theory — `manim:S05`

**ES:** Cuarto frente: la teoría. Falta una teoría de la complejidad termodinámica: cuánto tiempo de mezcla y cuánta energía exige cada distribución, y cómo se compara con el cómputo digital. Sabemos que la expresividad se paga en mezcla, y que el error de compilación se acumula con la profundidad. Y queda mucho margen físico: un muestreo de Z1 cuesta unos trece femtojulios, cuatro millones y medio de veces la escala térmica k T ln 2 a temperatura ambiente.

**EN:** Fourth front: theory. A theory of thermodynamic complexity is missing: how much mixing time and how much energy each distribution demands, and how it compares with digital computing. We know expressivity is paid for in mixing, and that compilation error accumulates with depth. And there is a lot of physical headroom: a Z1 sample costs about thirteen femtojoules, four and a half million times the thermal scale k T ln 2 at room temperature.

### [02:25.3] Energy policy and society — `manim:S06`

**ES:** Quinto frente: la sociedad. La Agencia Internacional de la Energía estimó que los centros de datos consumieron unos cuatrocientos quince teravatios hora en dos mil veinticuatro, alrededor del uno coma cinco por ciento de la electricidad mundial, y proyectó cerca de novecientos cuarenta y cinco para dos mil treinta. Un hardware más eficiente ayuda, pero la eficiencia también puede aumentar el uso total, el efecto rebote. Abierto: cómo medir y reportar la energía de la inteligencia artificial de forma honesta, y qué políticas acompañan a la tecnología.

**EN:** Fifth front: society. The International Energy Agency estimated that data centers consumed about four hundred fifteen terawatt hours in twenty twenty-four, around 1.5 percent of world electricity, and projected close to nine hundred forty-five by twenty thirty. More efficient hardware helps, but efficiency can also increase total use, the rebound effect. Open: how to measure and report the energy of artificial intelligence honestly, and which policies accompany the technology.

### [02:59.6] Capstone directions — `slide`

**ES:** Para tu proyecto final, hay espacio en cuatro direcciones: arquitecturas con menor impuesto de dispersión, sacar la cabeza y el pegamento de lo digital, entrenamiento robusto al ruido y la deriva, y bancos de prueba con contabilidad energética completa y etiquetada.

**EN:** For your final project, there is room in four directions: architectures with a smaller sparsity tax, moving the head and the glue out of digital, training robust to noise and drift, and benchmarks with complete, labeled energy accounting.

### [03:16.8] What would convince you — `slide`

**ES:** Una ventaja real exige medición en un chip físico de principio a fin, el mismo alcance en ambos lados, la misma calidad con lote y utilización declarados, y reproducción independiente con etiquetas de evidencia en cada número.

**EN:** A real advantage requires measurement on a physical chip end to end, the same scope on both sides, the same quality with declared batch and utilization, and independent reproduction with evidence labels on every number.

### [03:31.3] Summary — `manim:S09`

**ES:** En resumen, los problemas abiertos son cinco: el precio de la conectividad, el pegamento digital que domina la energía, la precisión y la física del dispositivo, una teoría de la complejidad termodinámica, y el impacto social de la energía. La escalera va de microjulios a femtojulios: hay margen enorme, y por eso vale la pena medirlo bien. Gracias por llegar hasta aquí.

**EN:** In summary, there are five open problems: the price of connectivity, the digital glue that dominates energy, precision and device physics, a theory of thermodynamic complexity, and the social impact of energy. The ladder goes from microjoules to femtojoules: there is enormous headroom, and that is why it is worth measuring it well. Thank you for making it this far.

### [03:56.5] Self-assessment — `slide`

**ES:** Para practicar: calcula el factor entre la cabeza y la FPGA. Calcula la escala térmica y su razón con trece femtojulios. Recuerda la fracción de electricidad de los centros de datos. Y enumera cuatro requisitos de evidencia convincente.

**EN:** To practice: compute the factor between the head and the FPGA. Compute the thermal scale and its ratio to thirteen femtojoules. Recall the electricity share of data centers. And list four requirements of convincing evidence.

## Key equations
- $$136\ \mu\text{J}\ \xrightarrow{\div 477}\ 286\ \text{nJ}\ \xrightarrow{\div 33}\ 8.74\ \text{nJ}\ \xrightarrow{\div 4.5\times10^{6}}\ \approx 1.9\ \text{fJ}$$ — Z1T token: head → FPGA glue → Z1 sampling → kT ln 2 per sample.
- $$k_BT\ln 2 \approx 2.87\times10^{-21}\ \text{J}\ (300\ \text{K})\quad\text{vs}\quad 1.3\times10^{-14}\ \text{J per Z1 sample}$$ — Thermal scale vs reported sampling energy.
- $$\approx 415\ \text{TWh}\ (2024,\ \approx 1.5\%)\ \to\ \approx 945\ \text{TWh}\ (2030)$$ — Data-center electricity, IEA Energy and AI (2025) [P].

## Summary
- Connectivity: sparsity tax (~10× training compute; +0.34 bits/char at k = 4).
- Glue: head ≫ FPGA ≫ sampling; remove the upper rungs.
- Precision: 4^b samples per bit, noise bias, ~5% calibration.
- Theory and society: kT ln 2 headroom ×4.5·10⁶; data centers ≈ 415 → 945 TWh.

## Further reading
- International Energy Agency, Energy and AI, Paris (2025).
- Extropic, Z1T, extropic.ai/writing/z1t (September 2026).
- R. Landauer, Irreversibility and heat generation in the computing process, IBM J. Res. Dev. 5, 183 (1961).
