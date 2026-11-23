# Lesson 10.8 — Energy metrics for LLMs

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define J/token, J/FLOP and MFU and reconstruct a published GPU baseline from them.
- Distinguish headline ratios from net, same-scope ratios.
- Explain the sparsity tax and write a fair energy comparison.

## Prerequisites
- Lesson 10.1: MFU and the roofline.
- Lesson 10.7: the Z1T energy tables.

## Narrated script

### [00:05.8] Introduction — `manim:S01`

**ES:** Una razón de energía es tan buena como su denominador. Cien veces más eficiente, ¿frente a qué GPU, con qué utilización, contando qué partes del modelo y con qué calidad? Hoy aprendemos las métricas y las aplicamos a las cifras de Z1T, para separar el titular de la ganancia neta.

**EN:** An energy ratio is only as good as its denominator. One hundred times more efficient: against which GPU, at what utilization, counting which parts of the model and at what quality? Today we learn the metrics and apply them to the Z1T figures, to separate the headline from the net gain.

### [00:24.7] J/token, J/FLOP, MFU — `manim:S02`

**ES:** Tres métricas. Julios por token: la energía para generar un token. Julios por operación: el costo de una operación de coma flotante al rendimiento pico. Y la utilización, MFU, la fracción del pico que realmente se usa. Se relacionan así: la energía por token es dos veces los parámetros, por la energía por operación, dividido por la utilización. Con once coma cinco cinco millones de parámetros y cero coma uno siete siete picojulios por operación, obtenemos cuatro coma cero nueve microjulios al cien por cien, exactamente la cifra de la H100 en la tabla de Z1T.

**EN:** Three metrics. Joules per token: the energy to generate one token. Joules per operation: the cost of a floating-point operation at peak performance. And utilization, MFU, the fraction of the peak that is actually used. They are related like this: energy per token is twice the parameters, times the energy per operation, divided by the utilization. With 11.55 million parameters and 0.177 picojoules per operation, we get 4.09 microjoules at one hundred percent, exactly the H100 figure in the Z1T table.

### [01:03.6] The headline — `manim:S03`

**ES:** El titular de Z1T, ciento treinta y nueve veces, usa una utilización del diez por ciento. Es razonable para decode con lote uno, pero el propio artículo menciona que en modelos como Llama tres la utilización ronda el cuarenta por ciento. Con ese valor, la ventaja baja a unas treinta y cinco veces. Ningún número es falso; lo que cambia es el supuesto.

**EN:** The Z1T headline, one hundred thirty-nine times, uses a utilization of ten percent. It is reasonable for batch-one decode, but the article itself mentions that in models like Llama three utilization is around forty percent. With that value, the advantage drops to about thirty-five times. No number is false; what changes is the assumption.

### [01:27.0] Same scope: the vocabulary head — `manim:S04`

**ES:** Ahora el alcance. El titular excluye la cabeza de vocabulario. Comparemos con el mismo alcance en ambos lados, suponiendo un vocabulario de cincuenta mil doscientos cincuenta y siete tokens, el de GPT-2, porque el artículo no da el tamaño. En la H100, la cabeza cuesta nueve coma uno microjulios al cien por cien, o noventa y uno al diez por ciento. En Z1T, en la FPGA, unos ciento treinta y seis. Con todo incluido, al diez por ciento hay empate, y al cuarenta por ciento la GPU es unas cuatro veces mejor. Esta es una estimación nuestra, con un supuesto explícito.

**EN:** Now the scope. The headline excludes the vocabulary head. Let's compare with the same scope on both sides, assuming a vocabulary of fifty thousand two hundred fifty-seven tokens, GPT-2's, because the article does not give the size. On the H100, the head costs 9.1 microjoules at one hundred percent, or ninety-one at ten percent. On Z1T, on the FPGA, about one hundred thirty-six. With everything included, at ten percent there is a tie, and at forty percent the GPU is about four times better. This is our own estimate, with an explicit assumption.

### [02:05.4] The sparsity tax — `manim:S05`

**ES:** Falta la calidad. Un modelo disperso de igual tamaño es peor que uno denso. Según el artículo, igualar la pérdida de GPT-2 small exige del orden de diez veces más operaciones de entrenamiento: es el impuesto de la dispersión. En inferencia, una comparación de igual calidad podría requerir un modelo disperso más grande, y ese factor no se reporta. La ganancia neta es el titular dividido por todos estos factores.

**EN:** Quality is missing. A sparse model of equal size is worse than a dense one. According to the article, matching the loss of GPT-2 small requires on the order of ten times more training operations: that is the sparsity tax. At inference, an equal-quality comparison could require a larger sparse model, and that factor is not reported. The net gain is the headline divided by all these factors.

### [02:33.0] A fair comparison — `manim:S06`

**ES:** Una comparación justa declara cinco cosas: la utilización supuesta de la GPU, el alcance de lo que se cuenta, incluida la cabeza y el movimiento de datos, la calidad a la que se compara, la razón del sistema completo y la de solo el tejido termodinámico, y la etiqueta de evidencia de cada número. Con eso, la lección de Z1T es clara: las capas termodinámicas son muy eficientes, y el trabajo pendiente es llevar todo lo demás a ese nivel.

**EN:** A fair comparison declares five things: the assumed GPU utilization, the scope of what is counted, including the head and data movement, the quality at which it compares, the ratio of the full system and that of the thermodynamic fabric alone, and the evidence label of each number. With that, the lesson of Z1T is clear: the thermodynamic layers are very efficient, and the pending work is bringing everything else to that level.

### [03:02.0] Applications — `slide`

**ES:** Al escribir una afirmación de energía: reporta julios por token con utilización, lote y alcance; da la razón del sistema y la del tejido; y declara la calidad y el impuesto de la dispersión. En el laboratorio veintinueve construirás tu tabla de titular frente a neto.

**EN:** When writing an energy claim: report joules per token with utilization, batch and scope; give the system ratio and the fabric ratio; and declare the quality and the sparsity tax. In lab twenty-nine you will build your headline-versus-net table.

### [03:19.4] Common mistakes — `slide`

**ES:** Errores comunes: comparar con distinto alcance. Elegir la utilización de la GPU que maximiza la razón. Comparar modelos de distinta calidad. Y mezclar números medidos y proyectados sin etiquetas.

**EN:** Common mistakes: comparing with a different scope. Choosing the GPU utilization that maximizes the ratio. Comparing models of different quality. And mixing measured and projected numbers without labels.

### [03:33.3] Summary — `manim:S09`

**ES:** En resumen, la energía por token es dos veces los parámetros por la energía por operación, dividido por la utilización, y con ella reconstruimos la cifra de la H100. El titular de Z1T depende del diez por ciento de utilización y excluye la cabeza; con el mismo alcance y nuestro supuesto de vocabulario, hay empate o gana la GPU. La ganancia neta exige declarar utilización, alcance y calidad.

**EN:** In summary, energy per token is twice the parameters times the energy per operation, divided by the utilization, and with it we reconstructed the H100 figure. The Z1T headline depends on ten percent utilization and excludes the head; with the same scope and our vocabulary assumption, there is a tie or the GPU wins. The net gain requires declaring utilization, scope and quality.

### [04:00.4] Self-assessment — `slide`

**ES:** Para practicar: calcula la energía por token al veinticinco por ciento. Calcula la razón al cuarenta por ciento. Calcula las operaciones de la cabeza con otro vocabulario. Y enumera los cinco elementos de una comparación justa.

**EN:** To practice: compute the energy per token at twenty-five percent. Compute the ratio at forty percent. Compute the head operations with another vocabulary. And list the five items of a fair comparison.

## Key equations
- $$E_{\text{token}} = \frac{2P\,e_{\text{FLOP}}}{\text{MFU}},\quad 2\cdot 11.55\text{M}\cdot 0.177\ \text{pJ} = 4.09\ \mu\text{J}$$ — Reconstructs the H100 baseline of the Z1T table.
- $$\text{headline} = \frac{E^{\text{GPU}}_{\text{body}}}{E^{\text{Z1T}}_{\text{body}}}\quad\text{vs}\quad \text{net} = \frac{E^{\text{GPU}}_{\text{body+head}}}{E^{\text{Z1T}}_{\text{body+head}}}\cdot\frac{1}{\text{tax}}$$ — Same scope and same quality.
- $$E^{\text{GPU}}_{\text{head}} = \frac{2DV\,e_{\text{FLOP}}}{\text{MFU}} \approx 9.1\ \mu\text{J}\ (\text{MFU} = 1,\ V = 50\,257)$$ — Vocabulary head on the GPU [E], vocabulary assumed.

## Summary
- E_token = 2P·e_FLOP/MFU reproduces the 4.09 µJ H100 figure.
- Headline 139× assumes 10% MFU; ≈ 35× at 40%.
- Same scope incl. head (V = 50 257 assumed): ≈ 1× at 10%, GPU ≈ 4× better at 40% [E].
- Sparsity tax: ~10× training FLOPs to match GPT-2 small [P].

## Further reading
- Extropic, Z1T, extropic.ai/writing/z1t (September 2026).
- A. Chowdhery et al., PaLM: scaling language modeling with Pathways (MFU definition), arXiv:2204.02311 (2022).
- R. Schwartz et al., Green AI, Communications of the ACM 63, 54 (2020).
