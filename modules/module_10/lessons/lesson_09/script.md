# Lesson 10.9 — Case study: an AFT language model end to end

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build and train a small AFT-conv language model with DyT and tanh MLP in JAX, autoregressive and masked-diffusion.
- Compare Adam with natural gradient (the digital stand-in for TNGD) and measure the sparsity tax of k = 4 masks.
- Log FLOPs and energy estimates and fill a TSU-mapping record.

## Prerequisites
- Lessons 10.1–10.8.
- Lesson 8.3: TNGD.
- Lesson 9.2: masked (discrete) diffusion.

## Narrated script

### [00:07.7] Introduction — `manim:S01`

**ES:** Cerramos la unidad con un caso de estudio real, de principio a fin. Entrenamos un modelo de lenguaje pequeño, de unos ciento trece mil parámetros, sobre el propio texto de las narraciones de este curso: trescientos cuarenta mil caracteres en español. Usamos todas las piezas de la unidad y medimos cuatro variantes con los mismos datos, la misma semilla y el mismo número de pasos.

**EN:** We close the unit with a real case study, end to end. We train a small language model, of about one hundred thirteen thousand parameters, on the very text of this course's narrations: three hundred forty thousand characters in Spanish. We use all the pieces of the unit and measure four variants with the same data, the same seed and the same number of steps.

### [00:31.7] The model — `manim:S02`

**ES:** El modelo tiene dos bloques de dimensión sesenta y cuatro, con contexto de sesenta y cuatro caracteres. La mezcla es AFT causal con sesgos locales aprendidos en una ventana de cuatro posiciones, como AFT-conv. La normalización es DyT y el MLP usa tangente. Para la difusión enmascarada, la mezcla es bidireccional: el promedio de una pasada hacia adelante y otra hacia atrás.

**EN:** The model has two blocks of dimension sixty-four, with a context of sixty-four characters. Mixing is causal AFT with learned local biases in a window of four positions, like AFT-conv. Normalization is DyT and the MLP uses tangent. For masked diffusion, mixing is bidirectional: the average of a forward and a backward pass.

### [00:58.6] A lesson from debugging — `manim:S03`

**ES:** Una lección del proceso. En la primera versión, el modelo de difusión no aprendía nada más allá de la frecuencia de cada letra. La causa: una posición enmascarada solo recibe información de sus vecinas, y con mezcla global esa información se diluye entre sesenta y cuatro posiciones. El gradiente de los sesgos locales era demasiado ruidoso para crecer. Inicializar esos sesgos con preferencia por las vecinas cercanas lo resolvió. La inicialización importa.

**EN:** A lesson from the process. In the first version, the diffusion model learned nothing beyond the frequency of each letter. The cause: a masked position only receives information from its neighbors, and with global mixing that information is diluted among sixty-four positions. The gradient of the local biases was too noisy to grow. Initializing those biases with a preference for nearby neighbors solved it. Initialization matters.

### [01:27.8] Results — `manim:S04`

**ES:** Los resultados, en bits por carácter sobre texto de validación, tras tres mil pasos. Autoregresivo con Adam: uno coma nueve ocho. Con gradiente natural, resuelto con gradiente conjugado: uno coma nueve cuatro, y a los quinientos pasos la ventaja era mayor, dos coma dos frente a dos coma tres dos. Con máscaras dispersas de grado cuatro: dos coma tres dos, el impuesto de la dispersión. Y la difusión enmascarada da una cota de tres coma uno ocho: a esta escala, claramente peor.

**EN:** The results, in bits per character on validation text, after three thousand steps. Autoregressive with Adam: 1.98. With natural gradient, solved with conjugate gradient: 1.94, and at five hundred steps the advantage was larger, 2.2 versus 2.32. With sparse masks of degree four: 2.32, the sparsity tax. And masked diffusion gives a bound of 3.18: at this scale, clearly worse.

### [02:00.4] Where TNGD fits — `manim:S05`

**ES:** El gradiente natural gana por paso, pero en la GPU tardó cincuenta y dos segundos frente a nueve y medio de Adam, porque cada paso resuelve un sistema lineal con diez iteraciones de gradiente conjugado. Esa resolución es justo lo que TNGD delega en un circuito termodinámico, como vimos en la lección ocho punto tres. Si la resolución analógica fuera rápida y barata, el gradiente natural ganaría también por segundo.

**EN:** Natural gradient wins per step, but on the GPU it took fifty-two seconds against nine and a half for Adam, because each step solves a linear system with ten iterations of conjugate gradient. That solve is exactly what TNGD delegates to a thermodynamic circuit, as we saw in lesson 8.3. If the analog solve were fast and cheap, natural gradient would also win per second.

### [02:27.0] Energy log and TSU-mapping record — `manim:S06`

**ES:** Registramos la energía. El modelo denso cuesta unas doscientas siete mil operaciones por token; con utilización del diez por ciento y cero coma uno siete siete picojulios por operación, unos trescientos sesenta y seis nanojulios en la GPU, una estimación. El modelo de grado cuatro usa veintiuna veces menos pesos en las proyecciones. Su registro de mapeo: cuatro mil seiscientos ocho pbits, grado dieciséis, ocho capas de muestreo secuenciales; la mezcla AFT, el embedding y la cabeza quedan en lo digital.

**EN:** We log the energy. The dense model costs about two hundred seven thousand operations per token; at ten percent utilization and 0.177 picojoules per operation, about three hundred sixty-six nanojoules on the GPU, an estimate. The degree-four model uses twenty-one times fewer weights in the projections. Its mapping record: four thousand six hundred eight pbits, degree sixteen, eight sequential sampling layers; AFT mixing, the embedding and the head stay digital.

### [03:01.8] Applications — `slide`

**ES:** El código está en la carpeta de datos de la lección. Puedes cambiar el optimizador, incluido un simulador de TNGD, y registrar en cada ejecución bits por carácter, tiempo, operaciones y el registro de mapeo. En los laboratorios veintiocho y veintinueve lo extenderás con capas muestreadas y entradas dy4p.

**EN:** The code is in the lesson's data folder. You can swap the optimizer, including a TNGD simulator, and log in each run bits per character, time, operations and the mapping record. In labs twenty-eight and twenty-nine you will extend it with sampled layers and dy4p inputs.

### [03:22.2] Common mistakes — `slide`

**ES:** Errores comunes: comparar la verosimilitud autoregresiva con una cota de difusión como si ambas fueran exactas. Juzgar el gradiente natural solo por su tiempo en hardware digital. Cambiar semillas, datos o pasos entre variantes. Y reportar energía sin utilización ni alcance.

**EN:** Common mistakes: comparing the autoregressive likelihood with a diffusion bound as if both were exact. Judging natural gradient only by its time on digital hardware. Changing seeds, data or steps between variants. And reporting energy without utilization or scope.

### [03:40.7] Summary — `manim:S09`

**ES:** En resumen, un modelo AFT pequeño con DyT y tangente aprende el texto del curso hasta uno coma nueve ocho bits por carácter. El gradiente natural gana por paso, y TNGD podría hacerlo ganar por segundo. La dispersión de grado cuatro cuesta un tercio de bit, y la difusión enmascarada queda atrás a esta escala. Todo queda registrado: calidad, tiempo, operaciones y mapeo.

**EN:** In summary, a small AFT model with DyT and tangent learns the course text down to 1.98 bits per character. Natural gradient wins per step, and TNGD could make it win per second. Degree-four sparsity costs a third of a bit, and masked diffusion falls behind at this scale. Everything is logged: quality, time, operations and mapping.

### [04:06.7] Self-assessment — `slide`

**ES:** Para practicar: explica por qué la primera difusión solo aprendió frecuencias. Calcula la razón de pesos entre el modelo denso y el disperso. Di qué haría ganar al gradiente natural en tiempo. Y explica por qué la cifra de difusión es una cota.

**EN:** To practice: explain why the first diffusion only learned frequencies. Compute the weight ratio between the dense and the sparse model. Say what would make natural gradient win in time. And explain why the diffusion figure is a bound.

## Key equations
- $$\text{bits/char (3000 steps)}\colon\ 1.98\ (\text{Adam}),\ 1.94\ (\text{NGD}),\ 2.32\ (k = 4),\ \le 3.18\ (\text{MDLM})$$ — Validation results on the course narration corpus [S].
- $$(G + \lambda I)\,\delta = \nabla L\quad\text{(10 CG iterations digitally; analog in TNGD)}$$ — The natural-gradient solve per step.
- $$E_{\text{token}} \approx \frac{2.07\times10^5\cdot 0.177\ \text{pJ}}{0.1} \approx 366\ \text{nJ}$$ — GPU estimate for the dense model [E].

## Summary
- AFT-conv + DyT + tanh MLP, 113k params, 340k-char Spanish corpus.
- 3000 steps: Adam 1.98, NGD 1.94, k = 4 2.32, MDLM ≤ 3.18 bits/char [S].
- NGD: better per step, 5× slower digitally — the solve TNGD offloads.
- Mapping record (k = 4): 4608 pbits, degree 16, 8 sampling layers.

## Further reading
- S. Zhai et al., An attention free transformer, arXiv:2105.14103 (2021).
- K. Donatella et al., Thermodynamic natural gradient descent, arXiv:2405.13817 (2024).
- S. Sahoo et al., Simple and effective masked diffusion language models, NeurIPS (2024).
