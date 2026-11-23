# Lesson 3.7 — Thermodynamics of resetting and error-free readout

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Compute the minimum cost of resetting a memory with an arbitrary prior: $W \ge k_BT\,[H(p) - H(\varepsilon)]$ (nats).
- Relate the retention time of a bit to its barrier height through the Arrhenius law.
- Estimate the signal energy needed for a readout with error probability $\varepsilon$: $E \approx k_BT\,\tfrac12 Q^{-1}(\varepsilon)^2$.

## Prerequisites
- Lesson 1.5: Landauer's principle.
- Lesson 1.6: thermal noise and $k_BT/C$.
- Lesson 3.2: entropy production.

## Narrated script

### [00:06.3] Introduction — `manim:S01`

**ES:** Todo computador repite un ciclo: pone su memoria en un estado conocido, calcula y lee el resultado. En la lección uno punto cinco vimos el costo de borrar un bit completamente desconocido. Pero en la práctica la memoria casi nunca es uniforme, el reinicio nunca es perfecto y la lectura también tiene ruido. Esta lección pone precio a las tres cosas: reiniciar, conservar y leer un bit sin errores.

**EN:** Every computer repeats a cycle: it puts its memory in a known state, computes, and reads the result. In lesson 1.5 we saw the cost of erasing a completely unknown bit. But in practice memory is almost never uniform, reset is never perfect, and readout is noisy too. This lesson puts a price on all three: resetting, retaining and reading a bit without errors.

### [00:33.2] Reset with a prior — `manim:S02`

**ES:** Supongamos que la memoria vale uno con probabilidad p y cero con probabilidad uno menos p. Reiniciarla a cero elimina su entropía de Shannon, así que la cota de Landauer generalizada es W ≥ k_B T H(p), con la entropía medida en nats. La curva muestra esa cota: vale k_B T ln 2 cuando el bit es uniforme y cae a cero cuando ya sabemos su valor. Reiniciar un bit que casi siempre vale cero es casi gratis.

**EN:** Suppose the memory is one with probability p and zero with probability one minus p. Resetting it to zero removes its Shannon entropy, so the generalized Landauer bound is W ≥ k_B T H(p), with entropy measured in nats. The curve shows that bound: it equals k_B T ln 2 when the bit is uniform and falls to zero when we already know its value. Resetting a bit that is almost always zero is almost free.

### [01:05.0] Imperfect reset — `manim:S03`

**ES:** Ningún reinicio real es perfecto: al final queda una probabilidad de error ε de que el bit siga en uno. La memoria final todavía tiene entropía H(ε), y la cota se convierte en W ≥ k_B T (H(p) − H(ε)). Con un bit uniforme y un error de uno por ciento, el mínimo baja de cero coma seis nueve a cero coma seis cuatro k_B T. Aceptar errores abarata el reinicio, pero muy poco. Y si el protocolo dura un tiempo finito, se suma el exceso que decae como uno sobre τ.

**EN:** No real reset is perfect: at the end there remains an error probability ε that the bit is still one. The final memory still has entropy H(ε), and the bound becomes W ≥ k_B T (H(p) − H(ε)). With a uniform bit and a one-percent error, the minimum drops from 0.69 to 0.64 k_B T. Accepting errors makes reset cheaper, but only slightly. And if the protocol takes a finite time, the excess that decays as one over τ is added.

### [01:40.0] Retention — `manim:S04`

**ES:** Un bit reiniciado también tiene que quedarse quieto. En un pozo doble, el ruido térmico lo hace saltar la barrera con la tasa de Arrhenius, ν₀ e^(−E_b/k_B T). Para que la probabilidad de un salto en un tiempo t sea menor que ε, la barrera debe cumplir E_b ≥ k_B T ln(ν₀ t / ε). Con una frecuencia de intento de 10¹² Hz y un error de uno en mil millones, conservar el bit un segundo exige unos cuarenta y ocho k_B T; diez años exigen unos sesenta y ocho. La retención crece exponencialmente con la barrera, pero la barrera solo crece con el logaritmo del tiempo.

**EN:** A reset bit must also stay put. In a double well, thermal noise makes it hop the barrier at the Arrhenius rate, ν₀ e^(−E_b/k_B T). For the probability of a hop within a time t to be below ε, the barrier must satisfy E_b ≥ k_B T ln(ν₀ t / ε). With an attempt frequency of 10¹² Hz and an error of one in a billion, keeping the bit for one second takes about forty-eight k_B T; ten years take about sixty-eight. Retention grows exponentially with the barrier, but the barrier only grows with the log of the time.

### [02:22.2] Error-free readout — `manim:S05`

**ES:** Ahora leamos el bit. El sensor es un nodo de capacidad C cuyo voltaje tiene ruido térmico de varianza k_B T/C. Un comparador decide cero o uno según el voltaje supere un umbral a mitad de camino. La probabilidad de error es la cola de la gaussiana, Q(V/σ). Para un error de uno en mil millones, la señal debe ser seis desviaciones estándar, y la energía de la señal, ½ C V², resulta de unos dieciocho k_B T. En general esa energía crece como k_B T ln(1/ε): cada factor diez de confiabilidad cuesta un poco más de dos k_B T.

**EN:** Now let's read the bit. The sensor is a node of capacitance C whose voltage has thermal noise of variance k_B T/C. A comparator decides zero or one depending on whether the voltage exceeds a threshold halfway. The error probability is the Gaussian tail, Q(V/σ). For an error of one in a billion, the signal must be six standard deviations, and the signal energy, ½ C V², comes to about eighteen k_B T. In general that energy grows as k_B T ln(1/ε): each factor of ten in reliability costs a little over two k_B T.

### [03:02.7] Readout and reset cycle — `manim:S06`

**ES:** ¿Dónde está el costo inevitable de leer? Como en el demonio de Maxwell, copiar el bit a una memoria limpia puede hacerse de forma reversible. Lo que no puede evitarse es reiniciar esa memoria para la siguiente lectura. Si el resultado se descarta, cada lectura paga al menos la entropía del resultado, k_B T H, al reiniciar. Por eso un chip que lee pbits millones de veces por segundo gasta energía de lectura y de reinicio que puede superar con creces la del propio muestreo.

**EN:** Where is the unavoidable cost of reading? As with Maxwell's demon, copying the bit into a clean memory can be done reversibly. What cannot be avoided is resetting that memory for the next readout. If the result is discarded, each readout pays at least the result's entropy, k_B T H, at reset. That is why a chip that reads pbits millions of times per second spends readout and reset energy that can far exceed that of the sampling itself.

### [03:33.4] Numerical example — `manim:S07`

**ES:** Reunamos los números a trescientos kelvin. Reiniciar un bit uniforme con un error del uno por ciento cuesta como mínimo cero coma seis cuatro k_B T, unos 2,6 × 10⁻²¹ J. Leerlo con un error de uno en mil millones exige una señal de dieciocho k_B T, unos 7,5 × 10⁻²⁰ J. Y conservarlo diez años exige una barrera de sesenta y ocho k_B T. La lectura confiable cuesta casi treinta veces más que el reinicio ideal.

**EN:** Let's gather the numbers at three hundred kelvin. Resetting a uniform bit with a one-percent error costs at least 0.64 k_B T, about 2.6 × 10⁻²¹ J. Reading it with an error of one in a billion requires an eighteen k_B T signal, about 7.5 × 10⁻²⁰ J. And keeping it for ten years requires a barrier of sixty-eight k_B T. Reliable readout costs almost thirty times more than the ideal reset.

### [04:04.9] Applications — `slide`

**ES:** En hardware estas cuentas deciden el diseño. En un chip termodinámico, la energía de entrada y salida para leer pbits suele dominar sobre la del tejido que muestrea. Leer con menos frecuencia, espaciando las lecturas más que el tiempo de autocorrelación, ahorra energía sin perder información. En Torx, cada actualización de Gibbs es un reinicio seguido de una compuerta, y veremos la diferencia entre un reinicio ideal y uno finito.

**EN:** In hardware these accounts drive the design. In a thermodynamic chip, the input and output energy to read pbits often dominates over that of the sampling fabric. Reading less often, spacing readouts more than the autocorrelation time, saves energy without losing information. In Torx, each Gibbs update is a reset followed by a gate, and we will see the difference between an ideal reset and a finite one.

### [04:32.9] Common mistakes — `slide`

**ES:** Errores frecuentes: usar k_B T ln 2 para cualquier reinicio, cuando la cota depende de la distribución previa. Confundir la barrera que conserva el bit con el costo de reiniciarlo. Creer que leer es gratis porque la copia puede ser reversible. Y mezclar bits con nats.

**EN:** Frequent mistakes: using k_B T ln 2 for any reset, when the bound depends on the prior distribution. Confusing the barrier that retains the bit with the cost of resetting it. Believing reading is free because the copy can be reversible. And mixing bits with nats.

### [04:51.6] Summary — `manim:S10`

**ES:** En resumen: reiniciar cuesta al menos k_B T (H(p) − H(ε)), que depende de lo que ya sabemos y del error aceptado. Conservar un bit exige una barrera que crece con el logaritmo del tiempo de retención. Leer con error ε exige una señal de unos k_B T ln(1/ε). Y el costo inevitable de leer aparece al reiniciar la memoria donde se guardó el resultado.

**EN:** In summary: resetting costs at least k_B T (H(p) − H(ε)), which depends on what we already know and on the accepted error. Retaining a bit requires a barrier that grows with the log of the retention time. Reading with error ε requires a signal of about k_B T ln(1/ε). And the unavoidable cost of reading appears when resetting the memory where the result was stored.

### [05:18.6] Self-assessment — `slide`

**ES:** Para practicar: calcula el costo de reiniciar un bit sesgado con un error dado. Encuentra la barrera para conservar un bit una hora. Calcula la energía y el voltaje de una lectura confiable. Y explica por qué leer en cada barrido desperdicia energía cuando las muestras están correlacionadas.

**EN:** To practice: compute the cost of resetting a biased bit with a given error. Find the barrier to retain a bit for one hour. Compute the energy and voltage of a reliable readout. And explain why reading every sweep wastes energy when samples are correlated.

## Key equations
- $$W_{\text{reset}} \ge k_BT\,\big[H(p) - H(\varepsilon)\big]$$ — Generalized Landauer bound for resetting with prior $p$ and residual error $\varepsilon$ (entropies in nats).
- $$E_b \ge k_BT\,\ln\frac{\nu_0\,t}{\varepsilon}$$ — Barrier needed to retain a bit for a time $t$ with flip probability $\le\varepsilon$ (Arrhenius).
- $$\varepsilon = Q\!\left(\frac{V}{\sigma}\right),\quad \sigma^2 = \frac{k_BT}{C},\quad E_{\text{read}} = \tfrac12 CV^2 = \tfrac{k_BT}{2}\,Q^{-1}(\varepsilon)^2$$ — Readout with a threshold comparator under $kT/C$ noise.

## Summary
- Reset: $W \ge k_BT[H(p) - H(\varepsilon)]$; it depends on the prior and on the accepted error.
- Retention: $E_b \ge k_BT\ln(\nu_0 t/\varepsilon)$; the barrier grows only logarithmically with time.
- Readout: $E \approx k_BT\ln(1/\varepsilon)$; $\varepsilon = 10^{-9}$ needs $\approx 18\,k_BT$.
- The unavoidable cost of reading appears when the result memory is reset.

## Further reading
- [9] C. H. Bennett, Notes on Landauer's principle, reversible computation and Maxwell's demon, 2003.
- [10] D. H. Wolpert, The stochastic thermodynamics of computation, 2019.
- [54] G. Verdon et al., A framework for stochastic differentiable programming (Torx), 2026.
