# Lesson 10.7 — The Z1T architecture

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe the Z1T model: GCA mixing, DyT, tanh-linear units, 4-sparse projections, dy4p activations.
- Explain disaggregated inference: what runs on the Z1 chip and what on the FPGA.
- Read the reported energy and latency tables critically: the FPGA bottleneck and the excluded vocabulary head.

## Prerequisites
- Lessons 10.2–10.6.
- Lesson 9.5: Amdahl and the digital glue.

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** En septiembre de dos mil veintiséis, Extropic publicó Z1T, un modelo de lenguaje parecido a un transformer, diseñado para su chip de pbits Z1. Reúne todo lo que vimos en esta unidad. Hoy lo desarmamos: su arquitectura, cómo se reparte el trabajo entre el chip y una FPGA, y qué dicen de verdad sus tablas de energía y latencia.

**EN:** In September twenty twenty-six, Extropic published Z1T, a transformer-like language model designed for its Z1 pbit chip. It brings together everything we saw in this unit. Today we take it apart: its architecture, how the work is split between the chip and an FPGA, and what its energy and latency tables really say.

### [00:27.0] The model — `manim:S02`

**ES:** Z1T es pequeño: cuatro capas, dimensión quinientos doce, contexto de mil veinticuatro tokens. La atención se reemplaza por atención convolucional con compuertas, de la familia AFT. La normalización es DyT. El MLP usa unidades tanh-lineales. Todas las proyecciones son dispersas, con cuatro entradas por salida, y los pesos usan cuatro bits.

**EN:** Z1T is small: four layers, dimension five hundred twelve, a context of one thousand twenty-four tokens. Attention is replaced by gated convolutional attention, from the AFT family. Normalization is DyT. The MLP uses tanh-linear units. All projections are sparse, with four inputs per output, and the weights use four bits.

### [00:52.9] Mapping to Z1 — `manim:S03`

**ES:** Cada pbit de salida gasta sus dieciséis acoplamientos en cuatro valores de entrada por cuatro pbits, con una codificación llamada dy4p, de cuatro bits. El chip Z1 tiene ocho núcleos y doscientos sesenta y nueve mil quinientos sesenta y ocho pbits, con muestreo a más de cincuenta megahercios y menos de un vatio. En el chip corren las proyecciones muestreadas y DyT.

**EN:** Each output pbit spends its sixteen couplings on four input values times four pbits, with a four-bit encoding called dy4p. The Z1 chip has eight cores and two hundred sixty-nine thousand five hundred sixty-eight pbits, sampling at more than fifty megahertz and under one watt. The sampled projections and DyT run on the chip.

### [01:16.9] Disaggregated inference — `manim:S04`

**ES:** Lo demás corre en una FPGA: el embedding, la aritmética de la atención convolucional, los residuos, la codificación posicional y la cabeza de vocabulario que produce los logits. Es inferencia desagregada: cada operación va al dispositivo donde es nativa. El artículo menciona que la FPGA podría cambiarse por una GPU u otro acelerador, aunque eso no se midió.

**EN:** The rest runs on an FPGA: the embedding, the arithmetic of convolutional attention, the residuals, positional encoding and the vocabulary head that produces the logits. It is disaggregated inference: each operation goes to the device where it is native. The article mentions that the FPGA could be swapped for a GPU or another accelerator, though that was not measured.

### [01:41.9] Energy: the FPGA bottleneck — `manim:S05`

**ES:** La estimación de energía es de doscientos noventa y cuatro coma cinco dos nanojulios por token: ocho coma siete cuatro para el muestreo en Z1 y doscientos ochenta y cinco coma siete ocho para la FPGA. El chip termodinámico es menos del tres por ciento. Frente a una H100 con utilización del diez por ciento, la ventaja reportada es de unas ciento treinta y nueve veces; al cincuenta por ciento, veintiocho; al cien por ciento, catorce. Las capas de Z1 por sí solas serían cientos o miles de veces más eficientes: el cuello de botella es la FPGA, como predijo Amdahl en la lección nueve punto cinco.

**EN:** The energy estimate is 294.52 nanojoules per token: 8.74 for sampling on Z1 and 285.78 for the FPGA. The thermodynamic chip is less than three percent. Against an H100 at ten percent utilization, the reported advantage is about one hundred thirty-nine times; at fifty percent, twenty-eight; at one hundred percent, fourteen. The Z1 layers on their own would be hundreds or thousands of times more efficient: the bottleneck is the FPGA, as Amdahl predicted in lesson 9.5.

### [02:21.2] The vocabulary head and the caveats — `manim:S06`

**ES:** Ahora la letra pequeña. La cabeza de vocabulario, la última capa densa que produce los logits, se excluye de las cifras principales; incluida, la energía sube a unos ciento treinta y seis microjulios por token, unas cuatrocientas sesenta veces más. Tampoco se cuenta el movimiento de datos entre chip y FPGA ni el número de chips. La latencia estimada es de cincuenta y ocho coma ocho microsegundos por token, frente a ciento dos en una H100 compilada, y la orquestación de la FPGA es la mayor parte. Todo son proyecciones con lote uno, no mediciones del sistema completo.

**EN:** Now the fine print. The vocabulary head, the last dense layer that produces the logits, is excluded from the headline figures; included, the energy rises to about one hundred thirty-six microjoules per token, some four hundred sixty times more. Data movement between chip and FPGA and the number of chips are not counted either. The estimated latency is 58.8 microseconds per token, against one hundred two on a compiled H100, and FPGA orchestration is most of it. All are batch-one projections, not measurements of the complete system.

### [02:58.7] Applications — `slide`

**ES:** De Z1T aprendemos una receta de diseño, la necesidad de contar la energía por dispositivo incluyendo la cabeza de vocabulario, y que la próxima ganancia está en reducir el pegamento digital. En el laboratorio veintinueve harás tu propia proyección de energía por token.

**EN:** From Z1T we learn a design recipe, the need to count energy per device including the vocabulary head, and that the next gain lies in reducing the digital glue. In lab twenty-nine you will make your own energy-per-token projection.

### [03:16.1] Common mistakes — `slide`

**ES:** Errores comunes: citar ciento treinta y nueve veces sin decir que supone diez por ciento de utilización. Ignorar la cabeza de vocabulario excluida. Confundir la ventaja de las capas de Z1 con la del sistema completo. Y tratar proyecciones como si fueran mediciones.

**EN:** Common mistakes: quoting one hundred thirty-nine times without saying it assumes ten percent utilization. Ignoring the excluded vocabulary head. Confusing the advantage of the Z1 layers with that of the complete system. And treating projections as if they were measurements.

### [03:33.6] Summary — `manim:S09`

**ES:** En resumen, Z1T combina atención convolucional con compuertas, DyT, unidades tanh-lineales y proyecciones de grado cuatro con pbits dy4p. El chip hace el muestreo; la FPGA, todo lo demás, y se lleva el noventa y siete por ciento de la energía estimada. Las cifras son proyecciones prometedoras con exclusiones importantes, la cabeza de vocabulario la primera.

**EN:** In summary, Z1T combines gated convolutional attention, DyT, tanh-linear units and degree-four projections with dy4p pbits. The chip does the sampling; the FPGA, everything else, and it takes ninety-seven percent of the estimated energy. The figures are promising projections with important exclusions, the vocabulary head first among them.

### [03:58.6] Self-assessment — `slide`

**ES:** Para practicar: calcula la fracción de la FPGA. Recalcula la ventaja de ciento treinta y nueve veces. Calcula el factor que añade la cabeza de vocabulario. Y explica qué componente domina la latencia.

**EN:** To practice: compute the FPGA share. Recompute the one hundred thirty-nine times advantage. Compute the factor the vocabulary head adds. And explain which component dominates latency.

## Key equations
- $$E_{\text{token}} = \underbrace{8.74}_{\text{Z1}} + \underbrace{285.78}_{\text{FPGA}} = 294.52\ \text{nJ}\quad(97\%\ \text{FPGA})$$ — Reported Z1T energy split, vocabulary head excluded [P].
- $$\frac{E_{\text{H100}}}{E_{\text{Z1T}}} = \frac{40.9\ \mu\text{J}}{294.52\ \text{nJ}} \approx 139\quad(\text{MFU} = 10\%)$$ — Headline ratio; 28× at 50% MFU, 14× at 100%.
- $$t_{\text{token}} = 38.0 + 16.0 + 3.2 + 1.3 + 0.3 \approx 58.8\ \mu\text{s}$$ — Latency: FPGA orchestration, Z1 sampling, reads, writes, rest.

## Summary
- Z1T: L = 4, D = 512, GCA, DyT, tanh-linear, k = 4, 4-bit weights, dy4p.
- Z1 samples; FPGA does embedding, GCA arithmetic, residuals, logits.
- 294.52 nJ/token, 97% FPGA; 139× / 28× / 14× vs H100 at 10/50/100% MFU [P].
- Excluded: vocabulary head (~136 µJ), data movement, chip count.

## Further reading
- Extropic, Z1T, extropic.ai/writing/z1t (September 2026).
- S. Zhai et al., An attention free transformer, arXiv:2105.14103 (2021).
- J. Zhu et al., Transformers without normalization, CVPR (2025).
