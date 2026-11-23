# Lesson 7.8 — Comparative complexity

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Compare quantum steps, diffusion steps and digital steps, and what each one costs physically.
- Estimate resources for factoring a 2048-bit number with Shor, diffusion, the number field sieve and Pollard's rho.
- Contrast HHL with thermodynamic linear algebra: input model, output and scaling.

## Prerequisites
- Lessons 7.1–7.7.
- Lessons 6.1 and 6.4: thermodynamic linear algebra and its complexity.

## Narrated script

### [00:04.5] Introduction — `manim:S01`

**ES:** Cerramos la unidad comparando. Hemos visto tres maneras de encontrar un orden: interferencia cuántica, difusión física y colisiones digitales. Cada una cuenta pasos distintos, y un paso de una no cuesta lo mismo que un paso de otra. Comparar en serio exige preguntar qué recurso físico consume cada paso.

**EN:** We close the unit by comparing. We have seen three ways to find an order: quantum interference, physical diffusion and digital collisions. Each counts different steps, and a step of one does not cost the same as a step of another. Comparing seriously requires asking which physical resource each step consumes.

### [00:25.0] Three kinds of step — `manim:S02`

**ES:** Un paso cuántico es una compuerta sobre unos pocos qubits; el algoritmo usa del orden de n qubits lógicos y n³ compuertas, con n el número de bits. Un paso de difusión es un promedio simultáneo sobre todos los nodos: solo hacen falta O(n²) pasos, pero sobre una red de al menos r nodos leída con unos 2n bits de precisión. Un paso digital es una operación de palabra: barata, pero los mejores algoritmos necesitan un número subexponencial de ellas.

**EN:** A quantum step is a gate on a few qubits; the algorithm uses on the order of n logical qubits and n³ gates, with n the number of bits. A diffusion step is a simultaneous average over all nodes: only O(n²) steps are needed, but on a network of at least r nodes read with about 2n bits of precision. A digital step is a word operation: cheap, but the best algorithms need a subexponential number of them.

### [00:57.5] A 2048-bit number — `manim:S03`

**ES:** Pongamos números para un número de dos mil cuarenta y ocho bits, como estimaciones de orden de magnitud. Shor: unos cuatro mil cien qubits lógicos y unos nueve mil millones de compuertas. Difusión: unos diecisiete millones de pasos, pero una red de hasta dos a la dos mil cuarenta y ocho nodos y cuatro mil bits de precisión de lectura. La criba de cuerpos de números: del orden de dos a la ciento diecisiete operaciones. Rho de Pollard: dos a la quinientos doce.

**EN:** Let's put numbers to a two-thousand-forty-eight-bit number, as order-of-magnitude estimates. Shor: about four thousand one hundred logical qubits and about nine billion gates. Diffusion: about seventeen million steps, but a network of up to two to the two thousand forty-eight nodes and four thousand bits of readout precision. The number field sieve: on the order of two to the one hundred seventeen operations. Pollard's rho: two to the five hundred twelve.

### [01:27.5] Where the cost goes — `manim:S04`

**ES:** La lección es que la dificultad no desaparece: se traslada. Shor la paga en coherencia cuántica y corrección de errores. La difusión la paga en área, en número de nodos y en precisión analógica, que crecen exponencialmente con los bits. Lo digital la paga en tiempo. Interferencia que amplifica frente a disipación que borra: la disipación es barata por paso, pero necesita representar todo el grupo.

**EN:** The lesson is that the difficulty does not disappear: it moves. Shor pays for it in quantum coherence and error correction. Diffusion pays for it in area, in number of nodes and in analog precision, which grow exponentially with the bits. Digital pays for it in time. Interference that amplifies versus dissipation that erases: dissipation is cheap per step, but needs to represent the whole group.

### [01:53.9] HHL versus thermodynamic linear algebra — `manim:S05`

**ES:** La misma comparación aparece en álgebra lineal. El algoritmo cuántico HHL resuelve A x = b en un tiempo que crece solo con el logaritmo de la dimensión, pero exige una matriz dispersa accesible por un oráculo y entrega un estado cuántico, no el vector: leer todas las entradas cuesta lo que se ganó. El álgebra lineal termodinámica de la unidad seis entrega el vector clásico, escala con d κ² ε⁻² y paga la carga de la matriz. Distintas promesas, distintas letras pequeñas.

**EN:** The same comparison appears in linear algebra. The quantum HHL algorithm solves A x = b in a time that grows only with the logarithm of the dimension, but requires a sparse matrix accessible through an oracle and delivers a quantum state, not the vector: reading all entries costs what was gained. The thermodynamic linear algebra of unit six delivers the classical vector, scales as d κ² ε⁻² and pays for loading the matrix. Different promises, different fine print.

### [02:28.8] How to read a claim — `manim:S06`

**ES:** Para cualquier afirmación de ventaja, pregunta cuatro cosas. ¿Qué es un paso, y cuánto cuesta físicamente? ¿Cómo crecen el área, la energía y la precisión con el tamaño del problema? ¿Qué se entrega al final, y cuánto cuesta leerlo? ¿Contra qué algoritmo clásico se compara, y en qué condiciones? Con esas preguntas, los resultados de esta unidad quedan en su lugar: ideas profundas sobre la estructura de los grupos, no atajos para la criptografía.

**EN:** For any advantage claim, ask four things. What is a step, and how much does it cost physically? How do area, energy and precision grow with problem size? What is delivered at the end, and how much does it cost to read it? Against which classical algorithm is it compared, and under what conditions? With those questions, the results of this unit fall into place: deep ideas about the structure of groups, not shortcuts for cryptography.

### [02:56.8] Applications — `slide`

**ES:** Usa esta comparación para evaluar afirmaciones con modelos explícitos de tiempo, área, energía y precisión, etiquetando cada número como en la lección cinco punto ocho. En el proyecto final incluirás una tabla de recursos como la de hoy.

**EN:** Use this comparison to evaluate claims with explicit models of time, area, energy and precision, labeling each number as in lesson 5.8. In the final project you will include a resource table like today's.

### [03:12.2] Common mistakes — `slide`

**ES:** Errores comunes: comparar números de pasos de modelos distintos como si costaran lo mismo. Ignorar que la difusión necesita del orden de r nodos. Ignorar el oráculo de entrada y la salida cuántica de HHL. Y confundir qubits físicos con lógicos.

**EN:** Common mistakes: comparing step counts of different models as if they cost the same. Ignoring that diffusion needs on the order of r nodes. Ignoring HHL's input oracle and quantum output. And confusing physical with logical qubits.

### [03:29.5] Summary — `manim:S09`

**ES:** En resumen: un paso cuántico, uno de difusión y uno digital consumen recursos distintos. Para dos mil cuarenta y ocho bits, Shor usa miles de qubits lógicos, la difusión pocos pasos pero una red exponencialmente grande y precisa, y lo digital un tiempo subexponencial. La dificultad se traslada, no desaparece. Y la misma lectura cuidadosa vale para HHL frente al álgebra lineal termodinámica.

**EN:** In summary: a quantum step, a diffusion step and a digital step consume different resources. For two thousand forty-eight bits, Shor uses thousands of logical qubits, diffusion few steps but an exponentially large and precise network, and digital a subexponential time. The difficulty moves, it does not disappear. And the same careful reading applies to HHL versus thermodynamic linear algebra.

### [03:57.4] Self-assessment — `slide`

**ES:** Para practicar: di qué recurso consume cada tipo de paso. Calcula la cota de difusión para dos mil cuarenta y ocho bits. Explica por qué leer la salida de HHL anula su ventaja. Y escribe las cuatro preguntas para cualquier afirmación de ventaja.

**EN:** To practice: say which resource each kind of step consumes. Compute the diffusion bound for two thousand forty-eight bits. Explain why reading HHL's output cancels its advantage. And write the four questions for any advantage claim.

## Key equations
- $$\text{Shor: } O(n^3)\ \text{gates},\ \sim 2n\ \text{logical qubits};\quad \text{diffusion: } \ell_0 = 4(M+1)(n+2)\ \text{steps on } \Omega(r)\ \text{nodes}$$ — Steps and physical resources for order finding ($n = \log_2 N$).
- $$\text{NFS: } \exp\Big(\big(\tfrac{64}{9}\big)^{1/3}(\ln N)^{1/3}(\ln\ln N)^{2/3}\Big),\qquad \text{rho: } O(N^{1/4})$$ — Classical baselines (heuristic NFS cost, $o(1)$ omitted).
- $$\text{HHL: } \tilde O\big(\log(d)\,s^2\kappa^2/\varepsilon\big) \to |x\rangle;\qquad \text{TLA: } O(d\kappa^2\varepsilon^{-2}) \to x$$ — Different input models and outputs for linear systems.

## Summary
- Quantum, diffusion and digital steps consume different physical resources.
- 2048 bits [E]: Shor ~4100 logical qubits, ~9·10⁹ gates; diffusion 1.7·10⁷ steps on ~2²⁰⁴⁸ nodes, ~4096 bits.
- NFS ~2¹¹⁷ operations; rho ~2⁵¹²: the difficulty moves, it does not disappear.
- HHL: log d, sparse oracle, quantum-state output; TLA: classical x, d κ² ε⁻², loading cost.

## Further reading
- A. W. Harrow, A. Hassidim and S. Lloyd, Quantum algorithm for linear systems of equations, Phys. Rev. Lett. 103, 150502 (2009).
- S. Aaronson, Read the fine print, Nature Physics 11, 291 (2015).
- Cadavid et al., Treatise on diffusion-driven factorization (course data/), Sections 1.3 and 20, 2026.
