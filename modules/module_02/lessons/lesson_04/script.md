# Lesson 2.4 — The Ornstein–Uhlenbeck process

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Solve the multivariate Ornstein–Uhlenbeck process $dx = -(Ax-b)\,dt + \sqrt{2\beta^{-1}}\,dW$.
- Derive its stationary state $x_\infty \sim \mathcal N(A^{-1}b,\ \beta^{-1}A^{-1})$ with the Lyapunov equation.
- Understand how the mean and covariance of a physical system solve $Ax = b$ and invert $A$.

## Prerequisites
- Lesson 0.4: SPD matrices, matrix exponential.
- Lessons 2.2–2.3: Langevin and Fokker–Planck.

## Narrated script

### [00:05.2] Introduction — `manim:S01`

**ES:** El proceso de Ornstein y Uhlenbeck es la ecuación de Langevin en un potencial cuadrático. Es el único proceso de difusión que es a la vez estacionario, gaussiano y de Markov, y se resuelve exactamente. Pero para nosotros es mucho más: su estado final contiene la solución de un sistema lineal y la inversa de una matriz. Es el corazón del álgebra lineal termodinámica.

**EN:** The Ornstein–Uhlenbeck process is the Langevin equation in a quadratic potential. It is the only diffusion process that is at once stationary, Gaussian and Markov, and it is solved exactly. But for us it is much more: its final state contains the solution of a linear system and the inverse of a matrix. It is the heart of thermodynamic linear algebra.

### [00:28.7] Intuition — `manim:S02`

**ES:** Imagina dos masas unidas entre sí y a las paredes por resortes, sumergidas en un fluido caliente. Los resortes definen una energía cuadrática: su rigidez es una matriz A, y una fuerza externa constante b desplaza el punto de equilibrio. Sin ruido, las masas se quedarían en el mínimo, que está en A⁻¹ b. Con ruido, tiemblan alrededor de ese punto. El promedio del temblor marca la solución, y la forma del temblor, más largo en las direcciones blandas, revela la inversa de A.

**EN:** Imagine two masses connected to each other and to the walls by springs, immersed in a hot fluid. The springs define a quadratic energy: their stiffness is a matrix A, and a constant external force b shifts the equilibrium point. Without noise, the masses would stay at the minimum, which is at A⁻¹ b. With noise, they jiggle around that point. The average of the jiggle marks the solution, and the shape of the jiggle, longer in the soft directions, reveals the inverse of A.

### [01:01.4] One-dimensional case — `manim:S03`

**ES:** En una dimensión, dx = −a(x − m) dt + √(2/β) dW. La solución es la condición inicial que olvida exponencialmente, más el centro m, más ruido filtrado: x(t) = m + (x₀ − m) e^(−at) + ∫ e^(−a(t−s)) √(2/β) dW(s). Las trayectorias salen de distintos puntos, convergen hacia m y se quedan temblando con varianza 1/(β a). La autocorrelación decae como e^(−a τ).

**EN:** In one dimension, dx = −a(x − m) dt + √(2/β) dW. The solution is the initial condition forgetting exponentially, plus the center m, plus filtered noise: x(t) = m + (x₀ − m) e^(−at) + ∫ e^(−a(t−s)) √(2/β) dW(s). Trajectories start from different points, converge toward m and keep jiggling with variance 1/(β a). The autocorrelation decays as e^(−a τ).

### [01:34.9] Multivariate case — `manim:S04`

**ES:** En varias dimensiones: dx = −(A x − b) dt + √(2/β) dW, con A simétrica definida positiva. La nube de partículas parte de un punto, se desplaza hacia A⁻¹ b y se ensancha hasta formar una elipse. En el estado estacionario la distribución es gaussiana con media A⁻¹ b y covarianza β⁻¹ A⁻¹. Los ejes de la elipse son los vectores propios de A, y son más largos en las direcciones de valores propios pequeños: las direcciones blandas son las que más tiemblan.

**EN:** In several dimensions: dx = −(A x − b) dt + √(2/β) dW, with A symmetric positive definite. The particle cloud starts from a point, drifts toward A⁻¹ b and widens into an ellipse. In the stationary state the distribution is Gaussian with mean A⁻¹ b and covariance β⁻¹ A⁻¹. The ellipse's axes are the eigenvectors of A, and they are longer in the directions of small eigenvalues: the soft directions jiggle the most.

### [02:10.8] Lyapunov equation — `manim:S05`

**ES:** ¿Por qué esa covarianza? Usando el lema de Itô, la covarianza Σ(t) obedece dΣ/dt = −AΣ − ΣA + 2β⁻¹ I. Los dos primeros términos contraen la nube; el último, que viene de (dW)² = dt, la ensancha. En el estado estacionario se equilibran: AΣ + ΣA = 2β⁻¹ I, la ecuación de Lyapunov. Como A es simétrica, la solución es Σ = β⁻¹ A⁻¹. La animación muestra la elipse de Σ(t) creciendo hasta esa forma.

**EN:** Why that covariance? Using Itô's lemma, the covariance Σ(t) obeys dΣ/dt = −AΣ − ΣA + 2β⁻¹ I. The first two terms shrink the cloud; the last, which comes from (dW)² = dt, widens it. In the stationary state they balance: AΣ + ΣA = 2β⁻¹ I, the Lyapunov equation. Since A is symmetric, the solution is Σ = β⁻¹ A⁻¹. The animation shows the ellipse of Σ(t) growing to that shape.

### [02:49.7] Solving Ax = b with noise — `manim:S06`

**ES:** Ahora la idea clave. Si dejamos que un solo sistema físico evolucione y promediamos su posición en el tiempo, por ergodicidad ese promedio converge a la media de la distribución estacionaria: A⁻¹ b. El sistema resuelve el sistema lineal. Y si promediamos los productos de las desviaciones, obtenemos β⁻¹ A⁻¹: el sistema invierte la matriz. El error de los promedios decae como uno sobre la raíz del tiempo de integración. Esa es la base del solucionador lineal termodinámico del laboratorio tres.

**EN:** Now the key idea. If we let a single physical system evolve and average its position over time, by ergodicity that average converges to the mean of the stationary distribution: A⁻¹ b. The system solves the linear system. And if we average the products of the deviations, we get β⁻¹ A⁻¹: the system inverts the matrix. The error of the averages decays as one over the square root of the integration time. That is the basis of the thermodynamic linear solver in lab three.

### [03:23.7] Numerical example — `manim:S07`

**ES:** Tomemos la matriz de la lección cero punto cuatro: tres, uno; uno, dos; y b = (1, 1). Su inversa es un quinto por dos, menos uno; menos uno, tres. Entonces A⁻¹ b es cero coma dos y cero coma cuatro. Con β = 1, la covarianza estacionaria es cero coma cuatro, menos cero coma dos; menos cero coma dos, cero coma seis. La simulación, con un promedio temporal sobre dos mil unidades de tiempo, reproduce estos números con errores de unos pocos centésimos.

**EN:** Let's take the matrix from lesson 0.4: three, one; one, two; and b = (1, 1). Its inverse is one fifth times two, minus one; minus one, three. So A⁻¹ b is 0.2 and 0.4. With β = 1, the stationary covariance is 0.4, −0.2; −0.2, 0.6. The simulation, with a time average over two thousand time units, reproduces these numbers with errors of a few hundredths.

### [03:56.8] Applications — `slide`

**ES:** El proceso de Ornstein y Uhlenbeck reaparece una y otra vez. En la unidad seis será el solucionador lineal termodinámico. En la unidad ocho, un OU con la matriz de curvatura calcula el gradiente natural. Los osciladores acoplados de Normal Computing implementan un OU en hardware. Y el proceso directo de los modelos de difusión también es un OU.

**EN:** The Ornstein–Uhlenbeck process shows up again and again. In unit six it will be the thermodynamic linear solver. In unit eight, an OU with the curvature matrix computes the natural gradient. Normal Computing's coupled oscillators implement an OU in hardware. And the forward process of diffusion models is also an OU.

### [04:20.7] Connections — `slide`

**ES:** Esta lección une varias piezas: las gaussianas multivariadas, la exponencial de matrices y el número de condición. La próxima pregunta es cuánto hay que promediar para obtener una precisión dada; la responderemos con la ergodicidad en la lección dos punto seis.

**EN:** This lesson ties together several pieces: multivariate Gaussians, the matrix exponential and the condition number. The next question is how long to average for a given precision; we will answer it with ergodicity in lesson 2.6.

### [04:37.8] Common mistakes — `slide`

**ES:** Errores frecuentes: olvidar que la matriz debe ser definida positiva. Confundir la covarianza estacionaria con potencias equivocadas de la matriz. Promediar desde el instante cero sin descartar el transitorio. Y tratar muestras consecutivas como independientes.

**EN:** Frequent mistakes: forgetting that the matrix must be positive definite. Confusing the stationary covariance with wrong powers of the matrix. Averaging from time zero without discarding the transient. And treating consecutive samples as independent.

### [04:54.9] Summary — `manim:S11`

**ES:** En resumen: el proceso de Ornstein y Uhlenbeck relaja exponencialmente hacia una gaussiana con media A⁻¹ b y covarianza β⁻¹ A⁻¹, fijada por la ecuación de Lyapunov. Promediar en el tiempo una sola trayectoria resuelve el sistema lineal e invierte la matriz.

**EN:** In summary: the Ornstein–Uhlenbeck process relaxes exponentially toward a Gaussian with mean A⁻¹ b and covariance β⁻¹ A⁻¹, set by the Lyapunov equation. Time-averaging a single trajectory solves the linear system and inverts the matrix.

### [05:14.2] Self-assessment — `slide`

**ES:** Para practicar: deriva la distribución estacionaria y explica cómo resuelve el problema lineal. Resuelve una ecuación de Lyapunov diagonal. Calcula la autocorrelación en una dimensión. Y explica por qué el tiempo hasta la solución crece con el número de condición.

**EN:** To practice: derive the stationary distribution and explain how it solves the linear problem. Solve a diagonal Lyapunov equation. Compute the autocorrelation in one dimension. And explain why the time to solution grows with the condition number.

## Key equations
- $$dx = -(Ax - b)\,dt + \sqrt{2\beta^{-1}}\,dW$$ — Multivariate Ornstein–Uhlenbeck process.
- $$x(t) = e^{-At}x_0 + (I - e^{-At})A^{-1}b + \int_0^t e^{-A(t-s)}\sqrt{2\beta^{-1}}\,dW(s)$$ — Exact solution.
- $$\dot\Sigma = -A\Sigma - \Sigma A + 2\beta^{-1}I\ \Rightarrow\ \Sigma_\infty = \beta^{-1}A^{-1}$$ — Lyapunov equation and stationary covariance.
- $$x_\infty \sim \mathcal N(A^{-1}b,\ \beta^{-1}A^{-1})$$ — Stationary state: the mean solves $Ax = b$; the covariance gives $A^{-1}$.

## Summary
- OU = Langevin in a quadratic potential; exact solution.
- Stationary $\mathcal N(A^{-1}b, \beta^{-1}A^{-1})$ via Lyapunov.
- Time averages of one trajectory: $A^{-1}b$ and $A^{-1}$.
- Speed limited by $\lambda_{\min}$ (and hence by $\kappa$).

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [1] Gardiner, Handbook of Stochastic Methods (Ornstein–Uhlenbeck process).
- Syllabus, App. C, question 1.
