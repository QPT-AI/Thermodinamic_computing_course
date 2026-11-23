# Lesson 10.6 — Tanh-linear units on a degree-16 graph

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the tanh-linear unit and show that a pbit implements it in expectation.
- Map a projection onto a degree-16 graph as 4 inputs × 4 pbits.
- Quantify the trade-off between pbits per input (bias) and fan-in (depth).

## Prerequisites
- Lesson 10.3: pbit mean = tanh.
- Lesson 10.4: fixed degree and depth.
- Lesson 10.5: encoding numbers in pbits.

## Narrated script

### [00:06.4] Introduction — `manim:S01`

**ES:** Ya tenemos las piezas: la tangente que calcula un pbit, las capas dispersas de grado fijo y la codificación de números en grupos de pbits. Hoy las juntamos en la unidad básica de un modelo de lenguaje para un chip de pbits: la unidad tanh-lineal. Y veremos cómo se acomoda en un grafo donde cada pbit tiene exactamente dieciséis vecinos.

**EN:** We already have the pieces: the tangent a pbit computes, sparse fixed-degree layers and the encoding of numbers in groups of pbits. Today we put them together into the basic unit of a language model for a pbit chip: the tanh-linear unit. And we will see how it fits in a graph where each pbit has exactly sixteen neighbors.

### [00:29.0] The tanh-linear unit — `manim:S02`

**ES:** Una unidad tanh-lineal calcula tanh(Σ wⱼ xⱼ + b). Es una neurona clásica con activación tangente. En un pbit, el campo local es la suma ponderada de los estados de los vecinos, y la salida media es exactamente la tangente de ese campo. La unidad tanh-lineal es, por tanto, el pbit visto en promedio.

**EN:** A tanh-linear unit computes tanh(Σ wⱼ xⱼ + b). It is a classical neuron with tangent activation. In a pbit, the local field is the weighted sum of the neighbors' states, and the mean output is exactly the tangent of that field. The tanh-linear unit is therefore the pbit seen on average.

### [00:53.0] 4 inputs × 4 pbits — `manim:S03`

**ES:** Ahora el grafo. Cada pbit tiene dieciséis vecinos. Si cada entrada se codifica con un grupo de cuatro pbits, una unidad puede leer cuatro entradas: cuatro por cuatro, dieciséis conexiones. Los cuatro pbits de una entrada comparten el mismo peso, así que su suma actúa como un entero probabilístico de cinco niveles.

**EN:** Now the graph. Each pbit has sixteen neighbors. If each input is encoded with a group of four pbits, a unit can read four inputs: four times four, sixteen connections. The four pbits of an input share the same weight, so their sum acts as a five-level probabilistic integer.

### [01:13.7] The noise bias — `manim:S04`

**ES:** Hay una sutileza. La salida media es la media de la tangente del campo ruidoso, no la tangente del campo medio. Como la tangente es curva, el ruido de las entradas produce un sesgo. Lo medimos con cuatro mil unidades al azar: con un pbit por entrada, el sesgo cuadrático medio es cero coma uno nueve siete; con cuatro, cero coma cero ocho cinco; con dieciséis, cero coma cero tres seis.

**EN:** There is a subtlety. The mean output is the mean of the tangent of the noisy field, not the tangent of the mean field. Since the tangent is curved, the noise of the inputs produces a bias. We measure it with four thousand random units: with one pbit per input, the root-mean-square bias is 0.197; with four, 0.085; with sixteen, 0.036.

### [01:40.4] Bias versus depth — `manim:S05`

**ES:** Con grado fijo de dieciséis, más pbits por entrada significa menos entradas por unidad. Menos entradas obliga a más capas para mezclar toda la información: para una dimensión de mil veinticuatro, con abanico de dieciséis bastan dos capas y media; con abanico cuatro, cinco capas. Cuatro por cuatro es un compromiso: sesgo moderado, profundidad razonable. Además, el entrenamiento con ruido absorbe buena parte del sesgo.

**EN:** With a fixed degree of sixteen, more pbits per input means fewer inputs per unit. Fewer inputs forces more layers to mix all the information: for a dimension of one thousand twenty-four, with fan-in sixteen two and a half layers suffice; with fan-in four, five layers. Four by four is a compromise: moderate bias, reasonable depth. Moreover, training with noise absorbs much of the bias.

### [02:08.9] Embedding projections — `manim:S06`

**ES:** Así entran los tokens al chip. El vector de embedding de cada token, calculado de forma digital, se escribe como sesgos sobre grupos de cuatro pbits. A partir de ahí, capas tanh-lineales de abanico cuatro proyectan y mezclan la información dentro del grafo. La salida se lee promediando muestras, como en la lección anterior, y vuelve a lo digital para la cabeza de vocabulario.

**EN:** This is how tokens enter the chip. Each token's embedding vector, computed digitally, is written as biases on groups of four pbits. From there, tanh-linear layers with fan-in four project and mix the information inside the graph. The output is read by averaging samples, as in the previous lesson, and returns to digital for the vocabulary head.

### [02:32.3] Applications — `slide`

**ES:** En la práctica: usa tangente en el MLP y DyT como normalización, enmascara las proyecciones a abanico cuatro con grupos de cuatro pbits, y entrena con pasadas muestreadas. En el laboratorio veintinueve convertirás un modelo pequeño y medirás el precio.

**EN:** In practice: use tangent in the MLP and DyT as normalization, mask the projections to fan-in four with groups of four pbits, and train with sampled passes. In lab twenty-nine you will convert a small model and measure the price.

### [02:50.3] Common mistakes — `slide`

**ES:** Errores comunes: suponer que la media de la tangente es la tangente de la media. Gastar las dieciséis conexiones en entradas de un solo pbit. Olvidar que un abanico pequeño cuesta profundidad. Y entrenar de forma determinista para desplegar de forma estocástica.

**EN:** Common mistakes: assuming the mean of the tangent is the tangent of the mean. Spending the sixteen connections on single-pbit inputs. Forgetting that a small fan-in costs depth. And training deterministically to deploy stochastically.

### [03:07.9] Summary — `manim:S09`

**ES:** En resumen, la unidad tanh-lineal es el pbit visto en promedio. En un grafo de grado dieciséis, cuatro entradas por cuatro pbits equilibran el sesgo del ruido, que medimos en cero coma cero ocho cinco, y la profundidad necesaria para mezclar. Los embeddings entran como sesgos y la salida se lee promediando.

**EN:** In summary, the tanh-linear unit is the pbit seen on average. In a degree-sixteen graph, four inputs times four pbits balance the noise bias, which we measured at 0.085, and the depth needed to mix. Embeddings enter as biases and the output is read by averaging.

### [03:28.1] Self-assessment — `slide`

**ES:** Para practicar: explica por qué un pbit implementa una unidad tanh-lineal. Cuenta los niveles de la suma de cuatro pbits. Calcula las capas para mezclar una dimensión de cuatro mil noventa y seis. Y explica el origen del sesgo.

**EN:** To practice: explain why a pbit implements a tanh-linear unit. Count the levels of the sum of four pbits. Compute the layers to mix a dimension of four thousand ninety-six. And explain the origin of the bias.

## Key equations
- $$y = \tanh\Big(\sum_j w_j x_j + b\Big) = \mathbb E[m \mid \text{neighbors}]$$ — Tanh-linear unit = pbit in expectation.
- $$16 = 4\ \text{inputs}\times 4\ \text{pbits}$$ — Degree budget of one unit.
- $$\mathbb E[\tanh(u)] \ne \tanh(\mathbb E[u])$$ — Input noise biases the output (Jensen).

## Summary
- Tanh-linear unit = pbit on average.
- Degree 16 = 4 inputs × 4 pbits (5-level inputs).
- Noise bias: 0.197 (1 pbit) → 0.085 (4) → 0.036 (16) [S].
- Trade-off bias vs depth; embeddings enter as biases.

## Further reading
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
- K. Y. Camsari et al., p-bits for probabilistic spin logic, Applied Physics Reviews 6, 011305 (2019).
