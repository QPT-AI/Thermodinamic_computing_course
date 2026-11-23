# Lesson 0.1 — AI's energy wall

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain where the switching energy $\tfrac12 C V^2$ and the dynamic power $P = \alpha C V^2 f$ come from.
- Describe Dennard scaling and why it ended.
- Argue why moving data costs more than computing (communication energy $\propto C V^2$, $C \propto$ length).
- Recognize the von Neumann bottleneck with the roofline model.

## Prerequisites
- Basic circuits: capacitor, resistor, energy $\tfrac12 C V^2$.
- Scientific notation and logarithms.

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** La inteligencia artificial está chocando contra un muro, y no es un muro de algoritmos sino de energía. Hoy la capacidad de la red eléctrica es uno de los principales obstáculos para construir centros de datos. En esta primera lección responderemos una pregunta concreta: ¿a dónde va realmente la energía de una GPU? La respuesta nos dirá por qué tiene sentido buscar una forma de computar radicalmente distinta.

**EN:** Artificial intelligence is hitting a wall, and it is not a wall of algorithms but of energy. Today grid capacity is one of the main obstacles to building data centers. In this first lesson we answer a concrete question: where does a GPU's energy actually go? The answer will tell us why it makes sense to look for a radically different way of computing.

### [00:30.1] Intuition — `manim:S02`

**ES:** Piensa en una fábrica muy eficiente cuyo almacén está al otro lado de la ciudad. Fabricar una pieza cuesta poco; lo caro es el camión que trae la materia prima y se lleva el producto. Un chip moderno funciona igual: el núcleo aritmético es la fábrica y la memoria es el almacén. Cada dato viaja por cables, y cada cable es un pequeño capacitor que hay que cargar y descargar. Cuanto más largo el cable, más carga hay que mover y más energía se pierde como calor.

**EN:** Think of a very efficient factory whose warehouse is on the other side of town. Making a part is cheap; what is expensive is the truck that brings the raw material and takes the product away. A modern chip works the same way: the arithmetic core is the factory and memory is the warehouse. Every datum travels along wires, and every wire is a small capacitor that must be charged and discharged. The longer the wire, the more charge must be moved and the more energy is lost as heat.

### [00:58.9] Visual explanation — `manim:S03`

**ES:** Veamos qué pasa cuando un cable cambia de cero a uno. Una fuente de voltaje V empuja carga a través de una resistencia hacia un capacitor C. La curva verde muestra el voltaje del capacitor, que sube de forma exponencial. La fuente entrega una energía igual a C V². La mitad queda guardada en el capacitor, y la otra mitad se disipa en la resistencia como calor. Lo sorprendente es que esa mitad no depende del valor de la resistencia: una resistencia pequeña da una corriente grande y breve, una resistencia grande da una corriente pequeña y larga, pero el área bajo la curva de potencia es la misma. Cuando el cable vuelve a cero, la energía guardada también se disipa. Cada ciclo completo cuesta C V².

**EN:** Let's see what happens when a wire switches from zero to one. A voltage source V pushes charge through a resistor into a capacitor C. The green curve shows the capacitor voltage, which rises exponentially. The source delivers an energy equal to C V². Half is stored in the capacitor, and the other half is dissipated in the resistor as heat. The surprise is that this half does not depend on the resistance: a small resistor gives a large, brief current, a large resistor gives a small, long current, but the area under the power curve is the same. When the wire returns to zero, the stored energy is dissipated too. Each full cycle costs C V².

### [01:44.3] Formal theory — `manim:S04`

**ES:** Si un chip tiene una capacidad total conmutada C, funciona a voltaje V y a frecuencia f, y en cada ciclo solo una fracción α de los nodos cambia de estado, la potencia dinámica es P = α C V² f. Cada factor tiene un significado físico. La capacidad crece con el número de transistores y con la longitud de los cables. El voltaje entra al cuadrado, por eso bajarlo era la palanca más poderosa. Y la frecuencia mide cuántas veces por segundo pagamos ese precio.

**EN:** If a chip has a total switched capacitance C, runs at voltage V and frequency f, and in each cycle only a fraction α of the nodes switch, the dynamic power is P = α C V² f. Each factor has a physical meaning. Capacitance grows with the number of transistors and with wire length. Voltage enters squared, which is why lowering it was the most powerful lever. And frequency measures how many times per second we pay that price.

### [02:16.2] Dennard scaling — `manim:S05`

**ES:** Durante décadas, la industria vivió del escalado de Dennard. Si reducimos todas las dimensiones de un transistor por un factor k, su capacidad baja por k, el voltaje baja por k y la frecuencia puede subir por k. La potencia por transistor cae entonces por k². Pero en el mismo espacio caben k² transistores más, así que la densidad de potencia queda constante: chips más rápidos y densos sin calentarse más. Hacia mediados de la década de dos mil, el voltaje dejó de bajar, porque por debajo de cierto umbral las fugas y el ruido térmico hacen poco confiable al transistor. Con el voltaje fijo, la densidad de potencia empieza a crecer como k², y las frecuencias se estancan.

**EN:** For decades, the industry lived off Dennard scaling. If we shrink all dimensions of a transistor by a factor k, its capacitance drops by k, voltage drops by k and frequency can rise by k. Power per transistor then falls by k². But k² more transistors fit in the same area, so power density stays constant: faster, denser chips that don't run hotter. Around the mid-2000s, voltage stopped dropping, because below a certain threshold leakage and thermal noise make the transistor unreliable. With voltage fixed, power density starts to grow as k², and clock frequencies stall.

### [03:02.5] Numerical example — `manim:S06`

**ES:** Hagamos cuentas con valores típicos, como estimación de orden de magnitud. Un cable en el chip tiene una capacidad del orden de 0,2 fF por micrómetro. Un cable de un milímetro tiene entonces unos doscientos femtofaradios. Con un voltaje de cero coma ocho voltios, una transición disipa la mitad de C V², unos sesenta y cuatro femtojulios. Una compuerta lógica local, con un femtofaradio, cuesta unas doscientas veces menos. Las mediciones clásicas en tecnología de cuarenta y cinco nanómetros lo confirman: una suma de punto flotante de treinta y dos bits cuesta menos de un picojulio, pero leer esos treinta y dos bits de la memoria DRAM externa cuesta del orden de seiscientos cuarenta picojulios. Mover el dato cuesta cientos de veces más que operar con él.

**EN:** Let's run the numbers with typical values, as an order-of-magnitude estimate. An on-chip wire has a capacitance of about 0.2 fF per micrometer. A one-millimeter wire then has about two hundred femtofarads. At 0.8 volts, one transition dissipates half of C V², about sixty-four femtojoules. A local logic gate, at one femtofarad, costs about two hundred times less. Classic measurements in 45-nanometer technology confirm it: a 32-bit floating-point add costs less than one picojoule, but reading those 32 bits from external DRAM costs on the order of six hundred forty picojoules. Moving the datum costs hundreds of times more than operating on it.

### [03:52.8] The von Neumann bottleneck — `manim:S07`

**ES:** En la arquitectura de von Neumann, la memoria y el procesador están separados y se comunican por un bus. El modelo roofline lo resume en una gráfica. El eje horizontal es la intensidad aritmética: cuántas operaciones hacemos por cada byte que traemos de memoria. El rendimiento alcanzable es el mínimo entre el pico de cómputo y el ancho de banda multiplicado por la intensidad. A la izquierda del codo, el chip espera a la memoria. La decodificación de un modelo de lenguaje con lote uno vive ahí: cada peso se lee una vez para hacer apenas dos operaciones.

**EN:** In the von Neumann architecture, memory and processor are separate and communicate over a bus. The roofline model sums it up in one plot. The horizontal axis is arithmetic intensity: how many operations we perform per byte fetched from memory. Attainable performance is the minimum of the compute peak and bandwidth times intensity. Left of the knee, the chip waits for memory. Batch-one decoding of a language model lives there: each weight is read once to do just two operations.

### [04:28.3] Applications — `slide`

**ES:** Volvamos a la pregunta inicial. En una GPU, gran parte de la energía se va en mover datos entre los registros, la memoria interna, la memoria externa y la red. Otra parte se va en garantizar márgenes de voltaje para que cada bit sea determinista frente al ruido. Y cuando el algoritmo es probabilístico, como la difusión o el muestreo de tokens, además gastamos energía en fabricar aleatoriedad con generadores pseudoaleatorios. En el reto del laboratorio uno medirás la energía por muestra aleatoria de tu propia GPU.

**EN:** Back to the opening question. In a GPU, much of the energy goes into moving data between registers, on-chip memory, external memory and the network. Another part goes into guaranteeing voltage margins so every bit is deterministic against noise. And when the algorithm is probabilistic, like diffusion or token sampling, we also spend energy manufacturing randomness with pseudorandom generators. In the lab one challenge you will measure the energy per random sample on your own GPU.

### [05:01.2] Connections — `slide`

**ES:** Esta lección plantea la tesis del curso. Si la aleatoriedad es tan cara de fabricar y el ruido tan caro de suprimir, ¿por qué no usar directamente las fluctuaciones térmicas para computar, y hacerlo localmente, donde están los datos? En la unidad uno veremos el límite fundamental de energía por bit, y en la unidad cinco aprenderemos a separar la energía del tejido de cómputo, de la entrada y salida, y del pegamento digital.

**EN:** This lesson states the thesis of the course. If randomness is so expensive to manufacture and noise so expensive to suppress, why not use thermal fluctuations directly to compute, and do it locally, where the data is? In unit one we will see the fundamental energy limit per bit, and in unit five we will learn to separate the energy of the compute fabric, of input and output, and of the digital glue.

### [05:28.5] Common mistakes — `slide`

**ES:** Cuatro confusiones frecuentes. La disipación por transición no depende de la resistencia: siempre es la mitad de C V². Contar operaciones no basta, porque con frecuencia domina el movimiento de datos. La ley de Moore y el escalado de Dennard no son lo mismo: la densidad siguió creciendo, pero la potencia por área dejó de ser constante. Y no confundas potencia con energía: la métrica justa es la energía por tarea, por ejemplo julios por token.

**EN:** Four frequent confusions. Dissipation per transition does not depend on the resistance: it is always half of C V². Counting operations is not enough, because data movement often dominates. Moore's law and Dennard scaling are not the same: density kept growing, but power per area stopped being constant. And don't confuse power with energy: the fair metric is energy per task, for example joules per token.

### [05:58.2] Summary — `manim:S11`

**ES:** En resumen: cada transición de un nodo cuesta C V² por ciclo, y la potencia dinámica es α C V² f. El fin del escalado de Dennard hizo que la potencia, y no los transistores, sea el recurso escaso. Mover datos cuesta cientos de veces más que operar con ellos, y la memoria separada del cómputo limita el rendimiento. Ese es el muro energético que el cómputo termodinámico intenta rodear.

**EN:** In summary: each node transition costs C V² per cycle, and dynamic power is α C V² f. The end of Dennard scaling made power, not transistors, the scarce resource. Moving data costs hundreds of times more than operating on it, and memory separated from compute limits performance. That is the energy wall that thermodynamic computing tries to get around.

### [06:25.4] Self-assessment — `slide`

**ES:** Comprueba tu comprensión con cuatro preguntas. Calcula el calor disipado al cargar un capacitor con dos resistencias distintas. Aplica el escalado de Dennard con un factor uno coma cuatro. Repite el cálculo con el voltaje fijo. Y encuentra el codo del roofline para un chip de cien teraflops con un terabyte por segundo de ancho de banda.

**EN:** Check your understanding with four questions. Compute the heat dissipated when charging a capacitor through two different resistors. Apply Dennard scaling with a factor of 1.4. Repeat the calculation with voltage fixed. And find the roofline knee for a hundred-teraflop chip with one terabyte per second of bandwidth.

## Key equations
- $$E_{\text{src}} = C V^2,\quad E_{\text{st}} = E_{\text{dis}} = \tfrac12 C V^2$$ — Charging a capacitor from a fixed source: half is stored and half is dissipated, for any $R$.
- $$P_{\text{dyn}} = \alpha\, C\, V^2 f$$ — Dynamic power: activity factor, switched capacitance, voltage and frequency.
- $$\text{Dennard: } C\to C/k,\ V\to V/k,\ f\to kf \Rightarrow P/\text{area} = \text{const}$$ — Shrinking dimensions by $k$ keeps power density constant if voltage also drops.
- $$\text{Perf.} = \min(\pi_{\max},\ \beta_{\text{mem}} \cdot I)$$ — Roofline model: compute peak versus bandwidth times arithmetic intensity $I$ (FLOP/byte).

## Summary
- Each charge–discharge cycle of a node dissipates $C V^2$, independent of the resistance.
- $P = \alpha C V^2 f$: voltage squared was the big lever of Dennard scaling.
- Since ~2005 voltage no longer drops: power is the scarce resource (not transistors).
- Moving a datum costs hundreds of times more than operating on it; von Neumann separates memory and compute.

## Further reading
- [6] T. Conte et al., Thermodynamic Computing (CCC workshop report), 2019.
- [7] Quanta Magazine, Thermodynamic Computers Go With the (Energy) Flow, 2026.
- [21] Extropic, Thermodynamic Computing From Zero to One, 2025.
- Video V2: Thermodynamic AI and the Fluctuation Frontier — P. Coles.
