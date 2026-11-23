# Lesson 7.1 — From factoring to order finding

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Reduce factoring $N$ to finding the multiplicative order of a random unit.
- Use the Chinese remainder theorem to explain when $x = a^{r/2}$ gives a nontrivial square root of 1.
- State the success probability $1 - (m+1)/2^m$ (sufficient pattern) and verify it on $N = 299$.

## Prerequisites
- Lesson 0.6: modular arithmetic and characters of Z/rZ.
- Basic number theory: gcd, Euclid's algorithm.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Factorizar un número grande es difícil para los computadores digitales, y sobre esa dificultad descansa buena parte de la criptografía. El algoritmo de Shor mostró que un computador cuántico lo haría eficientemente. En esta unidad estudiamos una alternativa basada en difusión. Pero todo empieza con un truco clásico: convertir la factorización en un problema de encontrar el orden de un número.

**EN:** Factoring a large number is hard for digital computers, and much of cryptography rests on that difficulty. Shor's algorithm showed that a quantum computer would do it efficiently. In this unit we study an alternative based on diffusion. But everything starts with a classical trick: turning factoring into a problem of finding the order of a number.

### [00:30.4] The order of a unit — `manim:S02`

**ES:** Tomemos N = 299 y un número a coprimo con N. Las potencias de a módulo N se repiten en un ciclo. El orden r es la longitud de ese ciclo: el menor exponente tal que a^r ≡ 1. Para a = 2, el orden es ciento treinta y dos.

**EN:** Take N = 299 and a number a coprime with N. The powers of a modulo N repeat in a cycle. The order r is the length of that cycle: the smallest exponent such that a^r ≡ 1. For a = 2, the order is one hundred thirty-two.

### [00:50.5] The square-root trick — `manim:S03`

**ES:** Si el orden es par, x = a^(r/2) cumple x² ≡ 1. Entonces N divide a (x − 1)(x + 1). Si además x no es ± 1, N no divide a ninguno de los dos factores por separado, así que el máximo común divisor de x − 1 y N es un factor propio. Para a = 2: x = 116, y el máximo común divisor de ciento quince y doscientos noventa y nueve es veintitrés. Así, doscientos noventa y nueve es trece por veintitrés.

**EN:** If the order is even, x = a^(r/2) satisfies x² ≡ 1. Then N divides (x − 1)(x + 1). If moreover x is not ± 1, N divides neither factor separately, so the greatest common divisor of x − 1 and N is a proper factor. For a = 2: x = 116, and the greatest common divisor of one hundred fifteen and two hundred ninety-nine is twenty-three. So two hundred ninety-nine is thirteen times twenty-three.

### [01:25.9] Why it works: CRT — `manim:S04`

**ES:** El teorema chino del resto explica cuándo funciona. Módulo N = p q, cada número es un par de restos, uno módulo p y otro módulo q. Una raíz cuadrada de uno es un par de signos. Las raíces triviales son más más y menos menos; las mixtas, más menos y menos más, son las que factorizan. El truco falla solo cuando las partes de potencia de dos del orden coinciden en todas las componentes.

**EN:** The Chinese remainder theorem explains when it works. Modulo N = p q, every number is a pair of remainders, one modulo p and one modulo q. A square root of one is a pair of signs. The trivial roots are plus-plus and minus-minus; the mixed ones, plus-minus and minus-plus, are the ones that factor. The trick fails only when the power-of-two parts of the order coincide in all components.

### [01:54.1] Success probability — `manim:S05`

**ES:** Para un a al azar y m factores primos distintos, un patrón de paridades suficiente tiene probabilidad 1 − (m + 1)/2^m, al menos un cuarto. La ley exacta es más fuerte: al menos un medio para semiprimos. En N = 299, contando todos los a coprimos, el truco funciona en ciento noventa y ocho de doscientos sesenta y tres casos: el setenta y cinco por ciento. Repetir con otro a lleva el fallo rápidamente a cero.

**EN:** For a random a and m distinct prime factors, a sufficient parity pattern has probability 1 − (m + 1)/2^m, at least one quarter. The exact law is stronger: at least one half for semiprimes. In N = 299, counting all coprime a, the trick works in one hundred ninety-eight of two hundred sixty-three cases: seventy-five percent. Repeating with another a drives failure quickly to zero.

### [02:23.9] The hard part — `manim:S06`

**ES:** Todo el trabajo difícil está en encontrar el orden. Recorrer las potencias una por una cuesta hasta r pasos, y r puede ser del tamaño de N: exponencial en el número de bits. Shor lo resuelve con interferencia cuántica, como veremos en la lección siguiente. La difusión lo resuelve con un calor que se reparte por un grafo. Ambas son formas físicas de detectar un período.

**EN:** All the hard work is in finding the order. Going through the powers one by one costs up to r steps, and r can be as large as N: exponential in the number of bits. Shor solves it with quantum interference, as we will see in the next lesson. Diffusion solves it with heat spreading over a graph. Both are physical ways of detecting a period.

### [02:48.1] Applications — `slide`

**ES:** Esta reducción importa porque la seguridad de RSA depende de la dificultad de factorizar, y porque cualquier método de búsqueda de orden, cuántico, de difusión o de colisiones, se conecta a ella. En la lección siete punto cuatro usaremos una base con orden impar. En el laboratorio diez la implementarás.

**EN:** This reduction matters because RSA security depends on the difficulty of factoring, and because any order-finding method, quantum, diffusion or collisions, plugs into it. In lesson 7.4 we will use a base with odd order. In lab ten you will implement it.

### [03:08.1] Common mistakes — `slide`

**ES:** Errores comunes: no calcular primero el máximo común divisor de a y N, que puede ser ya un factor. Aceptar x ≡ −1, que no factoriza. Aplicar el método a potencias de un primo. Y confundir la cota de un cuarto con la ley exacta.

**EN:** Common mistakes: not computing first the greatest common divisor of a and N, which may already be a factor. Accepting x ≡ −1, which does not factor. Applying the method to prime powers. And confusing the one-quarter bound with the exact law.

### [03:25.6] Summary — `manim:S09`

**ES:** En resumen: si conocemos el orden par de un número al azar, su raíz a^(r/2) da un factor con el máximo común divisor. El teorema chino del resto explica por qué funciona la mayoría de las veces. Todo lo difícil está en encontrar el orden.

**EN:** In summary: if we know the even order of a random number, its root a^(r/2) gives a factor through the greatest common divisor. The Chinese remainder theorem explains why it works most of the time. All the difficulty is in finding the order.

### [03:41.9] Self-assessment — `slide`

**ES:** Para practicar: factoriza quince con el orden de dos. Explica por qué x no puede ser más o menos uno. Evalúa la probabilidad para dos, tres y cuatro factores. Y explica por qué la búsqueda directa del orden es exponencial.

**EN:** To practice: factor fifteen with the order of two. Explain why x cannot be plus or minus one. Evaluate the probability for two, three and four factors. And explain why direct order search is exponential.

## Key equations
- $$r = \mathrm{ord}_N(a) = \min\{k > 0 : a^k \equiv 1 \pmod N\}$$ — Multiplicative order of a unit.
- $$x = a^{r/2},\ x^2 \equiv 1,\ x \not\equiv \pm1 \ \Rightarrow\ 1 < \gcd(x - 1, N) < N$$ — A nontrivial square root of 1 gives a proper factor.
- $$P_{\text{sufficient}} = 1 - \frac{m+1}{2^m}\quad (\ge 1/4\ \text{for } m \ge 2)$$ — Probability of the sufficient CRT parity pattern for $m$ distinct primes.

## Summary
- Factoring reduces to finding the order r of a random unit.
- x = a^(r/2) with x ≠ ±1 gives gcd(x − 1, N) a proper factor.
- N = 299, a = 2: r = 132, x = 116, gcd = 23 ⇒ 299 = 13 · 23.
- Success: ≥ 1/4 (sufficient pattern), ≥ 1/2 for semiprimes; 75 % for N = 299.

## Further reading
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
- P. W. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer, SIAM J. Comput. 26, 1484 (1997).
- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, ch. 5, Cambridge (2010).
