# Lesson 5.5 — Other physical substrates

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe Brownian token circuits (Hub, CJoin, Ratchet) and their computation time as a first-passage problem.
- Place superconducting (Josephson) and mechanical Langevin devices, RC diffusion networks and chemical reaction networks.
- Compare substrates by their primitive, operating temperature and what limits them.

## Prerequisites
- Lessons 2.8 and 3.6: first passage and TUR.
- Lesson 3.9: chemical reaction networks.

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** Los pbits de silicio y los osciladores acoplados no son las únicas formas de computar con ruido. Hay circuitos en los que la información la llevan partículas que se difunden al azar, neuronas superconductoras, redes de resistencias y capacitores que difunden voltaje, y reacciones químicas. En esta lección recorremos ese zoológico y lo que cada sustrato aporta.

**EN:** Silicon pbits and coupled oscillators are not the only ways to compute with noise. There are circuits where information is carried by particles that diffuse at random, superconducting neurons, networks of resistors and capacitors that diffuse voltage, and chemical reactions. In this lesson we tour that zoo and what each substrate brings.

### [00:27.5] Brownian token circuits — `manim:S02`

**ES:** En un circuito browniano, un token, por ejemplo un electrón aislado o un skyrmion magnético, se difunde al azar por un cable. Tres piezas bastan para construir lógica. Un Hub, donde el token puede salir por cualquiera de tres cables. Un CJoin, que solo deja pasar cuando llegan dos tokens a la vez, uno por cada entrada. Y un Ratchet, un trinquete que impide retroceder. Con ellas se arma cualquier circuito, y el cómputo avanza solo, impulsado por el ruido térmico.

**EN:** In a Brownian circuit, a token, for example an isolated electron or a magnetic skyrmion, diffuses at random along a wire. Three pieces suffice to build logic. A Hub, where the token can exit through any of three wires. A CJoin, which only lets tokens through when two arrive together, one on each input. And a Ratchet, which prevents going backward. With them one builds any circuit, and the computation advances by itself, driven by thermal noise.

### [00:58.3] Time to compute — `manim:S03`

**ES:** ¿Cuánto tarda? Sin trinquetes, un token que recorre veinte sitios por difusión libre tarda en promedio unas doscientas diez unidades de tiempo, y con enorme variabilidad: la desviación es el ochenta y cuatro por ciento de la media. Con un sesgo que duplica la tasa hacia adelante, el tiempo baja a unas diecinueve unidades y la variabilidad al treinta y ocho por ciento. El precio es disipar el logaritmo de dos, en k_B T, por cada paso: exactamente el compromiso de las relaciones de incertidumbre termodinámica.

**EN:** How long does it take? Without ratchets, a token crossing twenty sites by free diffusion takes on average about two hundred ten time units, with huge variability: the standard deviation is eighty-four percent of the mean. With a bias that doubles the forward rate, the time drops to about nineteen units and the variability to thirty-eight percent. The price is dissipating log two, in k_B T, per step: exactly the trade-off of thermodynamic uncertainty relations.

### [01:30.1] Superconducting and mechanical devices — `manim:S04`

**ES:** Un rf-SQUID, un anillo superconductor con una unión de Josephson, tiene un potencial de pozo doble en el flujo magnético, con barrera e inclinación ajustables por líneas de polarización. A temperatura de milikelvin, el ruido térmico lo hace saltar entre pozos: es una neurona termodinámica. Su ventaja es la velocidad y la baja disipación; su costo, la criogenia. Por debajo de cierta temperatura, el salto deja de ser térmico y pasa a ser por efecto túnel cuántico. También se han propuesto osciladores mecánicos microscópicos como dispositivos de Langevin.

**EN:** An rf-SQUID, a superconducting loop with a Josephson junction, has a double-well potential in magnetic flux, with barrier and tilt tunable by bias lines. At millikelvin temperatures, thermal noise makes it hop between wells: it is a thermodynamic neuron. Its advantage is speed and low dissipation; its cost, cryogenics. Below a certain temperature, hopping stops being thermal and becomes quantum tunneling. Microscopic mechanical oscillators have also been proposed as Langevin devices.

### [02:06.9] RC diffusion networks and chemistry — `manim:S05`

**ES:** Una red de resistencias y capacitores cumple C V̇ = −L V, donde L es el laplaciano del grafo: el voltaje se difunde como el calor. Si el grafo es el de Cayley de un grupo, esa difusión calcula la probabilidad de regreso de una caminata aleatoria, y es la base física del algoritmo de factorización por difusión de la unidad siete. Las redes de reacciones químicas, por su parte, computan con concentraciones y se analizan con la teoría de circuitos de la lección tres punto nueve.

**EN:** A network of resistors and capacitors satisfies C V̇ = −L V, where L is the graph Laplacian: voltage diffuses like heat. If the graph is the Cayley graph of a group, that diffusion computes the return probability of a random walk, and it is the physical basis of the factoring-by-diffusion algorithm of unit seven. Chemical reaction networks, for their part, compute with concentrations and are analyzed with the circuit theory of lesson 3.9.

### [02:38.6] Comparing substrates — `manim:S06`

**ES:** Comparemos. Los pbits CMOS y magnéticos trabajan a temperatura ambiente y en nanosegundos. Los osciladores acoplados resuelven problemas continuos. Los circuitos brownianos computan sin reloj, pero lentamente. Los SQUID son rápidos, pero necesitan criogenia. Las redes RC difunden sin ruido útil, y las reacciones químicas son lentas pero masivamente paralelas. Ningún sustrato gana en todo.

**EN:** Let's compare. CMOS and magnetic pbits work at room temperature and in nanoseconds. Coupled oscillators solve continuous problems. Brownian circuits compute without a clock, but slowly. SQUIDs are fast, but need cryogenics. RC networks diffuse without useful noise, and chemical reactions are slow but massively parallel. No substrate wins at everything.

### [03:06.5] Applications — `slide`

**ES:** En el reto del laboratorio siete simularás un sumador browniano con Gillespie. En la unidad siete usaremos redes RC para la búsqueda de orden. Y la teoría de conductancias de la lección tres punto nueve sirve para diseñar computadores químicos.

**EN:** In the lab seven challenge you will simulate a Brownian adder with Gillespie. In unit seven we will use RC networks for order finding. And the conductance theory of lesson 3.9 serves to design chemical computers.

### [03:23.1] Common mistakes — `slide`

**ES:** Errores comunes: creer que el cómputo browniano sin reloj es gratis. Ignorar la potencia de refrigeración de los dispositivos criogénicos. Confundir la difusión determinista de una red RC con el muestreo estocástico. Y comparar sustratos sin fijar la tarea y la precisión.

**EN:** Common mistakes: believing clockless Brownian computation is free. Ignoring the cooling power of cryogenic devices. Confusing the deterministic diffusion of an RC network with stochastic sampling. And comparing substrates without fixing the task and the precision.

### [03:41.7] Summary — `manim:S09`

**ES:** En resumen: los circuitos brownianos computan con tokens que se difunden y pagan su velocidad con disipación. Los SQUID son neuronas termodinámicas criogénicas, las redes RC difunden voltaje sobre un grafo, y las reacciones químicas computan con concentraciones. Cada sustrato tiene una primitiva y un límite propios.

**EN:** In summary: Brownian circuits compute with diffusing tokens and pay for their speed with dissipation. SQUIDs are cryogenic thermodynamic neurons, RC networks diffuse voltage over a graph, and chemical reactions compute with concentrations. Each substrate has its own primitive and its own limit.

### [04:03.1] Self-assessment — `slide`

**ES:** Para practicar: calcula el tiempo de primer paso de una caminata libre. Calcula la entropía disipada por paso con un sesgo de dos. Explica por qué hacen falta trinquetes. Y escribe la dinámica de una red RC.

**EN:** To practice: compute the first-passage time of a free walk. Compute the entropy dissipated per step with a bias of two. Explain why ratchets are needed. And write the dynamics of an RC network.

## Key equations
- $$\langle T\rangle_{\text{free}} = \frac{n(n+1)}{2k},\qquad \langle T\rangle_{\text{biased}} \approx \frac{n}{k_+ - k_-}$$ — First-passage times of a token over $n$ sites (free with reflecting start; biased).
- $$\Delta s_{\text{step}} = \ln(k_+/k_-)$$ — Entropy dissipated per net step (in $k_B$).
- $$C\,\dot V = -L\,V$$ — RC network: diffusion with the graph Laplacian $L$.

## Summary
- Brownian tokens: Hub, CJoin, Ratchet; time = first passage.
- 20 sites: free ≈ 210 (CV 0.84); biased k₊ = 2k₋ ≈ 19 (CV 0.38), cost ln 2 per step.
- rf-SQUID: cryogenic thermodynamic neuron; mechanical Langevin devices.
- RC diffusion ($C\dot V = -LV$) and chemical reaction networks.

## Further reading
- [26] Y. Utsumi et al., Computation time and thermodynamic uncertainty relation of Brownian circuits, 2022.
- [27] P. Raux, C. Goupil and G. Verley, Thermodynamic circuits for chemical reaction networks, 2025.
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
