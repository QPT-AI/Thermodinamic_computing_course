# Lesson 1.1 — Laws of thermodynamics and free energy

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- State the laws of thermodynamics and the notion of equilibrium.
- Interpret entropy as the logarithm of the number of microstates, $S = k_B \ln \Omega$.
- Use the free energy $F = U - TS$ to decide which state wins at a given temperature and to bound the work: $W \ge \Delta F$.

## Prerequisites
- Lesson 0.3: binomial and Gaussian distributions.
- Notions of energy, heat and temperature from basic physics.

## Narrated script

### [00:05.9] Introduction — `manim:S01`

**ES:** Un chip es una máquina térmica funcionando al revés: recibe trabajo eléctrico y lo convierte en calor. Si queremos computar con la física, y no a pesar de ella, necesitamos las reglas que gobiernan la energía, el calor y el desorden. En esta lección repasamos las leyes de la termodinámica y presentamos la cantidad que más usaremos en el curso: la energía libre.

**EN:** A chip is a heat engine running in reverse: it receives electrical work and turns it into heat. If we want to compute with physics, and not in spite of it, we need the rules that govern energy, heat and disorder. In this lesson we review the laws of thermodynamics and introduce the quantity we will use most in the course: free energy.

### [00:29.2] Intuition — `manim:S02`

**ES:** Pongamos en contacto dos cajas de partículas, una caliente y otra fría. En cada choque a través de la pared, dos partículas se reparten su energía al azar. Nadie le dice a la energía hacia dónde ir, y sin embargo la energía media de las dos cajas converge al mismo valor. Ese estado final, en el que ya no hay flujo neto, es el equilibrio térmico, y la temperatura es precisamente la cantidad que se iguala. La flecha del tiempo aparece sola, a partir de choques que son simétricos.

**EN:** Let's put two boxes of particles in contact, one hot and one cold. In each collision across the wall, two particles share their energy at random. Nobody tells the energy where to go, and yet the mean energy of the two boxes converges to the same value. That final state, with no net flow, is thermal equilibrium, and temperature is precisely the quantity that equalizes. The arrow of time emerges on its own, from collisions that are symmetric.

### [01:00.1] The laws — `manim:S03`

**ES:** La ley cero dice que el equilibrio térmico es transitivo, y eso permite definir la temperatura. La primera ley es la conservación de la energía: el cambio de energía interna es el calor que entra más el trabajo que se hace sobre el sistema. La segunda ley dice que la entropía total de un sistema aislado nunca disminuye; para un sistema en contacto con un baño a temperatura T, el cambio de entropía es al menos el calor recibido dividido por T. La tercera ley fija el cero: la entropía tiende a un mínimo cuando la temperatura tiende a cero.

**EN:** The zeroth law says thermal equilibrium is transitive, and that lets us define temperature. The first law is energy conservation: the change in internal energy is the heat that enters plus the work done on the system. The second law says the total entropy of an isolated system never decreases; for a system in contact with a bath at temperature T, the entropy change is at least the heat received divided by T. The third law sets the zero: entropy tends to a minimum as temperature tends to zero.

### [01:34.1] Entropy and microstates — `manim:S04`

**ES:** ¿Qué es la entropía? Boltzmann respondió: S = k_B ln Ω, donde Ω es el número de microestados compatibles con lo que observamos. Piensa en cien monedas. El macroestado cincuenta caras se puede lograr de muchísimas más maneras que el macroestado cien caras. Al crecer el número de monedas, la distribución se concentra alrededor de la mitad: su ancho relativo decae como uno sobre la raíz de N. La segunda ley es estadística: el sistema termina en los macroestados con más microestados simplemente porque son abrumadoramente más probables.

**EN:** What is entropy? Boltzmann answered: S = k_B ln Ω, where Ω is the number of microstates compatible with what we observe. Think of a hundred coins. The macrostate fifty heads can be achieved in vastly more ways than the macrostate a hundred heads. As the number of coins grows, the distribution concentrates around one half: its relative width decays as one over root N. The second law is statistical: the system ends up in the macrostates with more microstates simply because they are overwhelmingly more probable.

### [02:10.4] Free energy — `manim:S05`

**ES:** A temperatura fija, el sistema no minimiza su energía ni maximiza su entropía por separado: minimiza la energía libre, F = U − T S. Es una competencia. Considera dos estados: uno de energía baja con un solo microestado, y otro con energía ε más alta pero con mil microestados. A baja temperatura gana la energía y el sistema prefiere el estado bajo. Al subir la temperatura, el término de entropía, T S, crece hasta dominar, y la población se vuelca al estado de muchos microestados. La transición ocurre cuando las energías libres se igualan.

**EN:** At fixed temperature, the system neither minimizes its energy nor maximizes its entropy separately: it minimizes the free energy, F = U − T S. It is a competition. Consider two states: one with low energy and a single microstate, and another with energy ε higher but a thousand microstates. At low temperature energy wins and the system prefers the low state. As temperature rises, the entropy term, T S, grows until it dominates, and the population flips to the state with many microstates. The transition happens when the free energies are equal.

### [02:47.9] Work and free energy — `manim:S06`

**ES:** La energía libre tiene un significado operativo. En un proceso a temperatura constante, el trabajo que hay que hacer sobre un sistema para llevarlo de un estado a otro es al menos el cambio de energía libre: W ≥ ΔF. La igualdad solo se alcanza con procesos infinitamente lentos. La diferencia, W menos ΔF, es trabajo disipado como calor, y siempre es mayor o igual que cero. Esta desigualdad es la que, en la lección uno punto cinco, da el costo de borrar un bit.

**EN:** Free energy has an operational meaning. In a constant-temperature process, the work needed to take a system from one state to another is at least the change in free energy: W ≥ ΔF. Equality is reached only with infinitely slow processes. The difference, W minus ΔF, is work dissipated as heat, and it is always greater than or equal to zero. This inequality is what, in lesson 1.5, gives the cost of erasing a bit.

### [03:21.6] Numerical example — `manim:S07`

**ES:** Pongamos números al sistema de dos estados. Con una diferencia de energía de cero coma uno electronvoltios y mil microestados, la temperatura de transición es la energía dividida por k_B por el logaritmo de mil: unos ciento sesenta y ocho kelvin. A trescientos kelvin la diferencia de energía libre es negativa, unos menos setenta y nueve milielectronvoltios, y la fracción del sistema en el estado de muchos microestados es de aproximadamente noventa y cinco por ciento.

**EN:** Let's put numbers into the two-state system. With an energy gap of 0.1 electronvolts and a thousand microstates, the transition temperature is the energy divided by k_B times the log of a thousand: about one hundred sixty-eight kelvin. At three hundred kelvin the free-energy difference is negative, about minus seventy-nine millielectronvolts, and the fraction of the system in the many-microstate state is about ninety-five percent.

### [03:50.9] Applications — `slide`

**ES:** En un computador estas leyes son muy concretas. Por la primera ley, toda la potencia eléctrica termina como calor que hay que extraer. Por la segunda, borrar información exige expulsar entropía. Y en un chip termodinámico, el ruido térmico lleva al sistema hacia estados de baja energía libre: esa es la base del muestreo de Boltzmann.

**EN:** In a computer these laws are very concrete. By the first law, all electrical power ends up as heat that must be removed. By the second, erasing information requires expelling entropy. And in a thermodynamic chip, thermal noise drives the system toward low free-energy states: that is the basis of Boltzmann sampling.

### [04:12.3] Connections — `slide`

**ES:** En la siguiente lección pasaremos del conteo de microestados a la distribución de Boltzmann, y veremos que la energía libre es menos k_B T por el logaritmo de la función de partición. En la unidad tres refinaremos la desigualdad del trabajo con la igualdad de Jarzynski, que vale incluso para procesos rápidos.

**EN:** In the next lesson we will go from counting microstates to the Boltzmann distribution, and see that the free energy is minus k_B T times the log of the partition function. In unit three we will refine the work inequality with the Jarzynski equality, which holds even for fast processes.

### [04:31.4] Common mistakes — `slide`

**ES:** Cuidado con algunas confusiones: el calor es energía transferida, no temperatura. La entropía de un sistema sí puede disminuir, siempre que la del entorno aumente al menos lo mismo. Decir que la entropía es desorden es solo una metáfora. Y presta atención a la convención de signos del trabajo.

**EN:** Beware of some confusions: heat is transferred energy, not temperature. A system's entropy can decrease, as long as the environment's increases at least as much. Saying entropy is disorder is only a metaphor. And pay attention to the sign convention for work.

### [04:50.5] Summary — `manim:S11`

**ES:** En resumen: el equilibrio es el estado sin flujos netos, y la temperatura lo caracteriza. La energía se conserva y la entropía total no disminuye. La entropía cuenta microestados, y a temperatura fija el sistema minimiza la energía libre, F = U − T S, que además acota el trabajo necesario.

**EN:** In summary: equilibrium is the state with no net flows, and temperature characterizes it. Energy is conserved and total entropy does not decrease. Entropy counts microstates, and at fixed temperature the system minimizes the free energy, F = U − T S, which also bounds the required work.

### [05:11.9] Self-assessment — `slide`

**ES:** Para practicar: cuenta los microestados de cincuenta y de cien caras. Calcula la población del sistema de dos estados a cien kelvin. Aplica la primera ley a un balance de calor y trabajo. Y explica por qué la igualdad entre trabajo y energía libre exige un proceso infinitamente lento.

**EN:** To practice: count the microstates of fifty and of a hundred heads. Compute the population of the two-state system at a hundred kelvin. Apply the first law to a heat and work balance. And explain why equality between work and free energy requires an infinitely slow process.

## Key equations
- $$\Delta U = Q + W$$ — First law ($Q$ heat received, $W$ work done on the system).
- $$\Delta S_{\text{univ}} \ge 0,\qquad dS \ge \frac{\delta Q}{T}$$ — Second law (Clausius).
- $$S = k_B \ln \Omega$$ — Boltzmann entropy: number of compatible microstates.
- $$F = U - TS,\qquad W \ge \Delta F\ (T\ \text{constant})$$ — Helmholtz free energy and the bound on isothermal work.

## Summary
- Equilibrium: no net flows; temperature is what equalizes.
- First law: $\Delta U = Q + W$. Second law: $\Delta S_{\text{univ}} \ge 0$.
- $S = k_B\ln\Omega$: the second law is statistical.
- At fixed $T$, $F = U - TS$ is minimized; $W \ge \Delta F$, with equality only quasi-statically.

## Further reading
- [2] L. Peliti and S. Pigolotti, Stochastic Thermodynamics: An Introduction, 2021 (ch. 1).
- [10] D. H. Wolpert, The stochastic thermodynamics of computation, 2019 (section 2).
- Video V7: The Most Misunderstood Concept in Physics — Veritasium.
