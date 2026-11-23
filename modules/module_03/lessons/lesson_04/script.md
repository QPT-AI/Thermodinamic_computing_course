# Lesson 3.4 — Thermodynamic speed limits

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the speed limit $\tau \ge W_2^2/(\mu k_BT\,\Sigma)$ and its meaning: fast and efficient at once is impossible.
- Compute the Wasserstein distance between Gaussians (Gelbrich bound) and the efficiency $\eta = W_2^2/(\mu\tau k_BT\Sigma) \le 1$.
- Recognize the optimal protocol: constant-speed transport along the geodesic.

## Prerequisites
- Lessons 3.1–3.2: entropy production.
- Lesson 0.3: multivariate Gaussians.

## Narrated script

### [00:05.3] Introduction — `manim:S01`

**ES:** Un computador debe transformar una distribución de probabilidad en otra: del estado inicial al resultado. La pregunta del curso es si puede hacerlo rápido y a la vez con poca disipación. Los límites termodinámicos de velocidad responden con precisión: el producto del tiempo por la entropía producida está acotado por debajo por una distancia geométrica entre las distribuciones, la distancia de Wasserstein.

**EN:** A computer must transform one probability distribution into another: from the initial state to the result. The question of the course is whether it can do so fast and with little dissipation at the same time. Thermodynamic speed limits answer precisely: the product of time and entropy produced is bounded below by a geometric distance between the distributions, the Wasserstein distance.

### [00:31.2] Intuition — `manim:S02`

**ES:** Imagina que hay que trasladar un montón de arena de un lugar a otro, con una pala que se mueve en un fluido viscoso. El costo de mover la arena con fricción crece con la velocidad al cuadrado. Si tenemos mucho tiempo, vamos despacio y gastamos poco; si tenemos poco, gastamos mucho. Y hay una forma óptima de repartir el trabajo: mover cada grano en línea recta, a velocidad constante. La distancia mínima total, medida con cuadrados, es la distancia de Wasserstein.

**EN:** Imagine having to move a pile of sand from one place to another, with a shovel moving through a viscous fluid. The cost of moving sand against friction grows with the square of the speed. If we have lots of time, we go slowly and spend little; if we have little time, we spend a lot. And there is an optimal way to split the work: move each grain in a straight line, at constant speed. The minimum total distance, measured with squares, is the Wasserstein distance.

### [01:01.2] The speed limit — `manim:S03`

**ES:** El resultado, para dinámicas sobreamortiguadas, es: τ ≥ W₂² / (μ k_B T Σ). Aquí W₂ es la distancia de Wasserstein entre la distribución inicial y la final, μ la movilidad y Σ la entropía total producida. Leído al revés: Σ ≥ W₂²/(μ k_B T τ). Para recorrer una distancia fija en un tiempo menor, hay que pagar más entropía, inversamente proporcional al tiempo. La curva muestra la región prohibida.

**EN:** The result, for overdamped dynamics, is: τ ≥ W₂² / (μ k_B T Σ). Here W₂ is the Wasserstein distance between the initial and final distributions, μ the mobility and Σ the total entropy produced. Read backward: Σ ≥ W₂²/(μ k_B T τ). To cover a fixed distance in less time, you must pay more entropy, inversely proportional to the time. The curve shows the forbidden region.

### [01:35.2] Wasserstein and Gelbrich — `manim:S04`

**ES:** La distancia de Wasserstein es el costo mínimo de transportar una distribución a otra, con costo igual al cuadrado de la distancia recorrida por cada grano de masa. Para gaussianas tiene forma cerrada: el cuadrado de la diferencia de medias más un término de las covarianzas, la fórmula de Gelbrich. En una dimensión, es la diferencia de medias al cuadrado más la diferencia de desviaciones al cuadrado. Para distribuciones cualesquiera, esa misma fórmula con medias y covarianzas es una cota inferior.

**EN:** The Wasserstein distance is the minimum cost of transporting one distribution into another, with cost equal to the square of the distance traveled by each grain of mass. For Gaussians it has a closed form: the squared difference of the means plus a covariance term, the Gelbrich formula. In one dimension, it is the squared difference of the means plus the squared difference of the standard deviations. For arbitrary distributions, that same formula with means and covariances is a lower bound.

### [02:06.4] Efficiency — `manim:S05`

**ES:** Definimos la eficiencia como η = W₂² / (μ τ k_B T Σ), que nunca supera uno. Comparemos dos protocolos que trasladan una partícula en una trampa. Arrastrar la trampa a velocidad constante: la partícula arranca con retraso y su media se acelera; la eficiencia es de cero coma ochenta y ocho. El protocolo óptimo hace que la media de la distribución avance a velocidad constante desde el primer instante: la eficiencia es exactamente uno. La lección es general: el protocolo óptimo recorre la geodésica a velocidad constante.

**EN:** We define the efficiency as η = W₂² / (μ τ k_B T Σ), which never exceeds one. Let's compare two protocols that translate a particle in a trap. Dragging the trap at constant speed: the particle starts with a lag and its mean accelerates; the efficiency is 0.88. The optimal protocol makes the mean of the distribution move at constant speed from the very first instant: the efficiency is exactly one. The lesson is general: the optimal protocol travels the geodesic at constant speed.

### [02:43.3] Numerical example — `manim:S06`

**ES:** Con rigidez uno, movilidad uno y k_B T uno, arrastramos la trampa a velocidad uno durante tres unidades de tiempo. La media de la partícula avanza dos coma cero cinco y la varianza no cambia, así que W₂² es cuatro coma dos cero. La entropía producida es la integral de la velocidad media al cuadrado, uno coma seis. El límite exige al menos cuatro coma dos entre tres, uno coma cuarenta; la eficiencia es cero coma ochenta y ocho. Si quisiéramos hacer el mismo transporte en la mitad del tiempo, la entropía mínima se duplicaría.

**EN:** With stiffness one, mobility one and k_B T one, we drag the trap at speed one for three time units. The particle's mean advances 2.05 and the variance does not change, so W₂² is 4.20. The entropy produced is the integral of the squared mean velocity, 1.6. The limit requires at least 4.2 over three, 1.40; the efficiency is 0.88. If we wanted the same transport in half the time, the minimum entropy would double.

### [03:20.3] Applications — `slide`

**ES:** Para el cómputo esto es central: transformar una distribución en otra en un tiempo dado tiene un costo mínimo en disipación, y borrar rápido cuesta más. La geometría de Wasserstein nos dice cuál es el mejor protocolo. En el laboratorio cuatro calcularás la eficiencia de un proceso gaussiano.

**EN:** For computing this is central: transforming one distribution into another in a given time has a minimum dissipation cost, and erasing fast costs more. Wasserstein geometry tells us which protocol is best. In lab four you will compute the efficiency of a Gaussian process.

### [03:39.0] Common mistakes — `slide`

**ES:** Errores frecuentes: confundir la distancia de Wasserstein con el trabajo, olvidar la entropía del sistema, aplicar la cota sobreamortiguada a sistemas con inercia, y creer que la eficiencia ideal no tiene costo.

**EN:** Frequent mistakes: confusing the Wasserstein distance with work, forgetting the system entropy, applying the overdamped bound to systems with inertia, and believing ideal efficiency comes for free.

### [03:53.3] Summary — `manim:S09`

**ES:** En resumen: transformar distribuciones cuesta entropía, al menos W₂² sobre μ k_B T τ. Rápido y eficiente a la vez es imposible. La distancia de Wasserstein mide cuánto hay que transportar, la fórmula de Gelbrich la da para gaussianas, y el protocolo óptimo transporta a velocidad constante.

**EN:** In summary: transforming distributions costs entropy, at least W₂² over μ k_B T τ. Fast and efficient at once is impossible. The Wasserstein distance measures how much must be transported, the Gelbrich formula gives it for Gaussians, and the optimal protocol transports at constant speed.

### [04:14.7] Self-assessment — `slide`

**ES:** Para practicar: calcula una distancia de Wasserstein entre gaussianas, la entropía mínima de un traslado, demuestra la desigualdad con Cauchy y Schwarz, y describe el protocolo óptimo.

**EN:** To practice: compute a Wasserstein distance between Gaussians, the minimum entropy of a translation, prove the inequality with Cauchy–Schwarz, and describe the optimal protocol.

## Key equations
- $$\tau \ge \frac{W_2^2(p_0, p_\tau)}{\mu k_BT\,\Sigma}$$ — Thermodynamic speed limit (overdamped).
- $$W_2^2\big(\mathcal N_1, \mathcal N_2\big) = \|m_1 - m_2\|^2 + \mathrm{tr}\big(\Sigma_1 + \Sigma_2 - 2(\Sigma_1^{1/2}\Sigma_2\Sigma_1^{1/2})^{1/2}\big)$$ — Gelbrich formula (exact for Gaussians; a lower bound in general).
- $$\eta = \frac{W_2^2}{\mu\tau k_BT\,\Sigma} \le 1$$ — Transport efficiency of a protocol.

## Summary
- $\tau\,\Sigma \ge W_2^2/(\mu k_BT)$: fast and efficient at once is impossible.
- $W_2$: optimal transport cost; Gelbrich for Gaussians.
- $\eta \le 1$; optimum = geodesic at constant speed.
- Linear dragging of a trap: $\eta \approx 0.88$ in the example.

## Further reading
- [42] S. Whitelam, The thermodynamic freedom of a thermodynamic computer, 2026.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics.
- [11] U. Seifert, Stochastic thermodynamics..., 2012.
