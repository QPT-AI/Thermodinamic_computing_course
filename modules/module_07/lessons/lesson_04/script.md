# Lesson 7.4 — The diffusion order-finding theorem

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the theorem: after $\ell_0 = 4(M+1)(\log_2 N + 2)$ steps, $\mathrm{round}(1/p_\ell(e)) = r$.
- Prove the doubling lemma and use it to bound every nonzero eigenvalue by $1 - 1/(2(M+1))$.
- Explain why the bound is conservative, and what it does and does not say about physical cost.

## Prerequisites
- Lesson 7.3: Cayley walks and the character formula.
- Lesson 7.1: odd-order base $b = a^{2^M}$.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Ya vimos que el calor en el grafo de Cayley se reparte hasta valer uno sobre r en cada nodo. La pregunta es cuántos pasos hacen falta para leer r sin error, sin conocer r de antemano. El teorema de Cadavid y colaboradores responde: un número de pasos que crece solo como el cuadrado del número de bits de N.

**EN:** We already saw that heat on the Cayley graph spreads until it equals one over r at every node. The question is how many steps are needed to read r without error, without knowing r in advance. The theorem of Cadavid and colleagues answers: a number of steps that grows only as the square of the number of bits of N.

### [00:26.6] The statement — `manim:S02`

**ES:** Sea M = ⌊log₂ N⌋ + 1. Para todo ℓ ≥ 4(M + 1)(log₂ N + 2), el valor del núcleo de calor en la identidad está a menos de 1/(4N²) de uno sobre r. Y como dos recíprocos distintos de enteros menores que N difieren al menos en 1/N², redondear uno sobre ese valor da exactamente r. Para N = 299, M = 9 y la cota es de cuatrocientos nueve pasos.

**EN:** Let M = ⌊log₂ N⌋ + 1. For every ℓ ≥ 4(M + 1)(log₂ N + 2), the value of the heat kernel at the identity is within 1/(4N²) of one over r. And since two distinct reciprocals of integers smaller than N differ by at least 1/N², rounding one over that value gives exactly r. For N = 299, M = 9 and the bound is four hundred nine steps.

### [01:01.4] The doubling lemma — `manim:S03`

**ES:** La pieza clave es el lema de duplicación. Si 2^M > r, para cada frecuencia k distinta de cero existe un t ≤ M tal que k 2^t mod r cae en el intervalo central, entre r/4 y 3r/4. La razón: mientras no caiga ahí, la distancia a cero se duplica en cada paso, y no puede duplicarse para siempre. Con r = 33 y k = 1: uno, dos, cuatro, ocho, dieciséis; el dieciséis ya está en el centro.

**EN:** The key piece is the doubling lemma. If 2^M > r, for every nonzero frequency k there exists t ≤ M such that k 2^t mod r falls in the central interval, between r/4 and 3r/4. The reason: as long as it does not fall there, the distance to zero doubles at each step, and it cannot double forever. With r = 33 and k = 1: one, two, four, eight, sixteen; sixteen is already in the center.

### [01:35.4] Bounding the eigenvalues — `manim:S04`

**ES:** En el intervalo central, el coseno de 2πk2^t/r es negativo o cero. Así que en el promedio de M + 1 cosenos, al menos uno no suma: μ_k ≤ M/(M + 1), y λ_k ≤ 1 − 1/(2(M + 1)). Para M = 9, la cota es cero coma noventa y cinco. Es una sola cota para todas las frecuencias: una suma exponencial lacunaria, con saltos que se duplican, no puede quedarse cerca de su máximo.

**EN:** In the central interval, the cosine of 2πk2^t/r is negative or zero. So in the average of M + 1 cosines, at least one does not add up: μ_k ≤ M/(M + 1), and λ_k ≤ 1 − 1/(2(M + 1)). For M = 9, the bound is 0.95. It is a single bound for all frequencies: a lacunary exponential sum, with doubling jumps, cannot stay near its maximum.

### [02:07.6] Closing the proof — `manim:S05`

**ES:** Ahora todo encaja. El error es a lo sumo el mayor λ_k^ℓ, que es menor que e^(−ℓ/(2(M + 1))). Con ℓ_0 pasos, eso es menor que e^(−4)/N², por debajo de 1/(4N²). El orden queda determinado por una sola lectura, tras un número de pasos de orden (log₂ N)².

**EN:** Now everything fits. The error is at most the largest λ_k^ℓ, which is smaller than e^(−ℓ/(2(M + 1))). With ℓ_0 steps, that is smaller than e^(−4)/N², below 1/(4N²). The order is determined by a single readout, after a number of steps of order (log₂ N)².

### [02:32.5] In practice, and the caveat — `manim:S06`

**ES:** La cota es conservadora. Para N = 299, el redondeo ya da treinta y tres desde el paso diecisiete, frente a cuatrocientos nueve. Para N igual a un millón veintidós mil ciento diecisiete, con orden cinco mil trescientos trece, basta el paso cuarenta y seis, frente a mil ochocientos cuarenta y cinco. Pero cuidado: cada paso actualiza r nodos a la vez. Si se simula en digital, cuesta r operaciones por paso y la ventaja desaparece. El teorema traslada el costo del tiempo a los recursos físicos, que estudiaremos en la lección siete punto seis.

**EN:** The bound is conservative. For N = 299, rounding already gives thirty-three from step seventeen, against four hundred nine. For N equal to one million twenty-two thousand one hundred seventeen, with order five thousand three hundred thirteen, step forty-six suffices, against one thousand eight hundred forty-five. But beware: each step updates r nodes at once. If simulated digitally, it costs r operations per step and the advantage disappears. The theorem shifts the cost from time to physical resources, which we will study in lesson 7.6.

### [03:09.3] Applications — `slide`

**ES:** El algoritmo completo: elegir a, pasar a la base impar, difundir, leer y redondear, recuperar el orden de a con unas pocas duplicaciones y extraer el factor como en la lección siete punto uno. En el laboratorio diez lo ejecutarás de principio a fin.

**EN:** The full algorithm: pick a, move to the odd base, diffuse, read and round, recover the order of a with a few doublings and extract the factor as in lesson 7.1. In lab ten you will run it end to end.

### [03:27.0] Common mistakes — `slide`

**ES:** Errores comunes: afirmar que hay un algoritmo digital polinomial, cuando el vector tiene r entradas. Olvidar la condición del lema de duplicación. Ignorar que la lectura necesita unos dos log₂ N bits de precisión. Y leer la cota como el número típico de pasos.

**EN:** Common mistakes: claiming there is a polynomial digital algorithm, when the vector has r entries. Forgetting the condition of the doubling lemma. Ignoring that the readout needs about two log₂ N bits of precision. And reading the bound as the typical number of steps.

### [03:45.3] Summary — `manim:S09`

**ES:** En resumen: el lema de duplicación garantiza que toda frecuencia no nula cae alguna vez en la zona de coseno negativo, lo que acota todos los valores propios. Tras ℓ_0 = O((log N)²) pasos, redondear uno sobre p_ℓ(e) da el orden. En la práctica bastan muchos menos pasos, pero cada paso cuesta recursos físicos proporcionales a r.

**EN:** In summary: the doubling lemma guarantees that every nonzero frequency eventually falls in the negative-cosine zone, which bounds all eigenvalues. After ℓ_0 = O((log N)²) steps, rounding one over p_ℓ(e) gives the order. In practice far fewer steps suffice, but each step costs physical resources proportional to r.

### [04:11.0] Self-assessment — `slide`

**ES:** Para practicar: aplica el lema de duplicación a otra frecuencia. Demuestra la separación entre recíprocos. Calcula la cota para otro N. Y explica qué no dice el teorema sobre energía y área.

**EN:** To practice: apply the doubling lemma to another frequency. Prove the separation between reciprocals. Compute the bound for another N. And explain what the theorem does not say about energy and area.

## Key equations
- $$\ell \ge \ell_0 = 4(M+1)\big(\log_2 N + 2\big)\ \Rightarrow\ \Big|p_\ell(e) - \frac1r\Big| \le \frac{1}{4N^2},\quad r = \mathrm{round}\big(1/p_\ell(e)\big)$$ — Diffusion order-finding theorem (Cadavid et al.).
- $$2^M > r,\ 1 \le k < r\ \Rightarrow\ \exists\, t \le M:\ k2^t \bmod r \in \big[\tfrac r4, \tfrac{3r}4\big]$$ — Doubling lemma.
- $$\lambda_k \le 1 - \frac{1}{2(M+1)}\ \Rightarrow\ \Big|p_\ell(e) - \frac1r\Big| \le e^{-\ell/(2(M+1))}$$ — Uniform eigenvalue bound and error decay.

## Summary
- ℓ₀ = 4(M+1)(log₂N + 2) = O((log N)²) diffusion steps; one readout; round(1/p_ℓ(e)) = r.
- Doubling lemma ⇒ λ_k ≤ 1 − 1/(2(M+1)) for all k ≠ 0.
- Conservative: N = 299 needs 17 (bound 409); N = 1 022 117 needs 46 (bound 1845).
- Each step updates r nodes: cost moves from time to physical resources.

## Further reading
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
- Cadavid et al., Treatise on diffusion-driven factorization (course data/), Sections 4 and 8, 2026.
- D. A. Levin, Y. Peres and E. L. Wilmer, Markov Chains and Mixing Times, AMS (2009).
