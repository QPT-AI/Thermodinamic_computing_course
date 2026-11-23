# Lesson 8.2 — Curvature matrices

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the empirical Fisher $JJ^\top$ and the generalized Gauss–Newton $G = J_f H_L J_f^\top$, and know when they differ.
- Solve the damped system $(G + \lambda I)\tilde g = \nabla\ell$ with conjugate gradient (NGD-CG) or the Woodbury identity.
- Compare runtime and memory of NGD, NGD-CG and NGD-Woodbury.

## Prerequisites
- Lesson 8.1: Fisher information and the natural gradient.
- Linear algebra: rank, Woodbury identity.

## Narrated script

### [00:04.5] Introduction — `manim:S01`

**ES:** El gradiente natural necesita una matriz de curvatura. La información de Fisher verdadera exige muestrear del modelo, así que en la práctica se usan aproximaciones calculables con diferenciación automática. Hoy vemos las dos más comunes, el Fisher empírico y el Gauss-Newton generalizado, y dos formas digitales de resolver el sistema: gradiente conjugado y la identidad de Woodbury.

**EN:** The natural gradient needs a curvature matrix. The true Fisher information requires sampling from the model, so in practice approximations computable with automatic differentiation are used. Today we see the two most common ones, the empirical Fisher and the generalized Gauss-Newton, and two digital ways of solving the system: conjugate gradient and the Woodbury identity.

### [00:28.9] Empirical Fisher and GGN — `manim:S02`

**ES:** El Fisher empírico promedia el producto exterior de los gradientes por ejemplo: J Jᵀ. El Gauss-Newton generalizado usa el jacobiano de la salida de la red y el hessiano de la pérdida respecto de esa salida: G = J_f H_L J_fᵀ. Para pérdidas de la familia exponencial, el GGN coincide con el Fisher verdadero. El empírico, en cambio, puede ser muy distinto: en una regresión logística con pesos no nulos, la diferencia relativa entre ambos es del doscientos treinta por ciento.

**EN:** The empirical Fisher averages the outer product of per-example gradients: J Jᵀ. The generalized Gauss-Newton uses the Jacobian of the network output and the Hessian of the loss with respect to that output: G = J_f H_L J_fᵀ. For exponential-family losses, the GGN coincides with the true Fisher. The empirical one, in contrast, can be very different: in a logistic regression with nonzero weights, the relative difference between the two is two hundred thirty percent.

### [01:04.0] Low rank and damping — `manim:S03`

**ES:** Un detalle crucial: con un lote de b ejemplos y salida de dimensión d_z, la matriz tiene rango a lo sumo b d_z, mucho menor que el número de parámetros N. En nuestro ejemplo, doscientos parámetros y treinta y dos ejemplos dan rango treinta y dos. La matriz es singular, así que se amortigua: se resuelve (G + λI) g̃ = ∇ℓ.

**EN:** A crucial detail: with a batch of b examples and output dimension d_z, the matrix has rank at most b d_z, much smaller than the number of parameters N. In our example, two hundred parameters and thirty-two examples give rank thirty-two. The matrix is singular, so it is damped: one solves (G + λI) g̃ = ∇ℓ.

### [01:28.7] NGD-CG — `manim:S04`

**ES:** El gradiente conjugado resuelve el sistema usando solo productos matriz-vector, y el producto del GGN por un vector se calcula con productos jacobiano-vector en tiempo O(b N), sin formar la matriz. Como la matriz amortiguada tiene a lo sumo b + 1 valores propios distintos, el gradiente conjugado converge en pocas iteraciones: veintiuna a veintitrés en el ejemplo, aunque el número de condición llegue a siete mil. Su punto débil es que las iteraciones son secuenciales y no se paralelizan.

**EN:** Conjugate gradient solves the system using only matrix-vector products, and the GGN-vector product is computed with Jacobian-vector products in O(b N) time, without forming the matrix. Since the damped matrix has at most b + 1 distinct eigenvalues, conjugate gradient converges in few iterations: twenty-one to twenty-three in the example, even when the condition number reaches seven thousand. Its weak point is that the iterations are sequential and cannot be parallelized.

### [02:00.6] NGD-Woodbury — `manim:S05`

**ES:** La identidad de Woodbury explota el rango bajo: invertir G + λI se reduce a invertir una matriz pequeña de tamaño b d_z. En el ejemplo, el resultado coincide con la solución directa hasta diez a la menos doce. El costo es O(b² d_z² N + b³ d_z³): excelente si el lote y la salida son pequeños, pero intratable cuando d_z es el tamaño de un vocabulario, de decenas de miles.

**EN:** The Woodbury identity exploits the low rank: inverting G + λI reduces to inverting a small matrix of size b d_z. In the example, the result agrees with the direct solution to ten to the minus twelve. The cost is O(b² d_z² N + b³ d_z³): excellent if the batch and the output are small, but intractable when d_z is the size of a vocabulary, tens of thousands.

### [02:30.8] Comparison — `manim:S06`

**ES:** Así queda la tabla de Donatella y colaboradores. Adam y el descenso estocástico cuestan O(b N) por iteración. El gradiente natural directo cuesta O(N³) y memoria N². Con gradiente conjugado, c veces el costo de primer orden, secuencial. Con Woodbury, lineal en N pero cúbico en b d_z. En la próxima lección veremos que la versión termodinámica cuesta O(b d_z N) más el tiempo analógico.

**EN:** This is the table of Donatella and colleagues. Adam and stochastic descent cost O(b N) per iteration. Direct natural gradient costs O(N³) and N² memory. With conjugate gradient, c times the first-order cost, sequential. With Woodbury, linear in N but cubic in b d_z. In the next lesson we will see that the thermodynamic version costs O(b d_z N) plus the analog time.

### [02:59.8] Applications — `slide`

**ES:** En la práctica, prefiere el GGN al Fisher empírico; usa Woodbury cuando el lote por la salida es pequeño, y gradiente conjugado truncado cuando hay muchos parámetros. En el laboratorio once implementarás ambos en MNIST.

**EN:** In practice, prefer the GGN to the empirical Fisher; use Woodbury when batch times output is small, and truncated conjugate gradient when there are many parameters. In lab eleven you will implement both on MNIST.

### [03:14.8] Common mistakes — `slide`

**ES:** Errores comunes: usar el Fisher empírico como si fuera el verdadero. Formar la matriz completa cuando basta su producto por un vector. Llevar el gradiente conjugado hasta la convergencia total, cuando se trunca a propósito. Y aplicar Woodbury con una salida del tamaño de un vocabulario.

**EN:** Common mistakes: using the empirical Fisher as if it were the true one. Forming the full matrix when its product with a vector suffices. Running conjugate gradient to full convergence, when it is truncated on purpose. And applying Woodbury with an output the size of a vocabulary.

### [03:33.3] Summary — `manim:S09`

**ES:** En resumen: el GGN es la curvatura preferida y coincide con el Fisher en la familia exponencial; el Fisher empírico puede diferir mucho. La matriz tiene rango bajo y se amortigua. Gradiente conjugado y Woodbury la resuelven en digital, cada uno con su límite: el primero es secuencial, el segundo explota con la dimensión de salida.

**EN:** In summary: the GGN is the preferred curvature and coincides with the Fisher in the exponential family; the empirical Fisher can differ a lot. The matrix has low rank and is damped. Conjugate gradient and Woodbury solve it digitally, each with its limit: the first is sequential, the second explodes with the output dimension.

### [03:56.4] Self-assessment — `slide`

**ES:** Para practicar: calcula el rango del GGN. Escribe la fórmula de Woodbury. Explica por qué el gradiente conjugado converge en pocas iteraciones. Y di cuándo coinciden el Fisher empírico y el GGN en la regresión logística.

**EN:** To practice: compute the rank of the GGN. Write the Woodbury formula. Explain why conjugate gradient converges in few iterations. And say when the empirical Fisher and the GGN coincide in logistic regression.

## Key equations
- $$\bar F = JJ^\top,\qquad G = J_f H_L J_f^\top,\qquad \mathrm{rank}\,G \le b\,d_z$$ — Empirical Fisher and generalized Gauss–Newton.
- $$(UV + \lambda I)^{-1} = \lambda^{-1}I - \lambda^{-2}U\big(I + \lambda^{-1}VU\big)^{-1}V$$ — Woodbury identity ($U = J_f$, $V = H_L J_f^\top$).
- $$\text{NGD } O(N^3 + bd_zN^2),\ \ \text{CG } O(cbN),\ \ \text{Woodbury } O(b^2d_z^2N + b^3d_z^3)$$ — Runtime per iteration (Donatella et al., Table 1).

## Summary
- GGN = Fisher for exponential-family losses; empirical Fisher can differ (232 % in the example) [S].
- rank ≤ b d_z ≪ N: damp with λI.
- CG: Jacobian-vector products, ≤ b d_z + 1 iterations (21–23 even at κ = 7·10³); sequential.
- Woodbury: exact (10⁻¹² error), cubic in b d_z.

## Further reading
- [40] K. Donatella et al., Thermodynamic natural gradient descent, 2024.
- [37] J. Martens, New insights and perspectives on the natural gradient method, JMLR 21 (2020).
- N. N. Schraudolph, Fast curvature matrix-vector products for second-order gradient descent, Neural Computation 14, 1723 (2002).
