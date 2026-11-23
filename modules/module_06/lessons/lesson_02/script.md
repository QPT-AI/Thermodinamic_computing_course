# Lesson 6.2 — Matrix inverse and Lyapunov equations

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Estimate $A^{-1}$ from the equilibrium covariance $\Sigma = \beta^{-1}A^{-1}$ of an OU process.
- Solve Lyapunov equations $M\Sigma + \Sigma M^\top = C$ with a non-symmetric drift and shaped noise.
- Explain why second moments converge more slowly than the mean, and why temperature drops out.

## Prerequisites
- Lesson 6.1: linear systems from the first moment.
- Lesson 2.6: Fokker–Planck and stationary covariance.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** En la lección anterior usamos solo la media de la distribución de equilibrio. Pero las fluctuaciones también contienen información. La covarianza de equilibrio es β⁻¹ A⁻¹: si medimos cómo fluctúan las variables, obtenemos la inversa de la matriz completa. Y con un pequeño cambio, también resolvemos ecuaciones de Lyapunov.

**EN:** In the previous lesson we used only the mean of the equilibrium distribution. But the fluctuations also contain information. The equilibrium covariance is β⁻¹ A⁻¹: if we measure how the variables fluctuate, we get the inverse of the whole matrix. And with a small change, we also solve Lyapunov equations.

### [00:27.2] Inverse protocol — `manim:S02`

**ES:** El protocolo de la inversa pone b = 0, de modo que la media es cero. Tras equilibrar, multiplicadores analógicos calculan cada producto x_i x_j, e integradores analógicos lo promedian en el tiempo. Son d² multiplicadores e integradores. Al final, A⁻¹ es β por la matriz de promedios.

**EN:** The inverse protocol sets b = 0, so that the mean is zero. After equilibrating, analog multipliers compute each product x_i x_j, and analog integrators average it over time. That is d² multipliers and integrators. At the end, A⁻¹ is β times the matrix of averages.

### [00:48.8] Temperature drops out — `manim:S03`

**ES:** Aquí aparece una sorpresa. En el sistema lineal, enfriar reducía el error. En la inversa no: si la temperatura baja, las fluctuaciones se encogen en proporción, y el error relativo de la covarianza es exactamente el mismo. Lo que importa es cuántas fluctuaciones independientes promediamos, es decir, la ventana τ medida en tiempos de relajación.

**EN:** Here comes a surprise. In the linear system, cooling reduced the error. For the inverse it does not: if the temperature drops, the fluctuations shrink proportionally, and the relative error of the covariance is exactly the same. What matters is how many independent fluctuations we average, that is, the window τ measured in relaxation times.

### [01:12.1] Simulation and cost — `manim:S04`

**ES:** Simulamos una matriz de Wishart de dimensión diez, con número de condición veintidós. El error relativo de la inversa es del cincuenta por ciento con una ventana de cien unidades, del veintiséis con trescientas, y del siete por ciento con tres mil. Los segundos momentos convergen mucho más lento que la media. La ventana necesaria es τ = 4κ d(d + 1) τ_r / ((1 − P) ε²), así que la complejidad es de orden d² κ ε⁻², frente a d^ω digital.

**EN:** We simulate a Wishart matrix of dimension ten, with condition number twenty-two. The relative error of the inverse is fifty percent with a window of a hundred units, twenty-six with three hundred, and seven percent with three thousand. Second moments converge much more slowly than the mean. The required window is τ = 4κ d(d + 1) τ_r / ((1 − P) ε²), so the complexity is of order d² κ ε⁻², against d^ω digitally.

### [01:45.0] Lyapunov equations — `manim:S05`

**ES:** Ahora generalicemos. Si la deriva es una matriz estable M, no necesariamente simétrica, y el ruido tiene covarianza C, la covarianza estacionaria cumple la ecuación de Lyapunov M Σ + Σ Mᵀ = C. La inversa es el caso particular simétrico. Con dimensión diez, el error de la solución de Lyapunov es del veinticuatro por ciento con cien unidades y del cuatro por ciento con tres mil. Digitalmente, el algoritmo de Bartels y Stewart cuesta d³.

**EN:** Now let's generalize. If the drift is a stable matrix M, not necessarily symmetric, and the noise has covariance C, the stationary covariance satisfies the Lyapunov equation M Σ + Σ Mᵀ = C. The inverse is the symmetric special case. With dimension ten, the error of the Lyapunov solution is twenty-four percent with a hundred units and four percent with three thousand. Digitally, the Bartels–Stewart algorithm costs d³.

### [02:18.2] Where Lyapunov appears — `manim:S06`

**ES:** Las ecuaciones de Lyapunov aparecen en teoría de control, donde los gramianos de controlabilidad dicen qué estados puede alcanzar un sistema; en el análisis de estabilidad; y en filtros de Kalman en estado estacionario. Un dispositivo de osciladores acoplados las resuelve simplemente dejando que el ruido haga su trabajo y midiendo las correlaciones.

**EN:** Lyapunov equations appear in control theory, where controllability Gramians tell which states a system can reach; in stability analysis; and in steady-state Kalman filters. A device of coupled oscillators solves them simply by letting noise do its work and measuring the correlations.

### [02:40.0] Applications — `slide`

**ES:** Los segundos momentos sirven para precondicionadores aproximados, para la covarianza posterior en inferencia bayesiana, que veremos en la lección seis punto seis, y para gramianos y filtros de Kalman. En el laboratorio nueve lo compararás con los métodos digitales.

**EN:** Second moments are useful for approximate preconditioners, for the posterior covariance in Bayesian inference, which we will see in lesson 6.6, and for Gramians and Kalman filters. In lab nine you will compare it with digital methods.

### [02:56.7] Common mistakes — `slide`

**ES:** Errores comunes: bajar la temperatura para mejorar la inversa, que no ayuda. Olvidar poner b en cero o restar la media. Subestimar el hardware, que requiere d² multiplicadores. Y usar una deriva inestable, para la que no existe covarianza estacionaria.

**EN:** Common mistakes: lowering the temperature to improve the inverse, which does not help. Forgetting to set b to zero or to subtract the mean. Underestimating the hardware, which requires d² multipliers. And using an unstable drift, for which no stationary covariance exists.

### [03:14.7] Summary — `manim:S09`

**ES:** En resumen: la covarianza de equilibrio es β⁻¹ A⁻¹, así que medir correlaciones da la inversa, y con una deriva general da la solución de una ecuación de Lyapunov. La temperatura no cambia el error relativo; la ventana sí. La complejidad es de orden d² κ ε⁻².

**EN:** In summary: the equilibrium covariance is β⁻¹ A⁻¹, so measuring correlations gives the inverse, and with a general drift it gives the solution of a Lyapunov equation. Temperature does not change the relative error; the window does. The complexity is of order d² κ ε⁻².

### [03:35.8] Self-assessment — `slide`

**ES:** Para practicar: deduce la covarianza a partir de la ecuación de Lyapunov. Explica por qué el error relativo no depende de la temperatura. Cuenta los multiplicadores para dimensión cien. Y di qué ruido se necesita para resolver una ecuación de Lyapunov general.

**EN:** To practice: derive the covariance from the Lyapunov equation. Explain why the relative error does not depend on temperature. Count the multipliers for dimension one hundred. And say which noise is needed to solve a general Lyapunov equation.

## Key equations
- $$\Sigma_s = \lim_{t\to\infty}\langle x x^\top\rangle = \beta^{-1}A^{-1},\qquad A^{-1} \approx \frac{\beta}{\tau}\int_{t_0}^{t_0+\tau} x x^\top dt$$ — Inverse from the time-averaged second moment ($b = 0$).
- $$dx = -Mx\,dt + C^{1/2}dW \ \Rightarrow\ M\Sigma + \Sigma M^\top = C$$ — Stationary covariance solves a Lyapunov equation ($M$ stable).
- $$\tau = \frac{4\kappa\,d(d+1)}{(1-P_\varepsilon)\,\varepsilon^2}\,\tau_r$$ — Averaging window for the inverse (overdamped, Aifer et al.): independent of $\beta$.

## Summary
- Covariance = β⁻¹A⁻¹: correlations give the inverse (d² multipliers).
- Relative error independent of temperature; only τ matters.
- d = 10 simulation: 50 % (τ = 100) → 7 % (τ = 3000) [S].
- General drift M, noise C: Lyapunov MΣ + ΣMᵀ = C; O(d²κε⁻²) vs O(d³).

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
- R. H. Bartels and G. W. Stewart, Solution of the matrix equation AX + XB = C, Commun. ACM 15, 820 (1972).
