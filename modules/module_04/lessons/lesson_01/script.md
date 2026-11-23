# Lesson 4.1 — Energy-based models and graphical models

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define an energy-based model $p_\theta(x) = e^{-E_\theta(x)}/Z_\theta$ and read an energy as a sum of local factors.
- Draw the factor graph of an energy and identify Markov blankets and conditional independences.
- Distinguish pairwise graphs from hypergraphs (higher-order factors).

## Prerequisites
- Lesson 1.2: Boltzmann distribution and partition function.
- Lesson 0.3: conditional probability.

## Narrated script

### [00:06.1] Introduction — `manim:S01`

**ES:** En la unidad uno vimos que un sistema en equilibrio visita cada estado con probabilidad proporcional a e^(−E). Si invertimos la lectura, cualquier función de energía define una distribución de probabilidad. Eso es un modelo basado en energía. Y es exactamente el programa que ejecuta un chip termodinámico: le damos una energía, y nos devuelve muestras.

**EN:** In unit one we saw that a system at equilibrium visits each state with probability proportional to e^(−E). If we read it the other way around, any energy function defines a probability distribution. That is an energy-based model. And it is exactly the program a thermodynamic chip runs: we give it an energy, and it returns samples.

### [00:28.7] Intuition — `manim:S02`

**ES:** Piensa en la energía como un paisaje. Los valles son configuraciones probables y las montañas, improbables. Aprender un modelo es esculpir el paisaje para que los valles caigan sobre los datos. La forma del paisaje la fijan unos parámetros, y la temperatura decide cuánto exploramos fuera de los valles.

**EN:** Think of the energy as a landscape. Valleys are likely configurations and mountains, unlikely ones. Learning a model is sculpting the landscape so that the valleys fall on the data. Parameters set the shape of the landscape, and temperature decides how much we explore outside the valleys.

### [00:47.9] Local energies and graphs — `manim:S03`

**ES:** Una energía útil se escribe como suma de términos locales, cada uno sobre pocas variables. Entonces la probabilidad se factoriza en un producto de factores, uno por término. Dibujamos un nodo por variable y conectamos las que comparten un término: es el modelo gráfico. La consecuencia clave es la manta de Markov: la distribución de una variable, dadas todas las demás, solo depende de sus vecinas.

**EN:** A useful energy is written as a sum of local terms, each over a few variables. Then the probability factorizes into a product of factors, one per term. We draw one node per variable and connect those that share a term: that is the graphical model. The key consequence is the Markov blanket: the distribution of a variable, given all the others, depends only on its neighbors.

### [01:14.4] Factor graphs and hypergraphs — `manim:S04`

**ES:** El grafo de factores hace explícitos los términos: es bipartito, con círculos para las variables y cuadrados para los factores. Un factor de dos variables es una arista ordinaria. Un factor de tres o más variables, como s₁ s₂ s₃, es una hiperarista: el modelo es un hipergrafo. El hardware actual implementa sobre todo interacciones de a pares, así que los términos de orden alto se reescriben con variables auxiliares.

**EN:** The factor graph makes the terms explicit: it is bipartite, with circles for variables and squares for factors. A two-variable factor is an ordinary edge. A factor of three or more variables, like s₁ s₂ s₃, is a hyperedge: the model is a hypergraph. Current hardware implements mostly pairwise interactions, so higher-order terms are rewritten with auxiliary variables.

### [01:43.2] Conditional independence — `manim:S05`

**ES:** Veámoslo en una cadena de tres espines con energía E = −s₁s₂ − s₂s₃ a temperatura uno. Los extremos no interactúan, pero están correlacionados: la correlación entre s₁ y s₃ vale tanh² 1, unos cero coma cincuenta y ocho. Si fijamos el espín del medio, la correlación desaparece exactamente. La información viaja a través del grafo, y conocer al vecino corta el camino.

**EN:** Let's see it in a chain of three spins with energy E = −s₁s₂ − s₂s₃ at temperature one. The ends do not interact, but they are correlated: the correlation between s₁ and s₃ is tanh² 1, about 0.58. If we fix the middle spin, the correlation vanishes exactly. Information travels through the graph, and knowing the neighbor cuts the path.

### [02:14.3] Numerical example — `manim:S06`

**ES:** Con solo ocho configuraciones podemos calcular todo. La función de partición vale diecinueve coma cero cinco. Las dos configuraciones alineadas tienen probabilidad cero coma treinta y nueve cada una, y juntas suman casi el setenta y ocho por ciento. Las que tienen el espín del medio en contra de ambos vecinos son las más improbables, con menos del uno por ciento. Para cien espines ya no podríamos enumerar: tendremos que muestrear.

**EN:** With only eight configurations we can compute everything. The partition function is 19.05. The two aligned configurations have probability 0.39 each, and together add up to almost seventy-eight percent. Those with the middle spin against both neighbors are the least likely, under one percent. For a hundred spins we could no longer enumerate: we will have to sample.

### [02:42.3] Applications — `slide`

**ES:** En la práctica, un programa para un chip termodinámico es un grafo de factores de grado acotado. Bibliotecas como THRML trabajan directamente con grafos de factores. Y en aprendizaje automático, las máquinas de Boltzmann y los modelos de eliminación de ruido de la unidad nueve son modelos basados en energía.

**EN:** In practice, a program for a thermodynamic chip is a factor graph of bounded degree. Libraries like THRML work directly with factor graphs. And in machine learning, Boltzmann machines and the denoising models of unit nine are energy-based models.

### [03:02.9] Common mistakes — `slide`

**ES:** Errores comunes: creer que dos variables sin arista son independientes. Confundir el grafo de interacciones con el de correlaciones. Pensar que la función de partición es fácil porque cada factor es local. Y olvidar que el hardware de pares necesita variables auxiliares para los términos de orden alto.

**EN:** Common mistakes: believing two variables without an edge are independent. Confusing the interaction graph with the correlation graph. Thinking the partition function is easy because each factor is local. And forgetting that pairwise hardware needs auxiliary variables for higher-order terms.

### [03:21.8] Summary — `manim:S09`

**ES:** En resumen: un modelo basado en energía define p ∝ e^(−E). Si la energía es suma de términos locales, la probabilidad se factoriza y se dibuja como un grafo de factores. Cada variable depende solo de su manta de Markov, y la independencia condicional se lee en el grafo.

**EN:** In summary: an energy-based model defines p ∝ e^(−E). If the energy is a sum of local terms, the probability factorizes and is drawn as a factor graph. Each variable depends only on its Markov blanket, and conditional independence is read from the graph.

### [03:41.2] Self-assessment — `slide`

**ES:** Para practicar: dibuja un grafo de factores con un término de tres cuerpos. Encuentra la manta de Markov en una red cuadrada. Demuestra la independencia condicional en la cadena. Y cuenta los términos de la función de partición de una red de diez por diez.

**EN:** To practice: draw a factor graph with a three-body term. Find the Markov blanket in a square lattice. Prove conditional independence in the chain. And count the terms in the partition function of a ten-by-ten lattice.

## Key equations
- $$p_\theta(x) = \frac{e^{-E_\theta(x)}}{Z_\theta},\qquad E_\theta(x) = \sum_a E_a(x_{\partial a})$$ — Energy-based model with an energy that is a sum of local factors $a$ over their variables $x_{\partial a}$.
- $$p(x_i \mid x_{-i}) = p(x_i \mid x_{\mathcal N(i)})$$ — Markov blanket: the conditional depends only on the neighbors $\mathcal N(i)$.
- $$\langle s_1 s_3\rangle = \tanh^2(\beta J),\qquad \mathrm{Cov}(s_1, s_3 \mid s_2) = 0$$ — Three-spin chain: correlation through the graph, conditional independence given the middle spin.

## Summary
- EBM: $p \propto e^{-E}$; any energy defines a distribution.
- Local energies ⇒ factorization ⇒ graphical model / factor graph.
- Markov blanket: conditionals depend only on neighbors.
- Pairwise graphs vs hypergraphs; hardware is mostly pairwise.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
- D. Koller and N. Friedman, Probabilistic Graphical Models, MIT Press, 2009 (supplementary).
