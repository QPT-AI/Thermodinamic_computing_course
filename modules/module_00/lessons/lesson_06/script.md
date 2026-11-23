# Lesson 0.6 — Fourier analysis on finite abelian groups

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the characters of $\mathbb Z/r\mathbb Z$, $\chi_k(x) = e^{2\pi i kx/r}$, and check that they are homomorphisms.
- Prove orthogonality $\sum_x \chi_k(x)\overline{\chi_l(x)} = r\,\delta_{kl}$.
- Use the discrete Fourier transform to diagonalize random walks on a cycle.

## Prerequisites
- Complex numbers: $e^{i\theta} = \cos\theta + i\sin\theta$.
- Lesson 0.5: Markov chains and eigenvalues.

## Narrated script

### [00:06.0] Introduction — `manim:S01`

**ES:** El algoritmo de Shor y el algoritmo termodinámico de búsqueda de orden por difusión, que estudiaremos en la unidad siete, comparten un mismo lenguaje: el análisis de Fourier sobre los enteros módulo r. Shor amplifica picos de Fourier con interferencia cuántica; la difusión amortigua todos los modos de Fourier salvo uno. Para entender ambos necesitamos los caracteres de un grupo finito y su propiedad clave, la ortogonalidad.

**EN:** Shor's algorithm and the thermodynamic order-finding-by-diffusion algorithm, which we study in unit seven, share one language: Fourier analysis over the integers modulo r. Shor amplifies Fourier peaks with quantum interference; diffusion damps every Fourier mode except one. To understand both we need the characters of a finite group and their key property, orthogonality.

### [00:33.2] Intuition — `manim:S02`

**ES:** Los enteros módulo r son la aritmética de un reloj de r horas: después de r menos uno viene el cero. Pongamos esas r posiciones sobre el círculo unitario del plano complejo. Elegimos una frecuencia k: la posición x se envía al punto que está k por x pasos de r más allá en la circunferencia. Con frecuencia uno, damos una vuelta completa al recorrer el reloj; con frecuencia dos, damos dos vueltas. Cada frecuencia es una onda que vive en el reloj.

**EN:** The integers modulo r are the arithmetic of an r-hour clock: after r minus one comes zero. Let's place those r positions on the unit circle of the complex plane. We choose a frequency k: position x is sent to the point k times x steps of r further around the circle. With frequency one, we go around once as we traverse the clock; with frequency two, twice. Each frequency is a wave living on the clock.

### [01:03.6] Characters — `manim:S03`

**ES:** Esa onda es un carácter: χ_k(x) = e^(2πikx/r). Su propiedad esencial es que convierte sumas en productos: χ_k(x + y) = χ_k(x) χ_k(y). Sumar en el reloj equivale a componer rotaciones en el círculo. Hay exactamente r caracteres distintos, uno por cada frecuencia de cero a r menos uno. El carácter de frecuencia cero es constante e igual a uno.

**EN:** That wave is a character: χ_k(x) = e^(2πikx/r). Its essential property is that it turns sums into products: χ_k(x + y) = χ_k(x) χ_k(y). Adding on the clock is equivalent to composing rotations on the circle. There are exactly r distinct characters, one for each frequency from zero to r minus one. The zero-frequency character is constant and equal to one.

### [01:31.7] Orthogonality — `manim:S04`

**ES:** Ahora sumemos todos los valores de un carácter. Cada valor es un vector unitario. Si los ponemos uno tras otro, punta con cola, forman un polígono regular que se cierra: la suma es cero. Solo cuando la frecuencia es un múltiplo de r todos los vectores apuntan en la misma dirección y la suma vale r. De aquí sale la ortogonalidad: el producto interno de dos caracteres distintos es cero, y el de un carácter consigo mismo es r.

**EN:** Now let's add up all the values of a character. Each value is a unit vector. If we place them head to tail, they form a regular polygon that closes: the sum is zero. Only when the frequency is a multiple of r do all vectors point the same way and the sum equals r. Orthogonality follows: the inner product of two different characters is zero, and that of a character with itself is r.

### [02:00.2] Fourier transform — `manim:S05`

**ES:** Como los caracteres son r vectores ortogonales en un espacio de dimensión r, forman una base. Cualquier función sobre el reloj se escribe como combinación de ondas. Los coeficientes son la transformada de Fourier discreta, f̂(k) = Σ f(x) χ̄_k(x), y la función se recupera sumando las ondas con esos pesos y dividiendo por r. La animación construye la función de barras sumando una onda a la vez.

**EN:** Since the characters are r orthogonal vectors in an r-dimensional space, they form a basis. Any function on the clock can be written as a combination of waves. The coefficients are the discrete Fourier transform, f̂(k) = Σ f(x) χ̄_k(x), and the function is recovered by adding the waves with those weights and dividing by r. The animation builds the bar function by adding one wave at a time.

### [02:30.3] Walks and the heat kernel — `manim:S06`

**ES:** ¿Por qué esto importa para el cómputo termodinámico? Una caminata aleatoria en el ciclo es una convolución, y los caracteres diagonalizan cualquier convolución. Para la caminata perezosa, que se queda con probabilidad un medio y se mueve a cada vecino con un cuarto, el valor propio del modo k es ½ (1 + cos(2πk/r)). Observa la probabilidad de un caminante que parte del cero: se difunde por el anillo. En la representación de Fourier, cada modo decae con su propio factor, y solo el modo cero sobrevive. Esta distribución es el núcleo de calor discreto, y su valor en el origen, la probabilidad de regreso, es el promedio de las potencias de los valores propios.

**EN:** Why does this matter for thermodynamic computing? A random walk on the cycle is a convolution, and characters diagonalize any convolution. For the lazy walk, which stays with probability one half and moves to each neighbor with one quarter, the eigenvalue of mode k is ½ (1 + cos(2πk/r)). Watch the probability of a walker starting at zero: it spreads around the ring. In the Fourier representation, each mode decays by its own factor, and only the zero mode survives. This distribution is the discrete heat kernel, and its value at the origin, the return probability, is the average of the powers of the eigenvalues.

### [03:13.7] Numerical example — `manim:S07`

**ES:** Calculemos una transformada pequeña con r = 4 y la función uno, dos, cero, uno. Los caracteres de cuatro valores toman los valores uno, i, menos uno y menos i. El coeficiente de frecuencia cero es la suma, cuatro. El de frecuencia uno es uno menos i. El de frecuencia dos es menos dos, y el de frecuencia tres, uno más i. Comprobemos la igualdad de Parseval: la suma de cuadrados de la función es seis, y la de la transformada es veinticuatro, que dividido por cuatro da seis.

**EN:** Let's compute a small transform with r = 4 and the function one, two, zero, one. The characters of four take the values one, i, minus one and minus i. The zero-frequency coefficient is the sum, four. The frequency-one coefficient is one minus i. The frequency-two one is minus two, and the frequency-three one, one plus i. Let's check Parseval's identity: the sum of squares of the function is six, and that of the transform is twenty-four, which divided by four gives six.

### [03:48.0] Applications — `slide`

**ES:** En la unidad siete usaremos todo esto. Shor usa una transformada cuántica de Fourier para revelar el período de una función modular. El algoritmo de difusión obtiene el mismo período a partir de la probabilidad de regreso de una caminata aleatoria, que es exactamente un promedio de potencias de valores propios de Fourier.

**EN:** In unit seven we will use all of this. Shor uses a quantum Fourier transform to reveal the period of a modular function. The diffusion algorithm obtains the same period from the return probability of a random walk, which is exactly an average of powers of Fourier eigenvalues.

### [04:08.4] Connections — `slide`

**ES:** Todo grupo abeliano finito es un producto de grupos cíclicos, y sus caracteres son productos de los que vimos hoy. En la unidad siete aplicaremos esta maquinaria a grafos de Cayley, y en los modelos de difusión de la unidad nueve veremos que la difusión borra primero las frecuencias altas.

**EN:** Every finite abelian group is a product of cyclic groups, and its characters are products of the ones we saw today. In unit seven we will apply this machinery to Cayley graphs, and in the diffusion models of unit nine we will see that diffusion erases high frequencies first.

### [04:26.6] Common mistakes — `slide`

**ES:** Errores frecuentes: olvidar el conjugado en el producto interno, olvidar el factor uno sobre r en la transformada inversa, y confundir la frecuencia con la posición. Recuerda también que la suma de las raíces de la unidad vale r siempre que r divida a k, no solo cuando k es cero.

**EN:** Frequent mistakes: forgetting the conjugate in the inner product, forgetting the one-over-r factor in the inverse transform, and confusing frequency with position. Remember too that the sum of the roots of unity equals r whenever r divides k, not only when k is zero.

### [04:45.9] Summary — `manim:S11`

**ES:** En resumen: los caracteres de los enteros módulo r son ondas que convierten sumas en productos. Son ortogonales porque las raíces de la unidad suman cero. Forman una base, la transformada de Fourier, y diagonalizan las caminatas aleatorias en el ciclo, cuyos modos decaen con sus valores propios.

**EN:** In summary: the characters of the integers modulo r are waves that turn sums into products. They are orthogonal because the roots of unity sum to zero. They form a basis, the Fourier transform, and they diagonalize random walks on the cycle, whose modes decay with their eigenvalues.

### [05:05.9] Self-assessment — `slide`

**ES:** Para practicar: calcula la suma de las raíces de la unidad para cualquier k. Verifica la propiedad de homomorfismo. Calcula dos transformadas de Fourier de cuatro puntos. Y encuentra los valores propios y la brecha de la caminata perezosa en un ciclo de ocho estados.

**EN:** To practice: compute the sum of the roots of unity for any k. Check the homomorphism property. Compute two four-point Fourier transforms. And find the eigenvalues and the gap of the lazy walk on an eight-state cycle.

## Key equations
- $$\chi_k(x) = e^{2\pi i kx/r},\quad \chi_k(x+y) = \chi_k(x)\chi_k(y)$$ — Characters of $\mathbb Z/r\mathbb Z$: homomorphisms to the unit circle.
- $$\sum_{x=0}^{r-1} \chi_k(x)\overline{\chi_l(x)} = r\,\delta_{kl},\quad \sum_{j=0}^{r-1} e^{2\pi i jk/r} = r\,[r \mid k]$$ — Orthogonality of characters and the sum of roots of unity.
- $$\hat f(k) = \sum_x f(x)\overline{\chi_k(x)},\quad f(x) = \frac1r\sum_k \hat f(k)\chi_k(x)$$ — Discrete Fourier transform and its inverse.
- $$p_n(x) = \frac1r\sum_k \lambda_k^n\,\chi_k(x),\quad \lambda_k = \tfrac12\big(1 + \cos\tfrac{2\pi k}{r}\big)$$ — Heat kernel of the lazy walk: each mode decays as $\lambda_k^n$.

## Summary
- Characters $\chi_k(x) = e^{2\pi ikx/r}$: waves on the clock that turn sums into products.
- Orthogonality: the roots of unity sum to zero unless $r \mid k$.
- DFT: basis of characters; inverse with factor $1/r$; Parseval.
- They diagonalize walks on the cycle: $p_n(x) = \frac1r\sum_k \lambda_k^n\chi_k(x)$.

## Further reading
- [34] C. A. Cadavid et al., On an approach for evaluating certain trigonometric character sums using the discrete time heat kernel, 2022.
- [4] Nielsen and Chuang, ch. 5 (quantum Fourier transform).
- [3] Levin, Peres and Wilmer, ch. 12 (eigenvalues of walks on groups).
