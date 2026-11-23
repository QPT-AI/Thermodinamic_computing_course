# Lesson 10.1 — Transformer review

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Recall the transformer block: attention, MLP, normalization, residual stream.
- Count parameters and FLOPs per token, and the size of the KV cache.
- Explain prefill vs decode with a roofline argument, and why decode MFU is low.

## Prerequisites
- Lesson 9.4: MFU and energy per token.
- Linear algebra: matrix products.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** Antes de llevar un modelo de lenguaje a hardware termodinámico, hay que saber con precisión qué hace un transformer y dónde gasta tiempo y energía. Esta lección es un repaso dirigido: las piezas del bloque, cuántas operaciones cuesta cada token, la memoria de la caché y la diferencia crucial entre procesar el prompt y generar token a token.

**EN:** Before taking a language model to thermodynamic hardware, we must know precisely what a transformer does and where it spends time and energy. This lesson is a targeted review: the parts of the block, how many operations each token costs, the cache memory and the crucial difference between processing the prompt and generating token by token.

### [00:26.9] The block — `manim:S02`

**ES:** Un transformer es una pila de bloques iguales sobre un flujo residual de dimensión d. Cada bloque tiene una normalización, una atención que mezcla información entre posiciones, otra normalización y una red de dos capas, el MLP, que procesa cada posición por separado. La atención calcula consultas, claves y valores, y pondera los valores con un softmax de los productos entre consultas y claves.

**EN:** A transformer is a stack of identical blocks on a residual stream of dimension d. Each block has a normalization, an attention that mixes information across positions, another normalization and a two-layer network, the MLP, that processes each position separately. Attention computes queries, keys and values, and weights the values with a softmax of the products between queries and keys.

### [00:53.1] Counting — `manim:S03`

**ES:** Cada bloque tiene unos 12 d² parámetros: cuatro en las proyecciones de atención y ocho en el MLP con expansión de cuatro. Procesar un token cuesta unas dos operaciones por parámetro. La atención añade un término que crece con el contexto L: 4 L d por bloque. Para d = 4096 y un contexto de cuatro mil, son sesenta y siete millones de operaciones de atención frente a cuatrocientos de las matrices: las matrices dominan.

**EN:** Each block has about 12 d² parameters: four in the attention projections and eight in the MLP with a four-fold expansion. Processing a token costs about two operations per parameter. Attention adds a term that grows with the context L: 4 L d per block. For d = 4096 and a context of four thousand, that is sixty-seven million attention operations against four hundred million for the matrices: the matrices dominate.

### [01:22.6] The KV cache — `manim:S04`

**ES:** Al generar, las claves y valores de los tokens anteriores no cambian, así que se guardan: es la caché KV. Su tamaño por token es dos por el número de capas por d por los bytes por número. En un modelo de siete mil millones de parámetros con treinta y dos capas y precisión de dieciséis bits, es medio megabyte por token: con cuatro mil tokens de contexto, más de dos gigabytes por secuencia.

**EN:** When generating, the keys and values of previous tokens do not change, so they are stored: that is the KV cache. Its size per token is two times the number of layers times d times the bytes per number. In a seven-billion-parameter model with thirty-two layers and sixteen-bit precision, that is half a megabyte per token: with four thousand tokens of context, more than two gigabytes per sequence.

### [01:48.4] Prefill vs decode — `manim:S05`

**ES:** Procesar el prompt, el prefill, hace muchas operaciones por cada byte de peso leído: es limitado por cómputo. Generar token a token, el decode, lee todos los pesos para producir un solo token por secuencia. Con el modelo del techo, una GPU moderna necesita unas doscientas noventa y cinco operaciones por byte para trabajar a pleno. Con lote uno, el decode hace una: su utilización máxima es del cero coma tres por ciento. Con lote dieciséis, del cinco por ciento; con sesenta y cuatro, del veintidós.

**EN:** Processing the prompt, the prefill, performs many operations per byte of weights read: it is compute-bound. Generating token by token, the decode, reads all the weights to produce a single token per sequence. With the roofline model, a modern GPU needs about two hundred ninety-five operations per byte to run at full throughput. With batch one, decode does one: its maximum utilization is 0.3 percent. With batch sixteen, five percent; with sixty-four, twenty-two.

### [02:22.0] What this means for TSUs — `manim:S06`

**ES:** Aquí aparece la oportunidad. En un TSU espacial, los pesos viven en el propio chip como acoplamientos, así que no hay que leerlos de memoria en cada token. El decode con lote uno, el peor caso para una GPU, no penaliza la utilización de un TSU. En cambio, el prefill, que la GPU hace muy bien, no ofrece ventaja clara. Por eso los modelos de lenguaje termodinámicos apuntan sobre todo a la generación interactiva.

**EN:** Here the opportunity appears. In a spatial TSU, the weights live on the chip itself as couplings, so they need not be read from memory for every token. Batch-one decode, the worst case for a GPU, does not penalize a TSU's utilization. In contrast, prefill, which the GPU does very well, offers no clear advantage. That is why thermodynamic language models aim mainly at interactive generation.

### [02:50.4] Applications — `slide`

**ES:** Con estas cuentas se estiman las operaciones por token, se dimensiona la caché y se predice la utilización con el modelo del techo. En el laboratorio veintiocho medirás prefill y decode en tu GPU.

**EN:** With these counts one estimates operations per token, sizes the cache and predicts utilization with the roofline model. In lab twenty-eight you will measure prefill and decode on your GPU.

### [03:03.1] Common mistakes — `slide`

**ES:** Errores comunes: usar la utilización del prefill para estimar la energía del decode. Ignorar la caché en el presupuesto de memoria. Suponer que la atención domina con contextos moderados. Y afirmar ventaja de un TSU en cargas dominadas por el prefill.

**EN:** Common mistakes: using prefill utilization to estimate decode energy. Ignoring the cache in the memory budget. Assuming attention dominates at moderate context. And claiming a TSU advantage for prefill-dominated workloads.

### [03:19.9] Summary — `manim:S09`

**ES:** En resumen: un bloque tiene unos 12 d² parámetros y cada token cuesta dos operaciones por parámetro más la atención. La caché KV ocupa medio megabyte por token en un modelo de siete mil millones. El prefill está limitado por cómputo y el decode por memoria, con utilización bajísima en lotes pequeños: justo donde un TSU, con los pesos en el chip, tiene su oportunidad.

**EN:** In summary: a block has about 12 d² parameters and each token costs two operations per parameter plus attention. The KV cache takes half a megabyte per token in a seven-billion model. Prefill is compute-bound and decode memory-bound, with very low utilization at small batch: exactly where a TSU, with the weights on chip, has its opportunity.

### [03:44.9] Self-assessment — `slide`

**ES:** Para practicar: cuenta los parámetros de un bloque. Calcula la caché por token. Calcula la utilización máxima del decode con lote treinta y dos. Y explica por qué el prefill está limitado por cómputo.

**EN:** To practice: count the parameters of a block. Compute the cache per token. Compute the maximum decode utilization with batch thirty-two. And explain why prefill is compute-bound.

## Key equations
- $$P_{\text{block}} \approx 12d^2,\qquad \text{FLOPs/token} \approx 2P + 4Ld\ \text{per block}$$ — Parameter and compute counts.
- $$\text{KV/token} = 2\,n_{\text{layers}}\,d\,b_{\text{bytes}}\quad (7\text{B}: 2\cdot32\cdot4096\cdot2 = 0.5\ \text{MB})$$ — KV cache size.
- $$\text{MFU}_{\max} = \min\Big(1,\ \frac{I}{I^\ast}\Big),\quad I_{\text{decode}} \approx B\ \text{FLOP/byte},\ I^\ast \approx 295$$ — Roofline bound (H100-class: 989 TFLOP/s, 3.35 TB/s).

## Summary
- Block ≈ 12 d² parameters; ≈ 2 FLOPs per parameter per token (+4Ld attention).
- KV cache: 0.5 MB/token for a 7B model; 2.1 GB at 4096 tokens.
- Roofline: decode MFU ≤ 0.3 % (B = 1), 5.4 % (B = 16), 22 % (B = 64) [E].
- TSUs keep weights on chip: opportunity in batch-1 decode, not prefill.

## Further reading
- A. Vaswani et al., Attention is all you need, NeurIPS (2017).
- S. Williams, A. Waterman and D. Patterson, Roofline: an insightful visual performance model, CACM 52, 65 (2009).
- R. Pope et al., Efficiently scaling transformer inference, MLSys (2023).
