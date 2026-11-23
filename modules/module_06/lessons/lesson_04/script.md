# Lesson 6.4 — Complexity of thermodynamic algorithms

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the assumptions behind analog complexity: time in relaxation units, hardware growing with $d$.
- Explain why relaxation scales with $\kappa$ (overdamped) or $\sqrt\kappa$ (underdamped, tuned damping).
- Use the energy–time bound $E\tau \gtrsim \kappa^2 d\,\beta^{-1}\tau_r/\varepsilon^2$ to reason about trade-offs.

## Prerequisites
- Lessons 6.1–6.3: thermodynamic linear-algebra protocols.
- Lesson 2.6: overdamped and underdamped Langevin dynamics.

## Narrated script

### [00:05.8] Introduction — `manim:S01`

**ES:** ¿Qué significa que un algoritmo analógico sea más rápido? Un computador digital cuenta operaciones. Un dispositivo termodinámico no hace operaciones: evoluciona en el tiempo. Para comparar hay que fijar reglas: medir el tiempo en unidades del tiempo de relajación y aceptar que el hardware crece con el problema. Hoy vemos de dónde salen las complejidades de la tabla de Aifer y qué limitaciones esconden.

**EN:** What does it mean for an analog algorithm to be faster? A digital computer counts operations. A thermodynamic device does not perform operations: it evolves in time. To compare, we must fix rules: measure time in units of the relaxation time and accept that the hardware grows with the problem. Today we see where the complexities in Aifer's table come from and what limitations they hide.

### [00:31.3] Assumptions — `manim:S02`

**ES:** Tres supuestos. Primero, el dispositivo tiene d osciladores y hasta d² acoplamientos, que evolucionan todos en paralelo. Segundo, la escala de tiempo física es τ_r = γ/‖A‖, fijada por el modo más rápido. Tercero, la complejidad cuenta el tiempo total en unidades de τ_r, sin incluir la carga de la matriz, que veremos en la lección siguiente. Con estas reglas, el análisis de complejidad analógica es sutil, y los propios autores lo advierten.

**EN:** Three assumptions. First, the device has d oscillators and up to d² couplings, all evolving in parallel. Second, the physical timescale is τ_r = γ/‖A‖, set by the fastest mode. Third, the complexity counts the total time in units of τ_r, not including the loading of the matrix, which we will see in the next lesson. With these rules, the analysis of analog complexity is subtle, and the authors themselves warn about it.

### [01:02.8] Why κ appears — `manim:S03`

**ES:** Cada modo propio de A relaja con su propia tasa, proporcional a su autovalor. El modo más rápido fija la escala de tiempo, pero el más lento decide cuándo terminamos. La razón entre ambos es el número de condición κ. Por eso la equilibración en el régimen sobreamortiguado tarda del orden de κ τ_r: una matriz mal condicionada es un sistema físico con modos muy lentos.

**EN:** Each eigenmode of A relaxes at its own rate, proportional to its eigenvalue. The fastest mode sets the timescale, but the slowest decides when we are done. The ratio between them is the condition number κ. That is why equilibration in the overdamped regime takes on the order of κ τ_r: an ill-conditioned matrix is a physical system with very slow modes.

### [01:27.9] Overdamped vs underdamped — `manim:S04`

**ES:** La inercia ayuda. En el régimen subamortiguado, con masa y un amortiguamiento ajustado al modo lento, la relajación escala como la raíz de κ en lugar de κ. Lo simulamos con la matriz de la lección seis punto uno, normalizada. Con κ igual a treinta y cuatro, llegar a un error de una milésima tarda doscientas siete unidades sobreamortiguado y cuarenta y nueve subamortiguado. Con κ diez veces mayor, dos mil trescientas setenta frente a ciento setenta y dos: el primero creció once veces y el segundo apenas tres y media. Es la misma aceleración del método de la bola pesada en optimización.

**EN:** Inertia helps. In the underdamped regime, with mass and a damping tuned to the slow mode, relaxation scales as the square root of κ instead of κ. We simulate it with the matrix from lesson 6.1, normalized. With κ equal to thirty-four, reaching an error of one thousandth takes two hundred seven units overdamped and forty-nine underdamped. With κ ten times larger, two thousand three hundred seventy against one hundred seventy-two: the first grew eleven times and the second only three and a half. It is the same acceleration as the heavy-ball method in optimization.

### [02:07.1] Comparing with digital — `manim:S05`

**ES:** Ahora la tabla completa. Para sistemas lineales, el método sobreamortiguado escala como d κ² ε⁻², y el subamortiguado como d κ^(3/2) ε⁻², frente a d² √κ del gradiente conjugado. La ganancia es lineal en d, pero se paga con peor dependencia en κ y en la precisión. En sus simulaciones, Aifer y colaboradores encuentran ventaja práctica para dimensiones de mil o cinco mil y precisiones modestas, no para soluciones de alta precisión.

**EN:** Now the full table. For linear systems, the overdamped method scales as d κ² ε⁻², and the underdamped as d κ^(3/2) ε⁻², against d² √κ for conjugate gradient. The gain is linear in d, but it is paid for with worse dependence on κ and on precision. In their simulations, Aifer and colleagues find a practical advantage for dimensions of a thousand or five thousand and modest precision, not for high-precision solutions.

### [02:41.8] Energy–time bound — `manim:S06`

**ES:** Una tentación: si multiplicamos b por una constante grande, la fórmula del tiempo baja con su cuadrado. Pero inicializar el sistema cuesta una energía proporcional a bᵀ A⁻¹ b, que sube con el mismo cuadrado. Lo que queda acotado es el producto: la energía por el tiempo es al menos 2κ² d β⁻¹ τ_r / (ε²(1 − P)). Se puede ir más rápido gastando más energía, pero no gratis: es una relación energía tiempo propia de estos algoritmos.

**EN:** A temptation: if we multiply b by a large constant, the time formula drops with its square. But initializing the system costs an energy proportional to bᵀ A⁻¹ b, which rises with the same square. What stays bounded is the product: energy times time is at least 2κ² d β⁻¹ τ_r / (ε²(1 − P)). One can go faster by spending more energy, but not for free: it is an energy–time relation specific to these algorithms.

### [03:14.7] Applications — `slide`

**ES:** Ante cualquier afirmación de complejidad, pregunta en qué unidades se mide el tiempo, cómo crece el hardware con la dimensión, qué número de condición y qué precisión tiene tu problema real, y si incluye la carga y la lectura.

**EN:** Faced with any complexity claim, ask in which units time is measured, how the hardware grows with the dimension, what condition number and precision your real problem has, and whether loading and readout are included.

### [03:28.8] Common mistakes — `slide`

**ES:** Errores comunes: comparar unidades de relajación con operaciones sin un modelo de tiempo. Olvidar que el hardware crece como el cuadrado de la dimensión. Ignorar los factores de condición y precisión. Y escalar el vector para acelerar sin contar la energía.

**EN:** Common mistakes: comparing relaxation units with operations without a timing model. Forgetting that the hardware grows as the square of the dimension. Ignoring the condition and precision factors. And scaling the vector to speed up without counting the energy.

### [03:45.5] Summary — `manim:S09`

**ES:** En resumen: la complejidad analógica se mide en tiempos de relajación con hardware que crece con el problema. El número de condición aparece porque los modos lentos tardan κ veces más, o solo raíz de κ con inercia bien ajustada. La ganancia es lineal en la dimensión, a cambio de peor dependencia en precisión, y la energía por el tiempo está acotada.

**EN:** In summary: analog complexity is measured in relaxation times with hardware that grows with the problem. The condition number appears because slow modes take κ times longer, or only √κ with well-tuned inertia. The gain is linear in the dimension, in exchange for worse dependence on precision, and energy times time is bounded.

### [04:08.4] Self-assessment — `slide`

**ES:** Para practicar: calcula el tiempo de relajación del modo lento. Encuentra el amortiguamiento óptimo. Encuentra la dimensión a partir de la cual gana el método termodinámico en el ejemplo. Y explica por qué escalar el vector no lo hace infinitamente rápido.

**EN:** To practice: compute the relaxation time of the slow mode. Find the optimal damping. Find the dimension beyond which the thermodynamic method wins in the example. And explain why scaling the vector does not make it infinitely fast.

## Key equations
- $$\tau_r = \gamma/\|A\|,\qquad t_{\text{slow}} = \gamma/\lambda_{\min} = \kappa\,\tau_r$$ — The slowest mode sets the overdamped equilibration time.
- $$\text{Linear system: } O(d\kappa^2\varepsilon^{-2})\ \text{(OD)},\ O(\gamma d\kappa^{3/2}\varepsilon^{-2})\ \text{(UD)}\ \text{vs}\ O(\min\{d^\omega, d^2\sqrt\kappa\})$$ — Aifer et al., Table II.
- $$E\,\tau \ \ge\ \frac{2\kappa^2 d}{\varepsilon^2(1-P_\varepsilon)}\,\beta^{-1}\tau_r$$ — Energy–time bound for the overdamped linear-system protocol.

## Summary
- Analog complexity: time in units of τ_r; hardware with d² couplers in parallel.
- Overdamped equilibration ∝ κ; tuned underdamped ∝ √κ (heavy ball).
- Simulation: 207 → 2372 (OD) vs 49 → 172 (UD) when κ: 34 → 344 [S].
- Gain linear in d; worse in κ and ε; E·τ bounded below.

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- B. T. Polyak, Some methods of speeding up the convergence of iteration methods, USSR Comput. Math. Math. Phys. 4, 1 (1964).
- [29] M. Aifer et al., Solving the compute crisis with physics-based ASICs, 2025.
