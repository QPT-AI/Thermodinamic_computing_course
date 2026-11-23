# Lesson 9.2 — Discrete diffusion

**Unit:** Unit 9 — Thermodynamic generative models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe masked (absorbing-state) diffusion for tokens: the forward process masks, the reverse process unmasks.
- State the MDLM objective as a weighted cross-entropy on masked positions.
- Quantify the error of unmasking many tokens in parallel, and why few-step samplers need distillation.

## Prerequisites
- Lesson 9.1: diffusion models.
- Lesson 4.1: graphical models and conditional independence.

## Narrated script

### [00:04.4] Introduction — `manim:S01`

**ES:** El texto está hecho de símbolos, no de números reales, así que la difusión gaussiana no encaja directamente. La difusión discreta reemplaza el ruido gaussiano por corrupción de símbolos. La versión más exitosa es la difusión enmascarada: los tokens se van ocultando, y el modelo aprende a revelarlos. Es la base de los modelos de lenguaje por difusión y, como veremos, encaja con hardware que muestrea variables discretas.

**EN:** Text is made of symbols, not real numbers, so Gaussian diffusion does not fit directly. Discrete diffusion replaces Gaussian noise with symbol corruption. The most successful version is masked diffusion: tokens are gradually hidden, and the model learns to reveal them. It is the basis of diffusion language models and, as we will see, it fits hardware that samples discrete variables.

### [00:31.4] Masking as the forward process — `manim:S02`

**ES:** En el tiempo t entre cero y uno, cada token se reemplaza por un símbolo de máscara con probabilidad t, de forma independiente. La máscara es un estado absorbente: una vez oculto, el token sigue oculto. En t = 1 la secuencia está totalmente enmascarada. El proceso inverso parte de todo enmascarado y revela tokens, usando un modelo que predice cada token oculto dado lo visible.

**EN:** At time t between zero and one, each token is replaced by a mask symbol with probability t, independently. The mask is an absorbing state: once hidden, the token stays hidden. At t = 1 the sequence is fully masked. The reverse process starts from all masks and reveals tokens, using a model that predicts each hidden token given what is visible.

### [00:56.8] The MDLM objective — `manim:S03`

**ES:** El modelo de lenguaje por difusión enmascarada, MDLM, entrena con una cota inferior de la verosimilitud que resulta ser sorprendentemente simple: una entropía cruzada sobre las posiciones enmascaradas, ponderada por un factor que depende del tiempo, que para un calendario lineal es uno sobre t. Es como el entrenamiento de BERT, pero con todas las tasas de enmascarado y con un peso que convierte la suma en una cota de la verosimilitud.

**EN:** The masked diffusion language model, MDLM, trains with a lower bound on the likelihood that turns out to be surprisingly simple: a cross-entropy over the masked positions, weighted by a time-dependent factor, which for a linear schedule is one over t. It is like BERT training, but with all masking rates and with a weight that turns the sum into a likelihood bound.

### [01:25.2] Parallel unmasking and its error — `manim:S04`

**ES:** Al muestrear, revelar un token por paso es exacto si el modelo es perfecto. Pero eso cuesta tantos pasos como tokens. Revelar varios a la vez es más rápido, pero los muestrea de forma independiente, ignorando sus correlaciones. Lo medimos con cadenas binarias de ocho símbolos muy correlacionadas, donde casi la mitad de las secuencias son constantes, y un modelo que conoce las condicionales exactas.

**EN:** When sampling, revealing one token per step is exact if the model is perfect. But it costs as many steps as tokens. Revealing several at once is faster, but samples them independently, ignoring their correlations. We measure it with highly correlated binary strings of eight symbols, where almost half the sequences are constant, and a model that knows the exact conditionals.

### [01:51.4] Measured error — `manim:S05`

**ES:** Con ocho pasos, uno por token, la distancia de variación total a la distribución verdadera es de apenas cero coma cero tres, el ruido de muestreo. Con cuatro pasos sube a cero coma dos. Con dos, a cero coma cuatro seis. Y con un solo paso, revelando todo a la vez, a cero coma siete nueve: las secuencias constantes, que en los datos son el cuarenta y ocho por ciento, aparecen menos del uno por ciento de las veces. El error no viene del modelo, sino del muestreo en paralelo.

**EN:** With eight steps, one per token, the total variation distance to the true distribution is only 0.03, the sampling noise. With four steps it rises to 0.2. With two, to 0.46. And with a single step, revealing everything at once, to 0.79: constant sequences, which are forty-eight percent of the data, appear less than one percent of the time. The error does not come from the model, but from parallel sampling.

### [02:21.7] Few-step samplers and the hardware angle — `manim:S06`

**ES:** Por eso los muestreadores de pocos pasos requieren trucos: elegir qué tokens revelar según la confianza, o destilar un modelo de muchos pasos en uno de pocos. El hardware probabilístico ofrece otra salida: en lugar de muestrear los tokens de un paso de forma independiente, puede muestrear su distribución conjunta con un modelo basado en energía que capture sus correlaciones. Esa es la idea de los modelos termodinámicos de eliminación de ruido.

**EN:** That is why few-step samplers need tricks: choosing which tokens to reveal based on confidence, or distilling a many-step model into a few-step one. Probabilistic hardware offers another way out: instead of sampling a step's tokens independently, it can sample their joint distribution with an energy-based model that captures their correlations. That is the idea of denoising thermodynamic models.

### [02:49.1] Applications — `slide`

**ES:** La difusión discreta se usa en modelos de lenguaje no autorregresivos, que generan en paralelo y permiten rellenar o editar cualquier parte del texto. En el laboratorio trece entrenarás un MDLM pequeño y medirás la calidad frente al número de pasos.

**EN:** Discrete diffusion is used in non-autoregressive language models, which generate in parallel and allow infilling or editing any part of the text. In lab thirteen you will train a small MDLM and measure quality against the number of steps.

### [03:05.8] Common mistakes — `slide`

**ES:** Errores comunes: olvidar que la máscara es absorbente. Quitar el peso temporal, con lo que la pérdida deja de ser una cota. Revelar muchos tokens correlacionados a la vez y culpar al modelo. Y comparar números de pasos sin igualar las evaluaciones del modelo.

**EN:** Common mistakes: forgetting that the mask is absorbing. Removing the time weight, so the loss is no longer a bound. Revealing many correlated tokens at once and blaming the model. And comparing step counts without matching model evaluations.

### [03:22.8] Summary — `manim:S09`

**ES:** En resumen: la difusión enmascarada oculta tokens hacia adelante y los revela hacia atrás, con una pérdida de entropía cruzada ponderada. Revelar un token por paso es exacto; revelar muchos a la vez los muestrea independientemente y destruye correlaciones, en nuestro ejemplo de cero coma cero tres a cero coma siete nueve de distancia. Muestrear la conjunta es justo lo que puede aportar el hardware termodinámico.

**EN:** In summary: masked diffusion hides tokens forward and reveals them backward, with a weighted cross-entropy loss. Revealing one token per step is exact; revealing many at once samples them independently and destroys correlations, in our example from 0.03 to 0.79 in distance. Sampling the joint is exactly what thermodynamic hardware can contribute.

### [03:49.4] Self-assessment — `slide`

**ES:** Para practicar: di la probabilidad de enmascarar en el tiempo t. Explica por qué revelar uno por paso es exacto. Analiza dos bits perfectamente correlacionados con un muestreador de un paso. Y nombra dos formas de reducir los pasos.

**EN:** To practice: give the probability of masking at time t. Explain why revealing one per step is exact. Analyze two perfectly correlated bits with a one-step sampler. And name two ways to reduce the steps.

## Key equations
- $$q(x_t^i \mid x_0^i) = (1-t)\,\delta_{x_0^i} + t\,\delta_{[\mathrm{M}]}$$ — Absorbing-state (masking) forward process, independently per token.
- $$\mathcal L_{\text{MDLM}} = \mathbb E_{t, x_t}\Big[\frac{1}{t}\sum_{i:\,x_t^i = [\mathrm M]} -\log p_\theta\big(x_0^i \mid x_t\big)\Big]$$ — Weighted masked cross-entropy (linear schedule): an ELBO.
- $$\prod_{i \in S} p(x^i \mid x_{\text{vis}}) \ne p(x_S \mid x_{\text{vis}})$$ — Parallel unmasking ignores correlations within a step.

## Summary
- Forward: mask each token with probability t (absorbing); reverse: reveal.
- MDLM loss: masked cross-entropy weighted by 1/t (linear schedule).
- Exact-conditional toy, L = 8: TV 0.03 (8 steps), 0.20 (4), 0.46 (2), 0.79 (1) [S].
- Few steps need confidence ordering or distillation — or joint sampling (DTM).

## Further reading
- S. S. Sahoo et al., Simple and effective masked diffusion language models, NeurIPS (2024).
- J. Austin et al., Structured denoising diffusion models in discrete state-spaces, NeurIPS (2021).
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, 2025.
