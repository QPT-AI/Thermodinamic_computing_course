# Lesson 9.3 — Denoising thermodynamic models (DTM)

**Unit:** Unit 9 — Thermodynamic generative models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain the mixing–expressivity tradeoff of monolithic energy-based models.
- Build a DTM: a chain of conditional EBMs, each a denoising step sampled by Gibbs on hardware.
- Use the DTCA energy model $E = T\,K_{\text{mix}}\,L^2 E_{\text{cell}}$ and read the 10,000× claim correctly.

## Prerequisites
- Lessons 9.1–9.2: diffusion models.
- Lessons 4.3 and 5.3: Gibbs sampling and Extropic's TSUs.

## Narrated script

### [00:06.0] Introduction — `manim:S01`

**ES:** Los computadores probabilísticos muestrean modelos basados en energía con gran eficiencia. Pero usar un solo modelo de energía para representar datos reales tiene un problema serio, y Jelinčič y colaboradores, de Extropic, propusieron en dos mil veinticinco una solución inspirada en la difusión: los modelos termodinámicos de eliminación de ruido, o DTM. Hoy vemos el problema, la solución y la cuenta de energía.

**EN:** Probabilistic computers sample energy-based models very efficiently. But using a single energy model to represent real data has a serious problem, and Jelinčič and colleagues, at Extropic, proposed in twenty twenty-five a solution inspired by diffusion: denoising thermodynamic models, or DTMs. Today we see the problem, the solution and the energy accounting.

### [00:32.7] The mixing–expressivity tradeoff — `manim:S02`

**ES:** Los datos reales tienen modos separados. Un modelo de energía monolítico que los representa bien necesita valles profundos separados por montañas altas, y un muestreador local, como Gibbs o Langevin, cruza esas montañas con probabilidad exponencialmente pequeña. Más expresividad significa mezcla más lenta. Lo medimos con una mezcla de dos modos, con el ochenta por ciento del peso a la derecha: partiendo de una distribución ancha, el muestreo monolítico se queda en un cincuenta y uno por ciento aun con ocho mil pasos.

**EN:** Real data have separated modes. A monolithic energy model that represents them well needs deep valleys separated by high mountains, and a local sampler, such as Gibbs or Langevin, crosses those mountains with exponentially small probability. More expressivity means slower mixing. We measure it with a two-mode mixture, with eighty percent of the weight on the right: starting from a broad distribution, monolithic sampling stays at fifty-one percent even with eight thousand steps.

### [01:06.3] Denoising with EBMs — `manim:S03`

**ES:** La solución es no pedirle todo a un solo modelo. Como en la difusión, se añade ruido a los datos en T pasos, y cada paso inverso se representa con un modelo de energía condicional: la probabilidad de la versión menos ruidosa dada la más ruidosa. Cada uno de esos condicionales es casi unimodal y fácil de muestrear. La complejidad se construye a lo largo de la cadena. En nuestro ejemplo, con treinta y dos niveles y cuarenta pasos cada uno, la fracción en el modo derecho sube al setenta y cinco por ciento, acercándose al ochenta real.

**EN:** The solution is not to ask everything of a single model. As in diffusion, noise is added to the data in T steps, and each reverse step is represented by a conditional energy model: the probability of the less noisy version given the noisier one. Each of those conditionals is almost unimodal and easy to sample. Complexity is built up along the chain. In our example, with thirty-two levels and forty steps each, the fraction in the right mode rises to seventy-five percent, approaching the true eighty.

### [01:40.4] The DTCA hardware — `manim:S04`

**ES:** La arquitectura propuesta, DTCA, implementa cada condicional como una máquina de Boltzmann dispersa en una rejilla de setenta por setenta variables binarias, cada una conectada a doce vecinas, con algunas variables para los datos y el resto latentes. Cada nodo es un generador de bits aleatorios hecho solo de transistores, con respuesta sigmoidal medida en laboratorio y un tiempo de decorrelación de unos cien nanosegundos. La rejilla es bipartita, así que un barrido de Gibbs completo dura unos dos tiempos de decorrelación.

**EN:** The proposed architecture, DTCA, implements each conditional as a sparse Boltzmann machine on a seventy-by-seventy grid of binary variables, each connected to twelve neighbors, with some variables for the data and the rest latent. Each node is an all-transistor random bit generator, with a sigmoidal response measured in the lab and a decorrelation time of about one hundred nanoseconds. The grid is bipartite, so a full Gibbs sweep takes about two decorrelation times.

### [02:13.9] Energy accounting — `manim:S05`

**ES:** El modelo de energía es E = T K_mix L² E_cell: número de pasos de eliminación de ruido, por barridos de Gibbs, por número de celdas, por la energía de cada celda, estimada en unos dos femtojulios. Con ocho pasos, doscientos cincuenta barridos y setenta por setenta celdas, son unos veinte nanojulios por muestra, y unos cero coma cuatro milisegundos. Con esa cuenta, los autores estiman igualar la calidad de modelos en GPU sobre Fashion-MNIST binarizado con unas diez mil veces menos energía.

**EN:** The energy model is E = T K_mix L² E_cell: number of denoising steps, times Gibbs sweeps, times number of cells, times the energy of each cell, estimated at about two femtojoules. With eight steps, two hundred fifty sweeps and seventy-by-seventy cells, that is about twenty nanojoules per sample, and about 0.4 milliseconds. With that accounting, the authors estimate matching the quality of GPU models on binarized Fashion-MNIST with about ten thousand times less energy.

### [02:49.2] Reading the claim — `manim:S06`

**ES:** ¿Cómo leer esa cifra? Combina mediciones reales del generador de bits con modelos físicos y simulaciones: es una estimación, no la medición de un chip completo. La energía de la GPU se calcula dividiendo operaciones por la especificación del fabricante, lo que la subestima. Y el banco de prueba es pequeño. Para tareas más grandes, los autores combinan un DTM con una red neuronal: en CIFAR-diez igualan a un modelo puramente neuronal usando una red diez veces más pequeña. Prometedor, y todavía por demostrar en hardware completo.

**EN:** How to read that figure? It combines real measurements of the bit generator with physical models and simulations: it is an estimate, not a measurement of a complete chip. The GPU energy is computed by dividing operations by the manufacturer's specification, which underestimates it. And the benchmark is small. For larger tasks, the authors combine a DTM with a neural network: on CIFAR-ten they match a purely neural model using a network ten times smaller. Promising, and still to be demonstrated on complete hardware.

### [03:24.3] Applications — `slide`

**ES:** Los DTM sirven para modelado generativo en hardware probabilístico; durante el entrenamiento, una penalización adaptativa de correlación mantiene los condicionales fáciles de mezclar; y para datos más grandes se combinan con redes neuronales. En el laboratorio catorce entrenarás un DTM pequeño en THRML.

**EN:** DTMs serve for generative modeling on probabilistic hardware; during training, an adaptive correlation penalty keeps the conditionals easy to mix; and for larger data they are combined with neural networks. In lab fourteen you will train a small DTM in THRML.

### [03:46.0] Common mistakes — `slide`

**ES:** Errores comunes: usar un modelo monolítico para datos multimodales y confiar en cadenas cortas. Usar muy pocos pasos, con lo que los condicionales vuelven a ser multimodales. Confundir el tiempo de decorrelación del hardware con el número de barridos. Y citar las diez mil veces como si fuera una medición de un chip.

**EN:** Common mistakes: using a monolithic model for multimodal data and trusting short chains. Using too few steps, so the conditionals become multimodal again. Confusing the hardware decorrelation time with the number of sweeps. And quoting the ten thousand times as if it were a chip measurement.

### [04:05.8] Summary — `manim:S09`

**ES:** En resumen: un modelo de energía monolítico mezcla cada vez peor a medida que se vuelve expresivo. Un DTM encadena modelos condicionales fáciles, como pasos de difusión, y cada uno se muestrea con Gibbs en una rejilla de transistores. La energía se estima con T K_mix L² E_cell, y la ventaja de diez mil veces es una estimación prometedora sobre un banco pequeño.

**EN:** In summary: a monolithic energy model mixes worse and worse as it becomes expressive. A DTM chains easy conditional models, like diffusion steps, and each one is sampled with Gibbs on a transistor grid. Energy is estimated with T K_mix L² E_cell, and the ten-thousand-fold advantage is a promising estimate on a small benchmark.

### [04:31.1] Self-assessment — `slide`

**ES:** Para practicar: explica por qué un muestreador local mezcla lento. Escribe la energía de un condicional. Calcula la energía para cuatro pasos. Y enumera tres advertencias sobre la estimación de diez mil veces.

**EN:** To practice: explain why a local sampler mixes slowly. Write the energy of a conditional. Compute the energy for four steps. And list three caveats about the ten-thousand-fold estimate.

## Key equations
- $$P(x_{t-1}\mid x_t) \propto e^{-E^{\theta}_{t-1}(x_{t-1})}\,q(x_t\mid x_{t-1})$$ — Each denoising step is a conditional EBM (prior energy × forward kernel).
- $$E = T\,K_{\text{mix}}\,L^2\,E_{\text{cell}},\quad E_{\text{cell}} = E_{\text{rng}} + E_{\text{bias}} + E_{\text{clock}} + E_{\text{comm}} \approx 2\ \text{fJ}$$ — DTCA energy model per sample (Jelinčič et al.).
- $$t_{\text{sample}} \approx T\,K_{\text{mix}}\,2\tau_0,\quad \tau_0 \approx 100\ \text{ns}$$ — Time per sample with a bipartite (two-color) grid.

## Summary
- Mixing–expressivity tradeoff: monolithic EBM stuck at 51 % (target 80 %) [S].
- DTM: chain of easy conditional EBMs; 32 levels × 40 steps → 75 % [S].
- DTCA: 70×70 sparse Boltzmann machines, degree 12, all-transistor RNG (τ₀ ≈ 100 ns).
- E ≈ 8·250·4900·2 fJ ≈ 20 nJ/sample; ~10⁴× vs GPU on binarized Fashion-MNIST [E].

## Further reading
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, arXiv:2510.23972 (2025).
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- J. Ho, A. Jain and P. Abbeel, Denoising diffusion probabilistic models, NeurIPS (2020).
