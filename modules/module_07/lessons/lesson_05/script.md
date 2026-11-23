# Lesson 7.5 — Trigonometric sum identities

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Compute the return probability of a Cayley walk in two ways: counting words (combinatorial) and summing eigenvalues (spectral).
- Derive $\tfrac1r\sum_k\cos^{2\ell}(\pi k/r) = 4^{-\ell}\sum_j\binom{2\ell}{\ell + jr}$ from the uniqueness of the heat kernel.
- State the dyadic (lacunary) version and use it as an exact check of simulations and hardware.

## Prerequisites
- Lessons 7.3–7.4: heat kernel and characters.
- Binomial coefficients and generating functions.

## Narrated script

### [00:05.5] Introduction — `manim:S01`

**ES:** Cuando una misma cantidad se puede calcular de dos maneras distintas, igualar las dos respuestas produce una identidad gratis. La probabilidad de que la caminata vuelva a la identidad es una de esas cantidades: se puede contar caminos o sumar valores propios. Hoy obtenemos así identidades de sumas trigonométricas, algunas clásicas y otras nuevas.

**EN:** When the same quantity can be computed in two different ways, equating the two answers produces an identity for free. The probability that the walk returns to the identity is one of those quantities: one can count paths or sum eigenvalues. Today we obtain trigonometric sum identities this way, some classical and some new.

### [00:28.4] Combinatorial form — `manim:S02`

**ES:** En coordenadas de exponente, cada paso suma cero con probabilidad un medio, o un ± 2^t con probabilidad pequeña. Tras ℓ pasos tenemos un exponente total E, un entero cualquiera, sin reducir. La caminata está en la identidad exactamente cuando E es múltiplo de r. Así que la probabilidad de retorno es la suma de las probabilidades de E = j r sobre todos los enteros j. Lo notable: la distribución de E no depende de r; el orden solo aparece al final, al preguntar qué exponentes son múltiplos.

**EN:** In exponent coordinates, each step adds zero with probability one half, or ± 2^t with a small probability. After ℓ steps we have a total exponent E, any integer, not reduced. The walk is at the identity exactly when E is a multiple of r. So the return probability is the sum of the probabilities of E = j r over all integers j. The remarkable part: the distribution of E does not depend on r; the order only appears at the end, when asking which exponents are multiples.

### [01:03.9] Spectral form — `manim:S03`

**ES:** La otra forma es la de la lección siete punto tres: la probabilidad de retorno es el promedio de λ_k^ℓ sobre las r frecuencias. El núcleo de calor es único: ambas expresiones describen la misma probabilidad. Por lo tanto, la suma combinatoria es igual a la suma espectral para todo r y todo ℓ.

**EN:** The other form is the one from lesson 7.3: the return probability is the average of λ_k^ℓ over the r frequencies. The heat kernel is unique: both expressions describe the same probability. Therefore, the combinatorial sum equals the spectral sum for every r and every ℓ.

### [01:24.9] A classical identity — `manim:S04`

**ES:** Veámoslo en el caso más simple: el ciclo con saltos ± 1. Su valor propio es cos²(πk/r). Y un paso perezoso equivale a dos medios pasos de ± ½, así que el desplazamiento sigue una binomial. La identidad que sale es (1/r) Σ cos^(2ℓ)(πk/r) = 4^(−ℓ) Σ C(2ℓ, ℓ + j r). Con r = 5 y ℓ = 3, ambos lados valen veinte sobre sesenta y cuatro: cero coma tres uno dos cinco.

**EN:** Let's see it in the simplest case: the cycle with ± 1 jumps. Its eigenvalue is cos²(πk/r). And a lazy step is equivalent to two half steps of ± ½, so the displacement follows a binomial. The identity that comes out is (1/r) Σ cos^(2ℓ)(πk/r) = 4^(−ℓ) Σ C(2ℓ, ℓ + j r). With r = 5 and ℓ = 3, both sides equal twenty over sixty-four: 0.3125.

### [01:57.9] The dyadic identity — `manim:S05`

**ES:** Con los generadores diádicos obtenemos una identidad lacunaria nueva: el promedio de λ_k^ℓ, donde cada λ_k es un promedio de cosenos de 2πk2^t/r, es igual a la probabilidad de que una suma de saltos diádicos sea múltiplo de r. Para r = 33 y diez pasos, el lado combinatorio, calculado como fracción exacta con siete mil setecientos treinta y siete exponentes posibles, vale cero coma cero tres cinco ocho tres seis cinco cuatro ocho, y el lado espectral coincide hasta la última cifra de la máquina.

**EN:** With the dyadic generators we obtain a new lacunary identity: the average of λ_k^ℓ, where each λ_k is an average of cosines of 2πk2^t/r, equals the probability that a sum of dyadic jumps is a multiple of r. For r = 33 and ten steps, the combinatorial side, computed as an exact fraction with seven thousand seven hundred thirty-seven possible exponents, equals 0.035836548, and the spectral side agrees to the last digit of the machine.

### [02:33.0] What the identities are for — `manim:S06`

**ES:** ¿Para qué sirven? Primero, como prueba: la forma combinatoria muestra que el valor es un número racional con denominador conocido, y la espectral, que converge a uno sobre r. Segundo, como control: cualquier simulación o hardware de difusión debe reproducir exactamente estos valores en casos pequeños. Tercero, como herramienta: las sumas lacunarias son difíciles de acotar directamente, y la interpretación como caminata da estimaciones gratis.

**EN:** What are they for? First, as proof: the combinatorial form shows that the value is a rational number with a known denominator, and the spectral form, that it converges to one over r. Second, as a check: any simulation or diffusion hardware must reproduce these values exactly in small cases. Third, as a tool: lacunary sums are hard to bound directly, and the walk interpretation gives estimates for free.

### [03:03.0] Applications — `slide`

**ES:** Úsalas como pruebas unitarias de simuladores y prototipos de difusión, reconoce en ellas identidades clásicas de multisección de binomiales, y acota sumas lacunarias con tiempos de mezcla. En el laboratorio diez verificarás ambas formas.

**EN:** Use them as unit tests for diffusion simulators and prototypes, recognize in them classical binomial multisection identities, and bound lacunary sums with mixing times. In lab ten you will verify both forms.

### [03:19.0] Common mistakes — `slide`

**ES:** Errores comunes: reducir el exponente módulo r en cada paso, lo que exige conocer el orden desde el principio. Olvidar el peso perezoso. Mezclar los valores propios de P y de W. Y verificar solo en coma flotante, cuando conviene usar fracciones exactas.

**EN:** Common mistakes: reducing the exponent modulo r at every step, which requires knowing the order from the start. Forgetting the lazy weight. Mixing the eigenvalues of P and W. And checking only in floating point, when exact fractions are better.

### [03:37.6] Summary — `manim:S09`

**ES:** En resumen: la probabilidad de retorno se calcula contando sumas de saltos que son múltiplos de r o promediando potencias de valores propios. Como el núcleo de calor es único, ambas coinciden, y eso da identidades trigonométricas exactas, desde la clásica de cosenos y binomiales hasta la lacunaria diádica.

**EN:** In summary: the return probability is computed by counting jump sums that are multiples of r or by averaging powers of eigenvalues. Since the heat kernel is unique, both agree, and that gives exact trigonometric identities, from the classical one of cosines and binomials to the dyadic lacunary one.

### [03:58.3] Self-assessment — `slide`

**ES:** Para practicar: verifica la identidad del ciclo a mano en un caso pequeño. Explica la equivalencia del paso perezoso con dos medios pasos. Encuentra el denominador del lado combinatorio. Y di qué lado muestra el límite inmediatamente.

**EN:** To practice: verify the cycle identity by hand in a small case. Explain the equivalence of the lazy step with two half steps. Find the denominator of the combinatorial side. And say which side shows the limit immediately.

## Key equations
- $$p_\ell(e) = \sum_{j\in\mathbb Z}\Pr\big(E_\ell = jr\big) = \frac1r\sum_{k=0}^{r-1}\lambda_k^\ell$$ — Combinatorial = spectral (uniqueness of the heat kernel).
- $$\frac1r\sum_{k=0}^{r-1}\cos^{2\ell}\frac{\pi k}{r} = 4^{-\ell}\sum_{j\in\mathbb Z}\binom{2\ell}{\ell + jr}$$ — Cycle with ±1 steps: a classical binomial multisection identity.
- $$\frac1r\sum_{k}\Big[\tfrac12\Big(1 + \tfrac{1}{M+1}\sum_{t=0}^{M}\cos\tfrac{2\pi k2^t}{r}\Big)\Big]^\ell = \Pr\Big(\textstyle\sum_{i\le\ell}\xi_i \equiv 0 \ (r)\Big)$$ — Dyadic lacunary identity; $\xi_i \in \{0, \pm 2^t\}$ with lazy weight 1/2.

## Summary
- Return probability: count jump sums ≡ 0 mod r, or average λ_k^ℓ.
- Cycle: (1/r) Σ cos^(2ℓ)(πk/r) = 4^(−ℓ) Σ_j C(2ℓ, ℓ + jr); r = 5, ℓ = 3: 0.3125.
- Dyadic: r = 33, ℓ = 10: 0.0358365488 both ways (exact fraction) [S].
- Uses: proofs, exact checks of simulators/hardware, bounds on lacunary sums.

## Further reading
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
- Cadavid et al., Treatise on diffusion-driven factorization (course data/), Sections 2 and 4, 2026.
- R. L. Graham, D. E. Knuth and O. Patashnik, Concrete Mathematics, Addison-Wesley (1994).
