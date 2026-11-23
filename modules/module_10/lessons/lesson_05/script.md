# Lesson 10.5 — Encoding numbers in pbits

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Represent a real number as the mean of a stream of pbit samples (a probabilistic integer).
- Derive and verify the effective-bits law $b_{\text{eff}} \approx b_1 + \tfrac12\log_2 S$.
- Explain precision on demand and its cost: one extra bit needs four times the samples.

## Prerequisites
- Lesson 5.6: stochastic rounding.
- Lesson 10.3: averaging pbit samples.

## Narrated script

### [00:05.0] Introduction — `manim:S01`

**ES:** Un chip digital guarda números con un ancho fijo de bits. Un chip de pbits solo produce unos y ceros aleatorios. ¿Cómo representa entonces una activación de valor cero coma treinta y siete? La idea es usar la probabilidad: el número es la frecuencia con la que aparecen los unos. Hoy vemos cuántos bits efectivos se obtienen así y cuánto cuestan.

**EN:** A digital chip stores numbers with a fixed width of bits. A pbit chip only produces random ones and zeros. How, then, does it represent an activation with value 0.37? The idea is to use probability: the number is the frequency with which ones appear. Today we see how many effective bits this yields and how much they cost.

### [00:27.8] Probabilistic integers — `manim:S02`

**ES:** Un entero probabilístico es una variable aleatoria entera cuya media es el valor que queremos. El caso más simple es un pbit con probabilidad x de valer uno. Con un grupo de n pbits, la suma toma valores de cero a n y su media es n x. En el temario, esta familia de codificaciones aparece como dy4p; aquí estudiamos el principio general, que no depende de los detalles de una implementación concreta.

**EN:** A probabilistic integer is a random integer variable whose mean is the value we want. The simplest case is one pbit with probability x of being one. With a group of n pbits, the sum takes values from zero to n and its mean is n x. In the syllabus, this family of encodings appears as dy4p; here we study the general principle, which does not depend on the details of a specific implementation.

### [00:55.6] Effective bits — `manim:S03`

**ES:** Definimos los bits efectivos comparando el error cuadrático medio con el de un cuantizador uniforme: un error de un medio elevado a b, dividido por raíz de doce, equivale a b bits. Si una muestra da b₁ bits efectivos, promediar S muestras divide el ruido por raíz de S, y eso suma un medio de logaritmo en base dos de S bits.

**EN:** We define effective bits by comparing the mean squared error with that of a uniform quantizer: an error of one half to the power b, divided by root twelve, is worth b bits. If one sample gives b₁ effective bits, averaging S samples divides the noise by root S, and that adds one half of log base two of S bits.

### [01:18.2] Verification — `manim:S04`

**ES:** Lo verificamos con veinte mil valores al azar, codificados con redondeo estocástico a dieciséis niveles. Una muestra da tres coma cuatro dos bits efectivos; cuatro muestras, cuatro coma cuatro uno; dieciséis, cinco coma cuatro uno; doscientas cincuenta y seis, siete coma cuatro uno. Cada factor cuatro en muestras suma exactamente un bit, tal como predice la ley.

**EN:** We verify it with twenty thousand random values, encoded with stochastic rounding to sixteen levels. One sample gives 3.42 effective bits; four samples, 4.41; sixteen, 5.41; two hundred fifty-six, 7.41. Each factor of four in samples adds exactly one bit, just as the law predicts.

### [01:42.8] Pbits and samples are interchangeable — `manim:S05`

**ES:** Con un grupo de n pbits binarios pasa lo mismo: lo que cuenta es el total de muestras, n · S. Un solo pbit con una muestra da menos de cero bits efectivos; con dieciséis muestras, uno coma cinco. Dieciséis pbits con dieciséis muestras dan tres coma cinco. Se puede gastar en espacio, con más pbits, o en tiempo, con más muestras.

**EN:** With a group of n binary pbits the same happens: what counts is the total number of samples, n · S. A single pbit with one sample gives less than zero effective bits; with sixteen samples, 1.5. Sixteen pbits with sixteen samples give 3.5. One can spend in space, with more pbits, or in time, with more samples.

### [02:05.9] Precision on demand — `manim:S06`

**ES:** Esto permite precisión a demanda: cada capa, o cada token, puede pedir los bits que necesita. Pero el costo crece rápido. Cada bit adicional exige cuatro veces más muestras, así que la energía crece como cuatro elevado al número de bits. Con pocos bits, la codificación probabilística es barata; con muchos, un multiplicador digital gana. Por eso los modelos para TSU se entrenan para funcionar con muy pocos bits efectivos.

**EN:** This enables precision on demand: each layer, or each token, can ask for the bits it needs. But the cost grows fast. Each additional bit requires four times more samples, so energy grows as four to the power of the number of bits. With few bits, probabilistic encoding is cheap; with many, a digital multiplier wins. That is why TSU models are trained to work with very few effective bits.

### [02:34.1] Applications — `slide`

**ES:** En la práctica: codifica las activaciones como frecuencias de pbits, reparte las muestras por capa según cuánto dañe el error, y entrena con el ruido incluido para necesitar menos bits. En el laboratorio veintinueve medirás la exactitud frente a las muestras.

**EN:** In practice: encode activations as pbit frequencies, distribute samples per layer according to how much the error hurts, and train with the noise included to need fewer bits. In lab twenty-nine you will measure accuracy against samples.

### [02:50.7] Common mistakes — `slide`

**ES:** Errores comunes: contar niveles como si fueran bits efectivos. Esperar ganancias lineales, cuando un bit más cuesta cuatro veces más muestras. Ignorar las correlaciones entre muestras, que reducen la ganancia. Y reportar bits sin decir cómo se define el error.

**EN:** Common mistakes: counting levels as if they were effective bits. Expecting linear gains, when one more bit costs four times more samples. Ignoring correlations between samples, which reduce the gain. And reporting bits without saying how the error is defined.

### [03:08.4] Summary — `manim:S09`

**ES:** En resumen, un número se codifica como la media de muestras de pbits. Los bits efectivos siguen la ley b₁ + ½ log₂ S, que verificamos: cuatro veces más muestras, un bit más. La precisión se puede pedir a demanda, pero su costo crece exponencialmente con los bits.

**EN:** In summary, a number is encoded as the mean of pbit samples. Effective bits follow the law b₁ + ½ log₂ S, which we verified: four times more samples, one more bit. Precision can be requested on demand, but its cost grows exponentially with the bits.

### [03:28.4] Self-assessment — `slide`

**ES:** Para practicar: calcula las muestras para ganar tres bits. Calcula la varianza de la media de un grupo de pbits. Explica por qué pbits y muestras se intercambian. Y di cuándo gana un multiplicador digital.

**EN:** To practice: compute the samples to gain three bits. Compute the variance of the mean of a group of pbits. Explain why pbits and samples trade off. And say when a digital multiplier wins.

## Key equations
- $$b_{\text{eff}} = -\log_2\big(\sqrt{12}\,\mathrm{rms}\big)$$ — Effective bits from the rms error (uniform-quantizer equivalence).
- $$b_{\text{eff}}(S) = b_1 + \tfrac12\log_2 S$$ — Averaging S independent samples: 4× samples per extra bit.
- $$\mathrm{Var}\Big(\frac1{nS}\sum m\Big) = \frac{x(1-x)}{nS}$$ — n pbits × S samples: only the product counts.

## Summary
- Probabilistic integer: random integer whose mean is the value.
- b_eff = b₁ + ½ log₂ S, verified: 3.42 → 7.41 bits for S = 1 → 256 [S].
- pbits (space) and samples (time) are interchangeable.
- Precision on demand; cost ∝ 4^b → train for few bits.

## Further reading
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
- B. R. Gaines, Stochastic computing systems, Advances in Information Systems Science 2, 37 (1969).
- A. Alaghi and J. P. Hayes, Survey of stochastic computing, ACM TECS 12, 92 (2013).
