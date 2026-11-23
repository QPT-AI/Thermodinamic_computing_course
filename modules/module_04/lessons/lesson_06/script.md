# Lesson 4.6 — Hopfield networks and associative memory

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Store patterns with the Hebb rule $J = \tfrac1N\sum_\mu \xi^\mu\xi^{\mu\top}$ and recall them by descending the Ising energy.
- Show that the update $s_i \leftarrow \mathrm{sgn}(u_i)$ never increases the energy.
- Estimate the capacity $P_{\max} \approx 0.14N$ and recognize spurious states.

## Prerequisites
- Lesson 4.2: the Ising model.
- Lesson 4.5: pbits and local fields.

## Narrated script

### [00:05.6] Introduction — `manim:S01`

**ES:** Tu memoria no busca recuerdos por dirección, como un disco duro. Basta un fragmento, un olor o la mitad de una cara, para recuperar el recuerdo completo. En mil novecientos ochenta y dos, John Hopfield mostró que un modelo de Ising a temperatura cero hace exactamente eso: es una memoria direccionable por contenido.

**EN:** Your memory does not look up memories by address, like a hard drive. A fragment, a smell or half a face is enough to recover the full memory. In 1982, John Hopfield showed that an Ising model at zero temperature does exactly that: it is a content-addressable memory.

### [00:26.3] Intuition — `manim:S02`

**ES:** La idea es esculpir el paisaje de energía para que cada recuerdo sea el fondo de un valle. Una pista incompleta o ruidosa es un punto en la ladera. Dejar que el sistema baje es recordar. Cuantos más recuerdos guardamos, más valles hay, y en algún momento empiezan a interferir.

**EN:** The idea is to sculpt the energy landscape so that each memory is the bottom of a valley. An incomplete or noisy cue is a point on the slope. Letting the system roll down is remembering. The more memories we store, the more valleys there are, and at some point they start to interfere.

### [00:44.4] Hebb rule and dynamics — `manim:S03`

**ES:** Para guardar los patrones ξ^μ usamos la regla de Hebb: los acoplamientos son J = (1/N) Σ ξ^μ ξ^μᵀ, con diagonal cero. Las neuronas que se activan juntas quedan conectadas. Para recordar, cada espín se alinea con su campo local: s_i ← sgn(u_i). Es el pbit con β infinito. Cada una de esas actualizaciones nunca aumenta la energía de Ising, así que la red siempre termina en un mínimo.

**EN:** To store the patterns ξ^μ we use the Hebb rule: the couplings are J = (1/N) Σ ξ^μ ξ^μᵀ, with zero diagonal. Neurons that fire together get wired together. To recall, each spin aligns with its local field: s_i ← sgn(u_i). It is the pbit with infinite β. Each of those updates never increases the Ising energy, so the network always ends in a minimum.

### [01:16.0] Recall — `manim:S04`

**ES:** Guardemos tres patrones de cien píxeles en una red de cien neuronas. Tomemos uno de ellos y volteemos el veinte por ciento de sus píxeles al azar. Al dejar correr la dinámica, los píxeles se corrigen uno a uno, y en pocos barridos la red recupera el patrón original completo. La pista ruidosa estaba en la cuenca de atracción correcta.

**EN:** Let's store three hundred-pixel patterns in a network of a hundred neurons. Take one of them and flip twenty percent of its pixels at random. As the dynamics run, the pixels are corrected one by one, and within a few sweeps the network recovers the full original pattern. The noisy cue was in the right basin of attraction.

### [01:37.0] Capacity — `manim:S05`

**ES:** ¿Cuántos recuerdos caben? El campo local de cada espín tiene una parte de señal, del patrón buscado, y una parte de ruido cruzado, de todos los demás. Mientras la carga α = P/N sea pequeña, la señal gana. Alrededor de α ≈ 0,14 el ruido cruzado domina y la memoria colapsa: los recuerdos se mezclan. Además aparecen estados espurios, mínimos que no corresponden a ningún patrón guardado, como mezclas de tres recuerdos.

**EN:** How many memories fit? Each spin's local field has a signal part, from the target pattern, and a crosstalk part, from all the others. As long as the load α = P/N is small, the signal wins. Around α ≈ 0.14 the crosstalk dominates and the memory collapses: memories get mixed. Spurious states also appear, minima that correspond to no stored pattern, such as mixtures of three memories.

### [02:08.6] Numerical example — `manim:S06`

**ES:** Con cuatrocientas neuronas y pistas con un diez por ciento de ruido, la superposición final con el patrón correcto es prácticamente uno para cargas de cero coma cero cinco y de cero coma uno. A cero coma uno seis cae a cero coma ocho tres, y a cero coma dos, a cero coma cinco cinco. Cuatrocientas neuronas guardan unos cincuenta recuerdos confiables.

**EN:** With four hundred neurons and cues with ten percent noise, the final overlap with the correct pattern is practically one for loads of 0.05 and 0.1. At 0.16 it falls to 0.83, and at 0.2, to 0.55. Four hundred neurons store about fifty reliable memories.

### [02:31.3] Applications — `slide`

**ES:** Con temperatura positiva, la misma red construida con pbits muestrea alrededor de los recuerdos, y ese es el punto de partida de las máquinas de Boltzmann. Las redes de Hopfield modernas tienen capacidad exponencial y una regla de actualización que se parece a la atención de los transformers. Y en dos mil veinticuatro, Hopfield recibió el Nobel de Física por estas ideas.

**EN:** At positive temperature, the same network built with pbits samples around the memories, and that is the starting point of Boltzmann machines. Modern Hopfield networks have exponential capacity and an update rule that resembles transformer attention. And in 2024, Hopfield received the Nobel Prize in Physics for these ideas.

### [02:54.6] Common mistakes — `slide`

**ES:** Errores comunes: dejar la diagonal distinta de cero, actualizar todas las neuronas a la vez, lo que puede producir oscilaciones, sobrecargar la memoria más allá del catorce por ciento, y guardar patrones muy correlacionados, que interfieren más.

**EN:** Common mistakes: leaving a nonzero diagonal, updating all neurons at once, which can cause oscillations, overloading the memory beyond fourteen percent, and storing highly correlated patterns, which interfere more.

### [03:11.3] Summary — `manim:S09`

**ES:** En resumen: una red de Hopfield es un modelo de Ising con acoplamientos de Hebb. Sus mínimos de energía son los recuerdos, y recordar es descender con s_i ← sgn(u_i). La capacidad es de unos 0,14 N patrones, y más allá aparecen interferencias y estados espurios.

**EN:** In summary: a Hopfield network is an Ising model with Hebbian couplings. Its energy minima are the memories, and remembering is descending with s_i ← sgn(u_i). The capacity is about 0.14 N patterns, and beyond that interference and spurious states appear.

### [03:31.1] Self-assessment — `slide`

**ES:** Para practicar: demuestra que la energía no aumenta. Calcula el campo local con un solo patrón guardado. Estima la capacidad de una red de mil neuronas. Y explica por qué el patrón invertido también es un mínimo.

**EN:** To practice: prove that the energy does not increase. Compute the local field with a single stored pattern. Estimate the capacity of a thousand-neuron network. And explain why the inverted pattern is also a minimum.

## Key equations
- $$J_{ij} = \frac1N\sum_{\mu=1}^P \xi_i^\mu\xi_j^\mu,\quad J_{ii} = 0$$ — Hebb rule for $P$ patterns $\xi^\mu \in \{\pm1\}^N$.
- $$s_i \leftarrow \mathrm{sgn}\Big(\sum_j J_{ij}s_j\Big),\qquad \Delta E \le 0$$ — Zero-temperature asynchronous dynamics: energy descent.
- $$\alpha_c = P_{\max}/N \approx 0.138$$ — Capacity of the Hopfield network (random patterns).

## Summary
- Hopfield = Ising with Hebbian $J$; memories = energy minima.
- Recall: $s_i \leftarrow \mathrm{sgn}(u_i)$ descends the energy (pbit with $\beta\to\infty$).
- Capacity $\approx 0.14N$; beyond it, crosstalk and spurious states.
- At $T > 0$: Boltzmann machines (lesson 4.7).

## Further reading
- [15] J. J. Hopfield, Neural networks and physical systems with emergent collective computational abilities, PNAS 79, 2554 (1982).
- D. J. Amit, H. Gutfreund and H. Sompolinsky, Storing infinite numbers of patterns in a spin-glass model of neural networks, PRL 55, 1530 (1985).
- H. Ramsauer et al., Hopfield networks is all you need, ICLR 2021 (supplementary).
