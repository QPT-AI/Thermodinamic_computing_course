# Lesson 1.7 — A historical arc

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Place the key ideas in time: Carnot, Boltzmann, Gibbs, Shannon, Landauer, Hopfield, Hinton, Jarzynski and Crooks.
- Recognize how thermodynamics, information and machine learning converged into thermodynamic computing.
- Associate each figure with the equation we will use in the course.

## Prerequisites
- Lessons 1.1 to 1.6.

## Narrated script

### [00:04.3] Introduction — `manim:S01`

**ES:** Las ideas de este curso no nacieron juntas. Vienen de tres ríos que corrieron por separado durante más de un siglo: la termodinámica de las máquinas de vapor, la teoría de la información de las telecomunicaciones, y las redes neuronales inspiradas en la física. En esta lección recorremos la línea de tiempo y vemos cómo esos ríos se juntan.

**EN:** The ideas of this course were not born together. They come from three rivers that ran separately for more than a century: the thermodynamics of steam engines, the information theory of telecommunications, and physics-inspired neural networks. In this lesson we walk the timeline and see how those rivers merge.

### [00:25.9] Heat engines — `manim:S02`

**ES:** En 1824, Sadi Carnot se preguntó cuánto trabajo puede dar una máquina de vapor. Su respuesta fue universal: la eficiencia máxima entre dos focos depende solo de sus temperaturas, uno menos la temperatura fría sobre la caliente. Clausius convirtió esa intuición en la segunda ley y definió la entropía. Era una ciencia de motores, sin átomos ni bits.

**EN:** In 1824, Sadi Carnot asked how much work a steam engine can deliver. His answer was universal: the maximum efficiency between two reservoirs depends only on their temperatures, one minus the cold temperature over the hot one. Clausius turned that intuition into the second law and defined entropy. It was a science of engines, without atoms or bits.

### [00:50.8] Statistics — `manim:S03`

**ES:** Ludwig Boltzmann, en la década de mil ochocientos setenta, explicó la entropía contando microestados: S = k ln W, la fórmula grabada en su tumba. Josiah Willard Gibbs, en 1902, construyó los ensambles estadísticos y la distribución que hoy usamos, e^(−βE)/Z. La termodinámica pasó a ser estadística: probabilidades sobre estados microscópicos.

**EN:** Ludwig Boltzmann, in the 1870s, explained entropy by counting microstates: S = k ln W, the formula engraved on his tomb. Josiah Willard Gibbs, in 1902, built statistical ensembles and the distribution we use today, e^(−βE)/Z. Thermodynamics became statistical: probabilities over microscopic states.

### [01:18.6] Information — `manim:S04`

**ES:** En 1948, Claude Shannon definió la información y su entropía para diseñar sistemas de comunicación. La fórmula era la de Gibbs. En 1961, Rolf Landauer conectó ambos mundos: borrar un bit cuesta al menos k T ln 2. Y Charles Bennett, en las décadas siguientes, mostró que el cómputo puede ser reversible y resolvió el demonio de Maxwell. La información se volvió física.

**EN:** In 1948, Claude Shannon defined information and its entropy to design communication systems. The formula was Gibbs's. In 1961, Rolf Landauer connected both worlds: erasing a bit costs at least k T ln 2. And Charles Bennett, in the following decades, showed that computation can be reversible and resolved Maxwell's demon. Information became physical.

### [01:47.0] Physical neural networks — `manim:S05`

**ES:** En 1982, John Hopfield mostró que una red de neuronas binarias con conexiones simétricas es un modelo de Ising: la memoria asociativa es descender por un paisaje de energía. En 1985, Geoffrey Hinton, con Ackley y Sejnowski, añadió temperatura y muestreo: la máquina de Boltzmann aprende ajustando las correlaciones del modelo a las de los datos. En 2024 ambos recibieron el premio Nobel de Física por estas ideas.

**EN:** In 1982, John Hopfield showed that a network of binary neurons with symmetric connections is an Ising model: associative memory is descending an energy landscape. In 1985, Geoffrey Hinton, with Ackley and Sejnowski, added temperature and sampling: the Boltzmann machine learns by matching the model's correlations to the data's. In 2024 both received the Nobel Prize in Physics for these ideas.

### [02:17.3] Fluctuations — `manim:S06`

**ES:** En 1997, Christopher Jarzynski descubrió una igualdad exacta: el promedio de la exponencial de menos el trabajo da la diferencia de energía libre, incluso para procesos rápidos. En 1999, Gavin Crooks la generalizó relacionando las probabilidades de una trayectoria y de su inversa en el tiempo. Nació la termodinámica estocástica: la termodinámica de sistemas pequeños, ruidosos y lejos del equilibrio, como un chip termodinámico.

**EN:** In 1997, Christopher Jarzynski discovered an exact equality: the average of the exponential of minus the work gives the free-energy difference, even for fast processes. In 1999, Gavin Crooks generalized it by relating the probabilities of a trajectory and of its time reverse. Stochastic thermodynamics was born: the thermodynamics of small, noisy systems far from equilibrium, like a thermodynamic chip.

### [02:48.5] Convergence — `manim:S07`

**ES:** Los tres ríos se juntan en el cómputo termodinámico. De la termodinámica toma la energía libre y los límites de eficiencia. De la información, el costo de borrar y la equivalencia entre bits y entropía. De las redes neuronales, la idea de que aprender es ajustar una distribución de Boltzmann. Y de la termodinámica estocástica, las herramientas para medir trabajo y calor en un dispositivo ruidoso. Ese es el mapa intelectual del curso.

**EN:** The three rivers merge in thermodynamic computing. From thermodynamics it takes free energy and efficiency limits. From information, the cost of erasing and the equivalence between bits and entropy. From neural networks, the idea that learning is fitting a Boltzmann distribution. And from stochastic thermodynamics, the tools to measure work and heat in a noisy device. That is the intellectual map of the course.

### [03:16.6] Applications — `slide`

**ES:** Cada nombre de esta historia es una herramienta del curso. Carnot y Clausius nos dan los límites. Boltzmann y Gibbs, el programa que ejecuta un chip termodinámico. Shannon, Landauer y Bennett, el costo de la información. Hopfield y Hinton, los modelos de aprendizaje de la unidad cuatro. Y Jarzynski y Crooks, la forma de extraer energías libres, e incluso determinantes de matrices, a partir de mediciones de trabajo.

**EN:** Every name in this story is a tool of the course. Carnot and Clausius give us the limits. Boltzmann and Gibbs, the program a thermodynamic chip executes. Shannon, Landauer and Bennett, the cost of information. Hopfield and Hinton, the learning models of unit four. And Jarzynski and Crooks, the way to extract free energies, and even matrix determinants, from work measurements.

### [03:43.9] Common mistakes — `slide`

**ES:** Algunos mitos a evitar. Shannon no copió a Gibbs: la coincidencia formal se reconoció después. El demonio no se resolvió en la medición, sino en el borrado. Las máquinas de Boltzmann no eran erróneas: eran caras de muestrear en hardware digital, y por eso el hardware termodinámico podría revivirlas. Y la igualdad de Jarzynski no contradice la segunda ley: la contiene.

**EN:** Some myths to avoid. Shannon did not copy Gibbs: the formal coincidence was recognized later. The demon was not resolved at measurement, but at erasure. Boltzmann machines were not wrong: they were expensive to sample on digital hardware, which is why thermodynamic hardware could revive them. And the Jarzynski equality does not contradict the second law: it contains it.

### [04:08.3] Summary — `manim:S10`

**ES:** En resumen: la termodinámica nació con los motores, se volvió estadística con Boltzmann y Gibbs, encontró la información con Shannon y Landauer, inspiró el aprendizaje con Hopfield y Hinton, y se volvió estocástica con Jarzynski y Crooks. El cómputo termodinámico es el punto donde todas esas líneas se cruzan.

**EN:** In summary: thermodynamics was born with engines, became statistical with Boltzmann and Gibbs, met information with Shannon and Landauer, inspired learning with Hopfield and Hinton, and became stochastic with Jarzynski and Crooks. Thermodynamic computing is the point where all those lines cross.

### [04:29.2] Self-assessment — `slide`

**ES:** Para practicar: calcula una eficiencia de Carnot. Explica la fórmula de la tumba de Boltzmann. Resume el aporte de Bennett. Y deduce la segunda ley a partir de la igualdad de Jarzynski.

**EN:** To practice: compute a Carnot efficiency. Explain the formula on Boltzmann's tomb. Summarize Bennett's contribution. And derive the second law from the Jarzynski equality.

## Key equations
- $$\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h}$$ — Maximum efficiency of a heat engine (Carnot, 1824).
- $$S = k\ln W,\qquad p = \frac{e^{-\beta E}}{Z}$$ — Boltzmann (1877) and Gibbs (1902).
- $$H = -\sum p\log_2 p,\qquad Q \ge k_BT\ln 2$$ — Shannon (1948) and Landauer (1961).
- $$\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$$ — Jarzynski (1997); Crooks (1999) generalizes it to trajectories.

## Summary
- Three rivers: thermodynamics, information and physical neural networks.
- Boltzmann/Gibbs: statistics; Shannon/Landauer/Bennett: physical information.
- Hopfield/Hinton: learning as physics (Nobel 2024).
- Jarzynski/Crooks: stochastic thermodynamics, out of equilibrium.

## Further reading
- [8] Landauer (1961); [9] Bennett (2003); [12] Jarzynski (1997).
- [14] Ackley, Hinton and Sejnowski (1985); [15] Hopfield (1982).
- Hinton's Nobel lecture, Boltzmann Machines (2024): https://www.nobelprize.org/prizes/physics/2024/hinton/lecture/
