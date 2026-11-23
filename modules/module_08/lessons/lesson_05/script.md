# Lesson 8.5 — Thermodynamic K-FAC

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Replace K-FAC's per-layer $n\times n$ inversions with thermodynamic linear solves.
- Compare per-layer complexity: $O(bn^2 + n^3)$ digital vs $O(bn^2 + n^2\kappa^2)$ thermodynamic.
- Understand input and output quantization: conservative quantizers and at least 8 output bits.

## Prerequisites
- Lesson 8.4: K-FAC.
- Lessons 6.1–6.2 and 5.6: thermodynamic solves and analog non-idealities.

## Narrated script

### [00:04.7] Introduction — `manim:S01`

**ES:** El cuello de botella de K-FAC es invertir los factores de cada capa, que cuesta n³ para una capa de n neuronas. En dos mil veinticinco, Donatella y colaboradores propusieron hacer esas inversiones en un computador termodinámico. La idea es la de la unidad seis aplicada a cada capa, con un detalle práctico importante: cuántos bits necesitan la entrada y la salida del dispositivo.

**EN:** K-FAC's bottleneck is inverting each layer's factors, which costs n³ for a layer of n neurons. In twenty twenty-five, Donatella and colleagues proposed doing those inversions on a thermodynamic computer. The idea is that of unit six applied to each layer, with an important practical detail: how many bits the device's input and output need.

### [00:30.0] The algorithm — `manim:S02`

**ES:** La GPU calcula, como siempre, las estadísticas de activaciones y gradientes de cada capa. En lugar de invertir los factores digitalmente, los carga en el dispositivo, que resuelve sistemas A x = b de tamaño n con dinámica de Ornstein-Uhlenbeck. El resultado vuelve a la GPU, que aplica el paso G⁻¹ ∇W A⁻¹. Los promedios móviles de los factores pueden vivir en la GPU o en el propio dispositivo.

**EN:** The GPU computes, as usual, the activation and gradient statistics of each layer. Instead of inverting the factors digitally, it loads them into the device, which solves A x = b systems of size n with Ornstein-Uhlenbeck dynamics. The result returns to the GPU, which applies the step G⁻¹ ∇W A⁻¹. The moving averages of the factors can live on the GPU or on the device itself.

### [00:58.1] Complexity — `manim:S03`

**ES:** Por capa y por iteración, K-FAC digital cuesta O(b n² + n³). La versión termodinámica cuesta O(b n² + n² κ²), donde κ acota el número de condición de los factores, y sin promedios móviles en memoria, solo O(b n) de memoria. La ventaja crece linealmente con el ancho de la red: el término cúbico se vuelve cuadrático. Con las capas de los transformers modernos, de miles de neuronas, eso importa.

**EN:** Per layer and per iteration, digital K-FAC costs O(b n² + n³). The thermodynamic version costs O(b n² + n² κ²), where κ bounds the condition number of the factors, and without moving averages in memory, only O(b n) memory. The advantage grows linearly with the network width: the cubic term becomes quadratic. With the layers of modern transformers, thousands of neurons wide, that matters.

### [01:29.9] Estimated speedups — `manim:S04`

**ES:** ¿Cuánto se gana en la práctica? Los autores midieron qué fracción del tiempo dedica K-FAC a invertir en tareas del banco AlgoPerf: un once por ciento en un transformer de visión sobre ImageNet, y un veintisiete por ciento en una red de grafos sobre moléculas. Si esa parte se vuelve casi gratuita, estiman llegar a la misma métrica de validación cerca de un cincuenta por ciento más rápido en la red de grafos. Ojo: acelerar solo un veintisiete por ciento del tiempo permite, por la ley de Amdahl, ganar a lo sumo un treinta y siete por ciento con el mismo número de pasos, así que esa estimación debe incluir también cambios en los pasos; conviene leer el detalle. Son estimaciones a partir de mediciones digitales y simulaciones: ningún dispositivo físico ejecutó estos experimentos.

**EN:** How much is gained in practice? The authors measured what fraction of time K-FAC spends inverting on AlgoPerf benchmark tasks: eleven percent on a vision transformer on ImageNet, and twenty-seven percent on a graph network on molecules. If that part becomes almost free, they estimate reaching the same validation metric about fifty percent faster on the graph network. Note: speeding up only twenty-seven percent of the time allows, by Amdahl's law, at most a thirty-seven percent gain with the same number of steps, so that estimate must also include changes in the steps; it is worth reading the details. These are estimates from digital measurements and simulations: no physical device ran these experiments.

### [02:17.7] Quantization: input and output — `manim:S05`

**ES:** El dispositivo recibe los factores por convertidores digital analógico y entrega la solución por convertidores analógico digital, con pocos bits. Un cuantizador ingenuo puede romper la positividad de los factores; los autores usan uno conservador, de diagonal dominante, que la preserva. En el entrenamiento de una ResNet encontraron que la cuantización de entrada afecta poco, pero la de salida importa: hacen falta al menos ocho bits de salida, y con ocho bits K-FAC ya compite con Adam en precisión completa.

**EN:** The device receives the factors through digital-to-analog converters and delivers the solution through analog-to-digital converters, with few bits. A naive quantizer can break the positivity of the factors; the authors use a conservative, diagonal-dominant one that preserves it. Training a ResNet, they found that input quantization has little effect, but output quantization matters: at least eight output bits are needed, and with eight bits K-FAC already competes with full-precision Adam.

### [02:50.2] A caution about metrics — `manim:S06`

**ES:** Una advertencia metodológica. En nuestra capa softmax medimos un solo paso: con un cuantizador uniforme ingenuo, la entrada es lo que más daña, con un coseno de cero coma siete a cuatro bits, y la salida apenas cambia la dirección. Es lo contrario de lo que encontraron los autores en entrenamiento completo, con su cuantizador conservador y errores que se acumulan durante miles de pasos. La lección: las métricas de un solo paso no sustituyen a los experimentos de entrenamiento.

**EN:** A methodological warning. In our softmax layer we measured a single step: with a naive uniform quantizer, the input is what hurts most, with a cosine of 0.7 at four bits, and the output barely changes the direction. It is the opposite of what the authors found in full training, with their conservative quantizer and errors that accumulate over thousands of steps. The lesson: single-step metrics are no substitute for training experiments.

### [03:20.5] Applications — `slide`

**ES:** Úsalo en redes anchas, donde la inversión cúbica domina. Antes de prometer aceleraciones, mide qué fracción del tiempo se va en invertir. Y diseña con un cuantizador de entrada conservador y al menos ocho bits de salida. En el laboratorio once barrerás los bits de entrada y salida.

**EN:** Use it in wide networks, where the cubic inversion dominates. Before promising speedups, measure what fraction of time goes into inverting. And design with a conservative input quantizer and at least eight output bits. In lab eleven you will sweep input and output bits.

### [03:39.0] Common mistakes — `slide`

**ES:** Errores comunes: prometer una aceleración total cuando la inversión es solo una fracción del tiempo. Ignorar el factor de condición al cuadrado. Usar cuantizadores ingenuos que rompen la positividad. Y juzgar la precisión necesaria con métricas de un solo paso.

**EN:** Common mistakes: promising a total speedup when inversion is only a fraction of the time. Ignoring the squared condition factor. Using naive quantizers that break positivity. And judging the precision needed with single-step metrics.

### [03:56.0] Summary — `manim:S09`

**ES:** En resumen, K-FAC termodinámico reemplaza las inversiones cúbicas de cada capa por soluciones analógicas de costo n² κ², con una ventaja que crece con el ancho. Las aceleraciones son estimadas, no medidas en hardware. Y la precisión importa: entrada con cuantizador conservador y al menos ocho bits de salida.

**EN:** In summary: thermodynamic K-FAC replaces each layer's cubic inversions with analog solves costing n² κ², with an advantage that grows with width. The speedups are estimated, not measured on hardware. And precision matters: input with a conservative quantizer and at least eight output bits.

### [04:18.1] Self-assessment — `slide`

**ES:** Para practicar: calcula la razón de costos para una capa ancha. Aplica la ley de Amdahl a la fracción de inversión. Explica cómo un cuantizador uniforme rompe la positividad. Y explica por qué los errores de salida pesan más en entrenamiento que en un paso.

**EN:** To practice: compute the cost ratio for a wide layer. Apply Amdahl's law to the inversion fraction. Explain how a uniform quantizer breaks positivity. And explain why output errors weigh more in training than in one step.

## Key equations
- $$\text{K-FAC: } O(bn^2 + n^3)\qquad \text{thermodynamic K-FAC: } O(bn^2 + n^2\kappa^2),\ \text{memory } O(bn)$$ — Per layer, per iteration (Donatella et al. 2025, Table 1).
- $$S_{\max} = \frac{1}{1 - f_{\text{inv}}}:\quad f = 0.11 \Rightarrow 1.12,\quad f = 0.27 \Rightarrow 1.37$$ — Amdahl bound at a fixed number of steps when only the inversion is accelerated.
- $$\text{output ADC} \ge 8\ \text{bits};\quad \text{input: conservative (diagonal-dominant) quantizer}$$ — Precision findings in ResNet training (simulated).

## Summary
- Per-layer inversions moved to the thermodynamic solver: O(bn² + n³) → O(bn² + n²κ²).
- Inversion share 11 % (ViT) and 27 % (GNN); ~50 % faster to target on GNN [P/S].
- Training: ≥ 8 output bits; conservative input quantizer; no hardware run yet.
- Single-step toy shows the opposite sensitivity: metrics must match the task.

## Further reading
- [41] K. Donatella et al., Scalable thermodynamic second-order optimization, arXiv:2502.08603 (2025).
- J. Martens and R. Grosse, Optimizing neural networks with Kronecker-factored approximate curvature, ICML (2015).
- [30] M. Aifer et al., Thermodynamic linear algebra, npj Unconv. Comput. 1, 13 (2024).
