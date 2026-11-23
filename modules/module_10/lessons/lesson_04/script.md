# Lesson 10.4 — Sparse transformers

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe sparse transformer layers where each unit connects to a fixed number $k$ of inputs.
- Compare dense and sparse layers at equal connection budget (iso-FLOP).
- Relate the optimal degree to the fixed-degree graphs of TSUs.

## Prerequisites
- Lesson 10.2: attention-free mixing.
- Lesson 5.7: embedding and chip connectivity.

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** Un chip termodinámico no tiene conexiones de todos con todos: cada pbit habla con un número fijo de vecinos. Si queremos que un modelo de lenguaje viva en el chip, sus capas también deben ser dispersas. La pregunta es cuánto se pierde, y la respuesta sorprende: con el mismo presupuesto de conexiones, una capa dispersa y ancha puede ganarle a una densa y estrecha.

**EN:** A thermodynamic chip does not have all-to-all connections: each pbit talks to a fixed number of neighbors. If we want a language model to live on the chip, its layers must also be sparse. The question is how much is lost, and the answer is surprising: with the same connection budget, a wide sparse layer can beat a narrow dense one.

### [00:28.1] Sparse layers — `manim:S02`

**ES:** En una capa dispersa, cada unidad de salida se conecta solo con k entradas, elegidas por un patrón fijo. Una capa densa de n unidades con d entradas tiene n · d conexiones; la dispersa, n · k. Como cada conexión es una multiplicación y suma, el número de conexiones mide el costo. El patrón puede ser aleatorio, local o estructurado en bloques.

**EN:** In a sparse layer, each output unit connects to only k inputs, chosen by a fixed pattern. A dense layer of n units with d inputs has n · d connections; the sparse one, n · k. Since each connection is a multiply-add, the number of connections measures the cost. The pattern can be random, local or block-structured.

### [00:52.9] Iso-FLOP comparison — `manim:S03`

**ES:** Para comparar con justicia, fijamos el presupuesto: ocho mil ciento noventa y dos conexiones. Con grado sesenta y cuatro, es decir denso, caben ciento veintiocho unidades; con grado dieciséis, quinientas doce; con grado dos, cuatro mil noventa y seis. Entrenamos la lectura de cada red sobre una tarea de regresión con un maestro no lineal y medimos el error en datos nuevos.

**EN:** To compare fairly, we fix the budget: eight thousand one hundred ninety-two connections. With degree sixty-four, that is dense, one hundred twenty-eight units fit; with degree sixteen, five hundred twelve; with degree two, four thousand ninety-six. We train the readout of each network on a regression task with a nonlinear teacher and measure the error on new data.

### [01:17.7] A U-shaped curve — `manim:S04`

**ES:** El resultado tiene forma de U. La red densa tiene un error relativo de cero coma uno uno cinco. Al hacerla más dispersa y más ancha, el error baja hasta cero coma cero ocho tres con grado dieciséis. Con grado más bajo vuelve a subir: con dos entradas por unidad, cero coma uno cero nueve, porque cada unidad ve demasiado poco. Hay un grado óptimo intermedio.

**EN:** The result is U-shaped. The dense network has a relative error of 0.115. Making it sparser and wider, the error drops to 0.083 with degree sixteen. With lower degree it rises again: with two inputs per unit, 0.109, because each unit sees too little. There is an optimal intermediate degree.

### [01:42.7] Connectivity scaling — `manim:S05`

**ES:** La literatura de leyes de escala encuentra un patrón parecido en modelos grandes: a igual cómputo, la dispersión ayuda cuando el entrenamiento es largo, y el grado óptimo depende del tamaño del modelo y de los datos. Para un TSU la restricción va al revés: el grado lo fija el chip, por ejemplo dieciséis, y el diseño consiste en elegir el ancho y el patrón para sacarle el mayor partido.

**EN:** The scaling-law literature finds a similar pattern in large models: at equal compute, sparsity helps when training is long, and the optimal degree depends on model size and data. For a TSU the constraint goes the other way: the degree is fixed by the chip, for example sixteen, and design consists of choosing the width and the pattern to make the most of it.

### [02:06.6] Mixing across the graph — `manim:S06`

**ES:** Con grado fijo, ¿cómo llega la información de un extremo al otro? Apilando capas. Con un patrón local, el campo receptivo crece de forma lineal con la profundidad; con un patrón de mundo pequeño, que mezcla conexiones locales con algunos saltos largos, crece de forma exponencial. Así, unas pocas capas de grado dieciséis bastan para que cada unidad dependa de todas las entradas.

**EN:** With fixed degree, how does information get from one end to the other? By stacking layers. With a local pattern, the receptive field grows linearly with depth; with a small-world pattern, which mixes local connections with a few long jumps, it grows exponentially. So a few layers of degree sixteen suffice for every unit to depend on all inputs.

### [02:31.3] Applications — `slide`

**ES:** En la práctica, elige el grado según el hardware y ajusta el ancho con presupuesto fijo; usa patrones de mundo pequeño; y entrena con máscaras estáticas, sin necesidad de podar. En el laboratorio treinta harás un barrido de grado en un modelo pequeño.

**EN:** In practice, choose the degree from the hardware and tune the width at a fixed budget; use small-world patterns; and train with static masks, with no need to prune. In lab thirty you will do a degree sweep on a small model.

### [02:47.3] Common mistakes — `slide`

**ES:** Errores comunes: comparar redes con distinto presupuesto. Suponer que las matrices dispersas son rápidas en una GPU, cuando a menudo no lo son. Usar patrones puramente locales en redes poco profundas. Y generalizar el grado óptimo de un ejemplo pequeño a modelos grandes.

**EN:** Common mistakes: comparing networks with different budgets. Assuming sparse matrices are fast on a GPU, when they often are not. Using purely local patterns in shallow networks. And generalizing the optimal degree of a small example to large models.

### [03:06.0] Summary — `manim:S09`

**ES:** En resumen, una capa dispersa conecta cada unidad con k entradas, y a igual presupuesto puede ser mejor que una densa. En nuestro ejemplo el error sigue una curva en U con mínimo en grado dieciséis. Con grado fijo, la profundidad y los saltos largos aseguran que la información se mezcle en todo el grafo.

**EN:** In summary, a sparse layer connects each unit to k inputs, and at equal budget it can be better than a dense one. In our example the error follows a U-shaped curve with a minimum at degree sixteen. With fixed degree, depth and long jumps ensure that information mixes across the whole graph.

### [03:25.9] Self-assessment — `slide`

**ES:** Para practicar: calcula el ancho con grado ocho. Explica por qué el error sube con grado muy bajo. Estima cuántas capas hacen falta para cubrir todas las entradas. Y explica por qué las capas dispersas pueden ser lentas en una GPU.

**EN:** To practice: compute the width with degree eight. Explain why the error rises at very low degree. Estimate how many layers are needed to cover all inputs. And explain why sparse layers can be slow on a GPU.

## Key equations
- $$C = n\,k \quad (\text{connections} = \text{width}\times\text{degree})$$ — Iso-FLOP budget of a sparse layer.
- $$r_{\text{local}}(\ell) \approx \ell\,k,\qquad r_{\text{small-world}}(\ell) \sim k^{\ell}$$ — Receptive field after ℓ layers.
- $$\text{NMSE}(k)\colon 0.115\ (k = 64) \to 0.083\ (k = 16) \to 0.109\ (k = 2)$$ — Iso-FLOP U-curve at C = 8192 [S].

## Summary
- Sparse layer: each unit has k inputs; cost = n·k.
- Iso-FLOP: wide-sparse beats narrow-dense up to an optimum [S].
- Toy optimum at k = 16; too-low degree starves each unit.
- Fixed chip degree: depth + long jumps mix the graph.

## Further reading
- E. Frantar et al., Scaling laws for sparsely-connected foundation models, ICLR (2024).
- R. Child et al., Generating long sequences with sparse transformers, arXiv:1904.10509 (2019).
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
