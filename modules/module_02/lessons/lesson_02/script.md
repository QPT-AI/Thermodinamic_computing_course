# Lesson 2.2 — The Langevin equation

**Unit:** Unit 2 — Stochastic dynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write the underdamped Langevin equation and its overdamped limit $\dot x = \mu f(x) + \sqrt{2\mu k_BT}\,\xi(t)$.
- Relate friction, noise and temperature through $D = \mu k_BT$ (Einstein relation).
- Estimate device time scales (inertial $m/\gamma$, relaxation $\gamma/\kappa$, $RC$).

## Prerequisites
- Lesson 2.1: Wiener process and Itô calculus.
- Lesson 1.2: Boltzmann distribution.

## Narrated script

### [00:04.7] Introduction — `manim:S01`

**ES:** Ya tenemos ruido puro. Ahora agreguemos física: fuerzas, fricción y masa. El resultado es la ecuación de Langevin, la ecuación de movimiento de una partícula en un baño térmico. Es la ecuación que obedecen los voltajes de un circuito ruidoso, los osciladores de un chip termodinámico y, como veremos, la que usan los algoritmos para muestrear distribuciones.

**EN:** We already have pure noise. Now let's add physics: forces, friction and mass. The result is the Langevin equation, the equation of motion of a particle in a heat bath. It is the equation obeyed by the voltages of a noisy circuit, the oscillators of a thermodynamic chip and, as we will see, the one algorithms use to sample distributions.

### [00:27.7] Intuition — `manim:S02`

**ES:** Imagina una canica en un tazón lleno de miel que, además, tiembla. Tres cosas actúan sobre ella: la pendiente del tazón la empuja hacia el fondo, la miel frena su movimiento, y los temblores la sacuden al azar. Si la miel es poco viscosa, la canica oscila antes de detenerse. Si es muy viscosa, la canica simplemente se arrastra hacia el fondo, sin oscilar. En ambos casos nunca se queda quieta: el temblor la mantiene explorando alrededor del mínimo.

**EN:** Imagine a marble in a bowl full of honey that is also shaking. Three things act on it: the slope of the bowl pushes it toward the bottom, the honey slows its motion, and the shaking jostles it at random. If the honey is thin, the marble oscillates before stopping. If it is very thick, the marble simply creeps toward the bottom, without oscillating. In both cases it never sits still: the shaking keeps it exploring around the minimum.

### [00:56.8] Underdamped Langevin — `manim:S03`

**ES:** En ecuaciones: masa por aceleración es igual a la fuerza del potencial, menos la fricción γ v, más una fuerza aleatoria de intensidad √(2 γ k_B T). A la izquierda ves la posición frente al tiempo; a la derecha, el espacio de fases, posición contra velocidad. La trayectoria gira en espiral hacia el mínimo, pero el ruido la mantiene dando vueltas en una nube. Esa nube es la distribución de Boltzmann en el espacio de fases.

**EN:** In equations: mass times acceleration equals the force from the potential, minus the friction γ v, plus a random force of strength √(2 γ k_B T). On the left you see position versus time; on the right, phase space, position against velocity. The trajectory spirals toward the minimum, but the noise keeps it circling in a cloud. That cloud is the Boltzmann distribution in phase space.

### [01:25.5] Overdamped limit — `manim:S04`

**ES:** Cuando la fricción domina, la inercia se vuelve irrelevante: la velocidad se ajusta instantáneamente a la fuerza. Eliminamos la masa y obtenemos la ecuación sobreamortiguada: ẋ = μ f(x) + √(2 μ k_B T) ξ(t), con movilidad μ = 1/γ. Las dos simulaciones usan el mismo potencial; con fricción alta, la trayectoria subamortiguada se vuelve indistinguible de la sobreamortiguada. Esta es la ecuación que usaremos casi siempre: es la del pozo doble de Landauer y la del solucionador lineal.

**EN:** When friction dominates, inertia becomes irrelevant: the velocity adjusts instantly to the force. We drop the mass and get the overdamped equation: ẋ = μ f(x) + √(2 μ k_B T) ξ(t), with mobility μ = 1/γ. Both simulations use the same potential; with high friction, the underdamped trajectory becomes indistinguishable from the overdamped one. This is the equation we will use almost always: it is the one for Landauer's double well and for the linear solver.

### [02:01.1] Einstein relation — `manim:S05`

**ES:** ¿Por qué el ruido tiene exactamente esa intensidad? Si fuera mayor, el sistema se calentaría; si fuera menor, se enfriaría. Solo con intensidad 2 μ k_B T la distribución estacionaria es la de Boltzmann a temperatura T. El coeficiente de difusión es entonces D = μ k_B T: la relación de Einstein. La fricción y el ruido no son independientes; los fija la misma temperatura. El histograma de la simulación coincide con e^(−βV).

**EN:** Why does the noise have exactly that strength? If it were larger, the system would heat up; if smaller, it would cool down. Only with strength 2 μ k_B T is the stationary distribution Boltzmann at temperature T. The diffusion coefficient is then D = μ k_B T: the Einstein relation. Friction and noise are not independent; the same temperature fixes both. The simulation histogram matches e^(−βV).

### [02:31.9] Time scales — `manim:S06`

**ES:** Hay dos relojes. El tiempo inercial, m/γ, dice cuánto tarda la velocidad en olvidar su valor. El tiempo de relajación, γ/κ, con κ la rigidez del potencial, dice cuánto tarda la posición en volver al mínimo. Si el primero es mucho más corto, la descripción sobreamortiguada es exacta. Para una esfera de un micrómetro en agua, el tiempo inercial es de unos dos décimos de microsegundo. En un circuito, el papel de γ/κ lo juega R C: con un kiloohmio y un picofaradio, un nanosegundo.

**EN:** There are two clocks. The inertial time, m/γ, says how long the velocity takes to forget its value. The relaxation time, γ/κ, with κ the stiffness of the potential, says how long the position takes to return to the minimum. If the first is much shorter, the overdamped description is exact. For a one-micrometer sphere in water, the inertial time is about two tenths of a microsecond. In a circuit, the role of γ/κ is played by R C: with one kilohm and one picofarad, one nanosecond.

### [03:07.0] Applications — `slide`

**ES:** Esta ecuación aparecerá en todos los laboratorios de la primera mitad: el borrado de Landauer, el solucionador lineal de Ornstein y Uhlenbeck, los osciladores acoplados de Normal Computing. Y también es un algoritmo: para muestrear una distribución de Boltzmann solo necesitamos el gradiente del potencial.

**EN:** This equation will appear in every lab of the first half: Landauer erasure, the Ornstein–Uhlenbeck linear solver, Normal Computing's coupled oscillators. And it is also an algorithm: to sample a Boltzmann distribution we only need the gradient of the potential.

### [03:26.0] Connections — `slide`

**ES:** En la próxima lección escribiremos la ecuación de Fokker y Planck para la densidad. Luego estudiaremos el caso cuadrático, el proceso de Ornstein y Uhlenbeck, y el teorema de fluctuación y disipación, que justifica la relación de Einstein.

**EN:** In the next lesson we will write the Fokker–Planck equation for the density. Then we will study the quadratic case, the Ornstein–Uhlenbeck process, and the fluctuation–dissipation theorem, which justifies the Einstein relation.

### [03:41.7] Common mistakes — `slide`

**ES:** Errores frecuentes: elegir el ruido sin relacionarlo con la fricción, usar la ecuación sobreamortiguada cuando la inercia importa, olvidar el factor dos en la intensidad del ruido, y confundir la movilidad con el coeficiente de difusión.

**EN:** Frequent mistakes: choosing the noise without relating it to friction, using the overdamped equation when inertia matters, forgetting the factor of two in the noise strength, and confusing mobility with the diffusion coefficient.

### [03:57.1] Summary — `manim:S10`

**ES:** En resumen: la ecuación de Langevin combina fuerza, fricción y ruido. En el régimen de alta fricción se reduce a ẋ = μ f + √(2 μ k_B T) ξ. La relación de Einstein, D = μ k_B T, garantiza que el estado estacionario sea la distribución de Boltzmann, y las escalas de tiempo de los dispositivos deciden qué descripción usar.

**EN:** In summary: the Langevin equation combines force, friction and noise. In the high-friction regime it reduces to ẋ = μ f + √(2 μ k_B T) ξ. The Einstein relation, D = μ k_B T, guarantees that the stationary state is the Boltzmann distribution, and device time scales decide which description to use.

### [04:21.3] Self-assessment — `slide`

**ES:** Para practicar: escribe la ecuación para un potencial cuadrático y su varianza. Calcula el tiempo inercial para una esfera de cien nanómetros. Muestra que un ruido mal calibrado equivale a otra temperatura. Y calcula un tiempo de relajación RC.

**EN:** To practice: write the equation for a quadratic potential and its variance. Compute the inertial time for a hundred-nanometer sphere. Show that a miscalibrated noise is equivalent to another temperature. And compute an RC relaxation time.

## Key equations
- $$m\ddot x = -\gamma\dot x + f(x) + \sqrt{2\gamma k_BT}\,\xi(t)$$ — Underdamped Langevin ($\langle\xi(t)\xi(t')\rangle = \delta(t-t')$).
- $$\dot x = \mu f(x) + \sqrt{2\mu k_BT}\,\xi(t),\quad \mu = 1/\gamma$$ — Overdamped Langevin.
- $$D = \mu k_BT = \frac{k_BT}{\gamma}$$ — Einstein relation: guarantees Boltzmann equilibrium.
- $$\tau_{\text{in}} = m/\gamma,\qquad \tau_{\text{rel}} = \gamma/\kappa$$ — Inertial and relaxation scales; overdamped if $\tau_{\text{in}} \ll \tau_{\text{rel}}$.

## Summary
- Langevin = force + friction + noise.
- Overdamped: $\dot x = \mu f + \sqrt{2\mu k_BT}\,\xi$.
- Einstein: $D = \mu k_BT$ ⇒ Boltzmann stationary state.
- Scales: $m/\gamma$, $\gamma/\kappa$, $RC$.

## Further reading
- [1] Gardiner, Handbook of Stochastic Methods (Langevin equations).
- [2] Peliti and Pigolotti, Stochastic Thermodynamics, ch. 2.
- [25] Melanson et al., Thermodynamic computing system for AI applications, 2025.
