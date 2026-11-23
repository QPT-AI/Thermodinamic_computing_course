# Lesson 8.3 — Thermodynamic natural gradient descent (TNGD)

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe the hybrid GPU + SPU loop that estimates $\tilde g = (G + \lambda I)^{-1}\nabla\ell$ with OU dynamics.
- Explain the interpolation between gradient descent ($t = 0$) and NGD ($t \to \infty$) and the momentum-like effect of delay.
- Know the complexity $O(bd_zN + t)$, TNGD-Adam, and the role of noise robustness.

## Prerequisites
- Lessons 6.1 and 8.2: OU linear-system solver and curvature matrices.

## Narrated script

### [00:05.9] Introduction — `manim:S01`

**ES:** El gradiente natural necesita resolver un sistema lineal en cada paso, y en la unidad seis vimos que un procesador estocástico, un SPU, resuelve sistemas lineales dejando que un proceso de Ornstein-Uhlenbeck se equilibre. Donatella y colaboradores unieron ambas ideas en el descenso de gradiente natural termodinámico, o TNGD: la GPU calcula gradientes y curvatura, y el SPU resuelve el sistema.

**EN:** The natural gradient needs to solve a linear system at every step, and in unit six we saw that a stochastic processing unit, an SPU, solves linear systems by letting an Ornstein-Uhlenbeck process equilibrate. Donatella and colleagues combined both ideas in thermodynamic natural gradient descent, or TNGD: the GPU computes gradients and curvature, and the SPU solves the system.

### [00:32.5] The hybrid loop — `manim:S02`

**ES:** En cada iteración, la GPU usa diferenciación automática para obtener el gradiente, el jacobiano de la salida y el hessiano de la pérdida. Esos factores se cargan en el SPU a través de convertidores. El SPU evoluciona según dg̃ = −((G + λI) g̃ − ∇ℓ) dt más ruido, cuya media de equilibrio es el gradiente natural. Tras un tiempo analógico t, se lee el estado, la GPU actualiza los parámetros y el ciclo se repite. Los dos lados pueden trabajar en paralelo, de forma asíncrona.

**EN:** At each iteration, the GPU uses automatic differentiation to get the gradient, the output Jacobian and the loss Hessian. Those factors are loaded into the SPU through converters. The SPU evolves according to dg̃ = −((G + λI) g̃ − ∇ℓ) dt plus noise, whose equilibrium mean is the natural gradient. After an analog time t, the state is read, the GPU updates the parameters and the cycle repeats. The two sides can work in parallel, asynchronously.

### [01:08.9] From SGD to NGD — `manim:S03`

**ES:** Si el SPU empieza en el gradiente ordinario, su media en el tiempo t es una mezcla: en t = 0 es el gradiente, el descenso estocástico de siempre; para t grande es el gradiente natural. El tiempo analógico es una perilla continua entre primer y segundo orden. En una regresión logística con cincuenta parámetros, la pérdida tras treinta iteraciones baja de cero coma cuatro cero siete con t = 0, a cero coma tres ocho nueve con cinco tiempos de relajación, cero coma tres siete ocho con veinte, cero coma tres siete tres con cincuenta, y cero coma tres seis ocho con el gradiente natural exacto.

**EN:** If the SPU starts at the ordinary gradient, its mean at time t is a blend: at t = 0 it is the gradient, the usual stochastic descent; for large t it is the natural gradient. Analog time is a continuous knob between first and second order. In a logistic regression with fifty parameters, the loss after thirty iterations falls from 0.407 with t = 0, to 0.389 with five relaxation times, 0.378 with twenty, 0.373 with fifty, and 0.368 with the exact natural gradient.

### [01:49.2] Delay acts like momentum — `manim:S04`

**ES:** Una sorpresa del artículo: no reiniciar el SPU entre iteraciones, o aceptar un retardo entre la medición y la actualización, mejora el resultado. El estado conserva información de la curvatura anterior mientras se adapta a la nueva, como el momento en los optimizadores. En nuestra simulación, con cinco tiempos de relajación y arranque en caliente, la pérdida final baja de cero coma tres ocho nueve a cero coma tres ocho tres. En los experimentos de MNIST de Donatella, ciertos retardos incluso superan al gradiente natural exacto.

**EN:** A surprise from the paper: not resetting the SPU between iterations, or accepting a delay between measurement and update, improves the result. The state keeps information about the previous curvature while adapting to the new one, like momentum in optimizers. In our simulation, with five relaxation times and a warm start, the final loss drops from 0.389 to 0.383. In Donatella's MNIST experiments, certain delays even outperform the exact natural gradient.

### [02:24.0] Cost and TNGD-Adam — `manim:S05`

**ES:** El costo por iteración es O(b d_z N + t): construir el jacobiano y el hessiano, más el tiempo analógico, que se puede hacer muy corto diseñando constantes de tiempo pequeñas. En MNIST, los autores estiman unas dos veces el costo por iteración de Adam, pero con muchas menos iteraciones. En el ajuste fino de DistilBERT, el TNGD puro fue peor que Adam, pero la variante TNGD-Adam, que pasa el gradiente natural por la regla de Adam, dio el mejor resultado.

**EN:** The cost per iteration is O(b d_z N + t): building the Jacobian and Hessian, plus the analog time, which can be made very short by designing small time constants. On MNIST, the authors estimate about twice Adam's cost per iteration, but with far fewer iterations. In DistilBERT fine-tuning, plain TNGD was worse than Adam, but the TNGD-Adam variant, which passes the natural gradient through Adam's rule, gave the best result.

### [02:55.8] Robustness and hardware — `manim:S06`

**ES:** Dos ventajas más. El gradiente conjugado puede divergir en sistemas mal condicionados; la dinámica de Ornstein-Uhlenbeck converge en promedio para cualquier matriz definida positiva. Y el ruido no es un enemigo: es parte del algoritmo. El hardware propuesto usa arreglos de resistencias para los productos con el jacobiano. La limitación honesta: los resultados son simulaciones, y su impacto depende de que existan SPU grandes.

**EN:** Two more advantages. Conjugate gradient can diverge on ill-conditioned systems; Ornstein-Uhlenbeck dynamics converges on average for any positive definite matrix. And noise is not an enemy: it is part of the algorithm. The proposed hardware uses resistor arrays for the products with the Jacobian. The honest limitation: the results are simulations, and their impact depends on large SPUs existing.

### [03:23.7] Applications — `slide`

**ES:** Usa el tiempo analógico como un hiperparámetro entre primer y segundo orden, arranca el SPU en caliente para aprovechar el efecto de momento, y combínalo con Adam en modelos grandes. En el laboratorio once simularás TNGD en MNIST.

**EN:** Use analog time as a hyperparameter between first and second order, warm-start the SPU to exploit the momentum effect, and combine it with Adam in large models. In lab eleven you will simulate TNGD on MNIST.

### [03:40.6] Common mistakes — `slide`

**ES:** Errores comunes: esperar el equilibrio completo en cada paso, cuando tiempos cortos ya ayudan. Olvidar el amortiguamiento. Contar solo el tiempo analógico, cuando construir el jacobiano también cuesta. Y presentar aceleraciones simuladas como resultados medidos en hardware.

**EN:** Common mistakes: waiting for full equilibrium at every step, when short times already help. Forgetting damping. Counting only the analog time, when building the Jacobian also costs. And presenting simulated speedups as measured hardware results.

### [03:59.1] Summary — `manim:S09`

**ES:** En resumen, TNGD reparte el trabajo entre una GPU, que calcula gradientes y curvatura, y un SPU, que resuelve el sistema del gradiente natural con dinámica de Ornstein-Uhlenbeck. El tiempo analógico interpola entre descenso de gradiente y gradiente natural, el retardo actúa como momento, y el costo por iteración se acerca al de un método de primer orden.

**EN:** In summary: TNGD splits the work between a GPU, which computes gradients and curvature, and an SPU, which solves the natural-gradient system with Ornstein-Uhlenbeck dynamics. Analog time interpolates between gradient descent and natural gradient, delay acts like momentum, and the cost per iteration approaches that of a first-order method.

### [04:22.2] Self-assessment — `slide`

**ES:** Para practicar: escribe la media del estado en función del tiempo. Explica por qué el tiempo cero es descenso de gradiente. Da una explicación del efecto de momento. Y di qué término domina el costo por iteración.

**EN:** To practice: write the mean of the state as a function of time. Explain why time zero is gradient descent. Give an explanation of the momentum effect. And say which term dominates the cost per iteration.

## Key equations
- $$d\tilde g = -\big((G + \lambda I)\tilde g - \nabla\ell\big)dt + \sqrt{2\kappa_0}\,dW,\qquad \langle\tilde g_\infty\rangle = (G+\lambda I)^{-1}\nabla\ell$$ — SPU dynamics for the natural gradient.
- $$\langle\tilde g_t\rangle = e^{-At}\big(\tilde g_0 - A^{-1}\nabla\ell\big) + A^{-1}\nabla\ell,\quad \tilde g_0 = \nabla\ell:\ t = 0 \to \text{GD},\ t\to\infty \to \text{NGD}$$ — Analog time interpolates between first and second order ($A = G + \lambda I$).
- $$\text{TNGD: } O(b\,d_z N + t)\ \text{runtime},\ \ O(b\,d_zN + b^2d_z^2)\ \text{memory}$$ — Cost per iteration (Donatella et al.).

## Summary
- GPU: gradient, J_f, H_L; SPU: OU dynamics whose mean is the natural gradient.
- Analog time t: GD (t = 0) → NGD (t → ∞); loss after 30 iters 0.407 → 0.389 → 0.378 → 0.373 → 0.368 [S].
- Warm start / delay acts like momentum (0.389 → 0.383 at t = 5τ) [S].
- Cost O(b d_z N + t); TNGD-Adam best on DistilBERT fine-tuning (simulated).

## Further reading
- [40] K. Donatella et al., Thermodynamic natural gradient descent, 2024.
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [31] M. Aifer et al., Error mitigation for thermodynamic computing, 2024.
