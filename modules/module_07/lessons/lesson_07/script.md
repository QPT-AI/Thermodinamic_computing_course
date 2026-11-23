# Lesson 7.7 — The collision variant

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Turn a collision of two random words into a relation $r \mid D$.
- Estimate the number of samples to the first collision with the birthday bound $T \approx \sqrt{r}$.
- Recover $r$ from running gcds and explain the $1/\zeta(s)$ law; relate the method to Pollard's rho.

## Prerequisites
- Lesson 7.3: words in the dyadic generators.
- Probability: the birthday paradox.

## Narrated script

### [00:04.9] Introduction — `manim:S01`

**ES:** La difusión necesita un hardware con r nodos y una lectura muy precisa. Existe una alternativa puramente digital que usa el mismo grafo: lanzar caminantes al azar y esperar a que dos caigan en el mismo nodo. Cada coincidencia, o colisión, revela un múltiplo del orden. Hoy vemos cuántas muestras hacen falta y cómo se extrae el orden.

**EN:** Diffusion needs hardware with r nodes and a very precise readout. There is a purely digital alternative that uses the same graph: launch random walkers and wait for two to land on the same node. Each coincidence, or collision, reveals a multiple of the order. Today we see how many samples are needed and how the order is extracted.

### [00:27.1] Words and relations — `manim:S02`

**ES:** Una palabra es una sucesión de saltos ± 2^t. Su exponente total E es un entero, y su punto final es b^E mod N, que se calcula con exponenciación modular. Si dos palabras con exponentes distintos llegan al mismo punto, entonces b^D ≡ 1 con D la diferencia de exponentes: el orden r divide a D. Una colisión es una relación.

**EN:** A word is a sequence of ± 2^t jumps. Its total exponent E is an integer, and its endpoint is b^E mod N, computed with modular exponentiation. If two words with different exponents reach the same point, then b^D ≡ 1 with D the difference of exponents: the order r divides D. A collision is a relation.

### [00:53.3] The birthday bound — `manim:S03`

**ES:** ¿Cuántas muestras hasta la primera colisión? Es la paradoja del cumpleaños: con T puntos casi uniformes en r casillas, el número esperado de pares que coinciden es T(T − 1)/(2r), y la primera colisión aparece hacia √(π r/2) muestras. Lo simulamos con N igual a un millón veintidós mil ciento diecisiete y orden cinco mil trescientos trece: en mil repeticiones, la primera colisión llega en promedio en la muestra noventa y cuatro coma seis, frente a la predicción de noventa y uno coma cuatro.

**EN:** How many samples until the first collision? It is the birthday paradox: with T nearly uniform points in r boxes, the expected number of matching pairs is T(T − 1)/(2r), and the first collision appears around √(π r/2) samples. We simulate it with N equal to one million twenty-two thousand one hundred seventeen and order five thousand three hundred thirteen: over a thousand repetitions, the first collision arrives on average at sample 94.6, against the prediction of 91.4.

### [01:27.0] Running gcd and the zeta law — `manim:S04`

**ES:** Cada relación es D_i = q_i r con un multiplicador desconocido. El máximo común divisor acumulado de las D_i es siempre un múltiplo de r, y es exactamente r cuando los q_i no comparten factores. Si se comportan como enteros al azar, eso ocurre con s relaciones con probabilidad uno sobre zeta de s: sesenta y uno por ciento con dos, ochenta y tres con tres, noventa y dos con cuatro. En la simulación, dos relaciones bastaron el sesenta por ciento de las veces, tres o menos el ochenta y cinco, y cuatro o menos el noventa y cuatro.

**EN:** Each relation is D_i = q_i r with an unknown multiplier. The running greatest common divisor of the D_i is always a multiple of r, and it is exactly r when the q_i share no factors. If they behave like random integers, that happens with s relations with probability one over zeta of s: sixty-one percent with two, eighty-three with three, ninety-two with four. In the simulation, two relations sufficed sixty percent of the time, three or fewer eighty-five, and four or fewer ninety-four.

### [02:04.0] Link with Pollard's rho — `manim:S05`

**ES:** Esta idea tiene un pariente famoso: el método rho de Pollard. Rho busca colisiones módulo un factor primo desconocido p de N, así que la escala es √p, es decir, del orden de N^(1/4) para un semiprimo, y detecta la colisión con el máximo común divisor, sin saber p. La variante de esta lección busca colisiones del orden r, que puede ser del tamaño de N: la escala √r puede ser mucho peor.

**EN:** This idea has a famous relative: Pollard's rho method. Rho looks for collisions modulo an unknown prime factor p of N, so the scale is √p, that is, of order N^(1/4) for a semiprime, and it detects the collision with the greatest common divisor, without knowing p. The variant in this lesson looks for collisions of the order r, which can be as large as N: the √r scale can be much worse.

### [02:33.0] Honest comparison — `manim:S06`

**ES:** El tratado de factorización por difusión lleva esta línea más lejos, con detectores sensibles a divisores que alcanzan la escala de N^(1/4) con garantías probadas. Pero su conclusión es honesta: en la comparación reproducible en software, Pollard con la mejora de Brent sigue siendo más rápido. Las colisiones son una herramienta útil para entender la estructura, no una vía nueva para romper criptografía.

**EN:** The treatise on diffusion-based factoring takes this line further, with divisor-sensitive detectors that reach the N^(1/4) scale with proven guarantees. But its conclusion is honest: in the reproducible software comparison, Pollard with Brent's improvement is still faster. Collisions are a useful tool for understanding the structure, not a new way to break cryptography.

### [02:58.8] Applications — `slide`

**ES:** El razonamiento del cumpleaños aparece en colisiones de funciones hash y en la detección de ciclos con poca memoria, como los métodos de Floyd y de Brent; los métodos rho y canguro resuelven logaritmos discretos. En el laboratorio diez compararás la variante por colisiones con Pollard y Brent.

**EN:** Birthday reasoning appears in hash-function collisions and in low-memory cycle detection, such as Floyd's and Brent's methods; the rho and kangaroo methods solve discrete logarithms. In lab ten you will compare the collision variant with Pollard and Brent.

### [03:17.8] Common mistakes — `slide`

**ES:** Errores comunes: contar colisiones triviales, con el mismo exponente, que dan diferencia cero. Tomar una sola relación como el orden, cuando es solo un múltiplo. Suponer que palabras muy cortas ya dan puntos uniformes. Y confundir la escala raíz de r con la raíz de p de Pollard.

**EN:** Common mistakes: counting trivial collisions, with the same exponent, which give a zero difference. Taking a single relation as the order, when it is only a multiple. Assuming very short words already give uniform points. And confusing the root-of-r scale with Pollard's root-of-p scale.

### [03:36.8] Summary — `manim:S09`

**ES:** En resumen: dos palabras que llegan al mismo punto dan un múltiplo del orden. La primera colisión aparece hacia raíz de r muestras, y el máximo común divisor de unas pocas relaciones da el orden, con la ley de uno sobre zeta. Es el mismo principio del método rho de Pollard, que en la práctica sigue ganando.

**EN:** In summary: two words reaching the same point give a multiple of the order. The first collision appears around root-of-r samples, and the greatest common divisor of a few relations gives the order, following the one-over-zeta law. It is the same principle as Pollard's rho method, which in practice still wins.

### [03:57.1] Self-assessment — `slide`

**ES:** Para practicar: demuestra que una colisión no trivial da un múltiplo del orden. Calcula los pares esperados para cien muestras. Calcula la probabilidad de acertar con tres relaciones. Y explica la escala de Pollard.

**EN:** To practice: prove that a nontrivial collision gives a multiple of the order. Compute the expected pairs for one hundred samples. Compute the probability of success with three relations. And explain Pollard's scale.

## Key equations
- $$b^{E(w)} \equiv b^{E(w')} \pmod N,\ E(w) \ne E(w')\ \Rightarrow\ r \mid D = E(w) - E(w')$$ — A nontrivial collision is a relation.
- $$\mathbb E[Z] = \binom T2 s_2(t) \approx \frac{T(T-1)}{2r},\qquad T_{\text{first}} \approx \sqrt{\pi r/2}$$ — Birthday bound for independent restarts.
- $$\gcd(D_1, \dots, D_s) = r\,\gcd(q_1, \dots, q_s),\qquad \Pr\big(\gcd(q_1, \dots, q_s) = 1\big) \to \frac{1}{\zeta(s)}$$ — Running gcd and the zeta law (heuristic independence model).

## Summary
- Collision of two words ⇒ relation r | D.
- First collision ≈ √(πr/2): 94.6 observed vs 91.4 predicted (r = 5313) [S].
- Running gcd: 2 relations 60 %, ≤ 3: 85 %, ≤ 4: 94 % (1/ζ: 0.61, 0.83, 0.92).
- Pollard's rho: √p ~ N^(1/4) scale; Pollard–Brent still faster in practice.

## Further reading
- Cadavid et al., Treatise on diffusion-driven factorization (course data/), Sections 6–7 and 12–13, 2026.
- J. M. Pollard, A Monte Carlo method for factorization, BIT 15, 331 (1975).
- R. P. Brent, An improved Monte Carlo factorization algorithm, BIT 20, 176 (1980).
