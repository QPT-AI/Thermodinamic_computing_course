# Lesson 9.1 — Diffusion models

**Unit:** Unit 9 — Thermodynamic generative models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe a diffusion model as a forward noising SDE and a learned reverse SDE driven by the score $\nabla\log p_t$.
- Relate DDPM's noise prediction to score matching, and the reverse SDE to the probability-flow ODE.
- Measure how sample quality depends on the sampler and the number of steps.

## Prerequisites
- Lesson 2.6: Langevin dynamics and Fokker–Planck.
- Lesson 6.1: the Ornstein–Uhlenbeck process.

## Narrated script

### [00:04.5] Introduction — `manim:S01`

**ES:** Los modelos de difusión generan imágenes, audio y video destruyendo los datos con ruido poco a poco y aprendiendo a deshacer ese proceso. Son, en el fondo, dinámica de Langevin dirigida por una red neuronal. Por eso encajan tan bien con el cómputo termodinámico: el hardware ya sabe hacer dinámica estocástica. Hoy vemos la teoría y medimos cuánto importan el muestreador y el número de pasos.

**EN:** Diffusion models generate images, audio and video by destroying data with noise little by little and learning to undo that process. Deep down, they are Langevin dynamics driven by a neural network. That is why they fit thermodynamic computing so well: the hardware already knows how to do stochastic dynamics. Today we see the theory and measure how much the sampler and the number of steps matter.

### [00:30.0] The forward process — `manim:S02`

**ES:** El proceso hacia adelante es un proceso de Ornstein-Uhlenbeck: dx = −x dt + √2 dW. Partiendo de un dato x₀, en el tiempo t la muestra es e^(−t) x₀ + √(1 − e^(−2t)) ε. Con tiempo suficiente, toda la estructura se borra y queda una gaussiana estándar. En nuestro ejemplo, dos modos en más y menos dos se funden en una sola campana.

**EN:** The forward process is an Ornstein-Uhlenbeck process: dx = −x dt + √2 dW. Starting from a data point x₀, at time t the sample is e^(−t) x₀ + √(1 − e^(−2t)) ε. Given enough time, all structure is erased and a standard Gaussian remains. In our example, two modes at plus and minus two merge into a single bell.

### [00:59.3] Reversing time: the score — `manim:S03`

**ES:** Anderson demostró en mil novecientos ochenta y dos que el proceso tiene un reverso en el tiempo, otra ecuación estocástica cuya deriva incluye el gradiente del logaritmo de la densidad, ∇ log p_t, llamado score. Si conocemos el score en cada tiempo, podemos partir de ruido y correr el tiempo hacia atrás para obtener datos. Todo el aprendizaje consiste en estimar ese campo.

**EN:** Anderson showed in nineteen eighty-two that the process has a time reversal, another stochastic equation whose drift includes the gradient of the log-density, ∇ log p_t, called the score. If we know the score at every time, we can start from noise and run time backwards to obtain data. All the learning consists of estimating that field.

### [01:23.9] DDPM and score matching — `manim:S04`

**ES:** El DDPM entrena una red que predice el ruido ε añadido a un dato ruidoso. Resulta que predecir el ruido equivale a estimar el score: ∇ log p_t ≈ −ε̂/σ_t. Eso es el emparejamiento de score con eliminación de ruido. La pérdida es un simple error cuadrático, estable y fácil de escalar, una de las razones del éxito de estos modelos.

**EN:** DDPM trains a network that predicts the noise ε added to a noisy data point. It turns out that predicting the noise is equivalent to estimating the score: ∇ log p_t ≈ −ε̂/σ_t. That is denoising score matching. The loss is a simple squared error, stable and easy to scale, one of the reasons these models succeed.

### [01:49.5] SDE and probability-flow ODE — `manim:S05`

**ES:** Hay dos formas de muestrear. La ecuación estocástica inversa añade ruido en cada paso. La ecuación diferencial ordinaria de flujo de probabilidad es determinista y tiene las mismas marginales. En nuestro ejemplo, con el score exacto de una mezcla de dos gaussianas, medimos la distancia de Wasserstein a los datos verdaderos. Con cinco pasos ambas fallan, cerca de cero coma ocho siete. Con cincuenta, la estocástica llega a cero coma uno seis y la ordinaria a cero coma uno uno. Con doscientos, cero coma cero siete y cero coma cero tres.

**EN:** There are two ways to sample. The reverse stochastic equation adds noise at every step. The probability-flow ordinary differential equation is deterministic and has the same marginals. In our example, with the exact score of a mixture of two Gaussians, we measure the Wasserstein distance to the true data. With five steps both fail, near 0.87. With fifty, the stochastic one reaches 0.16 and the ordinary one 0.11. With two hundred, 0.07 and 0.03.

### [02:25.1] Why the number of steps matters — `manim:S06`

**ES:** Cada paso cuesta una evaluación de la red: en una GPU, el costo de generar crece linealmente con el número de pasos. Por eso tanta investigación busca muestreadores de pocos pasos, mejores calendarios de tiempo y destilación. Para el hardware termodinámico la pregunta cambia: si cada paso es una dinámica física barata, ¿cuántos pasos podemos permitirnos? Esa es la idea que desarrollarán los modelos termodinámicos de eliminación de ruido de la lección nueve punto tres.

**EN:** Each step costs one network evaluation: on a GPU, the cost of generating grows linearly with the number of steps. That is why so much research seeks few-step samplers, better time schedules and distillation. For thermodynamic hardware the question changes: if each step is cheap physical dynamics, how many steps can we afford? That is the idea that the denoising thermodynamic models of lesson 9.3 will develop.

### [02:54.9] Applications — `slide`

**ES:** Los modelos de difusión dominan la generación de imágenes, video, audio y moléculas. En la práctica se combinan con muestreadores como DDIM y DPM-Solver, calendarios cuidados, destilación y guía sin clasificador. En el laboratorio doce entrenarás un DDPM pequeño.

**EN:** Diffusion models dominate the generation of images, video, audio and molecules. In practice they are combined with samplers such as DDIM and DPM-Solver, careful schedules, distillation and classifier-free guidance. In lab twelve you will train a small DDPM.

### [03:14.4] Common mistakes — `slide`

**ES:** Errores comunes: confundir el proceso hacia adelante, que es fijo, con el inverso, que se aprende. Olvidar el factor que relaciona ruido y score. Usar una malla de tiempo uniforme, cuando el error se concentra cerca del final. Y comparar muestreadores con distinto número de evaluaciones.

**EN:** Common mistakes: confusing the forward process, which is fixed, with the reverse, which is learned. Forgetting the factor relating noise and score. Using a uniform time grid, when the error concentrates near the end. And comparing samplers with different numbers of evaluations.

### [03:33.3] Summary — `manim:S09`

**ES:** En resumen: un modelo de difusión destruye los datos con un proceso de Ornstein-Uhlenbeck y aprende el score para invertirlo. Predecir el ruido es estimar el score. Se muestrea con la ecuación estocástica inversa o con la ordinaria de flujo de probabilidad, y la calidad depende mucho del número de pasos, que en una GPU es el costo.

**EN:** In summary: a diffusion model destroys data with an Ornstein-Uhlenbeck process and learns the score to reverse it. Predicting the noise is estimating the score. One samples with the reverse stochastic equation or the probability-flow ordinary one, and quality depends strongly on the number of steps, which on a GPU is the cost.

### [03:55.4] Self-assessment — `slide`

**ES:** Para practicar: escribe la marginal del proceso hacia adelante. Demuestra la relación entre ruido y score. Escribe la ecuación inversa y la de flujo de probabilidad. Y explica por qué una malla uniforme desperdicia pasos.

**EN:** To practice: write the marginal of the forward process. Prove the relation between noise and score. Write the reverse equation and the probability-flow one. And explain why a uniform grid wastes steps.

## Key equations
- $$dx = -x\,dt + \sqrt2\,dW,\qquad x_t = e^{-t}x_0 + \sqrt{1 - e^{-2t}}\,\varepsilon$$ — Forward (OU) noising process.
- $$dx = \big[-x - 2\nabla\log p_t(x)\big]dt + \sqrt2\,d\bar W,\qquad \frac{dx}{dt} = -x - \nabla\log p_t(x)$$ — Reverse-time SDE (Anderson) and probability-flow ODE.
- $$\nabla\log p_t(x_t) \approx -\hat\varepsilon_\theta(x_t, t)/\sigma_t,\quad \sigma_t = \sqrt{1-e^{-2t}}$$ — Noise prediction = score estimation (denoising score matching).

## Summary
- Forward OU process erases structure; reverse process needs the score ∇log p_t.
- DDPM noise prediction ≡ denoising score matching.
- Exact-score 1-D test: W₁ 0.87 (5 steps) → 0.07 SDE / 0.03 ODE (200 steps) [S].
- GPU cost ∝ number of steps; thermodynamic hardware changes that calculus.

## Further reading
- J. Ho, A. Jain and P. Abbeel, Denoising diffusion probabilistic models, NeurIPS (2020).
- Y. Song et al., Score-based generative modeling through stochastic differential equations, ICLR (2021).
- B. D. O. Anderson, Reverse-time diffusion equation models, Stoch. Proc. Appl. 12, 313 (1982).
