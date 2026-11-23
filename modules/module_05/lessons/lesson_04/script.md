# Lesson 5.4 — Continuous stochastic processing units

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain how coupled RC/LC oscillators implement Langevin dynamics in a quadratic potential $U = \tfrac12 x^\top A x - b^\top x$.
- Relate their stationary statistics to $A^{-1}b$ and $A^{-1}$, and their convergence to $1/\sqrt T$.
- Place Normal Computing's stochastic processing unit: 8-cell PCB prototype and first chip.

## Prerequisites
- Lessons 2.2 and 2.4: Langevin and Ornstein–Uhlenbeck.
- Lesson 1.6: Johnson–Nyquist noise.

## Narrated script

### [00:06.1] Introduction — `manim:S01`

**ES:** Los pbits muestrean variables binarias. Pero muchos problemas de inteligencia artificial son continuos: gaussianas, sistemas lineales, matrices de curvatura. Normal Computing propuso otro tipo de hardware termodinámico, la unidad de procesamiento estocástico, construida con osciladores eléctricos acoplados que tiemblan por el ruido térmico. Su estado final contiene la solución de un problema lineal.

**EN:** Pbits sample binary variables. But many artificial intelligence problems are continuous: Gaussians, linear systems, curvature matrices. Normal Computing proposed another kind of thermodynamic hardware, the stochastic processing unit, built from coupled electrical oscillators that jiggle from thermal noise. Its final state contains the solution of a linear problem.

### [00:31.6] An oscillator cell — `manim:S02`

**ES:** Cada celda es un circuito con una inductancia, un capacitor y una resistencia. El voltaje del capacitor oscila, la resistencia lo amortigua, y la misma resistencia, por el teorema de Nyquist, inyecta ruido térmico. La dinámica es exactamente la ecuación de Langevin subamortiguada de la lección dos punto dos, con un potencial cuadrático. Sin acoplamiento, cada celda muestrea una gaussiana.

**EN:** Each cell is a circuit with an inductor, a capacitor and a resistor. The capacitor voltage oscillates, the resistor damps it, and the same resistor, by Nyquist's theorem, injects thermal noise. The dynamics is exactly the underdamped Langevin equation from lesson 2.2, with a quadratic potential. Without coupling, each cell samples a Gaussian.

### [00:57.4] Coupling the cells — `manim:S03`

**ES:** Ahora conectamos las celdas con capacitores de acoplamiento. La energía total se vuelve U = ½ xᵀ A x − bᵀ x, donde la matriz A codifica las capacitancias y los acoplamientos, y b son voltajes de sesgo. El sistema relaja hacia la distribución de Boltzmann de esa energía: una gaussiana con media A⁻¹ b y covarianza k_B T A⁻¹. Midiendo los voltajes y promediando en el tiempo, leemos la solución del sistema lineal y la inversa de la matriz.

**EN:** Now we connect the cells with coupling capacitors. The total energy becomes U = ½ xᵀ A x − bᵀ x, where the matrix A encodes the capacitances and couplings, and b are bias voltages. The system relaxes toward the Boltzmann distribution of that energy: a Gaussian with mean A⁻¹ b and covariance k_B T A⁻¹. By measuring the voltages and time-averaging, we read the solution of the linear system and the inverse of the matrix.

### [01:32.0] Convergence — `manim:S04`

**ES:** Simulemos ocho celdas acopladas con una matriz bien condicionada. El error relativo de la covarianza estimada es de veintinueve por ciento tras cien unidades de tiempo, ocho por ciento tras mil, y cinco por ciento tras cuatro mil. Cae como uno sobre la raíz del tiempo de integración, como predijo la lección dos punto seis. La precisión se compra con tiempo, y el tiempo lo fija el número de condición.

**EN:** Let's simulate eight coupled cells with a well-conditioned matrix. The relative error of the estimated covariance is twenty-nine percent after a hundred time units, eight percent after a thousand, and five percent after four thousand. It falls as one over the square root of the integration time, as lesson 2.6 predicted. Precision is bought with time, and time is set by the condition number.

### [01:58.2] From PCB to chip — `manim:S05`

**ES:** El primer prototipo de Normal Computing fue una placa de circuito impreso con ocho celdas acopladas. Con ella se demostraron el muestreo de gaussianas y la inversión de matrices pequeñas. El paso siguiente es un chip integrado, donde las constantes de tiempo bajan a nanosegundos y caben muchas más celdas. En la unidad seis veremos los algoritmos y su complejidad, y en la unidad ocho, cómo usarlos para el gradiente natural.

**EN:** Normal Computing's first prototype was a printed circuit board with eight coupled cells. With it, Gaussian sampling and the inversion of small matrices were demonstrated. The next step is an integrated chip, where time constants drop to nanoseconds and many more cells fit. In unit six we will see the algorithms and their complexity, and in unit eight, how to use them for the natural gradient.

### [02:24.8] Numerical example — `manim:S06`

**ES:** Un orden de magnitud. Con una inductancia de un microhenrio y un capacitor de un nanofaradio, la frecuencia natural es de unos cinco megahercios. Si la relajación dura unos pocos periodos y necesitamos mil tiempos de relajación para un error del cinco por ciento, el cómputo dura del orden de un milisegundo en la placa. En un chip, con capacidades de femtofaradios, el mismo cálculo baja a microsegundos.

**EN:** An order of magnitude. With a one-microhenry inductor and a one-nanofarad capacitor, the natural frequency is about five megahertz. If relaxation takes a few periods and we need a thousand relaxation times for a five-percent error, the computation takes on the order of a millisecond on the board. On a chip, with femtofarad capacitances, the same computation drops to microseconds.

### [02:50.7] Applications — `slide`

**ES:** Una unidad de procesamiento estocástico resuelve sistemas lineales, invierte matrices, muestrea gaussianas y, como veremos, calcula el gradiente natural. Sus límites son la precisión analógica, el desajuste entre componentes y el costo de convertir voltajes a números.

**EN:** A stochastic processing unit solves linear systems, inverts matrices, samples Gaussians and, as we will see, computes the natural gradient. Its limits are analog precision, mismatch between components and the cost of converting voltages to numbers.

### [03:08.8] Common mistakes — `slide`

**ES:** Errores comunes: olvidar que la matriz debe ser definida positiva, porque si no el circuito es inestable. Promediar desde el principio sin descartar el transitorio. Esperar la precisión de un procesador digital. E ignorar el costo de cargar la matriz y de leer los voltajes.

**EN:** Common mistakes: forgetting that the matrix must be positive definite, because otherwise the circuit is unstable. Averaging from the start without discarding the transient. Expecting the precision of a digital processor. And ignoring the cost of loading the matrix and reading the voltages.

### [03:26.7] Summary — `manim:S09`

**ES:** En resumen: osciladores RLC acoplados implementan Langevin en un potencial cuadrático, con el ruido térmico de sus propias resistencias. Su estado estacionario es una gaussiana con media A⁻¹ b y covarianza A⁻¹, y promediar en el tiempo da esas cantidades con error proporcional a uno sobre la raíz del tiempo.

**EN:** In summary: coupled RLC oscillators implement Langevin in a quadratic potential, with the thermal noise of their own resistors. Their stationary state is a Gaussian with mean A⁻¹ b and covariance A⁻¹, and time-averaging gives those quantities with an error proportional to one over the square root of time.

### [03:49.9] Self-assessment — `slide`

**ES:** Para practicar: calcula la frecuencia natural de una celda. Explica el doble papel de la resistencia. Estima el tiempo para un error del dos por ciento. Y describe qué pasa si la matriz tiene un valor propio negativo.

**EN:** To practice: compute the natural frequency of a cell. Explain the double role of the resistor. Estimate the time for a two-percent error. And describe what happens if the matrix has a negative eigenvalue.

## Key equations
- $$U(x) = \tfrac12 x^\top A x - b^\top x,\qquad x_\infty \sim \mathcal N\big(A^{-1}b,\ k_BT\,A^{-1}\big)$$ — Quadratic energy of the coupled cells and its stationary distribution.
- $$\frac{\|\hat\Sigma_T - \Sigma\|}{\|\Sigma\|} \propto \frac{1}{\sqrt{T}}$$ — Convergence of time averages (8 cells: 29 % at T = 100, 8 % at 1000, 5 % at 4000).
- $$f_0 = \frac{1}{2\pi\sqrt{LC}}$$ — Natural frequency of an LC cell (1 µH, 1 nF ⇒ ≈ 5 MHz).

## Summary
- Coupled RLC cells = underdamped Langevin in $U = \tfrac12 x^\top Ax - b^\top x$.
- Stationary Gaussian: mean $A^{-1}b$, covariance $k_BT A^{-1}$.
- Error of time averages ∝ $1/\sqrt{T}$; time set by $\kappa$.
- Normal Computing: 8-cell PCB prototype → integrated chip.

## Further reading
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [29] M. Aifer et al., Solving the compute crisis with physics-based ASICs, 2025.
