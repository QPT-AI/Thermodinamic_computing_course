# Lesson 3.6 — Thermodynamic uncertainty relations

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the thermodynamic uncertainty relation (TUR): $\mathrm{Var}(J)/\langle J\rangle^2 \ge 2/\Sigma$.
- State the kinetic bound with the dynamical activity and compare both.
- Apply them to computation time: a precise, fast computation costs entropy or activity.

## Prerequisites
- Lesson 3.2: entropy production.
- Lesson 2.8: jump processes and Gillespie.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Un reloj, un motor molecular o un circuito que cuenta pasos tienen algo en común: producen una corriente, un número de eventos que crece con el tiempo. Pero en un sistema pequeño esa corriente fluctúa. ¿Cuánto cuesta hacerla precisa? Las relaciones de incertidumbre termodinámica responden: la precisión se paga con producción de entropía.

**EN:** A clock, a molecular motor or a circuit that counts steps have something in common: they produce a current, a number of events that grows with time. But in a small system that current fluctuates. How much does it cost to make it precise? Thermodynamic uncertainty relations answer: precision is paid for with entropy production.

### [00:28.2] Intuition — `manim:S02`

**ES:** Tomemos el modelo más simple: un contador que salta hacia adelante con tasa k₊ y hacia atrás con tasa k₋. Cada salto adelante disipa el logaritmo de k₊ sobre k₋, en unidades de k_B. Si las tasas son casi iguales, el contador avanza poco y de forma errática; si el salto atrás es muy raro, avanza de forma regular, pero cada paso cuesta mucha entropía. Aquí ves trayectorias simuladas con Gillespie para dos sesgos distintos.

**EN:** Let's take the simplest model: a counter that jumps forward with rate k₊ and backward with rate k₋. Each forward jump dissipates the log of k₊ over k₋, in units of k_B. If the rates are nearly equal, the counter advances little and erratically; if backward jumps are very rare, it advances regularly, but each step costs a lot of entropy. Here you see trajectories simulated with Gillespie for two different biases.

### [00:57.8] The TUR — `manim:S03`

**ES:** La relación de incertidumbre termodinámica, demostrada para procesos de Markov en estado estacionario, dice que la varianza relativa de cualquier corriente es al menos dos dividido por la entropía total producida: Var(J)/⟨J⟩² ≥ 2/Σ. Para reducir el error relativo a la mitad, hay que cuadruplicar la entropía. Para el contador, el producto de la varianza relativa por la entropía es (k₊ + k₋) ln(k₊/k₋)/(k₊ − k₋), que nunca baja de dos y lo alcanza cerca del equilibrio.

**EN:** The thermodynamic uncertainty relation, proven for Markov processes in a steady state, says that the relative variance of any current is at least two divided by the total entropy produced: Var(J)/⟨J⟩² ≥ 2/Σ. To halve the relative error, you must quadruple the entropy. For the counter, the product of relative variance and entropy is (k₊ + k₋) ln(k₊/k₋)/(k₊ − k₋), which never drops below two and reaches it near equilibrium.

### [01:36.0] Kinetic bound — `manim:S04`

**ES:** Hay una segunda cota, que no usa la entropía sino la actividad: el número medio total de saltos, hacia adelante y hacia atrás. La cota cinética dice que la varianza relativa es al menos uno sobre la actividad. Las dos cotas son complementarias: la termodinámica es ajustada cerca del equilibrio; la cinética, lejos de él, cuando casi no hay saltos hacia atrás. Existen también cotas mixtas que combinan entropía y actividad en una sola desigualdad.

**EN:** There is a second bound, which uses not entropy but activity: the mean total number of jumps, forward and backward. The kinetic bound says the relative variance is at least one over the activity. The two bounds are complementary: the thermodynamic one is tight near equilibrium; the kinetic one, far from it, when there are almost no backward jumps. There are also mixed bounds that combine entropy and activity in a single inequality.

### [02:04.8] Computation time — `manim:S05`

**ES:** Para un cómputo, lo que importa es el tiempo hasta terminar: el instante en que el contador llega a N pasos. Las mismas cotas valen para la varianza relativa de ese tiempo, con la entropía y la actividad acumuladas hasta terminar. Con cien pasos y k₊ = 3, k₋ = 1, la simulación da un tiempo medio de cincuenta y una varianza relativa de cero coma cero dos. La cota termodinámica exige al menos cero coma cero uno ocho; la cinética, cero coma cero cero cinco. Con k₊ = 20, la varianza relativa es cero coma cero uno uno, y ahora la cota cinética, cero coma cero cero nueve, es la más ajustada.

**EN:** For a computation, what matters is the time to finish: the instant the counter reaches N steps. The same bounds hold for the relative variance of that time, with the entropy and activity accumulated until it finishes. With a hundred steps and k₊ = 3, k₋ = 1, the simulation gives a mean time of fifty and a relative variance of 0.02. The thermodynamic bound requires at least 0.018; the kinetic one, 0.005. With k₊ = 20, the relative variance is 0.011, and now the kinetic bound, 0.009, is the tighter one.

### [02:46.1] Numerical example — `manim:S06`

**ES:** Comparemos los tres sesgos simulados, siempre con cien pasos. Con k₊ igual a uno coma dos, casi en equilibrio, la varianza relativa es cero coma once y la cota termodinámica es cero coma once: está saturada. Con tres, la cota termodinámica sigue cerca. Con veinte, la cinética domina. En todos los casos, la simulación respeta ambas cotas.

**EN:** Let's compare the three simulated biases, always with a hundred steps. With k₊ equal to 1.2, almost at equilibrium, the relative variance is 0.11 and the thermodynamic bound is 0.11: it is saturated. With three, the thermodynamic bound is still close. With twenty, the kinetic one dominates. In every case, the simulation respects both bounds.

### [03:10.2] Applications — `slide`

**ES:** Estas cotas se aplican al tiempo de cómputo de circuitos brownianos, a la precisión de relojes moleculares, y al revés: midiendo las fluctuaciones de una corriente se obtiene una cota inferior a la disipación, sin conocer los detalles del sistema.

**EN:** These bounds apply to the computation time of Brownian circuits, to the precision of molecular clocks, and in reverse: measuring the fluctuations of a current gives a lower bound on dissipation, without knowing the details of the system.

### [03:25.8] Common mistakes — `slide`

**ES:** Cuidado con el dominio de validez, con usar la tasa en lugar de la entropía total, con el factor dos, y con suponer que la cota siempre está saturada.

**EN:** Watch the domain of validity, using the rate instead of the total entropy, the factor of two, and assuming the bound is always saturated.

### [03:35.8] Summary — `manim:S09`

**ES:** En resumen: la precisión de cualquier corriente está limitada por la entropía producida, Var(J)/⟨J⟩² ≥ 2/Σ, y por la actividad, Var(J)/⟨J⟩² ≥ 1/A. La primera es ajustada cerca del equilibrio y la segunda lejos de él. Para un cómputo, las mismas cotas limitan las fluctuaciones del tiempo hasta terminar.

**EN:** In summary: the precision of any current is limited by the entropy produced, Var(J)/⟨J⟩² ≥ 2/Σ, and by the activity, Var(J)/⟨J⟩² ≥ 1/A. The first is tight near equilibrium and the second far from it. For a computation, the same bounds limit the fluctuations of the time to finish.

### [03:59.9] Self-assessment — `slide`

**ES:** Para practicar: calcula media, varianza y entropía del contador, verifica la TUR, estima la entropía para un error del uno por ciento y explica cuándo gana la cota cinética.

**EN:** To practice: compute the counter's mean, variance and entropy, check the TUR, estimate the entropy for a one-percent error and explain when the kinetic bound wins.

## Key equations
- $$\frac{\mathrm{Var}(J)}{\langle J\rangle^2} \ge \frac{2k_B}{\Sigma}$$ — Thermodynamic uncertainty relation (Markov, steady state).
- $$\frac{\mathrm{Var}(J)}{\langle J\rangle^2} \ge \frac{1}{\mathcal A}$$ — Kinetic bound: $\mathcal A$ is the mean number of jumps.
- $$\epsilon^2\Sigma = \frac{(k_+ + k_-)\ln(k_+/k_-)}{k_+ - k_-} \ge 2$$ — Biased counter: precision–entropy product.

## Summary
- Precision ↔ entropy: $\epsilon^2 \ge 2/\Sigma$.
- Precision ↔ activity: $\epsilon^2 \ge 1/\mathcal A$.
- TUR tight near equilibrium; kinetic bound far from it.
- The same bounds limit computation time.

## Further reading
- [26] Y. Utsumi et al., Computation time and thermodynamic uncertainty relation of Brownian circuits, 2022.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics.
- [11] U. Seifert, Stochastic thermodynamics..., 2012.
