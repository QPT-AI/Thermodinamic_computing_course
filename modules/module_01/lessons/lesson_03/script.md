# Lesson 1.3 — Shannon entropy and Gibbs entropy

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Interpret Shannon entropy as the average number of binary questions needed.
- Relate Gibbs entropy to Shannon entropy: $S = k_B\ln 2\cdot H$.
- Split physical entropy into a logical part and an internal part: information is physical.

## Prerequisites
- Lesson 0.3: Shannon entropy.
- Lessons 1.1–1.2: $S = k_B\ln\Omega$ and the Boltzmann distribution.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Shannon, pensando en mensajes telegráficos, escribió una fórmula para la información. Gibbs, setenta años antes, había escrito la misma fórmula para la entropía de un gas. ¿Es una coincidencia? En absoluto. En esta lección veremos que ambas miden lo mismo, la incertidumbre sobre un estado, y que la constante que las convierte, k_B ln 2, es el puente entre bits y julios por kelvin. Esa es la frase de Landauer: la información es física.

**EN:** Shannon, thinking about telegraph messages, wrote a formula for information. Gibbs, seventy years earlier, had written the same formula for the entropy of a gas. Is it a coincidence? Not at all. In this lesson we will see that both measure the same thing, uncertainty about a state, and that the constant converting them, k_B ln 2, is the bridge between bits and joules per kelvin. That is Landauer's phrase: information is physical.

### [00:36.6] Intuition — `manim:S02`

**ES:** Juguemos a adivinar. Escondo una carta entre ocho igualmente probables. La mejor estrategia es partir el conjunto por la mitad con cada pregunta de sí o no. Con tres preguntas siempre la encuentro: tres bits. Ahora supón que las cartas no son igualmente probables: una sale la mitad de las veces, otra un cuarto y dos un octavo cada una. Conviene preguntar primero por la más probable. El número medio de preguntas baja a uno coma setenta y cinco. Esa cifra es exactamente la entropía de Shannon de la distribución.

**EN:** Let's play a guessing game. I hide one card among eight equally likely ones. The best strategy is to split the set in half with each yes-or-no question. With three questions I always find it: three bits. Now suppose the cards are not equally likely: one comes up half the time, another a quarter, and two one eighth each. It pays to ask about the most likely one first. The average number of questions drops to 1.75. That figure is exactly the Shannon entropy of the distribution.

### [01:09.5] Shannon entropy — `manim:S03`

**ES:** La entropía de Shannon es H = −Σ p log₂ p. Cada resultado de probabilidad p aporta una sorpresa de menos logaritmo de p bits, y la entropía es la sorpresa promedio. El teorema de codificación de Shannon dice que ningún código puede usar, en promedio, menos de H bits por símbolo, y que se puede llegar tan cerca como se quiera. En el árbol de preguntas, la profundidad de cada hoja es su sorpresa.

**EN:** Shannon entropy is H = −Σ p log₂ p. Each outcome of probability p contributes a surprise of minus log p bits, and entropy is the average surprise. Shannon's coding theorem says no code can use, on average, fewer than H bits per symbol, and that you can get as close as you like. In the question tree, the depth of each leaf is its surprise.

### [01:39.1] Gibbs entropy — `manim:S04`

**ES:** La entropía de Gibbs aplica la misma fórmula a los microestados físicos, con logaritmo natural y la constante de Boltzmann: S = −k_B Σ p ln p. Si todos los microestados accesibles son igualmente probables, se reduce a k_B ln Ω, la fórmula de Boltzmann. Y si la distribución es la de Boltzmann, la entropía de Gibbs coincide con la termodinámica. Cambiar de base de logaritmo es solo cambiar de unidades: un bit equivale a k_B ln 2 de entropía física.

**EN:** Gibbs entropy applies the same formula to physical microstates, with the natural log and Boltzmann's constant: S = −k_B Σ p ln p. If all accessible microstates are equally likely, it reduces to k_B ln Ω, Boltzmann's formula. And if the distribution is Boltzmann's, Gibbs entropy matches the thermodynamic one. Changing the log base is just changing units: one bit is worth k_B ln 2 of physical entropy.

### [02:14.6] Information is physical — `manim:S05`

**ES:** Una memoria es un sistema físico cuyo espacio de microestados está dividido en regiones lógicas: la región del cero y la región del uno. La entropía física total se separa en dos partes: la entropía de Shannon de los estados lógicos, multiplicada por k_B ln 2, más el promedio de la entropía interna de cada región. Cuando borramos, fusionamos las regiones lógicas: la parte lógica desaparece y, por la segunda ley, esa entropía tiene que salir al entorno. Los bits no son abstracciones: cuentan microestados.

**EN:** A memory is a physical system whose space of microstates is divided into logical regions: the zero region and the one region. The total physical entropy splits into two parts: the Shannon entropy of the logical states, times k_B ln 2, plus the average internal entropy of each region. When we erase, we merge the logical regions: the logical part disappears and, by the second law, that entropy has to go out into the environment. Bits are not abstractions: they count microstates.

### [02:49.7] Numerical example — `manim:S06`

**ES:** Un gigabyte de datos completamente aleatorios contiene ocho mil millones de bits de entropía de Shannon. Como entropía física, eso es ocho mil millones por k_B ln 2: unos 7,7 × 10⁻¹⁴ J/K. Es diminuta comparada con la entropía térmica del propio chip, pero no es cero. Borrarla a temperatura ambiente exige expulsar al menos 2,3 × 10⁻¹¹ J de calor. Si los datos fueran un texto comprimible con dos bits por carácter, el costo mínimo sería proporcionalmente menor.

**EN:** A gigabyte of completely random data contains eight billion bits of Shannon entropy. As physical entropy, that is eight billion times k_B ln 2: about 7.7 × 10⁻¹⁴ J/K. It is tiny compared with the thermal entropy of the chip itself, but it is not zero. Erasing it at room temperature requires expelling at least 2.3 × 10⁻¹¹ J of heat. If the data were text compressible to two bits per character, the minimum cost would be proportionally lower.

### [03:25.5] Applications — `slide`

**ES:** En la práctica, un bit equivale a k_B ln 2, unos nueve coma seis por diez a la menos veinticuatro julios por kelvin. La compresión de datos fija cuántos bits hay que guardar y, por Landauer, cuánto cuesta como mínimo borrarlos. Y cuando un chip termodinámico produce una muestra, la aleatoriedad que contiene la toma prestada del baño térmico.

**EN:** In practice, one bit is worth k_B ln 2, about 9.6 × 10⁻²⁴ joules per kelvin. Data compression sets how many bits must be stored and, by Landauer, the minimum cost of erasing them. And when a thermodynamic chip produces a sample, the randomness it contains is borrowed from the heat bath.

### [03:48.6] Connections — `slide`

**ES:** En la próxima lección el demonio de Maxwell convertirá información en trabajo. Después veremos el costo de borrarla. En la unidad tres la entropía se volverá una cantidad por trayectoria, y en la unidad ocho la divergencia KL dará la geometría del aprendizaje.

**EN:** In the next lesson Maxwell's demon will turn information into work. Then we will see the cost of erasing it. In unit three entropy will become a trajectory-level quantity, and in unit eight the KL divergence will give the geometry of learning.

### [04:05.4] Common mistakes — `slide`

**ES:** Errores comunes: mezclar bits con nats. Pensar que una entropía es subjetiva y la otra objetiva, cuando ambas dependen de cómo agrupamos los estados. Creer que un texto con significado tiene más entropía que el ruido, cuando es al revés. Y olvidar la entropía interna de cada estado lógico.

**EN:** Common mistakes: mixing bits with nats. Thinking one entropy is subjective and the other objective, when both depend on how we group states. Believing meaningful text has more entropy than noise, when it is the other way around. And forgetting the internal entropy of each logical state.

### [04:24.5] Summary — `manim:S10`

**ES:** En resumen: la entropía de Shannon es el número medio de preguntas binarias, la sorpresa promedio. La de Gibbs es la misma fórmula sobre microestados físicos. Un bit equivale a k_B ln 2 de entropía física, y la entropía de una memoria se separa en una parte lógica y una interna. La información es física.

**EN:** In summary: Shannon entropy is the average number of binary questions, the average surprise. Gibbs entropy is the same formula over physical microstates. One bit is worth k_B ln 2 of physical entropy, and the entropy of a memory splits into a logical part and an internal one. Information is physical.

### [04:46.9] Self-assessment — `slide`

**ES:** Para practicar: calcula una entropía y su código óptimo. Cuenta las preguntas para adivinar un número entre uno y mil. Convierte un nat a bits y a julios por kelvin. Y calcula la entropía lógica de una memoria sesgada.

**EN:** To practice: compute an entropy and its optimal code. Count the questions needed to guess a number between one and a thousand. Convert one nat to bits and to joules per kelvin. And compute the logical entropy of a biased memory.

## Key equations
- $$H = -\sum_i p_i\log_2 p_i\ \ \text{(bits)}$$ — Shannon entropy: minimum average number of bits (yes/no questions).
- $$S = -k_B\sum_i p_i\ln p_i = k_B\ln 2\cdot H$$ — Gibbs entropy; one bit is worth $k_B\ln 2$.
- $$S_{\text{phys}} = k_B\ln 2\,H(\text{logical}) + \sum_i p_i S_i$$ — Split into logical and internal entropy (coarse-graining).

## Summary
- Shannon: average surprise = optimal yes/no questions.
- Gibbs: the same formula over microstates; uniform $\Rightarrow k_B\ln\Omega$.
- $1$ bit $= k_B\ln 2 \approx 9.57\times10^{-24}$ J/K.
- The entropy of a memory = logical part + internal part.

## Further reading
- [9] C. H. Bennett, Notes on Landauer's principle, reversible computation and Maxwell's demon, 2003.
- [10] D. H. Wolpert, The stochastic thermodynamics of computation, 2019.
- Video V7: The Most Misunderstood Concept in Physics — Veritasium.
