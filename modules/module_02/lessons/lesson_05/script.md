# Lesson 2.5 — The fluctuation–dissipation theorem

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the fluctuation–dissipation theorem: the response to a small perturbation is fixed by equilibrium fluctuations.
- Verify it on the Ornstein–Uhlenbeck process: $\langle x\rangle_F(t) = \beta F\,[C(0) - C(t)]$.
- Recognize its special cases, the Einstein relation and Nyquist noise, and its violation out of equilibrium.

## Prerequisites
- Lessons 2.2–2.4: Langevin, Fokker–Planck, OU.
- Lesson 1.6: Johnson–Nyquist noise.

## Narrated script

### [00:05.5] Introduction — `manim:S01`

**ES:** Hemos visto la misma idea tres veces: el ruido de una resistencia es proporcional a su resistencia; el coeficiente de difusión es proporcional a la movilidad; la fricción y el ruido de Langevin están amarrados por la temperatura. No es casualidad. Todas son casos de un solo principio: el teorema de fluctuación y disipación. Dice que la forma en que un sistema responde cuando lo empujamos está escrita en cómo fluctúa cuando lo dejamos solo.

**EN:** We have seen the same idea three times: a resistor's noise is proportional to its resistance; the diffusion coefficient is proportional to the mobility; Langevin friction and noise are tied together by temperature. It is no coincidence. They are all cases of a single principle: the fluctuation–dissipation theorem. It says that the way a system responds when we push it is written in how it fluctuates when we leave it alone.

### [00:33.7] Intuition — `manim:S02`

**ES:** Imagina un columpio en un parque con mucho viento. Puedes aprender cómo responde de dos maneras. Una: lo empujas suavemente y mides cómo se desplaza y cómo vuelve. Otra: no lo tocas y solo observas cómo se mueve por el viento, cómo se correlaciona su posición ahora con su posición un rato después. El teorema dice que, en equilibrio térmico, ambas mediciones contienen la misma información. La fricción que frena tu empujón es la misma que, con el viento térmico, produce las fluctuaciones.

**EN:** Imagine a swing in a very windy park. You can learn how it responds in two ways. One: push it gently and measure how it moves and how it comes back. Two: don't touch it and just watch how the wind moves it, how its position now correlates with its position a while later. The theorem says that, at thermal equilibrium, both measurements contain the same information. The friction that slows your push is the same one that, with the thermal wind, produces the fluctuations.

### [01:05.7] Statement — `manim:S03`

**ES:** Formalmente: aplicamos una fuerza pequeña F a partir del instante cero y medimos el desplazamiento medio. En el régimen lineal, ese desplazamiento es β F por la diferencia entre la autocorrelación en cero y la autocorrelación en t del sistema sin perturbar: ⟨x⟩_F(t) = β F [C(0) − C(t)]. Equivalentemente, la función de respuesta es menos β por la derivada de la autocorrelación. La respuesta a un empujón es la relajación de una fluctuación espontánea.

**EN:** Formally: we apply a small force F from time zero and measure the mean displacement. In the linear regime, that displacement is β F times the difference between the autocorrelation at zero and the autocorrelation at t of the unperturbed system: ⟨x⟩_F(t) = β F [C(0) − C(t)]. Equivalently, the response function is minus β times the derivative of the autocorrelation. The response to a push is the relaxation of a spontaneous fluctuation.

### [01:38.9] Numerical check — `manim:S04`

**ES:** Comprobémoslo con el proceso de Ornstein y Uhlenbeck. Primero, sin perturbar, medimos la autocorrelación de una trayectoria larga: decae exponencialmente. Después aplicamos una fuerza pequeña a un ensamble de diez mil partículas y medimos el desplazamiento medio. Los puntos de la respuesta caen sobre la curva predicha a partir de las fluctuaciones, dentro del error estadístico. Dos experimentos distintos, una sola ley.

**EN:** Let's check it with the Ornstein–Uhlenbeck process. First, unperturbed, we measure the autocorrelation of a long trajectory: it decays exponentially. Then we apply a small force to an ensemble of ten thousand particles and measure the mean displacement. The response points fall on the curve predicted from the fluctuations, within statistical error. Two different experiments, one law.

### [02:06.7] Special cases — `manim:S05`

**ES:** De este teorema salen, como casos particulares, resultados que ya conocemos. Para una partícula libre, la respuesta es la movilidad y la fluctuación es la difusión: D = μ k_B T, la relación de Einstein. Para un circuito, la respuesta es la impedancia y la fluctuación es el ruido de voltaje: S_V = 4 k_B T R, la fórmula de Nyquist. En el dominio de frecuencias, el espectro de las fluctuaciones es proporcional a la parte disipativa de la respuesta, la parte imaginaria de la susceptibilidad.

**EN:** Results we already know come out of this theorem as special cases. For a free particle, the response is the mobility and the fluctuation is diffusion: D = μ k_B T, the Einstein relation. For a circuit, the response is the impedance and the fluctuation is the voltage noise: S_V = 4 k_B T R, Nyquist's formula. In the frequency domain, the fluctuation spectrum is proportional to the dissipative part of the response, the imaginary part of the susceptibility.

### [02:41.0] Out of equilibrium — `manim:S06`

**ES:** El teorema solo vale en equilibrio. Si el sistema está forzado, como el anillo con corriente de la lección anterior, o si el ruido no es térmico, la relación se rompe. Una forma práctica de medir la violación es definir una temperatura efectiva: el cociente entre fluctuación y respuesta. Si coincide con la temperatura del baño, el sistema está en equilibrio; si no, algo lo está empujando. En un chip termodinámico, esta comparación sirve para diagnosticar ruido no térmico y desajustes.

**EN:** The theorem holds only at equilibrium. If the system is driven, like the ring with a current from the previous lesson, or if the noise is not thermal, the relation breaks. A practical way to measure the violation is to define an effective temperature: the ratio of fluctuation to response. If it matches the bath temperature, the system is at equilibrium; if not, something is driving it. In a thermodynamic chip, this comparison serves to diagnose non-thermal noise and mismatches.

### [03:12.5] Numerical example — `manim:S07`

**ES:** Una pinza óptica atrapa una esfera con rigidez de un micronewton por metro, a trescientos kelvin. Por equipartición, la varianza de la posición es k_B T / κ, unos cuatro por diez a la menos quince metros cuadrados: una fluctuación típica de sesenta y cuatro nanómetros. Sin aplicar ninguna fuerza, ese número ya nos dice la respuesta: una fuerza de un piconewton desplazará la esfera, en promedio, F/κ, un micrómetro. Medir el ruido calibra el instrumento.

**EN:** An optical tweezer traps a sphere with a stiffness of one micronewton per meter, at three hundred kelvin. By equipartition, the position variance is k_B T / κ, about four times ten to the minus fifteen square meters: a typical fluctuation of sixty-four nanometers. Without applying any force, that number already tells us the response: a one-piconewton force will displace the sphere, on average, F/κ, one micrometer. Measuring the noise calibrates the instrument.

### [03:44.1] Applications — `slide`

**ES:** En la práctica, el teorema permite calibrar instrumentos midiendo su ruido, medir temperaturas a partir de fluctuaciones, y diagnosticar hardware: si la temperatura efectiva no coincide con la del baño, hay ruido no térmico o forzamiento. Y en diseño impone un compromiso: más disipación significa más ruido.

**EN:** In practice, the theorem lets us calibrate instruments by measuring their noise, measure temperatures from fluctuations, and diagnose hardware: if the effective temperature does not match the bath's, there is non-thermal noise or driving. And in design it imposes a trade-off: more dissipation means more noise.

### [04:04.6] Connections — `slide`

**ES:** Esta lección une el ruido de Nyquist y la relación de Einstein. En la próxima lección usaremos la autocorrelación para poner barras de error. Y en la unidad tres veremos relaciones de fluctuación que valen incluso lejos del equilibrio.

**EN:** This lesson ties together Nyquist noise and the Einstein relation. In the next lesson we will use the autocorrelation to put error bars. And in unit three we will see fluctuation relations that hold even far from equilibrium.

### [04:19.4] Common mistakes — `slide`

**ES:** Errores frecuentes: usar el teorema con fuerzas grandes o fuera del equilibrio. Confundir la función de respuesta con la respuesta a un escalón. Olvidar el factor beta. Y usar la versión clásica a frecuencias cuánticas.

**EN:** Frequent mistakes: using the theorem with large forces or out of equilibrium. Confusing the response function with the step response. Forgetting the factor beta. And using the classical version at quantum frequencies.

### [04:34.3] Summary — `manim:S11`

**ES:** En resumen: en equilibrio, la respuesta lineal a un empujón está determinada por las fluctuaciones espontáneas: ⟨x⟩_F(t) = β F [C(0) − C(t)]. Einstein y Nyquist son casos particulares. Fuera del equilibrio, el teorema falla, y esa falla es una herramienta de diagnóstico.

**EN:** In summary: at equilibrium, the linear response to a push is determined by the spontaneous fluctuations: ⟨x⟩_F(t) = β F [C(0) − C(t)]. Einstein and Nyquist are special cases. Out of equilibrium, the theorem fails, and that failure is a diagnostic tool.

### [04:54.5] Self-assessment — `slide`

**ES:** Para practicar: calcula la autocorrelación y la respuesta de un OU concreto. Deriva la relación de Einstein. Calcula la rigidez de una trampa a partir del ruido. Y explica qué indica una temperatura efectiva más alta que la del baño.

**EN:** To practice: compute the autocorrelation and the response of a concrete OU. Derive the Einstein relation. Compute a trap's stiffness from its noise. And explain what an effective temperature above the bath's indicates.

## Key equations
- $$\langle x\rangle_F(t) = \beta F\,[C(0) - C(t)],\quad \chi(t) = -\beta\,\dot C(t)\ (t > 0)$$ — Classical fluctuation–dissipation theorem (linear response).
- $$S_x(\omega) = \frac{2k_BT}{\omega}\,\mathrm{Im}\,\chi(\omega)$$ — Spectral form: fluctuation ∝ dissipative part of the response.
- $$D = \mu k_BT,\qquad S_V = 4k_BTR$$ — Special cases: Einstein and Nyquist.

## Summary
- Linear response = relaxation of equilibrium fluctuations.
- OU: $\langle x\rangle_F = \beta F[C(0)-C(t)] = \frac{F}{\kappa}(1-e^{-t/\tau})$.
- Einstein and Nyquist are special cases.
- Out of equilibrium it fails: effective temperature as a diagnostic.

## Further reading
- [2] Peliti and Pigolotti, Stochastic Thermodynamics (linear response).
- [11] U. Seifert, Stochastic thermodynamics, fluctuation theorems and molecular machines, 2012.
- [1] Gardiner, Handbook of Stochastic Methods.
