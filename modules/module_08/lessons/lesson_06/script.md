# Lesson 8.6 — Nonlinear Langevin computers as classifiers

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Build a thermodynamic neuron from a quartic potential and understand its finite-time activation function.
- Train a network of such neurons for a fixed readout time, out of equilibrium.
- Read the evidence: cosine fitting, MNIST at about 93 %, noise robustness, and what remains unproven.

## Prerequisites
- Lesson 2.6: overdamped Langevin dynamics.
- Lesson 4.7: neural networks and energy-based models.

## Narrated script

### [00:06.6] Introduction — `manim:S01`

**ES:** Hasta ahora, el hardware termodinámico calculaba en el equilibrio: muestrear una distribución de Boltzmann o resolver un sistema lineal. Pero equilibrar puede ser lento, y no todo problema se escribe como una distribución de Boltzmann. Whitelam y Casert propusieron otra cosa: un computador de Langevin no lineal que se entrena para dar la respuesta correcta en un instante fijo, aunque no haya llegado al equilibrio.

**EN:** Until now, thermodynamic hardware computed at equilibrium: sampling a Boltzmann distribution or solving a linear system. But equilibrating can be slow, and not every problem can be written as a Boltzmann distribution. Whitelam and Casert proposed something else: a nonlinear Langevin computer trained to give the right answer at a fixed instant, even if it has not reached equilibrium.

### [00:32.3] The thermodynamic neuron — `manim:S02`

**ES:** La neurona es una sola variable que fluctúa en contacto con un baño térmico, confinada por el potencial U(x, I) = J₂x² + J₃x³ + J₄x⁴ − I x, donde I es la entrada. Con solo el término cuadrático, la respuesta media es lineal: en equilibrio vale I/2. El término cuártico la vuelve no lineal: la salida se satura, como una tangente hiperbólica, cerca de más o menos uno. Las neuronas se acoplan por términos bilineales, y forman capas.

**EN:** The neuron is a single variable fluctuating in contact with a heat bath, confined by the potential U(x, I) = J₂x² + J₃x³ + J₄x⁴ − I x, where I is the input. With only the quadratic term, the mean response is linear: at equilibrium it is I/2. The quartic term makes it nonlinear: the output saturates, like a hyperbolic tangent, near plus or minus one. Neurons are coupled by bilinear terms, and form layers.

### [01:07.3] Activation needs time — `manim:S03`

**ES:** La no linealidad no es instantánea. Simulamos la neurona cuártica con β = 10 partiendo de cero. En un tiempo de cero coma uno, la respuesta media aún es casi lineal: cero coma uno ocho para una entrada de dos y cero coma cinco tres para seis. En un tiempo de uno ya se satura: cero coma cinco siete y cero coma noventa y nueve, casi los valores de equilibrio. La única exigencia sobre el tiempo de lectura es que sea suficiente para que la activación sea no lineal.

**EN:** The nonlinearity is not instantaneous. We simulate the quartic neuron with β = 10 starting from zero. At time 0.1, the mean response is still almost linear: 0.18 for an input of two and 0.53 for six. At time one it already saturates: 0.57 and 0.99, almost the equilibrium values. The only requirement on the readout time is that it be long enough for the activation to be nonlinear.

### [01:38.6] Training for a readout time — `manim:S04`

**ES:** El entrenamiento fija un tiempo de observación, t_f = 1 en unidades del tiempo de relajación, y ajusta acoplamientos y sesgos para que la salida en ese instante, promediada sobre trayectorias reiniciadas, minimice la pérdida. Los autores usan un algoritmo genético. El resultado es un computador programado para expresar la función objetivo en el tiempo de lectura, no en el equilibrio: en el ejemplo de ajustar un coseno, la salida en equilibrio es muy distinta del objetivo. Opera lejos del equilibrio.

**EN:** Training fixes an observation time, t_f = 1 in units of the relaxation time, and adjusts couplings and biases so that the output at that instant, averaged over reset trajectories, minimizes the loss. The authors use a genetic algorithm. The result is a computer programmed to express the target function at the readout time, not at equilibrium: in the cosine-fitting example, the equilibrium output is very different from the target. It operates far from equilibrium.

### [02:11.8] Evidence — `manim:S05`

**ES:** ¿Qué se logró? Una red de solo neuronas cuadráticas no aprende el coseno; con el término cuártico sí. En MNIST, una red de tres capas de treinta y dos neuronas clasifica con cerca de un noventa y tres por ciento de acierto, no el estado del arte, pero mejor que un clasificador lineal, y con unas veinte muestras por entrada ya se alcanza esa precisión. Entrenada con una escala de energía diez veces la térmica, funciona casi igual con ruido diez veces mayor.

**EN:** What was achieved? A network of only quadratic neurons does not learn the cosine; with the quartic term it does. On MNIST, a three-layer network of thirty-two neurons classifies with about ninety-three percent accuracy, not state of the art, but better than a linear classifier, and about twenty samples per input already reach that accuracy. Trained with an energy scale ten times the thermal one, it works almost as well with noise ten times larger.

### [02:41.4] Efficiency and open questions — `manim:S06`

**ES:** Con un tiempo de relajación de un microsegundo, como en los dispositivos de circuitos, una clasificación tomaría del orden de microsegundos, impulsada por las fluctuaciones térmicas. Pero hay que ser honestos: todo es simulación, entrenar fue mucho más caro que entrenar una red convencional, y el artículo no reporta mediciones de energía. La eficiencia de los protocolos de inferencia, cuánta energía cuesta cargar la entrada y leer la salida, es una pregunta abierta que estudiaremos en el proyecto siete.

**EN:** With a relaxation time of one microsecond, as in circuit devices, a classification would take on the order of microseconds, driven by thermal fluctuations. But we must be honest: everything is simulation, training was much more expensive than training a conventional network, and the paper reports no energy measurements. The efficiency of inference protocols, how much energy it costs to load the input and read the output, is an open question we will study in project seven.

### [03:12.1] Applications — `slide`

**ES:** Estas ideas abren el camino a redes neuronales físicas con circuitos RLC, uniones de Josephson u osciladores mecánicos, donde el tiempo de lectura es un parámetro de diseño y el ruido un recurso. En el proyecto siete entrenarás un computador de este tipo.

**EN:** These ideas open the way to physical neural networks with RLC circuits, Josephson junctions or mechanical oscillators, where the readout time is a design parameter and noise a resource. In project seven you will train a computer of this kind.

### [03:29.7] Common mistakes — `slide`

**ES:** Errores comunes: suponer que el dispositivo entrenado calcula en el equilibrio. Leer la salida antes de que la activación sea no lineal. Citar una eficiencia energética que no se midió. E ignorar el costo del entrenamiento.

**EN:** Common mistakes: assuming the trained device computes at equilibrium. Reading the output before the activation is nonlinear. Quoting an energy efficiency that was not measured. And ignoring the cost of training.

### [03:44.4] Summary — `manim:S09`

**ES:** En resumen: una neurona termodinámica con potencial cuártico tiene una activación no lineal que aparece con el tiempo. Una red de ellas, entrenada para un tiempo de lectura fijo, clasifica MNIST con cerca de un noventa y tres por ciento operando fuera del equilibrio, y tolera ruido. Faltan hardware, mediciones de energía y métodos de entrenamiento más baratos.

**EN:** In summary: a thermodynamic neuron with a quartic potential has a nonlinear activation that appears over time. A network of them, trained for a fixed readout time, classifies MNIST at about ninety-three percent operating out of equilibrium, and tolerates noise. Hardware, energy measurements and cheaper training methods are still missing.

### [04:08.5] Self-assessment — `slide`

**ES:** Para practicar: calcula la media de equilibrio de la neurona cuadrática. Explica por qué el término cuártico satura la respuesta. Di qué optimiza el entrenamiento para un tiempo de lectura. Y nombra dos piezas que faltan para afirmar eficiencia.

**EN:** To practice: compute the equilibrium mean of the quadratic neuron. Explain why the quartic term saturates the response. Say what training for a readout time optimizes. And name two missing pieces before claiming efficiency.

## Key equations
- $$U(x, I) = J_2x^2 + J_3x^3 + J_4x^4 - Ix,\qquad \dot x = -\mu\,\partial_x V + \sqrt{2\mu k_BT}\,\eta(t)$$ — Thermodynamic neuron and overdamped dynamics (Whitelam & Casert).
- $$J = (1, 0, 0):\ \langle x\rangle_{\text{eq}} = I/2;\qquad J = (1, 0, 1):\ \langle x(t_f)\rangle \text{ saturates near } \pm1$$ — Linear vs nonlinear activation.
- $$\min_\theta\ \mathcal L\big(\langle y(t_f)\rangle_\theta,\ y^\ast\big),\quad t_f = 1/\mu$$ — Training for a fixed readout time (reset sampling).

## Summary
- Quartic neuron: nonlinear, saturating activation; quadratic neuron: linear.
- Nonlinearity needs time: ⟨x⟩ at I = 6 is 0.53 (t = 0.1) vs 0.99 (t = 1) [S].
- Train for readout time t_f: computes out of equilibrium; MNIST ≈ 93 % (simulated).
- Robust to 10× noise; no hardware or energy measurements yet.

## Further reading
- S. Whitelam and C. Casert, Nonlinear thermodynamic computing out of equilibrium, arXiv:2412.17183 (2024).
- S. Whitelam, The thermodynamic freedom of a thermodynamic computer, arXiv:2608.27938 (2026).
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
