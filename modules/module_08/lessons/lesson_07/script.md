# Lesson 8.7 — Hardware-aware training

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Train with the hardware in the loop: noise injection and 4-bit quantization-aware training (straight-through estimator).
- Impose the chip's fixed sparsity from step 0 instead of pruning afterwards.
- Measure the gains honestly: compare against the cost of deploying an unaware model.

## Prerequisites
- Lesson 5.6: analog non-idealities.
- Lesson 5.7: fixed parent graph and sparsity.

## Narrated script

### [00:05.3] Introduction — `manim:S01`

**ES:** Un modelo entrenado en una GPU con precisión completa no sabe nada del chip donde va a correr: pesos de pocos bits, dispositivos ruidosos y una conectividad fija y dispersa. Llevarlo así al hardware tiene un costo. La alternativa es entrenar sabiendo cómo es el hardware. Hoy medimos tres técnicas en un experimento pequeño, y cuánto ayudan de verdad.

**EN:** A model trained on a GPU at full precision knows nothing about the chip it will run on: few-bit weights, noisy devices and fixed, sparse connectivity. Taking it to hardware as is has a cost. The alternative is to train knowing what the hardware is like. Today we measure three techniques in a small experiment, and how much they really help.

### [00:28.7] The experiment — `manim:S02`

**ES:** Usamos un perceptrón con una capa oculta de treinta y dos neuronas para una tarea de clasificación no lineal en diez dimensiones. El hardware simulado tiene pesos de cuatro bits y un error multiplicativo aleatorio en cada dispositivo. En precisión completa, la red acierta el noventa y cinco por ciento. Llevada al hardware sin más, baja al noventa coma cuatro con un diez por ciento de ruido, y al ochenta y ocho con un veinte por ciento.

**EN:** We use a perceptron with a hidden layer of thirty-two neurons for a nonlinear classification task in ten dimensions. The simulated hardware has four-bit weights and a random multiplicative error in each device. At full precision, the network is correct ninety-five percent of the time. Taken to hardware as is, it drops to 90.4 with ten percent noise, and to eighty-eight with twenty percent.

### [00:55.6] Quantization-aware training — `manim:S03`

**ES:** El entrenamiento consciente de cuantización calcula la pérdida con los pesos ya cuantizados a cuatro bits, pero actualiza una copia en coma flotante. El redondeo no tiene derivada útil, así que se usa el estimador directo: en el paso hacia atrás, el redondeo se trata como la identidad. Así, la red aprende pesos que funcionan bien después de redondear.

**EN:** Quantization-aware training computes the loss with the weights already quantized to four bits, but updates a floating-point copy. Rounding has no useful derivative, so the straight-through estimator is used: in the backward pass, rounding is treated as the identity. That way, the network learns weights that work well after rounding.

### [01:18.5] Noise injection — `manim:S04`

**ES:** La inyección de ruido multiplica los pesos por un factor aleatorio en cada paso de entrenamiento, con la misma magnitud que el desajuste del dispositivo. La red aprende soluciones planas, que no dependen de valores exactos. En nuestro experimento, combinando cuantización y ruido, la precisión en el hardware sube del noventa coma cuatro al noventa coma cinco con un diez por ciento de ruido, y del ochenta y ocho al ochenta y nueve con un veinte por ciento. Promediando tres semillas, la mejora es real pero pequeña.

**EN:** Noise injection multiplies the weights by a random factor at every training step, with the same magnitude as the device mismatch. The network learns flat solutions, which do not depend on exact values. In our experiment, combining quantization and noise, the accuracy on hardware rises from 90.4 to 90.5 with ten percent noise, and from eighty-eight to eighty-nine with twenty percent. Averaging three seeds, the improvement is real but small.

### [01:50.2] Fixed sparsity from step 0 — `manim:S05`

**ES:** El chip tiene una conectividad fija y dispersa, como el grafo de grado dieciséis del Z1. En lugar de entrenar una red densa y podarla después, conviene fijar la máscara de conexiones desde el primer paso y entrenar solo los pesos permitidos. Con un veinticinco por ciento de conexiones, la red con máscara fija acierta el noventa y dos coma cinco por ciento, frente al noventa y uno coma nueve de podar una red densa sin reentrenar.

**EN:** The chip has fixed, sparse connectivity, like the degree-sixteen graph of the Z1. Instead of training a dense network and pruning it afterwards, it is better to fix the connection mask from the first step and train only the allowed weights. With twenty-five percent of the connections, the fixed-mask network is correct 92.5 percent of the time, against 91.9 for pruning a dense network without retraining.

### [02:16.9] Reading the result honestly — `manim:S06`

**ES:** ¿Qué aprendemos? En este experimento, el mayor efecto es la pérdida al pasar al hardware, de cinco a siete puntos; el entrenamiento consciente recupera solo una parte. Eso no contradice los resultados publicados con modelos grandes, donde la cuantización de cuatro bits con entrenamiento consciente es estándar, pero recuerda que las ganancias dependen del modelo, de la tarea y del nivel de ruido. Siempre hay que medir contra la línea base ingenua y con varias semillas.

**EN:** What do we learn? In this experiment, the biggest effect is the loss when moving to hardware, five to seven points; aware training recovers only part of it. That does not contradict published results with large models, where four-bit quantization-aware training is standard, but it reminds us that gains depend on the model, the task and the noise level. One must always measure against the naive baseline and with several seeds.

### [02:46.3] Applications — `slide`

**ES:** La receta: modela el chip, entrena con el paso hacia adelante cuantizado y con ruido de dispositivo, fija la máscara de dispersión desde el principio, como en los transformers tipo Z1T de la unidad diez, y reporta la precisión en hardware frente al despliegue ingenuo con varias semillas.

**EN:** The recipe: model the chip, train with a quantized forward pass and with device noise, fix the sparsity mask from the start, as in the Z1T-style transformers of unit ten, and report hardware accuracy against naive deployment with several seeds.

### [03:04.2] Common mistakes — `slide`

**ES:** Errores comunes: evaluar solo en coma flotante. Inyectar un ruido muy distinto del desajuste real. Podar después de entrenar para encajar en el grafo del chip. Y afirmar mejoras con una sola semilla.

**EN:** Common mistakes: evaluating only in floating point. Injecting noise very different from the real mismatch. Pruning after training to fit the chip's graph. And claiming improvements with a single seed.

### [03:17.9] Summary — `manim:S09`

**ES:** En resumen: entrenar sabiendo cómo es el hardware significa cuantizar en el paso hacia adelante, inyectar el ruido del dispositivo y fijar la dispersión desde el principio. En nuestro experimento, el hardware cuesta de cinco a siete puntos y el entrenamiento consciente recupera hasta uno; la máscara fija gana algo frente a podar. Mide siempre contra la línea base y con varias semillas.

**EN:** In summary: training with the hardware in mind means quantizing in the forward pass, injecting the device noise and fixing sparsity from the start. In our experiment, hardware costs five to seven points and aware training recovers up to one; the fixed mask gains a little over pruning. Always measure against the baseline and with several seeds.

### [03:42.4] Self-assessment — `slide`

**ES:** Para practicar: explica el estimador directo. Explica por qué la inyección de ruido favorece soluciones planas. Explica por qué fijar la máscara desde el principio. Y diseña la evaluación de un método consciente del hardware.

**EN:** To practice: explain the straight-through estimator. Explain why noise injection favors flat solutions. Explain why to fix the mask from the start. And design the evaluation of a hardware-aware method.

## Key equations
- $$\hat W = Q_4(W),\qquad \frac{\partial \mathcal L}{\partial W} \approx \frac{\partial \mathcal L}{\partial \hat W}\quad\text{(straight-through estimator)}$$ — 4-bit quantization-aware training.
- $$\tilde W = \hat W \odot (1 + \sigma\,\xi),\quad \xi \sim \mathcal N(0, 1)$$ — Device-level multiplicative noise injection.
- $$W = M \odot W_{\text{free}},\quad M\ \text{fixed at step 0 (chip connectivity)}$$ — Fixed sparsity mask.

## Summary
- Naive deployment: 95.0 % → 90.4 % (σ = 0.1) / 88.0 % (σ = 0.2) with 4-bit weights [S].
- QAT + noise injection: 90.5 % / 89.0 % on hardware (3 seeds): small but real gain.
- Fixed 25 % sparsity from step 0: 92.5 % vs 91.9 % for prune-after [S].
- Always compare to the naive baseline over several seeds.

## Further reading
- B. Jacob et al., Quantization and training of neural networks for efficient integer-arithmetic-only inference, CVPR (2018).
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- [31] M. Aifer et al., Error mitigation for thermodynamic computing, 2024.
