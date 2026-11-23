# Lesson 0.4 — Linear algebra refresher

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Recognize symmetric positive-definite (SPD) matrices and their spectral decomposition $A = Q\Lambda Q^\top$.
- Interpret the condition number $\kappa = \lambda_{\max}/\lambda_{\min}$ as a ratio of time scales.
- Use the matrix exponential to solve $\dot x = -Ax$.
- Apply Kronecker products and the Woodbury identity to save computation.

## Prerequisites
- Matrix product, transpose, inverse and determinant.
- Lesson 0.3: multivariate Gaussian and covariance.

## Narrated script

### [00:04.9] Introduction — `manim:S01`

**ES:** Casi todos los algoritmos termodinámicos de este curso terminan en una matriz. El solucionador lineal termodinámico relaja un sistema cuya dinámica la fija una matriz A. Su velocidad la limita el número de condición. El gradiente natural termodinámico usa la identidad de Woodbury, y el método K-FAC usa productos de Kronecker. En esta lección repasamos esas herramientas con una mirada geométrica.

**EN:** Almost every thermodynamic algorithm in this course ends up in a matrix. The thermodynamic linear solver relaxes a system whose dynamics are set by a matrix A. Its speed is limited by the condition number. Thermodynamic natural gradient uses the Woodbury identity, and the K-FAC method uses Kronecker products. In this lesson we review those tools with a geometric eye.

### [00:31.0] Intuition — `manim:S02`

**ES:** Una matriz de dos por dos es una transformación del plano. Mira lo que le hace al círculo unitario: lo convierte en una elipse. Si la matriz es simétrica, existen dos direcciones perpendiculares que solo se estiran, sin girar. Si además es definida positiva, los dos estiramientos son positivos: la matriz nunca invierte una dirección. Otra forma de verlo: la función ½ xᵀ A x es un cuenco con un único mínimo en el origen.

**EN:** A two-by-two matrix is a transformation of the plane. Look at what it does to the unit circle: it turns it into an ellipse. If the matrix is symmetric, there are two perpendicular directions that only stretch, without rotating. If it is also positive definite, both stretches are positive: the matrix never flips a direction. Another way to see it: the function ½ xᵀ A x is a bowl with a single minimum at the origin.

### [00:59.8] Spectral decomposition — `manim:S03`

**ES:** Los vectores propios son las direcciones que la matriz no gira: A v = λ v. Una matriz simétrica tiene vectores propios ortogonales y valores propios reales. Por eso se descompone como A = Q Λ Qᵀ: primero rotamos para alinear los ejes propios con los ejes coordenados, luego estiramos cada eje por su valor propio, y al final deshacemos la rotación. La animación aplica esos tres pasos uno por uno, y el resultado coincide con aplicar A directamente.

**EN:** Eigenvectors are the directions the matrix does not rotate: A v = λ v. A symmetric matrix has orthogonal eigenvectors and real eigenvalues. That is why it decomposes as A = Q Λ Qᵀ: first we rotate to align the eigen-axes with the coordinate axes, then stretch each axis by its eigenvalue, and finally undo the rotation. The animation applies those three steps one by one, and the result matches applying A directly.

### [01:31.3] Condition number — `manim:S04`

**ES:** El número de condición, κ = λ_max / λ_min, mide qué tan alargado es el cuenco. Con κ cercano a uno, las curvas de nivel son casi círculos y el descenso de gradiente llega directo al mínimo. Con κ grande, el valle es estrecho: el descenso de gradiente rebota de una pared a otra y avanza muy despacio por el fondo. Las dos trayectorias que ves son cálculos reales con el mismo número de pasos. En los algoritmos termodinámicos, κ aparece como el cociente entre la escala de tiempo más lenta y la más rápida del sistema físico.

**EN:** The condition number, κ = λ_max / λ_min, measures how elongated the bowl is. With κ close to one, the level curves are almost circles and gradient descent goes straight to the minimum. With large κ, the valley is narrow: gradient descent bounces from wall to wall and crawls along the bottom. The two trajectories you see are real computations with the same number of steps. In thermodynamic algorithms, κ appears as the ratio between the slowest and the fastest time scale of the physical system.

### [02:06.9] Matrix exponential — `manim:S05`

**ES:** Consideremos la dinámica ẋ = −A x. Su solución es x(t) = e^(−At) x₀, la exponencial de una matriz. En la base propia es sencilla: cada componente decae como e^(−λᵢ t). La componente con valor propio grande desaparece rápido; la que tiene valor propio pequeño tarda mucho. Por eso todas las trayectorias caen primero sobre el eje lento y luego se arrastran hacia el origen. El tiempo de relajación total lo fija el valor propio más pequeño, y el paso de integración lo limita el más grande. Su cociente es otra vez κ.

**EN:** Consider the dynamics ẋ = −A x. Its solution is x(t) = e^(−At) x₀, the exponential of a matrix. In the eigenbasis it is simple: each component decays as e^(−λᵢ t). The component with a large eigenvalue vanishes fast; the one with a small eigenvalue takes a long time. That is why all trajectories first fall onto the slow axis and then creep toward the origin. The total relaxation time is set by the smallest eigenvalue, and the integration step is limited by the largest. Their ratio is κ again.

### [02:46.6] Kronecker products — `manim:S06`

**ES:** El producto de Kronecker B ⊗ C construye una matriz grande colocando una copia de C multiplicada por cada entrada de B. Dos matrices de n por n producen una de n² por n². Lo valioso es que nunca hace falta formarla: (B ⊗ C) vec(X) = vec(C X Bᵀ), y la inversa es el Kronecker de las inversas. Invertir dos matrices pequeñas cuesta muchísimo menos que invertir una grande. Esta es la idea del método K-FAC de la unidad ocho.

**EN:** The Kronecker product B ⊗ C builds a big matrix by placing a copy of C scaled by each entry of B. Two n-by-n matrices produce one that is n² by n². The valuable part is that you never need to form it: (B ⊗ C) vec(X) = vec(C X Bᵀ), and the inverse is the Kronecker product of the inverses. Inverting two small matrices costs far less than inverting one big one. This is the idea behind the K-FAC method of unit eight.

### [03:19.3] Woodbury identity — `manim:S07`

**ES:** La identidad de Woodbury dice cómo cambia la inversa cuando sumamos una corrección de rango bajo. Si conocemos la inversa de A, la inversa de A más U C V solo exige invertir una matriz pequeña de tamaño k por k, donde k es el rango de la corrección. Los bloques de colores muestran los tamaños: en lugar de invertir algo de d por d, invertimos algo de k por k. En aprendizaje automático, la matriz de curvatura suele ser un múltiplo de la identidad más un término de rango igual al tamaño del lote, y Woodbury la vuelve manejable.

**EN:** The Woodbury identity says how the inverse changes when we add a low-rank correction. If we know the inverse of A, the inverse of A plus U C V only requires inverting a small k-by-k matrix, where k is the rank of the correction. The colored blocks show the sizes: instead of inverting something d by d, we invert something k by k. In machine learning, the curvature matrix is often a multiple of the identity plus a term whose rank equals the batch size, and Woodbury makes it tractable.

### [03:53.4] Numerical example — `manim:S08`

**ES:** Tomemos A con filas tres, uno y uno, dos. Es simétrica. Sus valores propios son cinco más o menos raíz de cinco, sobre dos: unos tres coma sesenta y dos y uno coma treinta y ocho. Ambos son positivos, así que es definida positiva. Su número de condición es aproximadamente dos coma sesenta y dos. El determinante es el producto de los valores propios, cinco, y la traza es su suma, también cinco.

**EN:** Take A with rows three, one and one, two. It is symmetric. Its eigenvalues are five plus or minus root five, over two: about 3.62 and 1.38. Both are positive, so it is positive definite. Its condition number is about 2.62. The determinant is the product of the eigenvalues, five, and the trace is their sum, also five.

### [04:21.3] Applications — `slide`

**ES:** En el curso, el número de condición determinará cuánto tarda el solucionador lineal termodinámico. La exponencial de matrices describe la relajación del proceso de Ornstein y Uhlenbeck. Los productos de Kronecker son el corazón de K-FAC y de su versión termodinámica. Y Woodbury permite invertir matrices de curvatura de rango bajo en el gradiente natural.

**EN:** In the course, the condition number will determine how long the thermodynamic linear solver takes. The matrix exponential describes the relaxation of the Ornstein–Uhlenbeck process. Kronecker products are the heart of K-FAC and of its thermodynamic version. And Woodbury lets us invert low-rank curvature matrices in the natural gradient.

### [04:43.8] Connections — `slide`

**ES:** Estas ideas se conectan con lo que ya vimos y con lo que viene. La covarianza de una gaussiana es una matriz simétrica definida positiva. La brecha espectral de una cadena de Markov también es un valor propio. El proceso de Ornstein y Uhlenbeck es la exponencial de matrices con ruido, y la estabilidad de su integración numérica depende del valor propio más grande.

**EN:** These ideas connect with what we have seen and what is coming. The covariance of a Gaussian is a symmetric positive-definite matrix. The spectral gap of a Markov chain is also an eigenvalue. The Ornstein–Uhlenbeck process is the matrix exponential with noise, and the stability of its numerical integration depends on the largest eigenvalue.

### [05:06.8] Common mistakes — `slide`

**ES:** Atención a cuatro errores. Simétrica no significa definida positiva: la matriz uno, dos, dos, uno tiene un valor propio negativo. Que todas las entradas sean positivas tampoco garantiza nada. La exponencial de una suma no es el producto de exponenciales si las matrices no conmutan. Y nunca formes el producto de Kronecker explícitamente: usa la identidad con el operador vec.

**EN:** Beware of four mistakes. Symmetric does not mean positive definite: the matrix one, two, two, one has a negative eigenvalue. All entries being positive guarantees nothing either. The exponential of a sum is not the product of exponentials if the matrices do not commute. And never form the Kronecker product explicitly: use the identity with the vec operator.

### [05:32.2] Summary — `manim:S12`

**ES:** En resumen: una matriz simétrica definida positiva estira el espacio a lo largo de ejes ortogonales, con A = Q Λ Qᵀ. El número de condición mide el cociente entre la escala más lenta y la más rápida. La exponencial de matrices resuelve la relajación lineal, y Kronecker y Woodbury convierten inversiones gigantes en inversiones pequeñas.

**EN:** In summary: a symmetric positive-definite matrix stretches space along orthogonal axes, with A = Q Λ Qᵀ. The condition number measures the ratio between the slowest and the fastest scale. The matrix exponential solves linear relaxation, and Kronecker and Woodbury turn giant inversions into small ones.

### [05:55.8] Self-assessment — `slide`

**ES:** Comprueba lo aprendido: demuestra que una matriz simétrica definida positiva tiene valores propios reales y positivos. Escribe la inversa de un producto de Kronecker y su acción sobre vec de X. Resuelve la relajación con una matriz diagonal de valores uno y cien. Y usa Woodbury para invertir lambda por la identidad más una corrección de rango uno.

**EN:** Check what you learned: prove that a symmetric positive-definite matrix has real, positive eigenvalues. Write the inverse of a Kronecker product and its action on vec of X. Solve the relaxation with a diagonal matrix with values one and one hundred. And use Woodbury to invert lambda times the identity plus a rank-one correction.

## Key equations
- $$A = A^\top \succ 0 \iff x^\top A x > 0\ \forall x\neq 0 \iff \lambda_i > 0$$ — Equivalent definition of a symmetric positive-definite matrix.
- $$A = Q\Lambda Q^\top,\quad \kappa(A) = \lambda_{\max}/\lambda_{\min}$$ — Spectral decomposition and condition number.
- $$\dot x = -Ax \Rightarrow x(t) = e^{-At}x_0 = \sum_i e^{-\lambda_i t}(v_i^\top x_0)\,v_i$$ — Linear relaxation: each eigenmode decays at its own rate.
- $$(B\otimes C)\mathrm{vec}(X) = \mathrm{vec}(C X B^\top),\quad (B\otimes C)^{-1} = B^{-1}\otimes C^{-1}$$ — Kronecker identities (vec stacks columns).
- $$(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}$$ — Woodbury identity: low-rank correction.

## Summary
- SPD: positive eigenvalues, $A = Q\Lambda Q^\top$, elliptical level curves.
- $\kappa = \lambda_{\max}/\lambda_{\min}$: ratio of time scales; it limits convergence speed.
- $x(t) = e^{-At}x_0$: each mode decays as $e^{-\lambda_i t}$.
- Kronecker and Woodbury reduce large inversions to small ones.

## Further reading
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
- [38] J. Martens and R. Grosse, K-FAC, ICML 2015 (Kronecker identities).
- [39] R. Grosse, CSC2541 lecture notes, Second-order optimization, 2021.
- Syllabus, Appendix A: questions 2 and 4.
