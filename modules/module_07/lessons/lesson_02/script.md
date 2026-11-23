# Lesson 7.2 — Shor's algorithm

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe the four stages of Shor's order finding: superposition, modular exponentiation, quantum Fourier transform, continued fractions.
- Compute the measurement distribution for a small example and explain the peaks at multiples of $Q/r$.
- Recover $r$ from a measured $y$ by continued fractions, and combine runs when only a divisor appears.

## Prerequisites
- Lesson 7.1: factoring reduces to order finding.
- Lesson 0.6: discrete Fourier transform and characters.

## Narrated script

### [00:04.3] Introduction — `manim:S01`

**ES:** En mil novecientos noventa y cuatro, Peter Shor mostró que un computador cuántico encuentra el orden en tiempo polinomial en el número de bits. Es la referencia contra la que compararemos la difusión. Hoy recorremos sus cuatro pasos con un ejemplo pequeño, N = 21, que podemos simular exactamente en un computador clásico.

**EN:** In nineteen ninety-four, Peter Shor showed that a quantum computer finds the order in time polynomial in the number of bits. It is the benchmark against which we will compare diffusion. Today we walk through its four steps with a small example, N = 21, which we can simulate exactly on a classical computer.

### [00:25.8] Superposition and modular exponentiation — `manim:S02`

**ES:** Primero se prepara una superposición uniforme de todos los exponentes x de cero a Q − 1, con Q una potencia de dos mayor que N²; aquí Q = 512. Segundo, un circuito reversible calcula a^x mod N en un segundo registro. Con a = 2, los valores se repiten cada seis exponentes: el orden es seis. Al medir el segundo registro, el primero queda en una superposición de exponentes separados exactamente por el período.

**EN:** First, a uniform superposition of all exponents x from zero to Q − 1 is prepared, with Q a power of two larger than N²; here Q = 512. Second, a reversible circuit computes a^x mod N in a second register. With a = 2, the values repeat every six exponents: the order is six. When the second register is measured, the first is left in a superposition of exponents separated exactly by the period.

### [00:57.2] Quantum Fourier transform — `manim:S03`

**ES:** Tercero, la transformada cuántica de Fourier convierte esa periodicidad en picos. Las amplitudes de los resultados que no encajan con el período se cancelan por interferencia, y las que encajan se refuerzan. En el ejemplo, la probabilidad se concentra cerca de los múltiplos de Q/r, unos ochenta y cinco coma tres: en cero, ochenta y cinco, ciento setenta y uno, doscientos cincuenta y seis, y así sucesivamente.

**EN:** Third, the quantum Fourier transform turns that periodicity into peaks. The amplitudes of outcomes that do not fit the period cancel by interference, and those that fit are reinforced. In the example, the probability concentrates near the multiples of Q/r, about 85.3: at zero, eighty-five, one hundred seventy-one, two hundred fifty-six, and so on.

### [01:25.0] Continued fractions — `manim:S04`

**ES:** Cuarto, el posprocesamiento clásico. Un resultado y cumple y/Q ≈ k/r. El algoritmo de fracciones continuas encuentra la mejor fracción con denominador menor que N. Para y = 85, 85/512 se aproxima por un sexto: el orden es seis. Pero para y = 171 sale un tercio, y solo obtenemos un divisor del orden. En este ejemplo, una sola corrida da el orden directamente con probabilidad treinta y uno por ciento; combinando unas pocas corridas con el mínimo común múltiplo se recupera siempre.

**EN:** Fourth, classical post-processing. An outcome y satisfies y/Q ≈ k/r. The continued-fraction algorithm finds the best fraction with denominator smaller than N. For y = 85, 85/512 is approximated by one sixth: the order is six. But for y = 171 we get one third, and only obtain a divisor of the order. In this example, a single run gives the order directly with probability thirty-one percent; combining a few runs with the least common multiple always recovers it.

### [02:03.2] Cost — `manim:S05`

**ES:** ¿Cuánto cuesta? La exponenciación modular domina: con aritmética de escuela son del orden de n³ compuertas, con n el número de bits de N. La transformada de Fourier cuesta n². Todo es polinomial, frente al costo subexponencial de los mejores algoritmos clásicos. El precio está en el hardware: miles de qubits lógicos con corrección de errores, que todavía no existen a escala.

**EN:** How much does it cost? Modular exponentiation dominates: with schoolbook arithmetic it is on the order of n³ gates, with n the number of bits of N. The Fourier transform costs n². Everything is polynomial, against the subexponential cost of the best classical algorithms. The price is in the hardware: thousands of error-corrected logical qubits, which do not yet exist at scale.

### [02:29.4] The analogy — `manim:S06`

**ES:** Guardemos la idea central para el resto de la unidad. Shor amplifica los picos de Fourier por interferencia: las frecuencias que no encajan se cancelan. La difusión hará lo contrario: amortiguará todos los modos de Fourier distintos de cero, y lo que sobrevive, la distribución uniforme sobre el grupo, revela su tamaño. Interferencia que amplifica frente a disipación que borra.

**EN:** Let's keep the central idea for the rest of the unit. Shor amplifies Fourier peaks by interference: frequencies that do not fit cancel out. Diffusion will do the opposite: it will damp all nonzero Fourier modes, and what survives, the uniform distribution over the group, reveals its size. Interference that amplifies versus dissipation that erases.

### [02:53.5] Applications — `slide`

**ES:** Shor amenaza la criptografía de clave pública y motiva los estándares poscuánticos. El mismo núcleo de búsqueda de período resuelve logaritmos discretos. Las demostraciones experimentales hasta hoy factorizan números diminutos con circuitos simplificados. En el laboratorio diez simularás la distribución y las fracciones continuas.

**EN:** Shor threatens public-key cryptography and motivates post-quantum standards. The same period-finding core solves discrete logarithms. Experimental demonstrations so far factor tiny numbers with simplified circuits. In lab ten you will simulate the distribution and the continued fractions.

### [03:14.4] Common mistakes — `slide`

**ES:** Errores comunes: creer que el computador cuántico prueba todos los exponentes y lee todas las respuestas. Tomar el denominador como el orden sin verificarlo. Olvidar que algunos resultados dan solo un divisor. Y confundir qubits lógicos con qubits físicos.

**EN:** Common mistakes: believing the quantum computer tries all exponents and reads all answers. Taking the denominator as the order without verifying it. Forgetting that some outcomes give only a divisor. And confusing logical qubits with physical qubits.

### [03:31.6] Summary — `manim:S09`

**ES:** En resumen, Shor prepara una superposición, calcula la exponenciación modular, aplica la transformada de Fourier para convertir el período en picos de probabilidad, y recupera el orden con fracciones continuas. Su costo es polinomial en el número de bits. Interfiere para amplificar; la difusión disipará para borrar.

**EN:** In summary: Shor prepares a superposition, computes modular exponentiation, applies the Fourier transform to turn the period into probability peaks, and recovers the order with continued fractions. Its cost is polynomial in the number of bits. It interferes to amplify; diffusion will dissipate to erase.

### [03:52.3] Self-assessment — `slide`

**ES:** Para practicar: explica por qué Q debe ser al menos N². Desarrolla la fracción continua del ejemplo. Combina dos corridas que dan divisores. Y di qué etapa domina el costo.

**EN:** To practice: explain why Q must be at least N². Expand the continued fraction of the example. Combine two runs that give divisors. And say which stage dominates the cost.

## Key equations
- $$\frac{1}{\sqrt Q}\sum_{x=0}^{Q-1}|x\rangle|a^x \bmod N\rangle \ \xrightarrow{\ \text{QFT}\ }\ \Pr(y) \text{ peaked at } y \approx kQ/r$$ — Superposition, modular exponentiation and Fourier transform.
- $$\Big|\frac{y}{Q} - \frac{k}{r}\Big| \le \frac{1}{2Q} \le \frac{1}{2N^2} \ \Rightarrow\ k/r \text{ is a convergent of } y/Q$$ — Why continued fractions recover $k/r$ when $Q \ge N^2$.
- $$N = 21,\ a = 2,\ Q = 512:\ \ 85/512 \to 1/6,\ \ 171/512 \to 1/3$$ — Worked example: one outcome gives $r = 6$, another only a divisor.

## Summary
- Superposition → modular exponentiation → QFT → continued fractions.
- N = 21, a = 2: peaks at multiples of 512/6 ≈ 85.3 [S].
- One run gives r directly with probability 0.31; lcm of a few runs always works.
- Cost O(n³) gates; interference amplifies (diffusion will damp).

## Further reading
- P. W. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer, SIAM J. Comput. 26, 1484 (1997).
- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, §5.3, Cambridge (2010).
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
