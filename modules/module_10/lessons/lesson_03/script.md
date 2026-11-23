# Lesson 10.3 — DyT normalization

**Unit:** Unit 10 — Thermodynamic language models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define Dynamic Tanh, $\mathrm{DyT}(x) = \gamma\tanh(\alpha x) + \beta$, as a drop-in replacement for layer normalization.
- Show that the mean output of a pbit is exactly $\tanh(\beta u)$, so DyT maps to averaged pbits.
- Quantify the sampling error of the average: $\propto 1/\sqrt S$.

## Prerequisites
- Lesson 4.5: the pbit and its sigmoid response.
- Lesson 10.1: normalization in the transformer block.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** La normalización de capa calcula la media y la varianza de cada vector de activaciones: dos reducciones globales sobre toda la dimensión del modelo. En hardware con conectividad local, sumar sobre miles de componentes es caro. En dos mil veinticinco, Zhu y colaboradores mostraron que se puede reemplazar por algo mucho más simple, una tangente hiperbólica escalada, y esa tangente resulta ser justo lo que un pbit calcula en promedio.

**EN:** Layer normalization computes the mean and variance of each activation vector: two global reductions over the whole model dimension. On hardware with local connectivity, summing over thousands of components is expensive. In twenty twenty-five, Zhu and colleagues showed it can be replaced by something much simpler, a scaled hyperbolic tangent, and that tangent turns out to be exactly what a pbit computes on average.

### [00:32.3] Dynamic Tanh — `manim:S02`

**ES:** La tangente dinámica, DyT, aplica a cada componente γ tanh(α x) + β, con un escalar α aprendido y vectores γ y β por canal. La motivación es empírica: en transformers entrenados, la relación entre la entrada y la salida de la normalización de capa tiene forma de S, lineal en el centro y saturada en los extremos. DyT reproduce esa forma sin calcular estadísticas, y los autores reportan calidad comparable en visión y lenguaje.

**EN:** Dynamic tanh, DyT, applies γ tanh(α x) + β to each component, with a learned scalar α and per-channel vectors γ and β. The motivation is empirical: in trained transformers, the relationship between the input and output of layer normalization is S-shaped, linear in the center and saturated at the extremes. DyT reproduces that shape without computing statistics, and the authors report comparable quality in vision and language.

### [01:04.5] The pbit computes tanh — `manim:S03`

**ES:** Recordemos el pbit: con entrada u, sale más uno con probabilidad σ(2βu) y menos uno en caso contrario. Su salida media es 2σ(2βu) − 1 = tanh(βu), exactamente. Un pbit con ganancia β = α es, en promedio, una unidad DyT. La normalización se vuelve un fenómeno físico del dispositivo, sin reducciones globales.

**EN:** Recall the pbit: with input u, it outputs plus one with probability σ(2βu) and minus one otherwise. Its mean output is 2σ(2βu) − 1 = tanh(βu), exactly. A pbit with gain β = α is, on average, a DyT unit. Normalization becomes a physical phenomenon of the device, with no global reductions.

### [01:32.0] Averaging error — `manim:S04`

**ES:** Pero un pbit da una muestra binaria, no la media. Para estimar la tangente hay que promediar S muestras, y el error baja como uno sobre raíz de S. Lo medimos: con una muestra, el error cuadrático medio es cero coma cinco cuatro; con dieciséis, cero coma uno cuatro; con doscientas cincuenta y seis, cero coma cero tres. Cada factor cuatro en muestras divide el error por dos.

**EN:** But a pbit gives a binary sample, not the mean. To estimate the tangent one must average S samples, and the error falls as one over root S. We measure it: with one sample, the root-mean-square error is 0.54; with sixteen, 0.14; with two hundred fifty-six, 0.03. Each factor of four in samples halves the error.

### [01:57.3] Do we even need the average? — `manim:S05`

**ES:** Aquí aparece una pregunta de diseño, si hace falta promediar. Si la capa siguiente también es estocástica y suma muchas entradas, el ruido de cada muestra se promedia de forma natural en esa suma, como en las redes de pbits de la unidad cuatro. Muchas veces basta con pocas muestras, o con una, siempre que el entrenamiento tenga en cuenta el ruido. La lección diez punto cinco cuantifica cuántos bits efectivos da cada número de muestras.

**EN:** Here a design question appears, whether we need to average. If the next layer is also stochastic and sums many inputs, the noise of each sample averages out naturally in that sum, as in the pbit networks of unit four. Often a few samples, or even one, suffice, as long as training accounts for the noise. Lesson 10.5 quantifies how many effective bits each number of samples gives.

### [02:24.6] Costs compared — `manim:S06`

**ES:** Comparemos. La normalización de capa necesita, por token, dos reducciones sobre toda la dimensión del modelo, una raíz cuadrada y una división. DyT necesita, por componente, una multiplicación, una tangente y una suma, sin comunicación entre componentes. En un TSU, la tangente la hace el propio pbit. Por eso los modelos de lenguaje para chips probabilísticos, como Z1T, usan DyT en lugar de normalización de capa.

**EN:** Let's compare. Layer normalization needs, per token, two reductions over the whole model dimension, a square root and a division. DyT needs, per component, one multiplication, one tangent and one addition, with no communication between components. On a TSU, the tangent is done by the pbit itself. That is why language models for probabilistic chips, such as Z1T, use DyT instead of layer normalization.

### [02:54.0] Applications — `slide`

**ES:** En la práctica, reemplaza la normalización por DyT y ajusta el valor inicial de α; mapea cada unidad a un pbit con ganancia igual a α; y entrena con el ruido del muestreo incluido. En el laboratorio veintinueve lo harás en un transformer pequeño.

**EN:** In practice, replace normalization with DyT and tune the initial value of α; map each unit to a pbit with gain equal to α; and train with the sampling noise included. In lab twenty-nine you will do it on a small transformer.

### [03:11.1] Common mistakes — `slide`

**ES:** Errores comunes: creer que DyT normaliza, cuando solo acota. Confundir la sigmoide del pbit, cuyo argumento lleva un factor dos. Promediar pocas muestras sin incluir el ruido en el entrenamiento. Y olvidar que α se aprende y es sensible a la inicialización.

**EN:** Common mistakes: believing DyT normalizes, when it only bounds. Confusing the pbit's sigmoid, whose argument has a factor of two. Averaging few samples without including the noise in training. And forgetting that α is learned and sensitive to initialization.

### [03:29.3] Summary — `manim:S09`

**ES:** En resumen, DyT reemplaza la normalización de capa por γ tanh(α x) + β, sin reducciones globales. La salida media de un pbit es exactamente una tangente hiperbólica, así que DyT es nativa de un TSU. El precio es el ruido de muestreo, que cae como uno sobre raíz de S y que el entrenamiento puede absorber.

**EN:** In summary: DyT replaces layer normalization with γ tanh(α x) + β, with no global reductions. The mean output of a pbit is exactly a hyperbolic tangent, so DyT is native to a TSU. The price is sampling noise, which falls as one over root S and which training can absorb.

### [03:52.7] Self-assessment — `slide`

**ES:** Para practicar: demuestra la identidad entre la sigmoide y la tangente. Calcula la varianza de una muestra de pbit. Calcula las muestras para un error de cero coma cero cinco. Y explica por qué DyT es más barata que la normalización de capa en hardware local.

**EN:** To practice: prove the identity between the sigmoid and the tangent. Compute the variance of a pbit sample. Compute the samples for an error of 0.05. And explain why DyT is cheaper than layer normalization on local hardware.

## Key equations
- $$\mathrm{DyT}(x) = \gamma\odot\tanh(\alpha x) + \beta$$ — Dynamic Tanh (Zhu et al. 2025).
- $$\mathbb E[m] = 2\sigma(2\beta u) - 1 = \tanh(\beta u),\qquad \mathrm{Var}(m) = 1 - \tanh^2(\beta u)$$ — A pbit's mean output is tanh: DyT on hardware.
- $$\mathrm{rms}\Big(\tfrac1S\sum_{s=1}^S m_s - \tanh(\beta u)\Big) = \sqrt{\frac{1 - \tanh^2(\beta u)}{S}}$$ — Averaging error.

## Summary
- DyT = γ tanh(αx) + β: no mean/variance reductions.
- pbit mean = tanh(βu) exactly → DyT is native to TSUs.
- Averaging S samples: rms error 0.54 (S = 1) → 0.14 (16) → 0.034 (256) [S].
- Next layers can average the noise; train with noise in the loop.

## Further reading
- J. Zhu et al., Transformers without normalization, CVPR (2025).
- J. L. Ba, J. R. Kiros and G. E. Hinton, Layer normalization, arXiv:1607.06450 (2016).
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
