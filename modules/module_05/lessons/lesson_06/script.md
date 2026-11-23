# Lesson 5.6 — Analog non-idealities

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Quantify how coupling quantization and device mismatch distort the sampled distribution (KL divergence).
- Recognize nonlinearity and shot noise as additional error sources.
- Apply mitigations: calibration, stochastic rounding, conservative quantizers.

## Prerequisites
- Lessons 4.2 and 4.5: Ising model and pbits.
- Lesson 0.3: KL divergence.

## Narrated script

### [00:05.0] Introduction — `manim:S01`

**ES:** En la pizarra, un acoplamiento vale exactamente cero coma tres siete. En un chip analógico, ese número se guarda con pocos bits, cada transistor es un poco distinto de su vecino, los circuitos no son perfectamente lineales y la corriente misma tiene ruido. La pregunta práctica es cuánto deforman estas imperfecciones la distribución que muestreamos, y cómo se corrigen.

**EN:** On the blackboard, a coupling is exactly 0.37. On an analog chip, that number is stored with few bits, each transistor is slightly different from its neighbor, the circuits are not perfectly linear and the current itself is noisy. The practical question is how much these imperfections distort the distribution we sample, and how they are corrected.

### [00:29.1] Quantization — `manim:S02`

**ES:** Tomemos un modelo de Ising de diez espines con acoplamientos aleatorios, que podemos enumerar exactamente. Cuanticemos los acoplamientos a b bits y midamos la divergencia KL entre la distribución verdadera y la cuantizada. Con dos bits, la KL es uno coma ocho: el modelo es otro. Con tres, cero coma dos uno. Con cuatro, cero coma cero siete. Con seis bits baja a dos milésimas, y con ocho es despreciable. Cada bit adicional reduce el error a una fracción.

**EN:** Take a ten-spin Ising model with random couplings, which we can enumerate exactly. Let's quantize the couplings to b bits and measure the KL divergence between the true and the quantized distribution. With two bits, the KL is 1.8: it is a different model. With three, 0.21. With four, 0.07. With six bits it drops to two thousandths, and with eight it is negligible. Each additional bit reduces the error to a fraction.

### [01:00.7] Mismatch — `manim:S03`

**ES:** El desajuste entre dispositivos actúa como un error aleatorio en cada campo. Si cada pbit tiene un desplazamiento gaussiano de su campo con desviación cero coma cero cinco, la KL promedio es de unas ocho milésimas. Con cero coma uno sube a cero coma cero tres, y con cero coma dos, a cero coma uno tres: crece como el cuadrado del desajuste. Por eso cada pbit se calibra individualmente, como vimos en X0.

**EN:** Mismatch between devices acts as a random error in each field. If each pbit has a Gaussian offset in its field with standard deviation 0.05, the average KL is about eight thousandths. With 0.1 it rises to 0.03, and with 0.2, to 0.13: it grows as the square of the mismatch. That is why each pbit is calibrated individually, as we saw in X0.

### [01:28.1] Nonlinearity and shot noise — `manim:S04`

**ES:** Otras dos fuentes de error. La no linealidad: el circuito que suma el campo local no es perfectamente lineal, y la curva de transferencia del pbit no es exactamente una sigmoide; según el pensum, un comparador con ruido de disparo produce una curva tipo probit, cercana pero distinta. Y el ruido de disparo, debido a la naturaleza discreta de la carga, añade fluctuaciones que no son térmicas y que cambian la temperatura efectiva. Todo esto se modela, se mide y se compensa.

**EN:** Two more error sources. Nonlinearity: the circuit that sums the local field is not perfectly linear, and the pbit transfer curve is not exactly a sigmoid; according to the syllabus, a comparator with shot noise produces a probit-like curve, close but different. And shot noise, due to the discrete nature of charge, adds fluctuations that are not thermal and that change the effective temperature. All of this is modeled, measured and compensated.

### [01:59.7] Stochastic rounding — `manim:S05`

**ES:** Una mitigación elegante es el redondeo estocástico. En lugar de redondear un valor al nivel más cercano, se redondea hacia arriba o hacia abajo con probabilidad proporcional a la distancia. Cada redondeo es ruidoso, pero su valor esperado es exacto. Si promediamos varios redondeos independientes, el error medio de los acoplamientos baja de cero coma uno a cero coma cero dos con dieciséis repeticiones, mientras que el redondeo determinista se queda en cero coma cero nueve para siempre.

**EN:** An elegant mitigation is stochastic rounding. Instead of rounding a value to the nearest level, it is rounded up or down with probability proportional to the distance. Each rounding is noisy, but its expected value is exact. If we average several independent roundings, the mean coupling error drops from 0.1 to 0.02 with sixteen repetitions, while deterministic rounding stays at 0.09 forever.

### [02:31.5] Conservative quantizers — `manim:S06`

**ES:** Otra idea es el cuantizador conservador: elegir el rango y la escala de los niveles para que los acoplamientos grandes, que más pesan en la distribución, se representen bien, aunque los pequeños pierdan resolución. Y en la salida, como veremos en la unidad ocho, hacen falta al menos ocho bits para que los gradientes no se degraden. El diseño de un chip termodinámico es, en buena parte, un presupuesto de errores.

**EN:** Another idea is the conservative quantizer: choosing the range and scale of the levels so that the large couplings, which weigh most in the distribution, are represented well, even if the small ones lose resolution. And at the output, as we will see in unit eight, at least eight bits are needed so that gradients do not degrade. Designing a thermodynamic chip is, to a large extent, an error budget.

### [02:57.9] Applications — `slide`

**ES:** En la práctica se elige el número de bits a partir de una KL objetivo, se calibra cada dispositivo, se usa redondeo estocástico para eliminar sesgos y, como veremos en la lección ocho punto siete, se entrena el modelo sabiendo que el hardware es imperfecto.

**EN:** In practice one chooses the number of bits from a target KL, calibrates each device, uses stochastic rounding to remove bias and, as we will see in lesson 8.7, trains the model knowing the hardware is imperfect.

### [03:14.7] Common mistakes — `slide`

**ES:** Errores frecuentes: juzgar la precisión por el error de los acoplamientos en vez de por el error de la distribución. Suponer que los errores se promedian, cuando el sesgo determinista no lo hace. Ignorar el ruido de disparo. Y calibrar una sola vez, cuando la deriva con la temperatura exige recalibrar.

**EN:** Frequent mistakes: judging precision by coupling error instead of distribution error. Assuming errors average out, when deterministic bias does not. Ignoring shot noise. And calibrating only once, when drift with temperature requires recalibration.

### [03:34.2] Summary — `manim:S09`

**ES:** En resumen: la cuantización, el desajuste, la no linealidad y el ruido de disparo deforman la distribución muestreada. La KL cae rápido con los bits y crece como el cuadrado del desajuste. Calibrar, redondear estocásticamente y cuantizar con criterio forman el presupuesto de errores de un chip termodinámico.

**EN:** In summary: quantization, mismatch, nonlinearity and shot noise distort the sampled distribution. The KL falls quickly with bits and grows as the square of the mismatch. Calibrating, rounding stochastically and quantizing wisely make up the error budget of a thermodynamic chip.

### [03:54.8] Self-assessment — `slide`

**ES:** Para practicar: demuestra que el redondeo estocástico no tiene sesgo. Explica por qué la KL crece como el cuadrado del desajuste. Elige el número de bits para una KL objetivo. Y explica cómo el ruido de disparo cambia la temperatura efectiva.

**EN:** To practice: prove that stochastic rounding is unbiased. Explain why the KL grows as the square of the mismatch. Choose the number of bits for a target KL. And explain how shot noise changes the effective temperature.

## Key equations
- $$\mathrm{KL}\big(p_J\,\|\,p_{\hat J}\big)\ \text{vs. bits: } 1.82\ (2),\ 0.21\ (3),\ 0.070\ (4),\ 0.002\ (6)$$ — Distribution error from quantizing couplings (10-spin example, exact enumeration).
- $$q(x) = \lfloor x/\Delta\rfloor\Delta + \Delta\,\mathbb 1\big[u < \{x/\Delta\}\big],\quad \mathbb E[q(x)] = x$$ — Stochastic rounding with step $\Delta$ and $u \sim U(0,1)$: unbiased.
- $$\mathrm{KL} \approx \tfrac{\beta^2}{2}\,\delta h^\top\,\mathrm{Cov}(s)\,\delta h \propto \sigma^2$$ — Small field errors: KL quadratic in the mismatch.

## Summary
- Quantization: KL falls fast with bits (≥ 6 bits for KL < 10⁻² here).
- Mismatch: KL ∝ σ²; per-device calibration.
- Nonlinearity (probit vs sigmoid) and shot noise (effective temperature).
- Stochastic rounding: unbiased; averaging re-roundings shrinks error ∝ 1/√K.

## Further reading
- [31] M. Aifer et al., Error mitigation for thermodynamic computing, 2024.
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, 2026.
- [41] K. Donatella et al., Scalable thermodynamic second-order optimization, 2025.
