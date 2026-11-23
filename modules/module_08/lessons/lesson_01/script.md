# Lesson 8.1 — Information geometry and the natural gradient

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the Fisher information as the local metric of the KL divergence: $\mathrm{KL} \approx \tfrac12 d^\top F d$.
- Derive the natural gradient $\tilde g = F^{-1}\nabla\ell$ as steepest descent in distribution space.
- Compare gradient descent and natural gradient descent on a Gaussian fit.

## Prerequisites
- Lesson 0.3: KL divergence.
- Lesson 6.1: solving linear systems thermodynamically.

## Narrated script

### [00:06.0] Introduction — `manim:S01`

**ES:** El descenso de gradiente da pasos en la dirección más empinada, pero mide la distancia en el espacio de parámetros. Y los parámetros son una elección arbitraria: el mismo modelo se puede escribir de mil maneras. Lo que realmente importa es cuánto cambia la distribución que el modelo representa. Medir los pasos así lleva al gradiente natural, y resolverlo exige justo lo que el hardware termodinámico hace bien: un sistema lineal.

**EN:** Gradient descent takes steps in the steepest direction, but it measures distance in parameter space. And parameters are an arbitrary choice: the same model can be written in a thousand ways. What really matters is how much the distribution represented by the model changes. Measuring steps that way leads to the natural gradient, and solving it requires exactly what thermodynamic hardware does well: a linear system.

### [00:32.9] Fisher information as a metric — `manim:S02`

**ES:** Si movemos los parámetros de θ a θ + d, la divergencia KL entre la distribución vieja y la nueva es, para pasos pequeños, ½ dᵀ F d. La matriz F es la información de Fisher: el valor esperado del producto exterior del gradiente del logaritmo de la verosimilitud. Es una métrica: dice qué tan lejos están dos modelos cercanos, medidos por sus predicciones, no por sus números.

**EN:** If we move the parameters from θ to θ + d, the KL divergence between the old and new distribution is, for small steps, ½ dᵀ F d. The matrix F is the Fisher information: the expected outer product of the gradient of the log-likelihood. It is a metric: it says how far apart two nearby models are, measured by their predictions, not by their numbers.

### [00:59.7] The natural gradient — `manim:S03`

**ES:** El gradiente natural es la dirección de máximo descenso de la pérdida cuando el tamaño del paso se mide con la KL. Resolviendo ese problema con multiplicadores de Lagrange sale g̃ = F⁻¹ ∇ℓ. La regla de actualización es θ ← θ − η F⁻¹ ∇ℓ. Una consecuencia importante: en el límite de pasos pequeños, el gradiente natural no depende de cómo parametricemos el modelo.

**EN:** The natural gradient is the direction of steepest descent of the loss when the step size is measured with the KL. Solving that problem with Lagrange multipliers gives g̃ = F⁻¹ ∇ℓ. The update rule is θ ← θ − η F⁻¹ ∇ℓ. An important consequence: in the small-step limit, the natural gradient does not depend on how we parametrize the model.

### [01:27.6] A Gaussian example — `manim:S04`

**ES:** Ajustemos una gaussiana con media μ y desviación σ a datos con media dos y desviación cero coma uno, empezando en cero y uno. La información de Fisher es diagonal: uno sobre sigma al cuadrado para la media, y dos sobre sigma al cuadrado para la desviación. Cuando σ se achica, la pérdida se vuelve muy empinada y el descenso de gradiente necesita pasos diminutos. El gradiente natural multiplica por σ² y corrige exactamente ese efecto.

**EN:** Let's fit a Gaussian with mean μ and standard deviation σ to data with mean two and standard deviation 0.1, starting at zero and one. The Fisher information is diagonal: one over sigma squared for the mean, and two over sigma squared for the standard deviation. When σ shrinks, the loss becomes very steep and gradient descent needs tiny steps. The natural gradient multiplies by σ² and corrects exactly that effect.

### [01:58.0] GD versus NGD — `manim:S05`

**ES:** El resultado: con la mejor tasa de aprendizaje fija, el descenso de gradiente necesita ciento seis pasos para quedar a una milésima del óptimo. El gradiente natural, con tasa uno, lo logra en siete pasos. Las trayectorias también son distintas: el gradiente ordinario da una larga curva y luego avanza a pasos cortos por el valle estrecho; el natural corrige la media en un solo paso y después ajusta la desviación en pocos pasos.

**EN:** The result: with the best fixed learning rate, gradient descent needs one hundred six steps to get within one thousandth of the optimum. The natural gradient, with rate one, does it in seven steps. The trajectories are also different: ordinary gradient makes a long arc and then creeps along the narrow valley; the natural one fixes the mean in a single step and then adjusts the deviation in a few steps.

### [02:26.6] The cost: a linear system — `manim:S06`

**ES:** ¿Por qué no se usa siempre? Porque F es una matriz de N × N, con N el número de parámetros, que pueden ser millones. Formarla cuesta N² y resolver el sistema, N³. Por eso los optimizadores populares usan aproximaciones baratas, como Adam, que usa solo la diagonal del Fisher empírico. Las próximas lecciones muestran cómo un dispositivo termodinámico resuelve el sistema completo de forma eficiente.

**EN:** Why isn't it always used? Because F is an N × N matrix, with N the number of parameters, which can be millions. Forming it costs N² and solving the system, N³. That is why popular optimizers use cheap approximations, such as Adam, which uses only the diagonal of the empirical Fisher. The next lessons show how a thermodynamic device solves the full system efficiently.

### [02:54.3] Applications — `slide`

**ES:** El gradiente natural aparece en el entrenamiento de redes neuronales, en el gradiente natural de políticas del aprendizaje por refuerzo, y en la inferencia variacional. En esta unidad veremos cómo hacerlo asequible: gradiente conjugado, Woodbury, la versión termodinámica y K-FAC.

**EN:** The natural gradient appears in neural network training, in the natural policy gradient of reinforcement learning, and in variational inference. In this unit we will see how to make it affordable: conjugate gradient, Woodbury, the thermodynamic version and K-FAC.

### [03:12.4] Common mistakes — `slide`

**ES:** Errores comunes: confundir el Fisher con el hessiano. Olvidar el amortiguamiento, cuando el Fisher es singular porque hay menos datos que parámetros. Esperar invariancia exacta con pasos finitos. Y creer que Adam es un método de gradiente natural, cuando usa solo una diagonal.

**EN:** Common mistakes: confusing the Fisher with the Hessian. Forgetting damping, when the Fisher is singular because there are fewer data than parameters. Expecting exact invariance with finite steps. And believing Adam is a natural-gradient method, when it uses only a diagonal.

### [03:30.9] Summary — `manim:S09`

**ES:** En resumen: la información de Fisher es la métrica local de la KL, y el gradiente natural F⁻¹ ∇ℓ es el descenso más empinado en el espacio de distribuciones. En el ajuste gaussiano, siete pasos frente a ciento seis. Su costo es un sistema lineal de tamaño N, la tarea que el hardware termodinámico sabe resolver.

**EN:** In summary: the Fisher information is the local metric of the KL, and the natural gradient F⁻¹ ∇ℓ is steepest descent in distribution space. In the Gaussian fit, seven steps against one hundred six. Its cost is a linear system of size N, the task thermodynamic hardware knows how to solve.

### [03:52.9] Self-assessment — `slide`

**ES:** Para practicar: deduce la aproximación cuadrática de la KL. Calcula el Fisher de la gaussiana. Deduce el gradiente natural con un multiplicador de Lagrange. Y di qué parte del Fisher usa Adam.

**EN:** To practice: derive the quadratic approximation of the KL. Compute the Fisher of the Gaussian. Derive the natural gradient with a Lagrange multiplier. And say which part of the Fisher Adam uses.

## Key equations
- $$\mathrm{KL}\big(p_{\theta+d}\,\|\,p_\theta\big) = \tfrac12\,d^\top F d + O(\|d\|^3),\qquad F = \mathbb E\big[\nabla\log p\,\nabla\log p^\top\big]$$ — Fisher information as the local metric of the KL divergence.
- $$\tilde g = F^{-1}\nabla\ell,\qquad \theta_{k+1} = \theta_k - \eta\,F^{-1}\nabla\ell$$ — Natural gradient and NGD update.
- $$\mathcal N(\mu, \sigma^2):\ F = \mathrm{diag}\big(1/\sigma^2,\ 2/\sigma^2\big)$$ — Fisher of a Gaussian in the $(\mu, \sigma)$ parametrization.

## Summary
- Fisher information = local metric of the KL.
- Natural gradient F⁻¹∇ℓ: steepest descent in distribution space, parametrization-invariant (small steps).
- Gaussian fit to 10⁻³: GD 106 steps (best rate) vs NGD 7 steps [S].
- Cost: N × N linear system — the thermodynamic primitive.

## Further reading
- [36] S.-I. Amari, Natural gradient works efficiently in learning, Neural Computation 10, 251 (1998).
- [37] J. Martens, New insights and perspectives on the natural gradient method, JMLR 21 (2020).
- [40] K. Donatella et al., Thermodynamic natural gradient descent, 2024.
