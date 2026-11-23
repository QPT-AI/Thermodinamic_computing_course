# Lesson 3.3 — Fluctuation theorems: Crooks and Jarzynski

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the Jarzynski equality $\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$ and the Crooks theorem.
- Estimate free-energy differences from work measured in fast processes.
- Understand estimator bias and why Bennett's method (BAR) is more efficient.

## Prerequisites
- Lessons 3.1–3.2: trajectory work and fluctuation theorems.
- Lesson 1.1: $W \ge \Delta F$.

## Narrated script

### [00:06.2] Introduction — `manim:S01`

**ES:** Durante un siglo, para medir una diferencia de energía libre había que hacer un proceso infinitamente lento, porque solo entonces el trabajo es igual a ΔF. En 1997 Christopher Jarzynski mostró algo sorprendente: se puede obtener ΔF exactamente a partir de procesos rápidos, irreversibles, si promediamos la exponencial del trabajo. Dos años después, Gavin Crooks dio la relación detallada entre el proceso directo y el inverso.

**EN:** For a century, measuring a free-energy difference required an infinitely slow process, because only then is the work equal to ΔF. In 1997 Christopher Jarzynski showed something surprising: ΔF can be obtained exactly from fast, irreversible processes, if we average the exponential of the work. Two years later, Gavin Crooks gave the detailed relation between the forward and reverse processes.

### [00:36.1] Intuition — `manim:S02`

**ES:** Endurecemos una trampa armónica: la rigidez pasa de uno a cuatro en medio segundo. Como la trampa más rígida confina más a la partícula, la energía libre sube ½ ln 4, unos cero coma sesenta y nueve k_B T. Pero el proceso es rápido: el trabajo medio es mayor, uno coma cero ocho. Algunas trayectorias, sin embargo, gastan menos que ΔF. La igualdad de Jarzynski pondera esas trayectorias raras exactamente lo necesario para recuperar el valor verdadero.

**EN:** We stiffen a harmonic trap: the stiffness goes from one to four in half a second. Since the stiffer trap confines the particle more, the free energy rises by ½ ln 4, about 0.69 k_B T. But the process is fast: the mean work is larger, 1.08. Some trajectories, however, spend less than ΔF. The Jarzynski equality weights those rare trajectories exactly enough to recover the true value.

### [01:08.5] Jarzynski equality — `manim:S03`

**ES:** La igualdad dice: ⟨e^(−βW)⟩ = e^(−βΔF). El promedio es sobre trayectorias que empiezan en equilibrio con el parámetro inicial; el estado final no necesita estar en equilibrio. Es una consecuencia del teorema de fluctuación integral de la lección anterior. Con la desigualdad de Jensen recupera la segunda ley, ⟨W⟩ ≥ ΔF. Y con nuestra simulación de cien mil trayectorias, el estimador de Jarzynski da cero coma seis nueve tres, frente al valor exacto cero coma seis nueve tres.

**EN:** The equality says: ⟨e^(−βW)⟩ = e^(−βΔF). The average is over trajectories that start at equilibrium with the initial parameter; the final state need not be at equilibrium. It is a consequence of the integral fluctuation theorem from the previous lesson. With Jensen's inequality it recovers the second law, ⟨W⟩ ≥ ΔF. And with our simulation of a hundred thousand trajectories, the Jarzynski estimator gives 0.693, versus the exact value 0.693.

### [01:45.1] Crooks theorem — `manim:S04`

**ES:** Crooks compara el proceso directo con el inverso: ablandar la trampa de cuatro a uno. La distribución del trabajo directo, dividida por la del trabajo inverso cambiado de signo, es e^(β(W − ΔF)). Consecuencia visible: los dos histogramas se cruzan exactamente en W = ΔF. Además, la energía libre queda encerrada entre los trabajos medios: entre menos el trabajo medio inverso, cero coma cuarenta y nueve, y el trabajo medio directo, uno coma cero ocho.

**EN:** Crooks compares the forward process with the reverse: softening the trap from four to one. The forward work distribution, divided by the reverse work distribution with flipped sign, is e^(β(W − ΔF)). Visible consequence: the two histograms cross exactly at W = ΔF. Moreover, the free energy is bracketed by the mean works: between minus the mean reverse work, 0.49, and the mean forward work, 1.08.

### [02:18.0] Estimator bias — `manim:S05`

**ES:** Hay una trampa práctica. El promedio exponencial está dominado por trayectorias raras con trabajo bajo. Con pocas trayectorias, es probable no haber visto ninguna, y el estimador sobreestima ΔF. Con cinco trayectorias, el estimador promedia cero coma setenta y tres; con veinte, cero coma setenta; con mil, cero coma seis nueve tres. El sesgo y la varianza caen al aumentar el número de muestras. El estimador de Bennett, que usa a la vez trayectorias directas e inversas, es el de mínima varianza y necesita muchas menos.

**EN:** There is a practical catch. The exponential average is dominated by rare trajectories with low work. With few trajectories, you probably have not seen any, and the estimator overestimates ΔF. With five trajectories, the estimator averages 0.73; with twenty, 0.70; with a thousand, 0.693. Bias and variance fall as the number of samples grows. Bennett's estimator, which uses forward and reverse trajectories together, has minimum variance and needs far fewer.

### [02:51.8] Numerical example — `manim:S06`

**ES:** Resumamos los números del ejemplo. Energía libre exacta: un medio del logaritmo de cuatro, cero coma seis nueve tres. Trabajo medio directo: uno coma cero ocho, es decir, cero coma tres nueve de trabajo disipado. Menos el trabajo medio inverso: cero coma cuarenta y nueve. La segunda ley se cumple en ambos sentidos, y Jarzynski acierta con tres cifras usando cien mil trayectorias.

**EN:** Let's summarize the numbers of the example. Exact free energy: one half of the log of four, 0.693. Mean forward work: 1.08, that is, 0.39 of dissipated work. Minus the mean reverse work: 0.49. The second law holds in both directions, and Jarzynski gets three digits right using a hundred thousand trajectories.

### [03:18.0] Applications — `slide`

**ES:** Jarzynski y Crooks se usan en biofísica para medir energías libres de plegamiento estirando moléculas rápidamente. En este curso los usaremos para calcular el logaritmo del determinante de una matriz a partir del trabajo entre dos potenciales cuadráticos, en el laboratorio cuatro y en la unidad seis.

**EN:** Jarzynski and Crooks are used in biophysics to measure folding free energies by pulling molecules quickly. In this course we will use them to compute the log-determinant of a matrix from the work between two quadratic potentials, in lab four and in unit six.

### [03:37.1] Common mistakes — `slide`

**ES:** Errores comunes: no empezar en equilibrio. Usar pocas trayectorias en procesos muy disipativos. Confundir el promedio de la exponencial con la exponencial del promedio. Y creer que Jarzynski contradice la segunda ley.

**EN:** Common mistakes: not starting at equilibrium. Using few trajectories in highly dissipative processes. Confusing the average of the exponential with the exponential of the average. And believing Jarzynski contradicts the second law.

### [03:51.6] Summary — `manim:S09`

**ES:** En resumen: Jarzynski da la energía libre exacta a partir de procesos rápidos, ⟨e^(−βW)⟩ = e^(−βΔF). Crooks relaciona los trabajos directo e inverso, cuyas distribuciones se cruzan en ΔF. En la práctica, el estimador tiene un sesgo que decrece con el número de trayectorias, y Bennett lo reduce.

**EN:** In summary: Jarzynski gives the exact free energy from fast processes, ⟨e^(−βW)⟩ = e^(−βΔF). Crooks relates the forward and reverse works, whose distributions cross at ΔF. In practice, the estimator has a bias that decreases with the number of trajectories, and Bennett reduces it.

### [04:16.0] Self-assessment — `slide`

**ES:** Para practicar: calcula la energía libre de endurecer una trampa, demuestra que Crooks implica Jarzynski, aplica la fórmula gaussiana y explica el sesgo del estimador.

**EN:** To practice: compute the free energy of stiffening a trap, prove that Crooks implies Jarzynski, apply the Gaussian formula and explain the estimator's bias.

## Key equations
- $$\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$$ — Jarzynski equality (start at equilibrium).
- $$\frac{P_F(W)}{P_R(-W)} = e^{\beta(W - \Delta F)}$$ — Crooks theorem.
- $$\Delta F = \tfrac{k_BT}{2}\ln\frac{\kappa_f}{\kappa_i}$$ — Free energy of changing the stiffness of a harmonic trap.
- $$-\langle W_R\rangle \le \Delta F \le \langle W_F\rangle$$ — The free energy is bounded by the mean forward and reverse works.

## Summary
- Jarzynski: exact $\Delta F$ from fast processes.
- Crooks: $P_F(W)/P_R(-W) = e^{\beta(W-\Delta F)}$; crossing at $W = \Delta F$.
- The exponential estimator is biased with few samples; BAR is optimal.
- Application: $\ln\det A$ from work (L4, Unit 6).

## Further reading
- [12] C. Jarzynski, Nonequilibrium equality for free energy differences, Phys. Rev. Lett. 78, 2690 (1997).
- [11] U. Seifert, Stochastic thermodynamics..., 2012.
- Video V8: Seifert, BIRS 2020.
