# Lesson 1.5 — Landauer's principle

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain why erasing a bit has a minimum energy cost $k_B T \ln 2$.
- Derive the Landauer bound from the second law and from the free energy $F = U - TS$.
- Compute $k_B T \ln 2$ at different temperatures and compare it with real devices.
- Distinguish logical reversibility from thermodynamic reversibility (Bennett's computation).

## Prerequisites
- Lesson 1.1: laws of thermodynamics and free energy $F = U - TS$.
- Lesson 1.3: Shannon entropy $H = -\sum_i p_i \log p_i$ and Gibbs entropy.
- Lesson 1.4: Maxwell's demon and the Szilard engine.

## Narrated script

### [00:04.7] Introduction — `manim:S01`

**ES:** Tu teléfono se calienta cuando trabaja. Cada operación que realiza un procesador termina, tarde o temprano, convertida en calor. La pregunta de esta lección es sorprendentemente profunda: ¿existe un costo mínimo, impuesto por la física, para procesar información? En 1961 Rolf Landauer dio una respuesta precisa. No todas las operaciones cuestan, pero hay una que sí: borrar. Borrar un bit tiene un precio mínimo en energía, y ese precio depende solo de la temperatura.

**EN:** Your phone heats up when it works. Every operation a processor performs ends up, sooner or later, as heat. The question of this lesson is surprisingly deep: is there a minimum cost, imposed by physics, for processing information? In 1961 Rolf Landauer gave a precise answer. Not every operation costs something, but one does: erasing. Erasing a bit has a minimum price in energy, and that price depends only on temperature.

### [00:37.3] Intuition — `manim:S02`

**ES:** Imaginemos la memoria más simple posible: una caja con una sola partícula y una pared en el medio. Si la partícula está a la izquierda, el bit vale cero; si está a la derecha, vale uno. Borrar significa dejar el bit en cero sin importar su valor anterior. Una forma de hacerlo es quitar la pared y empujar un pistón desde la derecha hasta la mitad. Al final, la partícula está siempre a la izquierda. Observa lo que ocurrió: el espacio disponible se redujo a la mitad. Comprimir algo que está en contacto con un baño térmico exige trabajo, y ese trabajo sale como calor hacia el entorno.

**EN:** Picture the simplest possible memory: a box with a single particle and a wall in the middle. If the particle is on the left, the bit is zero; if it is on the right, it is one. Erasing means leaving the bit at zero regardless of its previous value. One way to do it is to remove the wall and push a piston from the right to the middle. At the end, the particle is always on the left. Notice what happened: the available space was cut in half. Compressing something in contact with a heat bath requires work, and that work leaves as heat into the environment.

### [01:14.5] Visual explanation — `manim:S03`

**ES:** Ahora una versión más realista: un pozo doble de potencial. Cada punto amarillo es una copia de la memoria, una partícula que tiembla por el ruido térmico, simulada con la dinámica de Langevin. Al inicio, la mitad de las copias está en el pozo izquierdo y la otra mitad en el derecho: el bit es desconocido. El protocolo de borrado tiene tres pasos. Primero bajamos la barrera, y las partículas se mezclan libremente. Después inclinamos el potencial hacia la izquierda, y todas se deslizan hacia el pozo del cero. Por último subimos la barrera de nuevo. El histograma verde muestra la distribución: empezó con dos picos iguales y terminó con un solo pico. Perdimos un bit de incertidumbre.

**EN:** Now a more realistic version: a double-well potential. Each amber dot is a copy of the memory, a particle jittering from thermal noise, simulated with Langevin dynamics. At the start, half the copies are in the left well and half in the right: the bit is unknown. The erasure protocol has three steps. First we lower the barrier, and the particles mix freely. Then we tilt the potential to the left, and they all slide into the zero well. Finally we raise the barrier again. The green histogram shows the distribution: it started with two equal peaks and ended with a single one. We lost one bit of uncertainty.

### [01:59.0] Formal theory — `manim:S04`

**ES:** Pongamos números a esa pérdida. La entropía de la memoria es S = −k_B Σ p ln p. Antes del borrado, cada estado tiene probabilidad un medio, así que la entropía vale k_B ln 2. Después, el estado cero tiene probabilidad uno, y la entropía es cero. La memoria perdió k_B ln 2 de entropía. Pero la segunda ley exige que la entropía total del universo no disminuya. Por lo tanto, el entorno debe ganar al menos esa cantidad. Un entorno a temperatura T que recibe un calor Q gana una entropía Q/T. Despejando, el calor disipado cumple Q ≥ k_B T ln 2. Esta es la cota de Landauer.

**EN:** Let's put numbers on that loss. The entropy of the memory is S = −k_B Σ p ln p. Before erasure, each state has probability one half, so the entropy is k_B ln 2. Afterwards, state zero has probability one, and the entropy is zero. The memory lost k_B ln 2 of entropy. But the second law requires that the total entropy of the universe does not decrease. Therefore the environment must gain at least that amount. An environment at temperature T that receives heat Q gains entropy Q/T. Solving, the dissipated heat satisfies Q ≥ k_B T ln 2. This is the Landauer bound.

### [02:47.4] Derivation — `manim:S05`

**ES:** Podemos llegar al mismo resultado con la energía libre, F = U − TS. En un proceso isotérmico, el trabajo que hacemos sobre el sistema es al menos el cambio de energía libre. Como los dos pozos son simétricos, la energía interna no cambia: ΔU = 0. Entonces el cambio de energía libre es menos T por el cambio de entropía, que vale k_B T ln 2. Y como la energía interna no cambió, todo ese trabajo se convierte en calor que sale hacia el baño. Las dos rutas, la de la entropía y la de la energía libre, dan la misma cota.

**EN:** We can reach the same result with the free energy, F = U − TS. In an isothermal process, the work we do on the system is at least the change in free energy. Since the two wells are symmetric, the internal energy does not change: ΔU = 0. So the change in free energy is minus T times the change in entropy, which equals k_B T ln 2. And since the internal energy did not change, all that work becomes heat flowing into the bath. Both routes, entropy and free energy, give the same bound.

### [03:24.5] Numerical example — `manim:S06`

**ES:** Calculemos el número. La constante de Boltzmann vale 1,380649 × 10⁻²³ J/K. A temperatura ambiente, trescientos kelvin, y con el logaritmo natural de dos, aproximadamente cero coma seis nueve tres, obtenemos 2,87 × 10⁻²¹ J por bit. La cota crece linealmente con la temperatura: si enfriamos el sistema a cuatro kelvin, baja unas setenta y cinco veces. Comparemos con el hardware. Según el pensum, una actualización de pbit en un chip tipo Z1 cuesta como máximo 7,4 × 10⁻¹⁴ J. Eso es unos veintiséis millones de veces la cota de Landauer. Los dispositivos actuales están muy lejos del límite fundamental.

**EN:** Let's compute the number. Boltzmann's constant is 1.380649 × 10⁻²³ J/K. At room temperature, three hundred kelvin, and with the natural log of two, about 0.693, we get 2.87 × 10⁻²¹ J per bit. The bound grows linearly with temperature: cooling the system to four kelvin lowers it about seventy-five times. Let's compare with hardware. According to the syllabus, one pbit update on a Z1-type chip costs at most 7.4 × 10⁻¹⁴ J. That is about twenty-six million times the Landauer bound. Today's devices are very far from the fundamental limit.

### [04:13.2] Reversibility — `manim:S07`

**ES:** ¿Qué operaciones están obligadas a pagar? Las que son lógicamente irreversibles, es decir, las que fusionan varias entradas en una misma salida. La compuerta NOT es una biyección: de la salida se recupera la entrada, y no exige disipar nada. La compuerta AND, en cambio, envía tres entradas distintas a la salida cero. Con entradas uniformes, entra la información de dos bits y sale apenas cero coma ochenta y uno. Se pierden unos uno coma diecinueve bits, y eso tiene un costo mínimo de Landauer. Charles Bennett mostró la salida: calcular de forma reversible, copiar el resultado y luego descalcular, deshaciendo los pasos intermedios. Así, el borrado obligatorio se reduce al mínimo.

**EN:** Which operations are forced to pay? The logically irreversible ones, that is, those that merge several inputs into the same output. The NOT gate is a bijection: the input can be recovered from the output, and it requires no dissipation. The AND gate, in contrast, sends three different inputs to output zero. With uniform inputs, two bits of information go in and only 0.81 come out. About 1.19 bits are lost, and that has a minimum Landauer cost. Charles Bennett showed the way out: compute reversibly, copy the result, then uncompute, undoing the intermediate steps. That way, mandatory erasure is kept to a minimum.

### [04:57.8] The cost of speed — `manim:S08`

**ES:** Hay una condición escondida: la cota de Landauer solo se alcanza si el borrado es infinitamente lento. Si el protocolo dura un tiempo τ finito, el sistema no alcanza a seguir el equilibrio y se disipa un trabajo extra. Para protocolos lentos, ese exceso decrece como uno sobre τ. La curva amarilla muestra el trabajo medio frente a la duración del protocolo: se acerca a la línea de Landauer, pero desde arriba. Este es el primer ejemplo de un compromiso fundamental del curso, que estudiaremos en la unidad tres: calcular rápido cuesta más energía.

**EN:** There is a hidden condition: the Landauer bound is reached only if erasure is infinitely slow. If the protocol lasts a finite time τ, the system cannot keep up with equilibrium and extra work is dissipated. For slow protocols, that excess decays as one over τ. The amber curve shows the mean work versus protocol duration: it approaches the Landauer line, but from above. This is the first example of a fundamental trade-off of the course, which we study in unit three: computing fast costs more energy.

### [05:32.3] Applications — `slide`

**ES:** ¿Por qué entonces los chips gastan millones de veces más? Primero, por confiabilidad: la probabilidad de que el ruido térmico voltee un bit decae exponencialmente con la altura de la barrera, así que un bit digital robusto necesita barreras de decenas de k_B T. Segundo, por la comunicación: mover un bit por un cable cuesta del orden de C V², sin relación con Landauer. Por eso el cómputo termodinámico no busca llegar al límite de Landauer, sino dejar de pagar por suprimir el ruido y usarlo como recurso. En el laboratorio dos simularás este borrado y medirás el trabajo en función de la duración del protocolo.

**EN:** So why do chips spend millions of times more? First, reliability: the probability that thermal noise flips a bit decays exponentially with the barrier height, so a robust digital bit needs barriers of tens of k_B T. Second, communication: moving a bit along a wire costs on the order of C V², unrelated to Landauer. That is why thermodynamic computing does not try to reach the Landauer limit, but to stop paying for suppressing noise and use it as a resource. In lab two you will simulate this erasure and measure the work as a function of protocol duration.

### [06:11.6] Connections — `slide`

**ES:** Este principio aparece en todo el curso. Resuelve la paradoja del demonio de Maxwell de la lección anterior: el demonio debe borrar su memoria, y ese borrado paga exactamente lo que había ganado. En la unidad tres veremos el trabajo y el calor a nivel de una sola trayectoria, la igualdad de Jarzynski y los límites de velocidad, que hacen preciso el costo del borrado rápido. Y en la unidad cinco compararemos la energía real de un pbit con esta cota.

**EN:** This principle appears throughout the course. It resolves the Maxwell's demon paradox from the previous lesson: the demon must erase its memory, and that erasure pays back exactly what it had gained. In unit three we will see work and heat at the level of a single trajectory, the Jarzynski equality and speed limits, which make the cost of fast erasure precise. And in unit five we will compare the real energy of a pbit with this bound.

### [06:41.1] Common mistakes — `slide`

**ES:** Cuatro errores frecuentes. Primero, creer que toda operación cuesta k_B T ln 2: solo el borrado lógicamente irreversible tiene un costo mínimo. Segundo, pensar que el costo se paga al medir: en la formulación de Landauer y Bennett se paga al borrar. Tercero, olvidar que la cota supone un bit completamente desconocido; si el bit ya se conoce, no hay entropía que eliminar. Y cuarto, creer que Landauer es lo que hoy limita a los chips; lo que domina son los márgenes de ruido y el movimiento de datos.

**EN:** Four frequent mistakes. First, believing every operation costs k_B T ln 2: only logically irreversible erasure has a minimum cost. Second, thinking the cost is paid when measuring: in the Landauer and Bennett formulation it is paid when erasing. Third, forgetting that the bound assumes a completely unknown bit; if the bit is already known, there is no entropy to remove. And fourth, believing Landauer is what limits chips today; what dominates are noise margins and data movement.

### [07:15.8] Summary — `manim:S12`

**ES:** Resumamos. Borrar un bit reduce la entropía de la memoria en k_B ln 2. La segunda ley obliga a expulsar al menos k_B T ln 2 de calor, unos 2,87 × 10⁻²¹ J a temperatura ambiente. Solo pagan las operaciones lógicamente irreversibles, y el límite solo se alcanza con protocolos lentos. La información es física.

**EN:** Let's summarize. Erasing a bit reduces the memory's entropy by k_B ln 2. The second law forces at least k_B T ln 2 of heat to be expelled, about 2.87 × 10⁻²¹ J at room temperature. Only logically irreversible operations pay, and the bound is reached only with slow protocols. Information is physical.

### [07:42.7] Self-assessment — `slide`

**ES:** Antes de seguir, pon a prueba tu comprensión. Calcula el calor mínimo para borrar un gigabyte a trescientos kelvin. Calcula el costo de reiniciar un bit que ya vale cero con probabilidad cero coma nueve. Explica por qué la compuerta NOT no tiene costo de Landauer y la AND sí. Y piensa qué ocurre con el trabajo de borrado si el protocolo se hace diez veces más rápido. Las soluciones están en la hoja de ejercicios de esta lección.

**EN:** Before moving on, test your understanding. Compute the minimum heat to erase one gigabyte at three hundred kelvin. Compute the cost of resetting a bit that is already zero with probability 0.9. Explain why the NOT gate has no Landauer cost and the AND gate does. And think about what happens to the erasure work if the protocol runs ten times faster. The solutions are in this lesson's exercise sheet.

## Key equations
- $$Q_{\text{dis}} \ge k_B T \ln 2$$ — Minimum heat released to the environment when erasing an unknown bit.
- $$S = -k_B \sum_i p_i \ln p_i$$ — Gibbs entropy of the memory; equals $k_B\ln 2$ for a uniform bit.
- $$W \ge \Delta F = \Delta U - T\Delta S$$ — Second law for isothermal processes; with $\Delta U = 0$ it gives $W \ge k_B T \ln 2$.
- $$k_B T \ln 2 \approx 2.87\times 10^{-21}\,\text{J} \;(T = 300\,\text{K})$$ — Numerical value of the bound at room temperature.

## Summary
- Erasing = merging states: the memory's entropy drops by $k_B \ln 2$ per bit.
- The second law forces a dissipation $Q \ge k_B T \ln 2$ ($\approx 2.87\times10^{-21}$ J at 300 K).
- Only logically irreversible operations have a minimum cost (Bennett: compute, copy, uncompute).
- The bound is reached only by quasi-static protocols; fast erasure dissipates an excess $\propto 1/\tau$.

## Further reading
- [8] R. Landauer, Irreversibility and heat generation in the computing process, IBM J. Res. Dev. 5, 183 (1961).
- [9] C. H. Bennett, Notes on Landauer's principle, reversible computation and Maxwell's demon (2003).
- [10] D. H. Wolpert, The stochastic thermodynamics of computation, J. Phys. A 52, 193001 (2019).
- Video V7 (supplementary): The Most Misunderstood Concept in Physics — Veritasium.
