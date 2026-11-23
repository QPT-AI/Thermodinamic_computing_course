# Lesson 2.7 — Numerical SDEs

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Implement the Euler–Maruyama method: $x_{k+1} = x_k + f(x_k)\Delta t + \sqrt{2D\Delta t}\,z_k$.
- Derive the stability condition $\Delta t < 2/\lambda_{\max}$ and the discretization bias.
- Compare strong convergence orders (Euler–Maruyama $\tfrac12$, Milstein $1$) and know exact schemes for the OU.

## Prerequisites
- Lesson 2.1: increments $\Delta W \sim \mathcal N(0, \Delta t)$ and Itô.
- Lesson 2.4: Ornstein–Uhlenbeck process.

## Narrated script

### [00:04.3] Introduction — `manim:S01`

**ES:** Casi ninguna ecuación diferencial estocástica se resuelve con papel y lápiz. Para simular un pozo doble, un modelo de Ising continuo o un solucionador lineal termodinámico necesitamos discretizar el tiempo. Esta lección presenta el método más usado, el de Euler y Maruyama, y sus dos riesgos: la inestabilidad, si el paso es grande, y el sesgo, que contamina las estadísticas aunque la simulación parezca correcta.

**EN:** Almost no stochastic differential equation can be solved with pencil and paper. To simulate a double well, a continuous Ising model or a thermodynamic linear solver we need to discretize time. This lesson presents the most used method, Euler–Maruyama, and its two risks: instability, if the step is large, and bias, which contaminates the statistics even when the simulation looks right.

### [00:31.7] Euler–Maruyama — `manim:S02`

**ES:** La idea es la de Euler, más ruido. En cada paso, avanzamos con la fuerza evaluada en el punto actual durante un tiempo Δt, y sumamos un incremento de Wiener, una gaussiana de varianza Δt. Fíjate en las escalas: el término determinista es del orden de Δt, pero el ruido es del orden de la raíz de Δt. Por eso, en pasos pequeños, el ruido domina cada paso individual, mientras que la fuerza domina en tiempos largos.

**EN:** The idea is Euler's, plus noise. At each step, we advance with the force evaluated at the current point for a time Δt, and add a Wiener increment, a Gaussian of variance Δt. Notice the scales: the deterministic term is of order Δt, but the noise is of order root Δt. That is why, for small steps, noise dominates each individual step, while the force dominates over long times.

### [01:00.5] Stability — `manim:S03`

**ES:** Apliquemos el método a ẋ = −λ x, la parte determinista de un OU. Cada paso multiplica x por 1 − λ Δt. Si ese factor tiene valor absoluto menor que uno, la simulación decae; si es mayor, explota. La condición es Δt < 2/λ. Con λ = 10, un paso de cero coma quince oscila pero converge; uno de cero coma veintiuno explota. En varias dimensiones manda el valor propio más grande: Δt < 2/λ_max. Y como la relajación lenta tarda 1/λ_min, el número de pasos crece como el número de condición.

**EN:** Let's apply the method to ẋ = −λ x, the deterministic part of an OU. Each step multiplies x by 1 − λ Δt. If that factor has absolute value less than one, the simulation decays; if larger, it blows up. The condition is Δt < 2/λ. With λ = 10, a step of 0.15 oscillates but converges; one of 0.21 blows up. In several dimensions the largest eigenvalue rules: Δt < 2/λ_max. And since slow relaxation takes 1/λ_min, the number of steps grows as the condition number.

### [01:42.4] Discretization bias — `manim:S04`

**ES:** Incluso cuando es estable, el método no muestrea exactamente la distribución correcta. Para el OU, la varianza estacionaria de la cadena discreta es 1/(β λ (1 − λ Δt/2)), un poco mayor que la verdadera. La curva muestra el sesgo relativo en función del paso: es aproximadamente λ Δt/2. Con un paso igual a la mitad del límite de estabilidad, la varianza se duplica. Para el OU existe una alternativa exacta: usar el factor e^(−λ Δt) y el ruido con la varianza correspondiente.

**EN:** Even when stable, the method does not sample exactly the right distribution. For the OU, the stationary variance of the discrete chain is 1/(β λ (1 − λ Δt/2)), a bit larger than the true one. The curve shows the relative bias as a function of the step: it is about λ Δt/2. With a step equal to half the stability limit, the variance doubles. For the OU there is an exact alternative: use the factor e^(−λ Δt) and noise with the matching variance.

### [02:18.0] Orders of convergence — `manim:S05`

**ES:** ¿Qué tan rápido mejora la simulación al reducir el paso? Medimos el error fuerte, la distancia promedio entre la trayectoria simulada y la exacta con el mismo ruido, para el movimiento browniano geométrico, que tiene solución exacta. En escala logarítmica, Euler y Maruyama baja con pendiente un medio: hay que dividir el paso por cuatro para reducir el error a la mitad. El método de Milstein, que añade un término de Itô con (ΔW)² − Δt, baja con pendiente uno. Para ruido aditivo, como en Langevin, ese término se anula y Euler y Maruyama ya tiene orden fuerte uno.

**EN:** How fast does the simulation improve as the step shrinks? We measure the strong error, the average distance between the simulated and the exact trajectory with the same noise, for geometric Brownian motion, which has an exact solution. On a log scale, Euler–Maruyama drops with slope one half: you must divide the step by four to halve the error. The Milstein method, which adds an Itô term with (ΔW)² − Δt, drops with slope one. For additive noise, as in Langevin, that term vanishes and Euler–Maruyama already has strong order one.

### [02:57.2] Numerical example — `manim:S06`

**ES:** En el laboratorio tres usarás matrices de Wishart. Si el valor propio más grande es cuarenta, el paso debe ser menor que dos sobre cuarenta, cero coma cero cinco; para tener un sesgo de covarianza menor al uno por ciento, λ Δt/2 debe ser menor que cero coma cero uno, es decir, un paso de cero coma cero cero cero cinco. Si el valor propio más pequeño es cero coma cuatro, relajar requiere unas 5/λ_min, doce coma cinco unidades de tiempo: veinticinco mil pasos solo para el transitorio.

**EN:** In lab three you will use Wishart matrices. If the largest eigenvalue is forty, the step must be below two over forty, 0.05; to keep the covariance bias under one percent, λ Δt/2 must be below 0.01, that is, a step of 0.0005. If the smallest eigenvalue is 0.4, relaxing takes about 5/λ_min, 12.5 time units: twenty-five thousand steps just for the transient.

### [03:30.2] Applications — `slide`

**ES:** En los laboratorios simularás todas estas dinámicas con Euler y Maruyama dentro de scan y jit. La regla práctica: un paso muy por debajo del límite de estabilidad, y comprobar el sesgo variando el paso. Para el OU, usa la discretización exacta. Y recuerda una ventaja del hardware analógico: integra en tiempo continuo, sin la restricción de Euler, aunque con su propio ancho de banda.

**EN:** In the labs you will simulate all these dynamics with Euler–Maruyama inside scan and jit. The practical rule: a step well below the stability limit, and check the bias by varying the step. For the OU, use the exact discretization. And remember an advantage of analog hardware: it integrates in continuous time, without Euler's constraint, though with its own bandwidth.

### [03:55.7] Common mistakes — `slide`

**ES:** Errores frecuentes: escalar el ruido con el paso en lugar de su raíz. Ignorar el límite de estabilidad en sistemas mal condicionados. Confundir convergencia fuerte con convergencia débil. Y reutilizar números aleatorios.

**EN:** Frequent mistakes: scaling the noise with the step instead of its square root. Ignoring the stability limit in ill-conditioned systems. Confusing strong convergence with weak convergence. And reusing random numbers.

### [04:11.1] Summary — `manim:S09`

**ES:** En resumen: Euler y Maruyama avanza con la fuerza por Δt más un ruido de tamaño raíz de Δt. Es estable si Δt < 2/λ_max, tiene un sesgo de orden λ Δt en las estadísticas estacionarias, y converge fuertemente con orden un medio, o uno con ruido aditivo o con Milstein.

**EN:** In summary: Euler–Maruyama advances with the force times Δt plus noise of size root Δt. It is stable if Δt < 2/λ_max, has a bias of order λ Δt in the stationary statistics, and converges strongly with order one half, or one with additive noise or with Milstein.

### [04:32.9] Self-assessment — `slide`

**ES:** Para practicar: calcula un paso máximo estable, la varianza sesgada de un OU discretizado, la discretización exacta, y explica por qué el término de Milstein se anula con ruido aditivo.

**EN:** To practice: compute a maximum stable step, the biased variance of a discretized OU, the exact discretization, and explain why the Milstein term vanishes with additive noise.

## Key equations
- $$x_{k+1} = x_k + f(x_k)\,\Delta t + \sqrt{2D\,\Delta t}\;z_k,\quad z_k\sim\mathcal N(0,1)$$ — Euler–Maruyama.
- $$|1 - \lambda\Delta t| < 1 \iff \Delta t < 2/\lambda$$ — Linear stability (in several dimensions, $\lambda_{\max}$).
- $$\mathrm{Var}_{\text{EM}} = \frac{1}{\beta\lambda\,(1 - \lambda\Delta t/2)}$$ — Bias of the stationary variance of the discretized OU.
- $$x_{k+1} = e^{-\lambda\Delta t}x_k + \sqrt{\tfrac{1 - e^{-2\lambda\Delta t}}{\beta\lambda}}\,z_k$$ — Exact discretization of the OU.

## Summary
- Euler–Maruyama: drift $\propto\Delta t$, noise $\propto\sqrt{\Delta t}$.
- Stable if $\Delta t < 2/\lambda_{\max}$; total steps $\propto\kappa$.
- Stationary bias $\approx\lambda\Delta t/2$; exact OU available.
- Strong order: EM ½ (1 with additive noise), Milstein 1.

## Further reading
- [5] P. E. Kloeden and E. Platen, Numerical Solution of Stochastic Differential Equations, Springer, 1992.
- [1] Gardiner, Handbook of Stochastic Methods.
