# Lesson 2.1 — Brownian motion, the Wiener process and Itô calculus

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build the Wiener process as a limit of random walks and state its properties.
- Understand the quadratic variation $(dW)^2 = dt$ and why it changes the rules of calculus.
- Apply Itô's lemma: $df(W) = f'(W)\,dW + \tfrac12 f''(W)\,dt$.

## Prerequisites
- Lesson 0.3: Gaussians, variance, central limit theorem.
- Differential calculus: Taylor series.

## Narrated script

### [00:06.7] Introduction — `manim:S01`

**ES:** En 1827 el botánico Robert Brown observó al microscopio granos de polen suspendidos en agua: se movían sin cesar, en zigzag, sin ninguna causa visible. En 1905 Einstein explicó el fenómeno: los granos son golpeados por moléculas de agua que no vemos. Ese movimiento, el movimiento browniano, es el modelo matemático del ruido térmico que usaremos en toda la unidad.

**EN:** In 1827 the botanist Robert Brown looked through a microscope at pollen grains suspended in water: they moved ceaselessly, zigzagging, with no visible cause. In 1905 Einstein explained it: the grains are kicked by water molecules we cannot see. That motion, Brownian motion, is the mathematical model of thermal noise we will use throughout the unit.

### [00:33.3] Intuition — `manim:S02`

**ES:** Empecemos con una caminata aleatoria: en cada paso de tiempo, la partícula salta hacia arriba o hacia abajo. Ahora hagamos los pasos de tiempo más cortos y, a la vez, los saltos más pequeños. ¿Cómo hay que reducir el salto para que el límite no se congele ni explote? La respuesta es que el salto debe escalar como la raíz cuadrada del paso de tiempo. Con esa regla, las caminatas convergen a una curva continua pero extremadamente rugosa: el proceso de Wiener.

**EN:** Let's start with a random walk: at each time step, the particle jumps up or down. Now let's make the time steps shorter and, at the same time, the jumps smaller. How must the jump shrink so the limit neither freezes nor blows up? The answer is that the jump must scale as the square root of the time step. With that rule, the walks converge to a continuous but extremely rough curve: the Wiener process.

### [01:02.4] The Wiener process — `manim:S03`

**ES:** El proceso de Wiener, W(t), empieza en cero, tiene incrementos independientes, y cada incremento W(t) − W(s) es gaussiano con media cero y varianza t − s. Mira muchas trayectorias a la vez: se abren como un abanico, y el ancho del abanico crece como la raíz de t, no como t. El histograma en un instante fijo es exactamente una gaussiana. Y si ampliamos cualquier trozo de una trayectoria, se ve igual de rugoso: el proceso es continuo pero no es derivable en ningún punto.

**EN:** The Wiener process, W(t), starts at zero, has independent increments, and each increment W(t) − W(s) is Gaussian with mean zero and variance t − s. Look at many trajectories at once: they fan out, and the width of the fan grows as the square root of t, not as t. The histogram at a fixed instant is exactly a Gaussian. And if we zoom into any piece of a trajectory, it looks just as rough: the process is continuous but differentiable nowhere.

### [01:37.4] Quadratic variation — `manim:S04`

**ES:** Aquí aparece la propiedad que lo cambia todo. Dividamos el intervalo de cero a T en pedazos cada vez más finos y sumemos los cuadrados de los incrementos. Para una curva suave esa suma tendería a cero. Para el proceso de Wiener tiende a T, exactamente, sin aleatoriedad. Lo resumimos con la regla (dW)² = dt. Los incrementos son del orden de la raíz de dt, así que sus cuadrados son del orden de dt, y no se pueden despreciar.

**EN:** Here comes the property that changes everything. Let's split the interval from zero to T into finer and finer pieces and add up the squares of the increments. For a smooth curve that sum would tend to zero. For the Wiener process it tends to T, exactly, with no randomness. We summarize it with the rule (dW)² = dt. The increments are of order root dt, so their squares are of order dt, and they cannot be neglected.

### [02:08.2] Itô's lemma — `manim:S05`

**ES:** Consecuencia: la regla de la cadena cambia. Si f es una función suave, el desarrollo de Taylor de f(W + dW) tiene un término de primer orden, f' dW, y uno de segundo orden, un medio de f'' (dW)². En el cálculo ordinario el segundo se descarta, pero aquí (dW)² es dt. Así obtenemos el lema de Itô: df = f' dW + ½ f'' dt. Por ejemplo, para W², d(W²) = 2W dW + dt: el término dt extra es exactamente lo que hace que la media de W² crezca como t.

**EN:** Consequence: the chain rule changes. If f is a smooth function, the Taylor expansion of f(W + dW) has a first-order term, f' dW, and a second-order one, one half of f'' (dW)². In ordinary calculus the second is dropped, but here (dW)² is dt. So we get Itô's lemma: df = f' dW + ½ f'' dt. For example, for W², d(W²) = 2W dW + dt: the extra dt term is exactly what makes the mean of W² grow as t.

### [02:52.9] Numerical example — `manim:S06`

**ES:** Pongamos números reales. Una esfera de un micrómetro de radio en agua a trescientos kelvin tiene, según Einstein y Stokes, un coeficiente de difusión D = k_B T / (6π η a), unos 2,2 × 10⁻¹³ m²/s. Su posición en una dirección es √(2D) W(t), así que en un segundo se desplaza típicamente unos cero coma sesenta y seis micrómetros. En cien segundos, solo diez veces más: la raíz cuadrada del tiempo.

**EN:** Let's put in real numbers. A sphere of one micrometer radius in water at three hundred kelvin has, by Stokes–Einstein, a diffusion coefficient D = k_B T / (6π η a), about 2.2 × 10⁻¹³ m²/s. Its position along one direction is √(2D) W(t), so in one second it typically moves about 0.66 micrometers. In a hundred seconds, only ten times more: the square root of time.

### [03:26.0] Applications — `slide`

**ES:** El proceso de Wiener es la fuente de ruido de todas las ecuaciones estocásticas del curso: el ruido térmico de los circuitos y los pbits, el ruido que añaden los modelos de difusión a los datos, y el ruido del solucionador lineal termodinámico del laboratorio tres.

**EN:** The Wiener process is the noise source of every stochastic equation in the course: the thermal noise of circuits and pbits, the noise diffusion models add to data, and the noise of the thermodynamic linear solver in lab three.

### [03:43.2] Connections — `slide`

**ES:** En la próxima lección añadiremos fuerzas y obtendremos la ecuación de Langevin. Después escribiremos la ecuación para la densidad de probabilidad, la de Fokker y Planck, y aprenderemos a simular con el método de Euler y Maruyama.

**EN:** In the next lesson we will add forces and get the Langevin equation. Then we will write the equation for the probability density, the Fokker–Planck equation, and learn to simulate with the Euler–Maruyama method.

### [03:58.1] Common mistakes — `slide`

**ES:** Errores comunes: escalar los saltos como el paso de tiempo en lugar de su raíz. Aplicar la regla de la cadena ordinaria y olvidar el término de Itô. Tratar el ruido blanco como una función ordinaria. Y confundir las interpretaciones de Itô y de Stratonovich cuando el ruido depende del estado.

**EN:** Common mistakes: scaling the jumps like the time step instead of its square root. Applying the ordinary chain rule and forgetting the Itô term. Treating white noise as an ordinary function. And confusing the Itô and Stratonovich interpretations when the noise depends on the state.

### [04:17.3] Summary — `manim:S10`

**ES:** En resumen: el proceso de Wiener es el límite de caminatas aleatorias con saltos de tamaño raíz de dt. Tiene incrementos gaussianos independientes y varianza que crece como t. Su variación cuadrática hace que (dW)² = dt, y por eso el cálculo de Itô tiene un término extra de un medio de f'' por dt.

**EN:** In summary: the Wiener process is the limit of random walks with jumps of size root dt. It has independent Gaussian increments and a variance that grows as t. Its quadratic variation makes (dW)² = dt, which is why Itô calculus has an extra term of one half f'' times dt.

### [04:39.2] Self-assessment — `slide`

**ES:** Para practicar: obtén la distribución de un incremento y la covarianza del proceso. Usa el lema de Itô con la exponencial. Calcula cuánto tarda la esfera en desplazarse diez micrómetros. Y explica por qué la suma de cuadrados converge mientras la suma de valores absolutos diverge.

**EN:** To practice: find the distribution of an increment and the covariance of the process. Use Itô's lemma with the exponential. Compute how long the sphere takes to move ten micrometers. And explain why the sum of squares converges while the sum of absolute values diverges.

## Key equations
- $$W(t) - W(s) \sim \mathcal N(0,\, t - s),\quad \mathbb E[W(s)W(t)] = \min(s, t)$$ — Independent Gaussian increments.
- $$\sum_k (\Delta W_k)^2 \to T \quad\Longleftrightarrow\quad (dW)^2 = dt$$ — Quadratic variation of the Wiener process.
- $$df(W) = f'(W)\,dW + \tfrac12 f''(W)\,dt$$ — Itô's lemma.
- $$D = \frac{k_BT}{6\pi\eta a},\quad \langle x^2\rangle = 2Dt$$ — Stokes–Einstein and diffusive growth.

## Summary
- Wiener = limit of walks with jumps $\propto\sqrt{dt}$.
- Independent $\mathcal N(0, t-s)$ increments; continuous, nowhere differentiable.
- $(dW)^2 = dt$: the chain rule gains $\tfrac12 f''\,dt$ (Itô).
- Diffusion: the typical displacement grows as $\sqrt t$.

## Further reading
- [1] C. W. Gardiner, Handbook of Stochastic Methods, chs. 3–4.
- [5] P. E. Kloeden and E. Platen, Numerical Solution of SDEs, ch. 3.
- [46] P. Holderrieth and E. Erives, Introduction to flow matching and diffusion models (SDE appendix).
