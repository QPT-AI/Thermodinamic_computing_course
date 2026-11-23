# Lesson 6.1 — Linear systems from the first moment of an OU process

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Encode $Ax = b$ as the quadratic potential $U(x) = \tfrac12 x^\top A x - b^\top x$ of coupled oscillators.
- Run the linear-system protocol: equilibrate for $t_0$, then time-average $x$ over $\tau$.
- Relate the error to temperature and averaging time: $\varepsilon \propto 1/\sqrt{\beta\tau}$.

## Prerequisites
- Lesson 5.4: continuous stochastic processing units and the OU process.
- Lesson 2.6: Langevin dynamics and the Fokker–Planck equation.

## Narrated script

### [00:07.4] Introduction — `manim:S01`

**ES:** Resolver un sistema lineal es quizás la tarea más común de la computación científica. Un computador digital lo hace con factorizaciones o con gradiente conjugado. Hoy veremos otra forma: construir un sistema físico cuyo equilibrio sea la solución, dejarlo relajarse en presencia de ruido térmico y promediar su posición. Es la idea central del álgebra lineal termodinámica.

**EN:** Solving a linear system is perhaps the most common task in scientific computing. A digital computer does it with factorizations or with conjugate gradient. Today we see another way: build a physical system whose equilibrium is the solution, let it relax in the presence of thermal noise and average its position. It is the central idea of thermodynamic linear algebra.

### [00:31.5] Encoding Ax = b — `manim:S02`

**ES:** Tomemos una matriz A simétrica y definida positiva. Definimos el potencial U(x) = ½ xᵀ A x − bᵀ x. Su gradiente es A x − b, así que su único mínimo es exactamente x = A⁻¹ b. Físicamente, es un conjunto de osciladores armónicos acoplados: A fija los resortes y b las fuerzas externas.

**EN:** Take a symmetric positive definite matrix A. We define the potential U(x) = ½ xᵀ A x − bᵀ x. Its gradient is A x − b, so its only minimum is exactly x = A⁻¹ b. Physically, it is a set of coupled harmonic oscillators: A sets the springs and b the external forces.

### [00:56.8] Dynamics and equilibrium — `manim:S03`

**ES:** En contacto con un baño térmico, la posición obedece la ecuación de Langevin sobreamortiguada: un proceso de Ornstein-Uhlenbeck que empuja hacia el mínimo y añade ruido. En el equilibrio, x sigue una gaussiana con media A⁻¹ b y covarianza β⁻¹ A⁻¹. La solución del sistema es el primer momento de la distribución. El ruido no estorba: es lo que garantiza que el sistema explore y llegue al equilibrio.

**EN:** In contact with a heat bath, the position obeys the overdamped Langevin equation: an Ornstein-Uhlenbeck process that pushes toward the minimum and adds noise. At equilibrium, x follows a Gaussian with mean A⁻¹ b and covariance β⁻¹ A⁻¹. The solution of the system is the first moment of the distribution. The noise is not in the way: it is what guarantees that the system explores and reaches equilibrium.

### [01:25.5] The protocol — `manim:S04`

**ES:** El protocolo tiene tres pasos. Primero, cargar A y b en los acoplamientos y las fuerzas del dispositivo. Segundo, esperar un tiempo de equilibración t₀, del orden de κ τ_r por un logaritmo, donde κ es el número de condición y τ_r el tiempo de relajación. Tercero, promediar x en el tiempo durante una ventana τ con un integrador analógico. Ese promedio es la estimación de la solución.

**EN:** The protocol has three steps. First, load A and b into the couplings and forces of the device. Second, wait an equilibration time t₀, of order κ τ_r times a logarithm, where κ is the condition number and τ_r the relaxation time. Third, time-average x over a window τ with an analog integrator. That average is the estimate of the solution.

### [01:53.2] Simulation — `manim:S05`

**ES:** Simulemos una matriz de Wishart de dimensión cincuenta, con número de condición treinta y cuatro. Con k_B T = 0,01, tras equilibrar, el error relativo del promedio es de siete por ciento con una ventana de diez unidades, dos por ciento con cien y menos del uno por ciento con novecientas. Si enfriamos diez veces, el error cae unas tres veces: con cien unidades baja a seis milésimas. El error escala como uno sobre la raíz de β τ.

**EN:** Let's simulate a Wishart matrix of dimension fifty, with condition number thirty-four. With k_B T = 0.01, after equilibrating, the relative error of the average is seven percent with a window of ten units, two percent with a hundred and below one percent with nine hundred. If we cool ten times, the error falls about three times: with a hundred units it drops to six thousandths. The error scales as one over the square root of β τ.

### [02:23.1] How long to wait — `manim:S06`

**ES:** El artículo de Aifer y colaboradores da los tiempos exactos. En el régimen sobreamortiguado, la ventana necesaria es τ = 2κ²d‖A‖ τ_r / (β‖b‖²ε²(1 − P)). Crece con la dimensión, con el cuadrado del número de condición y con el inverso del cuadrado del error. Eso da una complejidad de orden d κ² ε⁻², frente a d² √κ del gradiente conjugado: la ventaja aparece con dimensión grande.

**EN:** The paper by Aifer and colleagues gives the exact times. In the overdamped regime, the required window is τ = 2κ²d‖A‖ τ_r / (β‖b‖²ε²(1 − P)). It grows with the dimension, with the square of the condition number and with the inverse square of the error. That gives a complexity of order d κ² ε⁻², against d² √κ for conjugate gradient: the advantage appears at large dimension.

### [02:56.3] Applications — `slide`

**ES:** Este solucionador brilla cuando basta una solución aproximada rápida: dentro de métodos iterativos, en pasos de Newton, en el gradiente natural que veremos en la unidad ocho, o en regresión con procesos gaussianos. En el laboratorio nueve lo compararás con el gradiente conjugado y con Cholesky.

**EN:** This solver shines when a fast approximate solution is enough: inside iterative methods, in Newton steps, in the natural gradient we will see in unit eight, or in Gaussian process regression. In lab nine you will compare it with conjugate gradient and with Cholesky.

### [03:14.8] Common mistakes — `slide`

**ES:** Errores comunes: promediar desde el instante cero, cuando el transitorio sesga la estimación. Usar una matriz que no es definida positiva sin transformar el sistema, lo que eleva al cuadrado el número de condición. Esperar alta precisión, cuando el error cae solo como uno sobre la raíz del tiempo. E ignorar el costo de cargar la matriz.

**EN:** Common mistakes: averaging from time zero, when the transient biases the estimate. Using a matrix that is not positive definite without transforming the system, which squares the condition number. Expecting high precision, when the error falls only as one over the square root of time. And ignoring the cost of loading the matrix.

### [03:36.5] Summary — `manim:S09`

**ES:** En resumen: con el potencial cuadrático adecuado, el equilibrio térmico de unos osciladores acoplados es una gaussiana centrada en la solución de A x = b. Se equilibra, se promedia en el tiempo, y el error cae como uno sobre la raíz de β τ. La complejidad es de orden d κ² ε⁻².

**EN:** In summary: with the right quadratic potential, the thermal equilibrium of coupled oscillators is a Gaussian centered on the solution of A x = b. One equilibrates, time-averages, and the error falls as one over the square root of β τ. The complexity is of order d κ² ε⁻².

### [03:57.8] Self-assessment — `slide`

**ES:** Para practicar: demuestra que el mínimo del potencial es la solución. Explica por qué se descarta el transitorio. Calcula cuánto baja el error si la ventana se multiplica por cuatro. Y di qué pasa con el número de condición al pasar a las ecuaciones normales.

**EN:** To practice: prove that the minimum of the potential is the solution. Explain why the transient is discarded. Compute how much the error falls if the window is multiplied by four. And say what happens to the condition number when moving to the normal equations.

## Key equations
- $$U(x) = \tfrac12 x^\top A x - b^\top x,\qquad \nabla U = 0 \iff x = A^{-1} b$$ — Encoding of the linear system as a potential.
- $$dx = -\tfrac{1}{\gamma}(Ax - b)\,dt + \sqrt{2/(\gamma\beta)}\,dW \ \Rightarrow\ x_\infty \sim \mathcal N\big(A^{-1}b,\ \beta^{-1}A^{-1}\big)$$ — Overdamped Langevin (OU) dynamics and its stationary distribution.
- $$\tau = \frac{2\kappa^2 d\,\|A\|}{\beta\|b\|^2\varepsilon^2(1-P_\varepsilon)}\,\tau_r,\qquad \tau_r = \gamma/\|A\|$$ — Averaging window for relative error $\varepsilon$ with probability $P_\varepsilon$ (Aifer et al., overdamped).

## Summary
- Ax = b ↔ minimum of U = ½xᵀAx − bᵀx; equilibrium N(A⁻¹b, β⁻¹A⁻¹).
- Protocol: load, equilibrate t₀ ~ κτ_r ln(·), time-average over τ.
- Error ∝ 1/√(βτ) (d = 50 simulation: 2 % → 0.7 % on cooling ×10).
- Complexity O(dκ²ε⁻²) vs O(min{d^ω, d²√κ}) digital.

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
- [28] P. J. Coles et al., Thermodynamic AI and the fluctuation frontier, 2023.
