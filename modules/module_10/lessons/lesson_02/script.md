# Lesson 10.2 — Attention-free and linear attention

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the Attention Free Transformer (AFT) and its simple and convolutional variants.
- Show that causal AFT-simple has a recurrent form with constant state instead of a KV cache.
- Explain why local, elementwise mixing (AFT-conv, gated convolutions) maps to fixed-connectivity hardware.

## Prerequisites
- Lesson 10.1: attention, KV cache, decode.

## Narrated script

### [00:05.2] Introduction — `manim:S01`

**ES:** La atención compara cada token con todos los anteriores: un costo que crece con el cuadrado del contexto y una caché que crece sin parar. Para un hardware con conectividad fija y dispersa, eso es un problema. Hoy vemos alternativas que mezclan información entre posiciones sin productos de consultas por claves: el transformer libre de atención, sus variantes locales y la atención convolucional con compuertas.

**EN:** Attention compares each token with all previous ones: a cost that grows with the square of the context and a cache that keeps growing. For hardware with fixed, sparse connectivity, that is a problem. Today we see alternatives that mix information across positions without query-key products: the attention-free transformer, its local variants and gated convolutional attention.

### [00:30.7] AFT — `manim:S02`

**ES:** El transformer libre de atención, AFT, propuesto por Zhai y colaboradores en dos mil veintiuno, calcula la salida de cada posición como una compuerta sigmoide de la consulta por un promedio ponderado de los valores. Los pesos son exponenciales de las claves más un sesgo de posición aprendido. Todo es elemento a elemento en la dimensión del modelo: no hay producto escalar entre consulta y clave.

**EN:** The attention-free transformer, AFT, proposed by Zhai and colleagues in twenty twenty-one, computes each position's output as a sigmoid gate of the query times a weighted average of the values. The weights are exponentials of the keys plus a learned position bias. Everything is elementwise in the model dimension: there is no dot product between query and key.

### [00:55.8] AFT-simple: no KV cache — `manim:S03`

**ES:** Sin sesgos de posición, la variante AFT-simple causal tiene una forma recurrente: basta acumular dos sumas, la de las exponenciales de las claves y la de esas exponenciales por los valores. Cada nuevo token actualiza las sumas y lee la salida. Verificamos con sesenta y cuatro posiciones que la forma paralela y la recurrente coinciden exactamente. El estado es de solo dos vectores, en lugar de una caché que crece con el contexto.

**EN:** Without position biases, the causal AFT-simple variant has a recurrent form: it suffices to accumulate two sums, that of the exponentials of the keys and that of those exponentials times the values. Each new token updates the sums and reads the output. We verify with sixty-four positions that the parallel and recurrent forms coincide exactly. The state is just two vectors, instead of a cache that grows with the context.

### [01:24.1] Cost — `manim:S04`

**ES:** En costo, la diferencia es grande. Para un contexto de cuatro mil noventa y seis tokens y dimensión cuatro mil noventa y seis, las puntuaciones de atención de una capa cuestan unas doscientas setenta y cinco mil millones de operaciones, y AFT-simple unas cien millones. Es una mezcla lineal en el contexto. El precio es expresividad, porque AFT-simple no puede enfocar una posición concreta como lo hace la atención.

**EN:** In cost, the difference is large. For a context of four thousand ninety-six tokens and dimension four thousand ninety-six, the attention scores of a layer cost about two hundred seventy-five billion operations, and AFT-simple about one hundred million. It is a mixing that is linear in the context. The price is expressivity, because AFT-simple cannot focus on a specific position the way attention can.

### [01:51.5] Local mixing — `manim:S05`

**ES:** AFT-conv recupera algo de expresividad con sesgos de posición locales, aprendidos dentro de una ventana, como una convolución. La atención convolucional con compuertas sigue la misma idea: mezcla cada posición con sus vecinas mediante un filtro aprendido y la modula con una compuerta multiplicativa. Las conexiones son locales y fijas, justo lo que un grafo de grado fijo puede implementar.

**EN:** AFT-conv recovers some expressivity with local position biases, learned within a window, like a convolution. Gated convolutional attention follows the same idea: it mixes each position with its neighbors through a learned filter and modulates it with a multiplicative gate. The connections are local and fixed, exactly what a fixed-degree graph can implement.

### [02:17.0] Why this matters for TSUs — `manim:S06`

**ES:** Para hardware termodinámico, estas variantes tienen tres virtudes: no necesitan productos densos entre consultas y claves, usan operaciones elemento a elemento como exponenciales y sigmoides, cercanas a la respuesta de un pbit, y su conectividad es local y fija. Por eso aparecen en los diseños de modelos de lenguaje para chips probabilísticos, como los transformers dispersos de las próximas lecciones.

**EN:** For thermodynamic hardware, these variants have three virtues: they do not need dense query-key products, they use elementwise operations such as exponentials and sigmoids, close to a pbit's response, and their connectivity is local and fixed. That is why they appear in language-model designs for probabilistic chips, like the sparse transformers of the next lessons.

### [02:42.5] Applications — `slide`

**ES:** Estos modelos sirven para contextos largos y generación en flujo con estado constante, y forman la familia de mezcladores eficientes junto a la atención lineal y los modelos de espacio de estados. En el laboratorio veintiocho entrenarás un modelo AFT-conv pequeño.

**EN:** These models serve long contexts and streaming generation with constant state, and belong to the family of efficient mixers together with linear attention and state-space models. In lab twenty-eight you will train a small AFT-conv model.

### [02:59.3] Common mistakes — `slide`

**ES:** Errores comunes: suponer que AFT completo es lineal, cuando sus sesgos completos cuestan cuadrático. Olvidar la estabilidad numérica de las exponenciales. Esperar la capacidad de recuperación de la atención con mezcla solo local. Y comparar calidad con distinto número de parámetros.

**EN:** Common mistakes: assuming full AFT is linear, when its full biases cost quadratic. Forgetting the numerical stability of the exponentials. Expecting attention's recall capacity from purely local mixing. And comparing quality with different parameter counts.

### [03:18.3] Summary — `manim:S09`

**ES:** En resumen, AFT reemplaza la atención por un promedio ponderado con pesos exponenciales y una compuerta, todo elemento a elemento. Su versión causal simple es recurrente, con estado constante y sin caché. Las variantes locales recuperan expresividad con conectividad fija, lo que las hace naturales para hardware termodinámico.

**EN:** In summary: AFT replaces attention with a weighted average with exponential weights and a gate, all elementwise. Its simple causal version is recurrent, with constant state and no cache. Local variants recover expressivity with fixed connectivity, which makes them natural for thermodynamic hardware.

### [03:40.8] Self-assessment — `slide`

**ES:** Para practicar: escribe la salida de AFT. Deduce su forma recurrente. Compara el tamaño del estado de decode con la atención. Y di qué puede hacer la atención que AFT-simple no.

**EN:** To practice: write the AFT output. Derive its recurrent form. Compare the decode state size with attention. And say what attention can do that AFT-simple cannot.

## Key equations
- $$Y_t = \sigma(Q_t)\odot\frac{\sum_{t'} \exp(K_{t'} + w_{t,t'})\odot V_{t'}}{\sum_{t'}\exp(K_{t'} + w_{t,t'})}$$ — Attention Free Transformer (Zhai et al. 2021).
- $$n_t = n_{t-1} + e^{K_t}\odot V_t,\quad d_t = d_{t-1} + e^{K_t},\quad Y_t = \sigma(Q_t)\odot n_t/d_t$$ — Causal AFT-simple as a recurrence: constant state.
- $$4T^2d \approx 2.7\times10^{11}\ \text{vs}\ \sim 6Td \approx 10^{8}\ \text{FLOPs}\ (T = d = 4096)$$ — Attention scores vs AFT-simple mixing per layer.

## Summary
- AFT: sigmoid gate × exp(K)-weighted average of V; elementwise, no QKᵀ.
- Causal AFT-simple = recurrence; parallel and recurrent forms agree exactly [S].
- No KV cache: state of 2 vectors; linear in context.
- AFT-conv / gated convolutions: local fixed connectivity → TSU-friendly.

## Further reading
- S. Zhai et al., An attention free transformer, arXiv:2105.14103 (2021).
- A. Katharopoulos et al., Transformers are RNNs: fast autoregressive transformers with linear attention, ICML (2020).
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
