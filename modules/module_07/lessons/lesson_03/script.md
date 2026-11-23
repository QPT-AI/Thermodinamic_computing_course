# Lesson 7.3 — Random walks on Cayley graphs

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build the Cayley graph of the cyclic group $\langle b\rangle$ with dyadic generators $b^{\pm 2^t}$.
- Define the half-lazy walk $W = \tfrac12(I + P)$ and its discrete-time heat kernel $p_\ell = W^\ell\delta_e$.
- Diagonalize $W$ with characters and write $p_\ell(e) = \tfrac1r\sum_k \lambda_k^\ell$.

## Prerequisites
- Lesson 0.6: characters of Z/rZ.
- Lesson 2.4: Markov chains and mixing.

## Narrated script

### [00:05.5] Introduction — `manim:S01`

**ES:** Imagina que pones una gota de calor en un nodo de un grafo y dejas que se reparta hacia los vecinos. Con el tiempo, el calor se vuelve uniforme, y su valor final en cada nodo es uno dividido por el número de nodos. Si el grafo es un grupo cuyo tamaño es el orden que buscamos, medir ese valor final revela el orden. Hoy construimos ese grafo y entendemos su dinámica.

**EN:** Imagine placing a drop of heat on one node of a graph and letting it spread to its neighbors. Over time, the heat becomes uniform, and its final value at each node is one divided by the number of nodes. If the graph is a group whose size is the order we are looking for, measuring that final value reveals the order. Today we build that graph and understand its dynamics.

### [00:29.1] The Cayley graph — `manim:S02`

**ES:** Tomemos b = 3 módulo doscientos noventa y nueve, cuyo orden es treinta y tres. Los nodos son las potencias de b: un ciclo de treinta y tres elementos. Las aristas multiplican por b^(± 2^t), con t de cero a M = 9. En coordenadas de exponente, cada nodo j se conecta con j ± 2^t módulo treinta y tres. Lo importante: los vecinos se calculan con multiplicación modular, sin conocer el orden.

**EN:** Take b = 3 modulo two hundred ninety-nine, whose order is thirty-three. The nodes are the powers of b: a cycle of thirty-three elements. The edges multiply by b^(± 2^t), with t from zero to M = 9. In exponent coordinates, each node j connects to j ± 2^t modulo thirty-three. The key point: the neighbors are computed with modular multiplication, without knowing the order.

### [00:58.9] The half-lazy walk — `manim:S03`

**ES:** El caminante, con probabilidad un medio, se queda quieto; con la otra mitad, salta por una de las veinte aristas al azar. Esa es la matriz W = ½(I + P). Empezando con toda la masa en la identidad, la distribución tras ℓ pasos es p_ℓ = W^ℓ δ_e: el núcleo de calor en tiempo discreto. Su diferencia entre pasos es el laplaciano aplicado a la distribución: una ecuación del calor discreta.

**EN:** The walker, with probability one half, stays put; with the other half, it jumps along one of the twenty edges at random. That is the matrix W = ½(I + P). Starting with all the mass on the identity, the distribution after ℓ steps is p_ℓ = W^ℓ δ_e: the discrete-time heat kernel. Its difference between steps is the Laplacian applied to the distribution: a discrete heat equation.

### [01:28.4] Characters diagonalize the walk — `manim:S04`

**ES:** Como el grafo es un grupo cíclico, las funciones χ_k(j) = e^(2πikj/r), los caracteres que vimos en la lección cero punto seis, son vectores propios. El valor propio de P es el promedio de los cosenos de 2πk2^t/r, y el de W es λ_k = (1 + μ_k)/2. Todos están entre cero y uno, y solo el modo cero vale exactamente uno.

**EN:** Since the graph is a cyclic group, the functions χ_k(j) = e^(2πikj/r), the characters we saw in lesson 0.6, are eigenvectors. The eigenvalue of P is the average of the cosines of 2πk2^t/r, and that of W is λ_k = (1 + μ_k)/2. They all lie between zero and one, and only the zero mode equals exactly one.

### [01:56.4] The heat kernel at the identity — `manim:S05`

**ES:** Expandiendo la delta en caracteres, el valor en la identidad es p_ℓ(e) = (1/r) Σ λ_k^ℓ. El término k = 0 da exactamente uno sobre r; los demás decaen. En el ejemplo, tras cinco pasos vale cero coma cero siete nueve; tras diez, cero coma cero tres seis; tras veinte, cero coma cero tres cero cuatro, ya muy cerca de uno sobre treinta y tres. Calculado con la fórmula espectral o multiplicando la matriz, el resultado coincide hasta la precisión de la máquina.

**EN:** Expanding the delta in characters, the value at the identity is p_ℓ(e) = (1/r) Σ λ_k^ℓ. The k = 0 term gives exactly one over r; the others decay. In the example, after five steps it is 0.079; after ten, 0.036; after twenty, 0.0304, already very close to one over thirty-three. Computed with the spectral formula or by multiplying the matrix, the result agrees to machine precision.

### [02:31.6] Why dyadic generators — `manim:S06`

**ES:** ¿Por qué potencias de dos? Con solo los saltos ± 1, el grafo es un ciclo y el valor propio más lento es cero coma nueve nueve: hacen falta setecientos sesenta y dos pasos para que los modos bajen de una milésima. Con los generadores diádicos, el más lento es cero coma seis seis nueve, y bastan dieciocho pasos. Las potencias de dos dispersan cualquier frecuencia: es la idea del lema de duplicación de la próxima lección.

**EN:** Why powers of two? With only ± 1 jumps, the graph is a cycle and the slowest eigenvalue is 0.99: seven hundred sixty-two steps are needed for the modes to drop below one thousandth. With the dyadic generators, the slowest is 0.669, and eighteen steps suffice. Powers of two scatter any frequency: that is the idea of the doubling lemma in the next lesson.

### [02:59.2] Applications — `slide`

**ES:** Los núcleos de calor en grupos describen los tiempos de mezcla de cadenas de Markov, como barajar cartas; aparecen en mapas de difusión y redes neuronales sobre grafos, y en los grafos expansores, que mezclan rápido con pocos generadores. En el laboratorio diez construirás esta caminata.

**EN:** Heat kernels on groups describe mixing times of Markov chains, such as shuffling cards; they appear in diffusion maps and graph neural networks, and in expander graphs, which mix fast with few generators. In lab ten you will build this walk.

### [03:18.1] Common mistakes — `slide`

**ES:** Errores comunes: olvidar la pereza, sin la cual puede haber un valor propio menos uno que impide asentarse. Creer que hace falta el orden para construir el grafo. Confundir los valores propios de P y de W. Y simular el vector completo en digital, que cuesta r por paso y pierde la ventaja.

**EN:** Common mistakes: forgetting laziness, without which there may be an eigenvalue of minus one that prevents settling. Believing the order is needed to build the graph. Confusing the eigenvalues of P and of W. And simulating the full vector digitally, which costs r per step and loses the advantage.

### [03:37.6] Summary — `manim:S09`

**ES:** En resumen: el grafo de Cayley de ⟨b⟩ con generadores diádicos se construye sin conocer el orden. La caminata semi-perezosa es una ecuación del calor discreta, diagonalizada por caracteres. Su valor en la identidad tiende a uno sobre r, y las potencias de dos hacen que lo alcance en pocos pasos.

**EN:** In summary: the Cayley graph of ⟨b⟩ with dyadic generators is built without knowing the order. The half-lazy walk is a discrete heat equation, diagonalized by characters. Its value at the identity tends to one over r, and powers of two make it get there in few steps.

### [03:58.8] Self-assessment — `slide`

**ES:** Para practicar: escribe los vecinos de un nodo. Demuestra que los caracteres son vectores propios. Explica por qué los valores propios de W están entre cero y uno. Y deduce la fórmula del núcleo de calor en la identidad.

**EN:** To practice: write the neighbors of a node. Prove that the characters are eigenvectors. Explain why the eigenvalues of W lie between zero and one. And derive the heat-kernel formula at the identity.

## Key equations
- $$(Pp)(j) = \frac{1}{2(M+1)}\sum_{t=0}^{M}\big[p(j + 2^t) + p(j - 2^t)\big],\qquad W = \tfrac12(I + P)$$ — Half-lazy dyadic walk on $\mathbb Z/r\mathbb Z$ (exponent coordinates).
- $$\mu_k = \frac{1}{M+1}\sum_{t=0}^{M}\cos\frac{2\pi k 2^t}{r},\qquad \lambda_k = \frac{1 + \mu_k}{2}$$ — Character eigenvalues of $P$ and $W$.
- $$p_\ell(e) = (W^\ell\delta_e)(e) = \frac1r\sum_{k=0}^{r-1}\lambda_k^\ell \ \xrightarrow{\ \ell\to\infty\ }\ \frac1r$$ — Heat kernel at the identity.

## Summary
- Cayley graph of ⟨b⟩ with generators b^(±2^t): built without knowing r.
- Half-lazy walk W = ½(I + P): discrete heat equation.
- Characters diagonalize W; p_ℓ(e) = (1/r) Σ λ_k^ℓ → 1/r.
- r = 33: max λ = 0.669 (dyadic) vs 0.991 (cycle); 18 vs 762 steps to 10⁻³.

## Further reading
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
- D. A. Levin, Y. Peres and E. L. Wilmer, Markov Chains and Mixing Times, AMS (2009).
- P. Diaconis, Group Representations in Probability and Statistics, IMS (1988).
