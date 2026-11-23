# Lesson 0.3 — Probability refresher

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Work with Bernoulli, categorical and Gaussian variables, and their moments.
- Transform multivariate Gaussians: if $y\sim\mathcal N(0,I)$ and $x = Ay+b$, then $x\sim\mathcal N(b, AA^\top)$.
- Compute Shannon entropy and the KL divergence, and interpret them.

## Prerequisites
- Single-variable calculus: integrals and exponentials.
- Matrix algebra: product and transpose.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** Un computador termodinámico no devuelve números exactos: devuelve muestras de una distribución de probabilidad. Para entender qué calcula, cuánto ruido tiene su respuesta y cuánta información contiene, necesitamos un lenguaje preciso. En esta lección repasamos las piezas que usaremos todo el semestre: las variables de Bernoulli, categóricas y gaussianas, sus momentos, la entropía de Shannon y la divergencia de Kullback y Leibler.

**EN:** A thermodynamic computer does not return exact numbers: it returns samples from a probability distribution. To understand what it computes, how noisy its answer is and how much information it contains, we need a precise language. In this lesson we review the pieces we will use all semester: Bernoulli, categorical and Gaussian variables, their moments, Shannon entropy and the Kullback–Leibler divergence.

### [00:32.2] Intuition — `manim:S02`

**ES:** Empecemos con una moneda cargada que sale uno con probabilidad p = 0,7. Es una variable de Bernoulli. Lancémosla muchas veces y sigamos la fracción de unos. Al principio la curva oscila mucho, pero a medida que crece el número de lanzamientos se acerca a cero coma siete. Es la ley de los grandes números: el promedio de muchas muestras converge al valor esperado. Si en lugar de dos resultados hay K, como en un dado, tenemos una variable categórica, descrita por un vector de probabilidades que suma uno.

**EN:** Let's start with a biased coin that comes up one with probability p = 0.7. It is a Bernoulli variable. Let's flip it many times and track the fraction of ones. At first the curve swings a lot, but as the number of flips grows it approaches 0.7. This is the law of large numbers: the average of many samples converges to the expected value. If instead of two outcomes there are K, like a die, we have a categorical variable, described by a probability vector that sums to one.

### [01:05.8] The Gaussian — `manim:S03`

**ES:** Ahora sumemos muchas variables de Bernoulli. Si sumamos veinte lanzamientos y repetimos el experimento miles de veces, el histograma de la suma toma forma de campana. La curva verde es una gaussiana con la misma media, n p, y la misma varianza, n p (1 − p). Es el teorema central del límite: sumas de muchas contribuciones independientes tienden a una gaussiana. Por eso el ruido térmico, que es la suma de innumerables choques microscópicos, es gaussiano. La densidad es p(x) = exp(−(x−μ)²/2σ²)/√(2πσ²).

**EN:** Now let's add up many Bernoulli variables. If we add twenty flips and repeat the experiment thousands of times, the histogram of the sum takes a bell shape. The green curve is a Gaussian with the same mean, n p, and the same variance, n p (1 − p). This is the central limit theorem: sums of many independent contributions tend to a Gaussian. That is why thermal noise, the sum of countless microscopic collisions, is Gaussian. The density is p(x) = exp(−(x−μ)²/2σ²)/√(2πσ²).

### [01:47.1] Multivariate Gaussian — `manim:S04`

**ES:** En varias dimensiones, la nube de puntos de una gaussiana estándar es redonda: cada coordenada es independiente y tiene varianza uno. Apliquemos una transformación lineal A a cada punto y sumemos un vector b. La nube se estira, rota y se traslada. La nueva media es b, y la nueva matriz de covarianza es A Aᵀ. La elipse dibujada encierra la región donde vive la mayor parte de la probabilidad: sus ejes son los vectores propios de la covarianza, y sus longitudes, las raíces de los valores propios. Esta regla de transformación es la base del solucionador lineal termodinámico que veremos en la unidad seis.

**EN:** In several dimensions, the point cloud of a standard Gaussian is round: each coordinate is independent with variance one. Let's apply a linear transformation A to each point and add a vector b. The cloud stretches, rotates and shifts. The new mean is b, and the new covariance matrix is A Aᵀ. The drawn ellipse encloses the region where most of the probability lives: its axes are the eigenvectors of the covariance, and its lengths, the square roots of the eigenvalues. This transformation rule is the basis of the thermodynamic linear solver we will see in unit six.

### [02:27.2] Moments — `manim:S05`

**ES:** Los momentos resumen una distribución. El primer momento es la media, el centro de masa. El segundo momento central es la varianza, que mide el ancho. Para una gaussiana, la media y la covarianza determinan todo. Esto tendrá una consecuencia profunda: un sistema físico que se relaja hacia una gaussiana guarda la respuesta de un problema lineal en su media, y la de la matriz inversa en su covarianza.

**EN:** Moments summarize a distribution. The first moment is the mean, the center of mass. The second central moment is the variance, which measures the width. For a Gaussian, the mean and the covariance determine everything. This will have a deep consequence: a physical system relaxing toward a Gaussian stores the answer to a linear problem in its mean, and the inverse matrix in its covariance.

### [02:53.5] Shannon entropy — `manim:S06`

**ES:** ¿Cuánta información trae un resultado? Shannon propuso medirla por la sorpresa, menos el logaritmo de su probabilidad. Un evento seguro no sorprende; uno raro sorprende mucho. La entropía es la sorpresa promedio: H = −Σ p log p. Para una moneda, la curva vale cero si el resultado es seguro y alcanza su máximo, un bit, cuando la moneda es justa. Para una gaussiana, la entropía crece con el logaritmo de la desviación estándar: más ancha, más incierta.

**EN:** How much information does an outcome carry? Shannon proposed measuring it by surprise, minus the log of its probability. A certain event is no surprise; a rare one is very surprising. Entropy is the average surprise: H = −Σ p log p. For a coin, the curve is zero if the outcome is certain and peaks at one bit when the coin is fair. For a Gaussian, entropy grows with the log of the standard deviation: wider means more uncertain.

### [03:26.9] KL divergence — `manim:S07`

**ES:** Para comparar dos distribuciones usamos la divergencia de Kullback y Leibler: el promedio, bajo p, del logaritmo del cociente p sobre q. Mide cuántos bits extra pagamos si codificamos datos de p usando un código diseñado para q. Siempre es mayor o igual que cero, y vale cero solo si las distribuciones coinciden. Pero no es una distancia: no es simétrica. Fíjate en los dos números cuando la gaussiana naranja se mueve y se ensancha: cambian de forma distinta.

**EN:** To compare two distributions we use the Kullback–Leibler divergence: the average, under p, of the log of the ratio p over q. It measures how many extra bits we pay if we encode data from p using a code designed for q. It is always greater than or equal to zero, and is zero only if the distributions coincide. But it is not a distance: it is not symmetric. Watch the two numbers as the orange Gaussian moves and widens: they change differently.

### [03:56.7] Numerical example — `manim:S08`

**ES:** Hagamos dos cálculos. La entropía de una moneda con p = 0,9 es menos cero coma nueve por el logaritmo en base dos de cero coma nueve, menos cero coma uno por el logaritmo de cero coma uno. El resultado es cero coma cuarenta y siete bits. Segundo: la divergencia entre una normal estándar y una normal de media uno y desviación dos. La fórmula cerrada da el logaritmo de dos, más un cuarto, menos un medio: unos cero coma cuarenta y cuatro nats.

**EN:** Let's do two calculations. The entropy of a coin with p = 0.9 is minus 0.9 times log base two of 0.9, minus 0.1 times log of 0.1. The result is 0.47 bits. Second: the divergence between a standard normal and a normal with mean one and standard deviation two. The closed form gives log of two, plus a quarter, minus a half: about 0.44 nats.

### [04:28.0] Applications — `slide`

**ES:** Estas piezas aparecen en todo el curso. El pbit es una variable de Bernoulli cuya probabilidad controla un campo local. El estado final del proceso de Ornstein y Uhlenbeck es una gaussiana multivariada. La entropía fija el costo de Landauer. Y la divergencia KL aparece en el aprendizaje de máquinas de Boltzmann, en los modelos de difusión y en el gradiente natural.

**EN:** These pieces appear throughout the course. The pbit is a Bernoulli variable whose probability is controlled by a local field. The final state of the Ornstein–Uhlenbeck process is a multivariate Gaussian. Entropy sets the Landauer cost. And the KL divergence appears in Boltzmann machine learning, in diffusion models and in the natural gradient.

### [04:52.0] Connections — `slide`

**ES:** En la próxima lección veremos las matrices simétricas definidas positivas, que dan forma a la elipse de covarianza. Luego estudiaremos cadenas de Markov, donde las distribuciones evolucionan en el tiempo. En la unidad uno conectaremos la entropía de Shannon con la de Gibbs, y en la unidad dos aprenderemos a poner barras de error a promedios de muestras correlacionadas.

**EN:** In the next lesson we will see symmetric positive-definite matrices, which shape the covariance ellipse. Then we will study Markov chains, where distributions evolve in time. In unit one we will connect Shannon entropy with Gibbs entropy, and in unit two we will learn to put error bars on averages of correlated samples.

### [05:15.0] Common mistakes — `slide`

**ES:** Errores frecuentes: la covarianza de A y más b es A Aᵀ, no A al cuadrado. La divergencia KL no es una distancia, porque no es simétrica. Cuida las unidades: con logaritmo en base dos medimos en bits, con logaritmo natural en nats. Y recuerda que la entropía diferencial de una densidad continua puede ser negativa, a diferencia de la entropía de una variable discreta.

**EN:** Frequent mistakes: the covariance of A y plus b is A Aᵀ, not A squared. The KL divergence is not a distance, because it is not symmetric. Watch the units: with log base two we measure in bits, with the natural log in nats. And remember that the differential entropy of a continuous density can be negative, unlike the entropy of a discrete variable.

### [05:41.9] Summary — `manim:S12`

**ES:** En resumen: Bernoulli, categórica y gaussiana son las variables básicas del curso. Una transformación lineal lleva una gaussiana estándar a una de media b y covarianza A Aᵀ. La entropía mide la sorpresa promedio, y la divergencia KL mide cuánto difiere una distribución de otra, sin ser simétrica.

**EN:** In summary: Bernoulli, categorical and Gaussian are the basic variables of the course. A linear transformation takes a standard Gaussian to one with mean b and covariance A Aᵀ. Entropy measures average surprise, and the KL divergence measures how much one distribution differs from another, without being symmetric.

### [06:04.0] Self-assessment — `slide`

**ES:** Para practicar: obtén la media y la covarianza de A y más b. Calcula la entropía de una Bernoulli y de una gaussiana de dimensión d. Compara las dos divergencias KL entre una normal de varianza uno y otra de varianza cuatro. Y calcula cuántos lanzamientos necesitas para estimar una probabilidad con error estándar de un centésimo.

**EN:** To practice: find the mean and covariance of A y plus b. Compute the entropy of a Bernoulli and of a d-dimensional Gaussian. Compare the two KL divergences between a normal with variance one and one with variance four. And compute how many flips you need to estimate a probability with a standard error of one hundredth.

## Key equations
- $$y\sim\mathcal N(0,I),\ x = Ay + b \;\Rightarrow\; x\sim\mathcal N(b,\,AA^\top)$$ — Linear transformation of Gaussians.
- $$H(p) = -\sum_i p_i \log_2 p_i,\quad h(\mathcal N(\mu,\Sigma)) = \tfrac12\ln\det(2\pi e\,\Sigma)$$ — Shannon entropy (bits) and Gaussian differential entropy (nats).
- $$\mathrm{KL}(p\|q) = \mathbb E_p\!\left[\ln \tfrac{p}{q}\right] \ge 0$$ — Kullback–Leibler divergence: non-negative, zero only if $p=q$, not symmetric.
- $$\mathrm{KL}(\mathcal N_1\|\mathcal N_2) = \ln\tfrac{\sigma_2}{\sigma_1} + \tfrac{\sigma_1^2 + (\mu_1-\mu_2)^2}{2\sigma_2^2} - \tfrac12$$ — KL between one-dimensional Gaussians.

## Summary
- Bernoulli, categorical and Gaussian; the law of large numbers and the central limit theorem.
- $x = Ay+b$ with $y\sim\mathcal N(0,I)$ gives $\mathcal N(b, AA^\top)$.
- Entropy = average surprise; maximum of 1 bit for the fair coin.
- KL $\ge 0$, not symmetric; bits versus nats.

## Further reading
- [3] D. A. Levin, Y. Peres and E. L. Wilmer, Markov Chains and Mixing Times, AMS, 2009 (ch. 1, probability notation).
- [46] P. Holderrieth and E. Erives, An introduction to flow matching and diffusion models, 2025 (probability appendix).
- Syllabus, Appendix A: prerequisite self-assessment (questions 1 and 5).
