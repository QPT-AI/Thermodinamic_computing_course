# Lesson 1.4 — Maxwell's demon and the Szilard engine

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Describe the Maxwell's demon paradox and why it seems to violate the second law.
- Compute the work extracted by the Szilard engine: $k_B T\ln 2$ per bit of information.
- Explain Bennett's resolution: the cost appears when erasing the demon's memory.

## Prerequisites
- Lesson 1.1: second law and isothermal work.
- Lesson 1.3: Shannon and Gibbs entropy.

## Narrated script

### [00:05.9] Introduction — `manim:S01`

**ES:** En 1867 James Clerk Maxwell imaginó un pequeño ser que vigila una puerta entre dos cámaras de gas. Sin hacer trabajo, solo mirando y abriendo la puerta en el momento justo, parece capaz de separar moléculas rápidas de lentas y crear una diferencia de temperatura de la nada. Esa paradoja tardó más de un siglo en resolverse, y su solución es el corazón de la termodinámica de la información.

**EN:** In 1867 James Clerk Maxwell imagined a tiny being guarding a door between two chambers of gas. Without doing work, just watching and opening the door at the right moment, it seems able to separate fast molecules from slow ones and create a temperature difference out of nothing. That paradox took more than a century to resolve, and its solution is the heart of the thermodynamics of information.

### [00:32.6] Intuition — `manim:S02`

**ES:** Mira el demonio en acción. Cuando una molécula rápida se acerca desde la izquierda, abre la puerta y la deja pasar a la derecha. Cuando una lenta se acerca desde la derecha, la deja pasar a la izquierda. Con el tiempo, la cámara derecha se calienta y la izquierda se enfría. Con esa diferencia de temperatura podríamos mover un motor. Si el demonio no gasta energía, hemos construido una máquina de movimiento perpetuo de segunda especie. Algo tiene que fallar.

**EN:** Watch the demon in action. When a fast molecule approaches from the left, it opens the door and lets it through to the right. When a slow one approaches from the right, it lets it through to the left. Over time, the right chamber heats up and the left one cools down. With that temperature difference we could drive an engine. If the demon spends no energy, we have built a perpetual motion machine of the second kind. Something has to give.

### [01:01.1] The Szilard engine — `manim:S03`

**ES:** Leó Szilard simplificó el problema al extremo en 1929: una sola molécula en una caja a temperatura T. Primero se inserta una pared en el medio. Después el demonio mira de qué lado está la molécula: adquiere un bit de información. Con ese bit, coloca un pistón del lado correcto y deja que la molécula lo empuje mientras se expande lentamente, tomando calor del baño. Al final la molécula vuelve a ocupar toda la caja. Se ha extraído trabajo, y el ciclo puede repetirse.

**EN:** Leó Szilard simplified the problem to the extreme in 1929: a single molecule in a box at temperature T. First a wall is inserted in the middle. Then the demon looks at which side the molecule is on: it acquires one bit of information. With that bit, it places a piston on the correct side and lets the molecule push it while it expands slowly, taking heat from the bath. At the end the molecule occupies the whole box again. Work has been extracted, and the cycle can repeat.

### [01:32.5] The extracted work — `manim:S04`

**ES:** Calculemos el trabajo. Para un gas de una molécula, la ecuación de estado es p V = k_B T. En la expansión isotérmica de la mitad del volumen al volumen completo, el trabajo extraído es la integral de p dV, que vale k_B T ln 2. Ese trabajo sale del calor del baño: la energía interna no cambia. Un bit de información se convirtió en k_B T ln 2 de trabajo. Con un ciclo por segundo, eso parece violar la segunda ley.

**EN:** Let's compute the work. For a one-molecule gas, the equation of state is p V = k_B T. In the isothermal expansion from half the volume to the full volume, the extracted work is the integral of p dV, which equals k_B T ln 2. That work comes from the bath's heat: the internal energy does not change. One bit of information became k_B T ln 2 of work. At one cycle per second, this seems to violate the second law.

### [02:04.9] Bennett's resolution — `manim:S05`

**ES:** Durante décadas se pensó que el costo estaba en medir: que observar la molécula disipaba al menos k_B T ln 2. En 1982 Charles Bennett mostró que la medición puede hacerse de forma reversible. El costo inevitable está en otra parte: la memoria del demonio. Para repetir el ciclo, el demonio debe borrar el bit que guardó, y por el principio de Landauer, borrarlo cuesta al menos k_B T ln 2. El balance del ciclo completo es cero en el mejor de los casos. La segunda ley se salva, pero solo si contamos la información como una cantidad física.

**EN:** For decades it was thought the cost lay in measuring: that observing the molecule dissipated at least k_B T ln 2. In 1982 Charles Bennett showed that measurement can be done reversibly. The unavoidable cost is elsewhere: the demon's memory. To repeat the cycle, the demon must erase the bit it stored, and by Landauer's principle, erasing it costs at least k_B T ln 2. The balance over the full cycle is zero at best. The second law survives, but only if we count information as a physical quantity.

### [02:43.4] Entropy balance — `manim:S06`

**ES:** Hagamos el balance de entropía de un ciclo. Al medir, la memoria del demonio pasa de un estado conocido a un bit correlacionado con la molécula: la entropía de la memoria sube k_B ln 2, mientras la incertidumbre del gas baja lo mismo. Durante la expansión, el baño entrega calor y pierde k_B ln 2 de entropía. Al borrar, la memoria vuelve a cero y el baño recupera al menos k_B ln 2. Sumando todo, la entropía total no disminuye.

**EN:** Let's do the entropy balance of one cycle. On measuring, the demon's memory goes from a known state to a bit correlated with the molecule: the memory's entropy rises by k_B ln 2, while the gas's uncertainty drops by the same amount. During the expansion, the bath delivers heat and loses k_B ln 2 of entropy. On erasing, the memory returns to zero and the bath regains at least k_B ln 2. Adding everything up, the total entropy does not decrease.

### [03:16.3] Numerical example — `manim:S07`

**ES:** A trescientos kelvin, cada ciclo extrae como máximo 2,87 × 10⁻²¹ J. Si la medición tiene errores y el demonio acierta el lado con probabilidad noventa por ciento, la información útil es solo la información mutua entre la medición y la posición: uno menos la entropía binaria de cero coma uno, unos cero coma cinco tres bits. El trabajo máximo extraíble baja a cero coma cinco tres por k_B T ln 2, unos 1,5 × 10⁻²¹ J.

**EN:** At three hundred kelvin, each cycle extracts at most 2.87 × 10⁻²¹ J. If the measurement has errors and the demon gets the side right with ninety percent probability, the useful information is only the mutual information between measurement and position: one minus the binary entropy of 0.1, about 0.53 bits. The maximum extractable work drops to 0.53 times k_B T ln 2, about 1.5 × 10⁻²¹ J.

### [03:50.5] Applications — `slide`

**ES:** Hoy existen demonios reales: motores de información que usan retroalimentación sobre partículas coloidales o sobre electrones individuales. Con mediciones imperfectas, el trabajo máximo es k_B T por la información mutua. Para el cómputo, la lección es clara: medir y controlar puede ser casi gratis, pero reiniciar memorias no. En el reto del laboratorio dos simularás una máquina de Szilard y cerrarás el ciclo.

**EN:** Real demons exist today: information engines that use feedback on colloidal particles or on single electrons. With imperfect measurements, the maximum work is k_B T times the mutual information. For computing, the lesson is clear: measuring and controlling can be almost free, but resetting memories is not. In the lab two challenge you will simulate a Szilard engine and close the cycle.

### [04:17.7] Connections — `slide`

**ES:** El demonio conecta lo que vimos sobre entropía de Shannon con el principio de Landauer de la próxima lección. En la unidad tres veremos la generalización de la igualdad de Jarzynski con retroalimentación y la termodinámica del reinicio.

**EN:** The demon connects what we saw about Shannon entropy with Landauer's principle in the next lesson. In unit three we will see the generalization of the Jarzynski equality with feedback and the thermodynamics of reset.

### [04:32.4] Common mistakes — `slide`

**ES:** Errores frecuentes: creer que el costo está en medir, cuando está en borrar. Pensar que el demonio viola la segunda ley, cuando lo que ocurre es que olvidamos su memoria. Olvidar que la expansión debe ser lenta. Y suponer el trabajo completo cuando la medición es ruidosa.

**EN:** Frequent mistakes: believing the cost is in measuring, when it is in erasing. Thinking the demon violates the second law, when what happens is that we forgot its memory. Forgetting that the expansion must be slow. And assuming the full work when the measurement is noisy.

### [04:49.7] Summary — `manim:S11`

**ES:** En resumen: el demonio de Maxwell usa información para extraer trabajo. La máquina de Szilard convierte un bit en k_B T ln 2 de trabajo. La segunda ley se salva porque la memoria del demonio debe borrarse, y borrar un bit cuesta al menos lo mismo. La información es un recurso termodinámico.

**EN:** In summary: Maxwell's demon uses information to extract work. The Szilard engine turns one bit into k_B T ln 2 of work. The second law survives because the demon's memory must be erased, and erasing a bit costs at least as much. Information is a thermodynamic resource.

### [05:10.2] Self-assessment — `slide`

**ES:** Para practicar: deriva el trabajo de la expansión. Calcula el trabajo promedio si la pared se coloca a un tercio del volumen. Encuentra el trabajo máximo con una medición que acierta el ochenta por ciento. Y señala en qué paso se paga el costo.

**EN:** To practice: derive the work of the expansion. Compute the average work if the wall is placed at one third of the volume. Find the maximum work with a measurement that is right eighty percent of the time. And identify the step where the cost is paid.

## Key equations
- $$W_{\text{ext}} = \int_{V/2}^{V} \frac{k_BT}{V'}dV' = k_BT\ln 2$$ — Work extracted by the Szilard engine per cycle (one bit).
- $$W_{\text{erase}} \ge k_BT\ln 2$$ — Landauer cost of resetting the demon's memory (Bennett's resolution).
- $$W_{\max} = k_BT\,I(X;M)$$ — Maximum work with an imperfect measurement (mutual information in nats).

## Summary
- The demon turns information into work.
- Szilard: one bit $\to k_BT\ln 2$ of work extracted from the bath.
- Bennett: measuring can be reversible; erasing the memory costs $\ge k_BT\ln 2$.
- With a noisy measurement: $W_{\max} = k_BT\,I(X;M)$.

## Further reading
- [9] C. H. Bennett, Notes on Landauer's principle, reversible computation and Maxwell's demon, 2003.
- [10] D. H. Wolpert, The stochastic thermodynamics of computation, 2019.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics (chapter on information and feedback).
