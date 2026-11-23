# Lesson 6.3 — Determinants from work statistics

**Unit:** Unit 6 — Thermodynamic linear algebra  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Relate $\ln|A|$ to the free energy of a Gaussian equilibrium state.
- Estimate a log-determinant from work measurements with the Jarzynski equality.
- Place the result in the moment hierarchy: first moment, second moment, all moments.

## Prerequisites
- Lesson 3.4: fluctuation theorems and the Jarzynski equality.
- Lessons 6.1–6.2: first and second moments.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Ya sabemos sacar del equilibrio la media, que resuelve sistemas lineales, y la covarianza, que da la inversa. Hoy subimos un escalón más: el determinante. No está en ningún momento finito de la distribución, sino en la función de partición, es decir, en la energía libre. Y la energía libre se mide con trabajo.

**EN:** We already know how to extract from equilibrium the mean, which solves linear systems, and the covariance, which gives the inverse. Today we go one step higher: the determinant. It is not in any finite moment of the distribution, but in the partition function, that is, in the free energy. And free energy is measured with work.

### [00:26.9] Determinant as free energy — `manim:S02`

**ES:** Para el potencial U = ½ xᵀ A x, la función de partición es una integral gaussiana proporcional a (det A)^(−1/2). Entonces la energía libre es F = ln det A / (2β) más una constante. Si pasamos de una matriz conocida, como la identidad, a la matriz A, la diferencia de energía libre es la mitad del logaritmo del determinante, dividida por β.

**EN:** For the potential U = ½ xᵀ A x, the partition function is a Gaussian integral proportional to (det A)^(−1/2). Then the free energy is F = ln det A / (2β) plus a constant. If we go from a known matrix, such as the identity, to the matrix A, the free energy difference is half the logarithm of the determinant, divided by β.

### [00:54.7] Jarzynski — `manim:S03`

**ES:** La igualdad de Jarzynski, de la lección tres punto cuatro, dice que el promedio de e^(−βW) sobre muchas repeticiones de un protocolo es exactamente e^(−βΔF), aunque el protocolo sea rápido y fuera del equilibrio. Así que el algoritmo es: empezar en equilibrio con la identidad, cambiar el potencial hacia A midiendo el trabajo, repetir muchas veces, y calcular ln det A = −2 ln⟨e^(−βW)⟩.

**EN:** The Jarzynski equality, from lesson 3.4, says that the average of e^(−βW) over many repetitions of a protocol is exactly e^(−βΔF), even if the protocol is fast and out of equilibrium. So the algorithm is: start at equilibrium with the identity, change the potential toward A while measuring the work, repeat many times, and compute ln det A = −2 ln⟨e^(−βW)⟩.

### [01:27.0] Simulation — `manim:S04`

**ES:** Simulemos una matriz de dimensión cinco, cuyo logaritmo del determinante es menos tres coma cuatro cero. Con lotes de cien repeticiones, un cambio instantáneo da menos dos coma cinco cuatro, con una dispersión de uno coma cero cuatro: sesgado y ruidoso. Con un tiempo de cambio de diez unidades, menos tres coma uno ocho, con dispersión de cero coma tres dos. Con cien unidades, menos tres coma cuatro uno, con dispersión de cero coma uno cinco. Cuanto más lento el protocolo, menos disipación y mejor el estimador.

**EN:** Let's simulate a matrix of dimension five, whose log-determinant is −3.40. With batches of a hundred repetitions, an instantaneous switch gives −2.54, with a spread of 1.04: biased and noisy. With a switching time of ten units, −3.18, with a spread of 0.32. With a hundred units, −3.41, with a spread of 0.15. The slower the protocol, the less dissipation and the better the estimator.

### [02:00.9] Why the naive average fails — `manim:S05`

**ES:** ¿Por qué no basta con promediar el trabajo? Por la segunda ley: el trabajo medio es siempre mayor que la diferencia de energía libre, y el exceso es el trabajo disipado. Con cien unidades, el doble del trabajo medio da menos tres coma uno siete, lejos de menos tres coma cuatro cero. La exponencial de Jarzynski pondera más las trayectorias raras con poco trabajo, y eso corrige el sesgo. Por eso decimos que el determinante usa todos los momentos del trabajo.

**EN:** Why isn't averaging the work enough? Because of the second law: the mean work is always larger than the free energy difference, and the excess is the dissipated work. With a hundred units, twice the mean work gives −3.17, far from −3.40. The Jarzynski exponential weights more heavily the rare trajectories with little work, and that corrects the bias. That is why we say the determinant uses all the moments of the work.

### [02:30.3] Moment hierarchy and cost — `manim:S06`

**ES:** Así queda la jerarquía de momentos. El primer momento resuelve sistemas lineales. El segundo da la inversa y las ecuaciones de Lyapunov. La estadística completa del trabajo da el determinante. Según Aifer y colaboradores, la complejidad del determinante es de orden d κ ln(κ)³ ε⁻², frente a d^ω digital. En la práctica se usan estimadores mejores que Jarzynski, como el de Bennett, que combina protocolos de ida y vuelta.

**EN:** This is the moment hierarchy. The first moment solves linear systems. The second gives the inverse and Lyapunov equations. The full work statistics give the determinant. According to Aifer and colleagues, the complexity of the determinant is of order d κ ln(κ)³ ε⁻², against d^ω digitally. In practice, better estimators than Jarzynski are used, such as Bennett's, which combines forward and backward protocols.

### [03:01.3] Applications — `slide`

**ES:** Los logaritmos de determinantes aparecen en la verosimilitud marginal de los procesos gaussianos, en los flujos normalizantes, y en toda estimación de energía libre en física y química. En el laboratorio nueve compararás Jarzynski, Bennett y Cholesky.

**EN:** Log-determinants appear in the marginal likelihood of Gaussian processes, in normalizing flows, and in every free-energy estimation in physics and chemistry. In lab nine you will compare Jarzynski, Bennett and Cholesky.

### [03:17.6] Common mistakes — `slide`

**ES:** Errores comunes: usar el trabajo medio en lugar de la exponencial. Hacer pocas repeticiones con un protocolo rápido, cuando el promedio depende de eventos raros. No empezar en equilibrio, que Jarzynski exige. Y equivocarse con los signos.

**EN:** Common mistakes: using the mean work instead of the exponential. Doing few repetitions with a fast protocol, when the average depends on rare events. Not starting at equilibrium, which Jarzynski requires. And getting the signs wrong.

### [03:33.6] Summary — `manim:S09`

**ES:** En resumen: el logaritmo del determinante es una diferencia de energía libre, y la igualdad de Jarzynski la obtiene del trabajo medido en protocolos repetidos. Los protocolos lentos disipan menos y dan estimadores más precisos. Es el tercer escalón de la jerarquía de momentos.

**EN:** In summary: the log-determinant is a free energy difference, and the Jarzynski equality obtains it from the work measured in repeated protocols. Slow protocols dissipate less and give more precise estimators. It is the third step of the moment hierarchy.

### [03:51.4] Self-assessment — `slide`

**ES:** Para practicar: deduce la energía libre de un potencial cuadrático. Explica por qué el trabajo medio acota el logaritmo del determinante. Escribe el trabajo de un cambio instantáneo. Y nombra el estimador que combina ida y vuelta.

**EN:** To practice: derive the free energy of a quadratic potential. Explain why the mean work bounds the log-determinant. Write the work of an instantaneous switch. And name the estimator that combines forward and backward.

## Key equations
- $$Z(A) = \int e^{-\frac\beta2 x^\top A x}dx = \Big(\tfrac{2\pi}{\beta}\Big)^{d/2}|A|^{-1/2},\qquad F = \tfrac{1}{2\beta}\ln|A| + \text{const}$$ — The determinant lives in the partition function.
- $$\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}\ \Rightarrow\ \ln|A| = \ln|A_0| - 2\ln\langle e^{-\beta W}\rangle$$ — Jarzynski estimator of the log-determinant, switching from $A_0$ (known) to $A$.
- $$W = \int_0^1 \tfrac12\,x_\lambda^\top (A - A_0)\,x_\lambda\,d\lambda,\qquad A_\lambda = (1-\lambda)A_0 + \lambda A$$ — Work along a linear switching protocol.

## Summary
- ln det A = 2βΔF: the determinant is a free energy difference.
- Jarzynski: ln det A = −2 ln⟨e^(−βW)⟩ (from A₀ = I).
- d = 5 simulation: −2.54 ± 1.04 (instant) → −3.41 ± 0.15 (τ_s = 100); true −3.40 [S].
- Moment hierarchy: mean → Ax = b; covariance → A⁻¹; all moments → ln det A.

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- C. Jarzynski, Nonequilibrium equality for free energy differences, Phys. Rev. Lett. 78, 2690 (1997).
- C. H. Bennett, Efficient estimation of free energy differences from Monte Carlo data, J. Comput. Phys. 22, 245 (1976).
