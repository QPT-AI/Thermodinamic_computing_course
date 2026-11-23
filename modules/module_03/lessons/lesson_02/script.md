# Lesson 3.2 — Entropy production and the second law for trajectories

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the total entropy production per trajectory $\Sigma$ and its mean rate.
- State the integral fluctuation theorem $\langle e^{-\Sigma}\rangle = 1$ and deduce $\langle\Sigma\rangle \ge 0$.
- Verify the detailed fluctuation theorem $P(\Sigma)/P(-\Sigma) = e^{\Sigma}$ in a non-equilibrium steady state.

## Prerequisites
- Lesson 3.1: stochastic entropy and heat.
- Lesson 2.3: probability current and NESS.

## Narrated script

### [00:06.4] Introduction — `manim:S01`

**ES:** La segunda ley dice que la entropía total no disminuye. En la lección anterior vimos trayectorias individuales con trabajo negativo, que parecen violarla. ¿Cuánto la violan, y con qué frecuencia? La respuesta es una de las leyes más bellas de la física moderna: los teoremas de fluctuación. Convierten la desigualdad de la segunda ley en una igualdad exacta sobre la distribución de la producción de entropía.

**EN:** The second law says total entropy does not decrease. In the previous lesson we saw individual trajectories with negative work, which seem to violate it. By how much do they violate it, and how often? The answer is one of the most beautiful laws of modern physics: the fluctuation theorems. They turn the inequality of the second law into an exact equality about the distribution of entropy production.

### [00:31.7] Intuition — `manim:S02`

**ES:** Imagina grabar en video una trayectoria y reproducirla hacia atrás. Si el sistema está en equilibrio, la película al revés es igual de plausible. Si hay una fuerza que lo empuja, la película al revés es menos probable: la partícula sube contra la fuerza. La producción de entropía mide exactamente eso: el logaritmo del cociente entre la probabilidad de la trayectoria y la de su inversa en el tiempo. Es una medida de irreversibilidad.

**EN:** Imagine filming a trajectory and playing it backward. If the system is at equilibrium, the reversed movie is just as plausible. If a force is pushing it, the reversed movie is less likely: the particle climbs against the force. Entropy production measures exactly that: the log of the ratio between the probability of the trajectory and that of its time reverse. It is a measure of irreversibility.

### [00:59.7] Definition — `manim:S03`

**ES:** La producción total de entropía en una trayectoria, en unidades de k_B, es el cambio de entropía del sistema más el calor entregado al baño dividido por k_B T. Y es exactamente el logaritmo del cociente de probabilidades de la trayectoria directa y de su inversa: Σ = ln P[x]/P̃[x̃]. En un estado estacionario, su tasa media se escribe con la corriente de probabilidad: la integral de J²/(D p), que es positiva y solo se anula si la corriente es cero, es decir, en equilibrio.

**EN:** The total entropy production along a trajectory, in units of k_B, is the change in system entropy plus the heat given to the bath divided by k_B T. And it is exactly the log of the ratio of probabilities of the forward trajectory and its reverse: Σ = ln P[x]/P̃[x̃]. In a steady state, its mean rate is written with the probability current: the integral of J²/(D p), which is positive and vanishes only if the current is zero, that is, at equilibrium.

### [01:34.2] Integral fluctuation theorem — `manim:S04`

**ES:** De esa definición sale una igualdad exacta: el promedio de e^(−Σ) es uno. Siempre, para cualquier protocolo y cualquier duración. Aplicando la desigualdad de Jensen, el promedio de Σ es mayor o igual que cero: la segunda ley es una consecuencia. Pero la igualdad dice más: para que el promedio de la exponencial sea uno, tiene que haber trayectorias con Σ negativa. Las violaciones individuales no son un accidente: son obligatorias.

**EN:** An exact equality follows from that definition: the average of e^(−Σ) is one. Always, for any protocol and any duration. Applying Jensen's inequality, the average of Σ is greater than or equal to zero: the second law is a consequence. But the equality says more: for the average of the exponential to be one, there must be trajectories with negative Σ. Individual violations are not an accident: they are mandatory.

### [02:04.4] Detailed theorem — `manim:S05`

**ES:** En un estado estacionario hay una versión aún más fuerte: la probabilidad de producir una cantidad Σ de entropía, dividida por la de producir menos Σ, es exactamente e^Σ. Comprobémoslo con una partícula en un anillo empujada por una fuerza constante. El histograma de la entropía producida en un intervalo es gaussiano y cruza el cero. Al graficar el logaritmo del cociente entre la probabilidad de Σ y la de menos Σ, los puntos caen sobre la recta de pendiente uno. Las trayectorias que destruyen entropía existen, pero son exponencialmente raras.

**EN:** In a steady state there is an even stronger version: the probability of producing an amount Σ of entropy, divided by that of producing minus Σ, is exactly e^Σ. Let's check it with a particle on a ring pushed by a constant force. The histogram of the entropy produced in an interval is Gaussian and crosses zero. Plotting the log of the ratio between the probability of Σ and that of minus Σ, the points fall on the line of slope one. Trajectories that destroy entropy exist, but they are exponentially rare.

### [02:41.1] Numerical example — `manim:S06`

**ES:** Con movilidad uno, k_B T uno, fuerza un medio y una ventana de tiempo dos, la producción de entropía es gaussiana con media cero coma cinco y varianza uno. La probabilidad de que una trayectoria destruya entropía es de alrededor del treinta y uno por ciento. Si alargamos la ventana a veinte, la media sube a cinco y esa probabilidad cae a alrededor del seis por ciento; con doscientas, a menos de una en un millón: la segunda ley emerge para tiempos largos.

**EN:** With mobility one, k_B T one, force one half and a time window of two, entropy production is Gaussian with mean 0.5 and variance one. The probability that a trajectory destroys entropy is about thirty-one percent. If we lengthen the window to twenty, the mean rises to five and that probability falls to about six percent; at two hundred, to less than one in a million: the second law emerges at long times.

### [03:11.8] Applications — `slide`

**ES:** La producción de entropía es el costo energético irreducible de cualquier cómputo irreversible. Gobierna la precisión de relojes y motores moleculares, puede inferirse a partir de trayectorias medidas, y en un chip forzado fuera del equilibrio se produce de forma continua.

**EN:** Entropy production is the irreducible energy cost of any irreversible computation. It governs the precision of clocks and molecular motors, it can be inferred from measured trajectories, and in a chip driven out of equilibrium it is produced continuously.

### [03:29.0] Common mistakes — `slide`

**ES:** Errores comunes: pensar que una trayectoria con producción negativa viola la segunda ley, cuando es obligatoria. Olvidar la entropía del sistema en los transitorios. Aplicar el teorema detallado fuera de sus condiciones. Y confundir la producción de entropía con el calor.

**EN:** Common mistakes: thinking a trajectory with negative production violates the second law, when it is mandatory. Forgetting the system entropy in transients. Applying the detailed theorem outside its conditions. And confusing entropy production with heat.

### [03:46.5] Summary — `manim:S09`

**ES:** En resumen: la producción de entropía de una trayectoria es el logaritmo del cociente entre su probabilidad y la de su inversa en el tiempo. Cumple la igualdad ⟨e^(−Σ)⟩ = 1, de la que la segunda ley es una consecuencia. En estado estacionario, la probabilidad de destruir entropía es exponencialmente menor que la de producirla.

**EN:** In summary: the entropy production of a trajectory is the log of the ratio between its probability and that of its time reverse. It satisfies the equality ⟨e^(−Σ)⟩ = 1, of which the second law is a consequence. In a steady state, the probability of destroying entropy is exponentially smaller than that of producing it.

### [04:08.6] Self-assessment — `slide`

**ES:** Para practicar: deduce la segunda ley de la igualdad integral. Muestra que una producción gaussiana debe tener varianza igual al doble de la media. Calcula una tasa de producción de entropía. Y evalúa un cociente del teorema detallado.

**EN:** To practice: deduce the second law from the integral equality. Show that a Gaussian production must have variance equal to twice the mean. Compute an entropy production rate. And evaluate a ratio from the detailed theorem.

## Key equations
- $$\Sigma = \Delta s + \frac{-Q}{k_BT} = \ln\frac{\mathcal P[x(\cdot)]}{\tilde{\mathcal P}[\tilde x(\cdot)]}$$ — Total entropy production per trajectory (units of $k_B$) as irreversibility.
- $$\langle e^{-\Sigma}\rangle = 1\ \Rightarrow\ \langle\Sigma\rangle \ge 0$$ — Integral fluctuation theorem and the second law.
- $$\frac{P(\Sigma)}{P(-\Sigma)} = e^{\Sigma}$$ — Detailed fluctuation theorem (steady state).
- $$\langle\dot\Sigma\rangle = \int\frac{J^2}{D\,p}\,dx \ge 0$$ — Mean rate in terms of the Fokker–Planck current.

## Summary
- $\Sigma$ = irreversibility of the trajectory (forward versus reverse).
- $\langle e^{-\Sigma}\rangle = 1$ ⇒ $\langle\Sigma\rangle \ge 0$, with mandatory violations.
- Stationary: $P(\Sigma)/P(-\Sigma) = e^{\Sigma}$.
- The dissipation of a computation is $k_BT\langle\Sigma\rangle$.

## Further reading
- [11] U. Seifert, Stochastic thermodynamics, fluctuation theorems and molecular machines, 2012.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics, ch. 6.
- Video V8: From Stochastic Thermodynamics to Thermodynamic Inference — U. Seifert.
