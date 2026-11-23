# Lesson 9.4 — A cost model for diffusion

**Unit:** Unit 9 — Thermodynamic generative models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write the energy per token of a diffusion model as $T \cdot e_{\text{pos}}$ and compare it with autoregressive decoding.
- Explain why MFU differs between autoregressive decoding and parallel diffusion on GPUs, and how spatial TSUs change $e_{\text{pos}}$.
- Use precision schedules across denoising steps to reduce cost.

## Prerequisites
- Lessons 9.1–9.3: diffusion models and DTMs.
- Lesson 5.8: energy accounting.

## Narrated script

### [00:05.1] Introduction — `manim:S01`

**ES:** Para decidir si la difusión conviene en un hardware dado, hace falta un modelo de costo explícito. La idea central es simple: un modelo de difusión hace T pasos, y en cada uno procesa cada posición de la secuencia. La energía por token es entonces T por la energía de procesar una posición en un paso. Hoy ponemos números para una GPU y para un TSU espacial, con supuestos declarados.

**EN:** To decide whether diffusion pays off on a given hardware, an explicit cost model is needed. The central idea is simple: a diffusion model takes T steps, and in each it processes every position in the sequence. The energy per token is then T times the energy of processing one position in one step. Today we put numbers for a GPU and for a spatial TSU, with stated assumptions.

### [00:31.3] Energy per position on a GPU — `manim:S02`

**ES:** En una GPU, procesar una posición con un modelo de N parámetros cuesta unas 2N operaciones. Con la especificación de una GPU moderna, unos cero coma siete picojulios por operación a pleno rendimiento. Pero la GPU rara vez trabaja a pleno: la fracción útil es el MFU, la utilización de operaciones del modelo. La energía por posición y paso es e_pos = 2N e_FLOP / MFU.

**EN:** On a GPU, processing one position with an N-parameter model costs about 2N operations. With the specification of a modern GPU, about 0.7 picojoules per operation at full throughput. But the GPU rarely runs at full throughput: the useful fraction is the MFU, the model FLOPs utilization. The energy per position and step is e_pos = 2N e_FLOP / MFU.

### [00:60.0] Autoregressive vs diffusion — `manim:S03`

**ES:** La generación autorregresiva produce un token por pasada y está limitada por la memoria: con lotes pequeños, el MFU puede ser de un cinco por ciento. La difusión procesa todas las posiciones en paralelo y puede alcanzar un MFU cercano al cincuenta por ciento, pero repite T veces. Para un modelo de mil millones de parámetros, con estos supuestos, la decodificación autorregresiva cuesta unos veintiocho milijulios por token. La difusión cuesta veintitrés con ocho pasos, noventa y uno con treinta y dos, y trescientos sesenta y dos con ciento veintiocho.

**EN:** Autoregressive generation produces one token per pass and is memory-bound: with small batches, the MFU can be five percent. Diffusion processes all positions in parallel and can reach an MFU near fifty percent, but repeats T times. For a billion-parameter model, under these assumptions, autoregressive decoding costs about twenty-eight millijoules per token. Diffusion costs twenty-three with eight steps, ninety-one with thirty-two, and three hundred sixty-two with one hundred twenty-eight.

### [01:36.2] The break-even number of steps — `manim:S04`

**ES:** El punto de equilibrio es T* = MFU_dif / MFU_AR: con estos números, diez pasos. Por debajo, la difusión gana en energía; por encima, pierde. Por eso en GPU todo se juega en reducir los pasos con buenos muestreadores y destilación. El número es tan bueno como los supuestos: el MFU real depende del lote, la longitud y la implementación, y hay que medirlo.

**EN:** The break-even point is T* = MFU_dif / MFU_AR: with these numbers, ten steps. Below it, diffusion wins in energy; above it, it loses. That is why on GPUs everything hinges on reducing steps with good samplers and distillation. The number is only as good as the assumptions: the real MFU depends on batch, length and implementation, and must be measured.

### [02:01.6] Spatial TSUs — `manim:S05`

**ES:** En un TSU espacial, cada variable tiene su propio circuito, así que no hay MFU que perder: la energía por posición y paso es el número de celdas por posición, por los barridos, por la energía de cada celda. En la DTM de la lección anterior, unos veinte nanojulios por imagen de setecientos ochenta y cuatro píxeles son unos veinticinco picojulios por píxel, o unos tres picojulios por píxel y paso. La difusión deja de penalizar tanto los pasos, porque cada paso es dinámica física barata.

**EN:** In a spatial TSU, each variable has its own circuit, so there is no MFU to lose: the energy per position and step is the number of cells per position, times the sweeps, times the energy of each cell. In the DTM of the previous lesson, about twenty nanojoules per seven-hundred-eighty-four-pixel image is about twenty-five picojoules per pixel, or about three picojoules per pixel and step. Diffusion stops penalizing steps so heavily, because each step is cheap physical dynamics.

### [02:34.2] Precision schedules — `manim:S06`

**ES:** Una última palanca: no todos los pasos necesitan la misma precisión. Los primeros, cuando la muestra es casi puro ruido, toleran menos bits; los últimos, que fijan los detalles, necesitan más. Si el costo por paso crece con los bits, ejecutar la primera mitad de treinta y dos pasos a la mitad de bits ahorra un veinticinco por ciento. Es un supuesto a validar con la calidad de las muestras.

**EN:** One last lever: not all steps need the same precision. The first ones, when the sample is almost pure noise, tolerate fewer bits; the last ones, which fix the details, need more. If cost per step grows with bits, running the first half of thirty-two steps at half the bits saves twenty-five percent. It is an assumption to validate against sample quality.

### [02:58.5] Applications — `slide`

**ES:** Usa este modelo para reportar julios por token con todos los supuestos explícitos, calcular el número de pasos de equilibrio antes de elegir difusión en GPU, y estimar la energía en TSU. En el laboratorio trece barrerás el número de pasos y reportarás calidad y energía proyectada.

**EN:** Use this model to report joules per token with all assumptions explicit, compute the break-even number of steps before choosing diffusion on a GPU, and estimate the energy on TSUs. In lab thirteen you will sweep the number of steps and report quality and projected energy.

### [03:17.0] Common mistakes — `slide`

**ES:** Errores comunes: suponer el rendimiento pico de la GPU. Comparar difusión y autorregresión con calidades distintas. Olvidar que la difusión repite cada posición T veces. Y mezclar energías estimadas de TSU con energías medidas de GPU.

**EN:** Common mistakes: assuming the GPU's peak throughput. Comparing diffusion and autoregression at different qualities. Forgetting that diffusion repeats each position T times. And mixing estimated TSU energies with measured GPU energies.

### [03:34.2] Summary — `manim:S09`

**ES:** En resumen: la energía por token de la difusión es T por la energía por posición y paso. En GPU, la difusión gana utilización frente a la autorregresión pero paga por cada paso, con un equilibrio cerca de diez pasos con nuestros supuestos. En un TSU espacial la energía por paso es pequeña y no depende de la utilización. Y los calendarios de precisión ahorran en los pasos ruidosos.

**EN:** In summary: the energy per token of diffusion is T times the energy per position and step. On a GPU, diffusion gains utilization over autoregression but pays for each step, with a break-even near ten steps under our assumptions. On a spatial TSU the energy per step is small and does not depend on utilization. And precision schedules save on the noisy steps.

### [03:59.7] Self-assessment — `slide`

**ES:** Para practicar: calcula la energía por posición para un modelo de siete mil millones. Calcula el equilibrio con otra utilización. Calcula la energía por posición en un TSU. Y explica por qué los primeros pasos toleran menos bits.

**EN:** To practice: compute the energy per position for a seven-billion model. Compute the break-even with another utilization. Compute the energy per position on a TSU. And explain why the first steps tolerate fewer bits.

## Key equations
- $$E_{\text{token}} \approx T\,e_{\text{pos}},\qquad e_{\text{pos}}^{\text{GPU}} = \frac{2N\,e_{\text{FLOP}}}{\text{MFU}}$$ — Diffusion cost per token on a GPU (forward pass ≈ 2N FLOPs per position).
- $$T^\ast = \frac{\text{MFU}_{\text{diff}}}{\text{MFU}_{\text{AR}}}\quad (\approx 10\ \text{for } 50\,\%\ /\ 5\,\%)$$ — Break-even number of denoising steps versus autoregressive decoding.
- $$e_{\text{pos}}^{\text{TSU}} = n_{\text{cells}}\,K\,E_{\text{cell}}$$ — Spatial TSU: no utilization loss.

## Summary
- E_token ≈ T · e_pos; GPU e_pos = 2N e_FLOP / MFU [E].
- 1B params, 0.71 pJ/FLOP: AR (MFU 5 %) 28 mJ/token; diffusion (MFU 50 %) 23 / 91 / 362 mJ for T = 8 / 32 / 128 [E].
- Break-even T* ≈ 10; spatial TSU (DTM): ~3 pJ per pixel per step [E].
- Precision schedule: half bits on first half of steps → −25 % (if cost ∝ bits).

## Further reading
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, 2025.
- S. S. Sahoo et al., Simple and effective masked diffusion language models, NeurIPS (2024).
- A. Chowdhery et al., PaLM: scaling language modeling with Pathways (MFU definition), JMLR 24 (2023).
