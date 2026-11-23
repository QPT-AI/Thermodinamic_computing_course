# Lesson 5.1 — Why digital hardware is inefficient for probabilistic AI

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Break down the energy of one Gibbs update on a digital processor: data movement, random number generation, arithmetic.
- Explain why sampling workloads are memory-bound and why noise margins cost energy.
- Estimate the gap between a digital update and a physical pbit update.

## Prerequisites
- Lesson 0.1: switching energy, data movement and the roofline model.
- Lessons 4.3 and 4.5: Gibbs sampling and pbits.

## Narrated script

### [00:07.2] Introduction — `manim:S01`

**ES:** Una GPU es una máquina extraordinaria para multiplicar matrices. Pero muestrear de un modelo probabilístico es otra cosa: muchas actualizaciones pequeñas, cada una con su número aleatorio, que leen a sus vecinos de la memoria. En esta lección desarmamos el costo de una actualización de Gibbs en hardware digital y vemos por qué un dispositivo físico ruidoso puede hacerla miles de veces más barata.

**EN:** A GPU is an extraordinary machine for multiplying matrices. But sampling from a probabilistic model is something else: many small updates, each with its own random number, that read their neighbors from memory. In this lesson we take apart the cost of one Gibbs update on digital hardware and see why a noisy physical device can make it thousands of times cheaper.

### [00:32.3] Anatomy of an update — `manim:S02`

**ES:** Una actualización de un espín con dieciséis vecinos necesita leer dieciséis estados y dieciséis acoplamientos, sumar el campo local, evaluar una sigmoide, generar un número aleatorio, comparar y escribir el resultado. La aritmética es mínima: unas treinta operaciones. Pero cada dato viaja desde la memoria, y en la tabla de la lección cero punto uno, leer una palabra de la memoria interna ya cuesta más que una suma, y leerla de la memoria externa, cientos de veces más.

**EN:** Updating a spin with sixteen neighbors requires reading sixteen states and sixteen couplings, summing the local field, evaluating a sigmoid, generating a random number, comparing and writing the result. The arithmetic is minimal: about thirty operations. But every datum travels from memory, and in the table from lesson 0.1, reading a word from on-chip memory already costs more than an addition, and from external memory, hundreds of times more.

### [01:03.3] Memory-bound sampling — `manim:S03`

**ES:** En el modelo roofline, la actualización de Gibbs hace del orden de una operación por cada byte leído. Está muy a la izquierda del codo: limitada por memoria. La GPU pasa la mayor parte del tiempo esperando datos, con sus unidades aritméticas ociosas. Y el grafo disperso de un modelo de Ising no se presta a reutilizar datos en caché como una multiplicación de matrices densa.

**EN:** In the roofline model, the Gibbs update performs on the order of one operation per byte read. It sits far to the left of the knee: memory-bound. The GPU spends most of its time waiting for data, with its arithmetic units idle. And the sparse graph of an Ising model does not lend itself to cache reuse like a dense matrix multiplication.

### [01:27.9] The cost of randomness — `manim:S04`

**ES:** Además, cada actualización necesita un número aleatorio. Un generador digital, como Philox o xorshift, fabrica bits pseudoaleatorios con varias multiplicaciones y desplazamientos por palabra. Es determinismo disfrazado de azar, y se paga con operaciones y con energía. Un dispositivo físico, en cambio, ya fluctúa: según el pensum, un generador de solo transistores basado en ruido de disparo produce un bit aleatorio con cientos de attojulios.

**EN:** In addition, every update needs a random number. A digital generator, like Philox or xorshift, manufactures pseudorandom bits with several multiplications and shifts per word. It is determinism disguised as chance, and it is paid for with operations and energy. A physical device, instead, already fluctuates: according to the syllabus, an all-transistor generator based on shot noise produces a random bit for hundreds of attojoules.

### [01:57.5] Noise margins — `manim:S05`

**ES:** El tercer costo es invisible: los márgenes de ruido. Cada bit digital se guarda con barreras de decenas de k_B T para que el ruido térmico nunca lo voltee, como vimos en la unidad uno. Para un muestreador eso es absurdo: gastamos energía en eliminar el ruido y luego más energía en fabricarlo de nuevo con el generador pseudoaleatorio. Un pbit trabaja con barreras del orden de k_B T y usa el ruido directamente.

**EN:** The third cost is invisible: noise margins. Each digital bit is stored with barriers of tens of k_B T so that thermal noise never flips it, as we saw in unit one. For a sampler that is absurd: we spend energy removing noise and then more energy manufacturing it again with the pseudorandom generator. A pbit works with barriers on the order of k_B T and uses the noise directly.

### [02:23.8] Numerical estimate — `manim:S06`

**ES:** Hagamos una estimación de orden de magnitud. Si una actualización lee unas doce palabras de memoria interna a cinco picojulios cada una, más unos pocos picojulios de aritmética y aleatoriedad, cuesta del orden de setenta picojulios. El chip Z1 declara menos de un vatio para doscientos sesenta y nueve mil pbits a cincuenta megahercios: como máximo setenta y cuatro femtojulios por actualización. La diferencia es de unas mil veces, y eso sin contar la memoria externa.

**EN:** Let's make an order-of-magnitude estimate. If an update reads about twelve words from on-chip memory at five picojoules each, plus a few picojoules of arithmetic and randomness, it costs on the order of seventy picojoules. The Z1 chip states under one watt for two hundred sixty-nine thousand pbits at fifty megahertz: at most seventy-four femtojoules per update. The difference is about a thousand times, and that is without counting external memory.

### [02:53.6] Applications — `slide`

**ES:** La lección para el diseño es clara: calcular donde viven los datos, guardando los acoplamientos junto a cada pbit; usar el ruido físico en lugar de generadores pseudoaleatorios; y leer resultados lo menos posible, porque la entrada y salida y el pegamento digital pueden dominar el presupuesto del sistema, como veremos en la lección cinco punto ocho.

**EN:** The design lesson is clear: compute where the data lives, storing the couplings next to each pbit; use physical noise instead of pseudorandom generators; and read out results as little as possible, because input, output and digital glue can dominate the system budget, as we will see in lesson 5.8.

### [03:16.0] Common mistakes — `slide`

**ES:** Errores frecuentes: comparar operaciones en lugar de bytes movidos. Comparar la energía del tejido de un chip con la energía de sistema de una GPU. Ignorar el costo del generador pseudoaleatorio. Y tratar estimaciones de orden de magnitud como si fueran mediciones.

**EN:** Frequent mistakes: comparing operations instead of bytes moved. Comparing a chip's fabric energy with a GPU's system energy. Ignoring the cost of the pseudorandom generator. And treating order-of-magnitude estimates as if they were measurements.

### [03:33.4] Summary — `manim:S09`

**ES:** En resumen: en hardware digital, una actualización de Gibbs paga movimiento de datos, generación de aleatoriedad y márgenes de ruido, y la aritmética es casi gratis. El muestreo está limitado por memoria. Un pbit físico, con los acoplamientos a su lado y el ruido como recurso, puede ser del orden de mil veces más eficiente por actualización.

**EN:** In summary: on digital hardware, a Gibbs update pays for data movement, randomness generation and noise margins, and the arithmetic is almost free. Sampling is memory-bound. A physical pbit, with its couplings next to it and noise as a resource, can be on the order of a thousand times more efficient per update.

### [03:55.9] Self-assessment — `slide`

**ES:** Para practicar: estima la intensidad aritmética de una actualización. Acota la energía por actualización del Z1 y compárala con Landauer. Explica por qué la GPU queda ociosa. Y enumera los tres costos que un pbit evita.

**EN:** To practice: estimate the arithmetic intensity of an update. Bound the Z1 energy per update and compare it with Landauer. Explain why the GPU sits idle. And list the three costs a pbit avoids.

## Key equations
- $$E_{\text{update}}^{\text{digital}} \approx n_{\text{words}}\,e_{\text{SRAM}} + e_{\text{PRNG}} + e_{\text{ALU}} \sim 12\times5\ \text{pJ} + \dots \sim 70\ \text{pJ}\ [E]$$ — Order-of-magnitude cost of a degree-16 Gibbs update on digital hardware (45 nm table, lesson 0.1).
- $$e_{\text{update}}^{\text{Z1}} \le \frac{1\ \text{W}}{269\,568 \times 50\ \text{MHz}} \approx 7.4\times10^{-14}\ \text{J}$$ — Upper bound on the Z1 energy per pbit update from its stated power and rate.

## Summary
- Gibbs on digital: data movement + PRNG + noise margins; arithmetic is nearly free.
- Memory-bound: ~1 FLOP/byte, far left of the roofline knee.
- Digital update ~70 pJ [E] vs Z1 ≤ 74 fJ: ~10³×.
- Design: compute in memory, physical noise, rare readout.

## Further reading
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- M. Horowitz, Computing's energy problem (and what we can do about it), ISSCC 2014.
