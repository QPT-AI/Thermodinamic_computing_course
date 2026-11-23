# Lesson 4.2 — The Ising model

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write the Ising energy $E(s) = -\sum_{i<j} J_{ij}s_is_j - \sum_i h_i s_i$ and interpret couplings and fields.
- Describe the ferromagnetic phase transition of the 2D model and its critical temperature $T_c = 2/\ln(1+\sqrt2)$.
- Recognize frustration and spin glasses as the source of rugged energy landscapes.

## Prerequisites
- Lesson 4.1: energy-based models and graphs.
- Lesson 1.2: Boltzmann distribution.

## Narrated script

### [00:04.5] Introduction — `manim:S01`

**ES:** Si hubiera que elegir un solo modelo para este curso, sería el de Ising. Espines que valen más uno o menos uno, acoplados de a pares. Es el programa nativo de un chip de pbits, el corazón de las redes de Hopfield y de las máquinas de Boltzmann, y el lenguaje en el que se escriben muchos problemas de optimización.

**EN:** If we had to choose a single model for this course, it would be the Ising model. Spins that are plus one or minus one, coupled in pairs. It is the native program of a pbit chip, the heart of Hopfield networks and Boltzmann machines, and the language in which many optimization problems are written.

### [00:24.2] Intuition — `manim:S02`

**ES:** Piensa en un imán como una red de pequeñas brújulas. Cada una prefiere apuntar igual que sus vecinas, porque así baja la energía. La temperatura las sacude al azar. A baja temperatura gana el orden y aparecen grandes dominios alineados; a alta temperatura gana el desorden. Entre los dos regímenes hay un cambio brusco: una transición de fase.

**EN:** Think of a magnet as a lattice of tiny compasses. Each one prefers to point the same way as its neighbors, because that lowers the energy. Temperature shakes them at random. At low temperature order wins and large aligned domains appear; at high temperature disorder wins. Between the two regimes there is an abrupt change: a phase transition.

### [00:46.5] The energy — `manim:S03`

**ES:** La energía es E = −Σ J_ij s_i s_j − Σ h_i s_i. Un acoplamiento positivo premia a los espines alineados: es ferromagnético. Uno negativo premia a los opuestos: es antiferromagnético. El campo h_i empuja a cada espín hacia un valor. Lo que siente cada espín es su campo local, u_i = Σ_j J_ij s_j + h_i, y veremos que un pbit es exactamente un espín que responde a ese campo.

**EN:** The energy is E = −Σ J_ij s_i s_j − Σ h_i s_i. A positive coupling rewards aligned spins: it is ferromagnetic. A negative one rewards opposite spins: it is antiferromagnetic. The field h_i pushes each spin toward a value. What each spin feels is its local field, u_i = Σ_j J_ij s_j + h_i, and we will see that a pbit is exactly a spin responding to that field.

### [01:19.7] Phase transition — `manim:S04`

**ES:** Simulemos una red cuadrada de treinta y dos por treinta y dos con acoplamiento uno y sin campo. A temperatura uno coma cinco casi todos los espines apuntan igual. Cerca de dos coma dos siete aparecen dominios de todos los tamaños. A tres coma cinco el patrón es ruido. La magnetización media cae desde uno hasta cero alrededor de la temperatura crítica, que Onsager calculó exactamente: T_c = 2/ln(1 + √2).

**EN:** Let's simulate a thirty-two by thirty-two square lattice with coupling one and no field. At temperature 1.5 almost all spins point the same way. Near 2.27 domains of all sizes appear. At 3.5 the pattern is noise. The mean magnetization falls from one to zero around the critical temperature, which Onsager computed exactly: T_c = 2/ln(1 + √2).

### [01:49.8] Frustration and spin glasses — `manim:S05`

**ES:** Ahora pongamos tres espines en un triángulo con acoplamientos antiferromagnéticos. Cada par quiere ser opuesto, pero con tres espines es imposible: al menos un par queda insatisfecho. Eso se llama frustración, y produce muchos estados fundamentales con la misma energía. Si los acoplamientos son aleatorios en toda una red, tenemos un vidrio de espín: un paisaje rugoso con muchísimos mínimos locales. Encontrar su mínimo global es, en general, un problema difícil.

**EN:** Now let's put three spins on a triangle with antiferromagnetic couplings. Each pair wants to be opposite, but with three spins it is impossible: at least one pair stays unsatisfied. That is called frustration, and it produces many ground states with the same energy. If the couplings are random across a whole lattice, we have a spin glass: a rugged landscape with very many local minima. Finding its global minimum is, in general, a hard problem.

### [02:20.4] Numerical example — `manim:S06`

**ES:** Comparemos simulación y teoría. La temperatura crítica exacta es dos coma dos seis nueve. A temperatura dos, la fórmula de Onsager da una magnetización de cero coma nueve uno uno, y la simulación de Gibbs da cero coma nueve uno tres. A uno coma cinco, cero coma nueve ocho seis frente a cero coma nueve ocho siete. Cerca de la temperatura crítica la red finita redondea la transición: es un efecto de tamaño finito.

**EN:** Let's compare simulation and theory. The exact critical temperature is 2.269. At temperature two, Onsager's formula gives a magnetization of 0.911, and the Gibbs simulation gives 0.913. At 1.5, 0.986 versus 0.987. Near the critical temperature the finite lattice rounds off the transition: it is a finite-size effect.

### [02:49.3] Applications — `slide`

**ES:** El modelo de Ising es el programa de los chips de pbits, el lenguaje de muchos problemas de optimización, y la base de las memorias de Hopfield y de las máquinas de Boltzmann. Y cerca de la temperatura crítica, como veremos en la lección cuatro punto cuatro, el muestreo se vuelve lento.

**EN:** The Ising model is the program of pbit chips, the language of many optimization problems, and the basis of Hopfield memories and Boltzmann machines. And near the critical temperature, as we will see in lesson 4.4, sampling becomes slow.

### [03:07.3] Common mistakes — `slide`

**ES:** Errores comunes: confundir el signo de los acoplamientos. Contar dos veces cada par. Esperar una transición abrupta en un sistema finito. Y olvidar que la cadena unidimensional no tiene transición a temperatura positiva.

**EN:** Common mistakes: getting the coupling sign wrong. Counting each pair twice. Expecting an abrupt transition in a finite system. And forgetting that the one-dimensional chain has no transition at positive temperature.

### [03:22.2] Summary — `manim:S09`

**ES:** En resumen: el modelo de Ising tiene espines binarios, acoplamientos de a pares y campos. En dos dimensiones tiene una transición entre orden y desorden en T_c ≈ 2,27. Y con acoplamientos de signo mixto aparece la frustración, que crea paisajes rugosos y problemas difíciles.

**EN:** In summary: the Ising model has binary spins, pairwise couplings and fields. In two dimensions it has an order–disorder transition at T_c ≈ 2.27. And with mixed-sign couplings frustration appears, creating rugged landscapes and hard problems.

### [03:42.9] Self-assessment — `slide`

**ES:** Para practicar: calcula un campo local. Encuentra los estados fundamentales del triángulo frustrado. Evalúa la fórmula de Onsager. Y explica por qué la cadena unidimensional no se ordena.

**EN:** To practice: compute a local field. Find the ground states of the frustrated triangle. Evaluate Onsager's formula. And explain why the one-dimensional chain does not order.

## Key equations
- $$E(s) = -\sum_{i<j}J_{ij}s_is_j - \sum_i h_i s_i,\qquad u_i = \sum_j J_{ij}s_j + h_i$$ — Ising energy and local field.
- $$T_c = \frac{2J}{k_B\ln(1+\sqrt2)} \approx 2.269\,J/k_B$$ — Critical temperature of the 2D square lattice (Onsager).
- $$m(T) = \big(1 - \sinh^{-4}(2J/k_BT)\big)^{1/8},\quad T < T_c$$ — Exact spontaneous magnetization of the 2D model.

## Summary
- Binary spins, pairwise couplings $J_{ij}$ and fields $h_i$; local field $u_i$.
- 2D: order–disorder transition at $T_c \approx 2.27$ (Onsager).
- Frustration (mixed signs) ⇒ degenerate ground states, rugged landscapes.
- Spin glasses: finding the minimum is hard in general.

## Further reading
- [13] H. G. Katzgraber, Introduction to Monte Carlo methods, 2009.
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, 2022.
- L. Onsager, Crystal statistics I, Phys. Rev. 65, 117 (1944).
