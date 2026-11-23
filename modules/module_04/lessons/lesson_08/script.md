# Lesson 4.8 — RBMs and contrastive divergence

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write the restricted Boltzmann machine $E(v,h) = -v^\top W h - b^\top v - c^\top h$ and its factorized conditionals.
- Train with contrastive divergence CD-$k$ and persistent CD, and understand their bias.
- Place deep belief networks, wake–sleep and Helmholtz machines in context.

## Prerequisites
- Lesson 4.7: Boltzmann machine learning rule.
- Lesson 4.3: block Gibbs.

## Narrated script

### [00:06.4] Introduction — `manim:S01`

**ES:** La máquina de Boltzmann general es difícil de entrenar: cada paso exige muestras de equilibrio de una red totalmente conectada. En dos mil dos, Hinton propuso dos simplificaciones que la volvieron práctica. Restringir la arquitectura, y no esperar al equilibrio. El resultado, la máquina de Boltzmann restringida entrenada con divergencia contrastiva, impulsó el renacimiento del aprendizaje profundo a mediados de los dos mil.

**EN:** The general Boltzmann machine is hard to train: every step requires equilibrium samples from a fully connected network. In 2002, Hinton proposed two simplifications that made it practical. Restrict the architecture, and don't wait for equilibrium. The result, the restricted Boltzmann machine trained with contrastive divergence, drove the revival of deep learning in the mid-2000s.

### [00:32.9] The restricted architecture — `manim:S02`

**ES:** Una RBM tiene una capa visible y una capa oculta, con conexiones solo entre capas, nunca dentro de una capa. La energía es E = −vᵀWh − bᵀv − cᵀh. Como el grafo es bipartito, dadas las visibles, las ocultas son independientes entre sí, y al revés. Cada condicional es un producto de sigmoides: p(h_j = 1 . Es un grafo de dos colores: el Gibbs por bloques es perfecto aquí.

**EN:** An RBM has a visible layer and a hidden layer, with connections only between layers, never within a layer. The energy is E = −vᵀWh − bᵀv − cᵀh. Since the graph is bipartite, given the visible units the hidden ones are independent of each other, and vice versa. Each conditional is a product of sigmoids: p(h_j = 1 | v) = σ(c_j + vᵀW_j). It is a two-colored graph: block Gibbs is perfect here.

### [01:13.1] Contrastive divergence — `manim:S03`

**ES:** La regla exacta sigue siendo correlaciones de los datos menos correlaciones del modelo. La idea de la divergencia contrastiva es aproximar el término del modelo empezando la cadena de Gibbs en un dato y dando solo k pasos, en lugar de esperar al equilibrio. Con k igual a uno: dato, ocultas, reconstrucción, ocultas otra vez. El gradiente queda sesgado, pero tiene poca varianza y es muy barato. En la variante persistente, la cadena no se reinicia en los datos: sigue corriendo entre pasos de aprendizaje.

**EN:** The exact rule is still data correlations minus model correlations. The idea of contrastive divergence is to approximate the model term by starting the Gibbs chain at a data point and taking only k steps, instead of waiting for equilibrium. With k equal to one: data, hidden, reconstruction, hidden again. The gradient is biased, but it has low variance and is very cheap. In the persistent variant, the chain is not restarted at the data: it keeps running between learning steps.

### [01:46.1] Training in action — `manim:S04`

**ES:** Entrenemos una RBM de nueve visibles y doce ocultas con los catorce patrones de barras y franjas de tres por tres. Con nueve visibles podemos calcular la log-verosimilitud exacta. El óptimo, repartir la probabilidad por igual entre los catorce patrones, es menos dos coma seis cuatro. Tras seis mil pasos, CD uno llega a menos tres coma uno cinco y CD diez, a menos dos coma ocho tres. Más pasos de Gibbs reducen el sesgo y dan un modelo mejor.

**EN:** Let's train an RBM with nine visible and twelve hidden units on the fourteen three-by-three bars-and-stripes patterns. With nine visible units we can compute the exact log-likelihood. The optimum, spreading probability equally over the fourteen patterns, is −2.64. After six thousand steps, CD-1 reaches −3.15 and CD-10, −2.83. More Gibbs steps reduce the bias and give a better model.

### [02:16.8] Deep belief networks and beyond — `manim:S05`

**ES:** Las RBM se pueden apilar: las ocultas de una son las visibles de la siguiente. Entrenando capa por capa se obtiene una red de creencia profunda, que en dos mil seis mostró que las redes profundas se podían entrenar. El algoritmo de vigilia y sueño y las máquinas de Helmholtz son parientes cercanos: una red de reconocimiento que infiere causas y una red generativa que sueña datos, entrenadas por turnos.

**EN:** RBMs can be stacked: the hidden units of one are the visible units of the next. Training layer by layer gives a deep belief network, which in 2006 showed that deep networks could be trained. The wake–sleep algorithm and Helmholtz machines are close relatives: a recognition network that infers causes and a generative network that dreams data, trained in turns.

### [02:43.4] Numerical example — `manim:S06`

**ES:** Un paso de CD uno con números. Supongamos un peso con correlación de datos ⟨v_i h_j⟩ = 0,62 y, tras una reconstrucción, 0,41. Con tasa de aprendizaje cero coma tres, el peso sube cero coma cero seis tres. En hardware de pbits, cada paso de Gibbs por bloques es una sola actualización paralela de una capa: un paso de CD uno son cuatro medias fases de reloj.

**EN:** One CD-1 step with numbers. Suppose a weight with data correlation ⟨v_i h_j⟩ = 0.62 and, after one reconstruction, 0.41. With learning rate 0.3, the weight increases by 0.063. On pbit hardware, each block Gibbs step is a single parallel update of one layer: one CD-1 step is four half clock phases.

### [03:11.5] Applications — `slide`

**ES:** Las RBM son ideales para hardware de pbits, porque su grafo bipartito se actualiza capa por capa. Se han usado para aprender características, en sistemas de recomendación y para representar estados cuánticos. En el laboratorio seis compararás CD y su versión persistente con la log-verosimilitud exacta.

**EN:** RBMs are ideal for pbit hardware, because their bipartite graph is updated layer by layer. They have been used to learn features, in recommender systems and to represent quantum states. In lab six you will compare CD and its persistent version using the exact log-likelihood.

### [03:32.3] Common mistakes — `slide`

**ES:** Errores comunes: creer que CD sigue el gradiente verdadero. Usar tasas grandes con CD persistente, porque las cadenas no alcanzan a seguir al modelo y el entrenamiento diverge; lo vimos en nuestro propio experimento. Muestrear las ocultas en la fase positiva en lugar de usar probabilidades. Y vigilar el error de reconstrucción en lugar de la verosimilitud.

**EN:** Common mistakes: believing CD follows the true gradient. Using large rates with persistent CD, because the chains cannot keep up with the model and training diverges; we saw it in our own experiment. Sampling the hidden units in the positive phase instead of using probabilities. And monitoring the reconstruction error instead of the likelihood.

### [03:55.5] Summary — `manim:S09`

**ES:** En resumen: la RBM restringe las conexiones a un grafo bipartito, y sus condicionales se factorizan en sigmoides. La divergencia contrastiva aproxima la fase del modelo con k pasos de Gibbs desde los datos: sesgada, pero barata. Apilar RBM dio las primeras redes profundas entrenables.

**EN:** In summary: the RBM restricts the connections to a bipartite graph, and its conditionals factorize into sigmoids. Contrastive divergence approximates the model phase with k Gibbs steps from the data: biased, but cheap. Stacking RBMs gave the first trainable deep networks.

### [04:17.0] Self-assessment — `slide`

**ES:** Para practicar: deriva la condicional de las ocultas. Escribe la energía libre de las visibles. Explica el sesgo de CD. Y cuenta los estados necesarios para la función de partición con nueve visibles.

**EN:** To practice: derive the hidden conditional. Write the free energy of the visible units. Explain the bias of CD. And count the states needed for the partition function with nine visible units.

## Key equations
- $$E(v,h) = -v^\top W h - b^\top v - c^\top h,\qquad p(h_j = 1\mid v) = \sigma\big(c_j + v^\top W_{:j}\big)$$ — RBM energy and factorized conditional (likewise $p(v_i = 1\mid h)$).
- $$\Delta W \propto \langle v h^\top\rangle_{\text{data}} - \langle v h^\top\rangle_{k}$$ — Contrastive divergence: model term after $k$ Gibbs steps from the data.
- $$F(v) = -b^\top v - \sum_j \ln\big(1 + e^{c_j + v^\top W_{:j}}\big),\quad p(v) = e^{-F(v)}/Z$$ — Free energy: the hidden units summed out exactly.

## Summary
- RBM: bipartite graph, factorized conditionals, 2-color block Gibbs.
- CD-$k$: cheap and biased; larger $k$ reduces bias.
- BAS 3×3: CD-1 −3.15, CD-10 −2.83 (optimum −2.64).
- Stacking RBMs: deep belief networks; relatives: wake–sleep, Helmholtz machines.

## Further reading
- [16] G. E. Hinton, A practical guide to training restricted Boltzmann machines, 2010.
- G. E. Hinton, Training products of experts by minimizing contrastive divergence, Neural Computation 14, 1771 (2002).
- G. E. Hinton, S. Osindero and Y.-W. Teh, A fast learning algorithm for deep belief nets, Neural Computation 18, 1527 (2006).
