# Lesson 1.6 — Thermal noise

**Unit:** Unit 1 — Thermodynamics and information  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Compute the Johnson–Nyquist noise of a resistor: $S_V = 4k_BTR$, $V_{\text{rms}} = \sqrt{4k_BTR\,\Delta f}$.
- Derive the $k_BT/C$ noise of a capacitor by equipartition and understand why it does not depend on $R$.
- Compare device energy scales with $k_BT$ and decide when noise is a problem or a resource.

## Prerequisites
- Lesson 1.2: Boltzmann distribution and equipartition.
- Lesson 0.1: RC circuit and energy $\tfrac12 CV^2$.

## Narrated script

### [00:04.2] Introduction — `manim:S01`

**ES:** Conecta un osciloscopio muy sensible a una resistencia sin ninguna fuente y verás un voltaje que nunca se queda quieto. No es un defecto del instrumento: es el movimiento térmico de los electrones. Ese ruido fija el piso de cualquier circuito analógico y es precisamente la materia prima de un computador termodinámico. En esta lección lo vamos a cuantificar.

**EN:** Connect a very sensitive oscilloscope to a resistor with no source at all and you will see a voltage that never sits still. It is not a defect of the instrument: it is the thermal motion of the electrons. That noise sets the floor of every analog circuit and is precisely the raw material of a thermodynamic computer. In this lesson we will quantify it.

### [00:26.6] Intuition — `manim:S02`

**ES:** Dentro de un conductor, los electrones chocan sin cesar con la red de átomos, que vibra a temperatura T. En cada instante, por puro azar, hay un pequeño exceso de carga en un extremo o en el otro, y eso produce un voltaje entre los terminales. Cuanto más caliente el material y mayor la resistencia, más grandes son estas fluctuaciones. El voltaje promedio es cero, pero su varianza no.

**EN:** Inside a conductor, electrons collide endlessly with the lattice of atoms, which vibrates at temperature T. At each instant, by pure chance, there is a small excess of charge at one end or the other, and that produces a voltage across the terminals. The hotter the material and the larger the resistance, the larger these fluctuations. The average voltage is zero, but its variance is not.

### [00:51.2] Johnson–Nyquist noise — `manim:S03`

**ES:** En 1928, Johnson midió este ruido y Nyquist lo explicó. La densidad espectral del voltaje en circuito abierto es plana, es decir, ruido blanco, con valor 4 k_B T R por unidad de ancho de banda. El voltaje cuadrático medio en un ancho de banda Δf es 4 k_B T R Δf. Fíjate en la estructura: es la energía térmica, k_B T, multiplicada por la resistencia, que mide cuánto disipa el material. Es un primer ejemplo del teorema de fluctuación y disipación: lo que disipa, también fluctúa.

**EN:** In 1928, Johnson measured this noise and Nyquist explained it. The spectral density of the open-circuit voltage is flat, that is, white noise, with value 4 k_B T R per unit bandwidth. The mean-square voltage in a bandwidth Δf is 4 k_B T R Δf. Notice the structure: it is the thermal energy, k_B T, times the resistance, which measures how much the material dissipates. It is a first example of the fluctuation–dissipation theorem: what dissipates also fluctuates.

### [01:27.4] kT/C noise — `manim:S04`

**ES:** Ahora pongamos un capacitor en paralelo con la resistencia. El capacitor filtra las frecuencias altas: el voltaje se vuelve un proceso de Ornstein y Uhlenbeck, con memoria. Lo que ves es una simulación de ese proceso. El histograma del voltaje es gaussiano, y su varianza es k_B T/C. Cambiemos la resistencia: con una resistencia grande, el ruido tiene más densidad espectral, pero el filtro es más angosto; con una pequeña, al revés. Los dos efectos se compensan exactamente. La varianza no depende de R.

**EN:** Now let's put a capacitor in parallel with the resistor. The capacitor filters out high frequencies: the voltage becomes an Ornstein–Uhlenbeck process, with memory. What you see is a simulation of that process. The voltage histogram is Gaussian, and its variance is k_B T/C. Let's change the resistance: with a large resistor, the noise has more spectral density, but the filter is narrower; with a small one, the opposite. The two effects cancel exactly. The variance does not depend on R.

### [02:01.7] Derivation by equipartition — `manim:S05`

**ES:** Hay una forma inmediata de llegar a k_B T/C. La energía del capacitor es ½ C V². En equilibrio, el voltaje sigue la distribución de Boltzmann, que es una gaussiana con varianza k_B T/C. Es el teorema de equipartición: cada grado de libertad cuadrático tiene en promedio un medio de k_B T de energía. También lo podemos ver con la integral espectral: 4 k_B T R por el ancho de banda efectivo del filtro, uno sobre cuatro R C, da otra vez k_B T/C.

**EN:** There is an immediate way to reach k_B T/C. The energy of the capacitor is ½ C V². At equilibrium, the voltage follows the Boltzmann distribution, which is a Gaussian with variance k_B T/C. This is the equipartition theorem: each quadratic degree of freedom holds, on average, one half of k_B T of energy. We can also see it with the spectral integral: 4 k_B T R times the filter's effective bandwidth, one over four R C, again gives k_B T/C.

### [02:35.0] Numerical example — `manim:S06`

**ES:** Hagamos números a trescientos kelvin. Una resistencia de un megaohmio medida con un ancho de banda de un megahercio tiene un ruido de unos ciento veintinueve microvoltios eficaces. Un capacitor de un femtofaradio, típico de un nodo de un chip moderno, fluctúa unos dos milivoltios. Con un picofaradio, el ruido baja a sesenta y cuatro microvoltios. Y la energía de una señal digital en ese nodo de un femtofaradio, con cero coma ocho voltios, es unas setenta y siete mil veces k_B T: el ruido térmico es irrelevante para la lógica digital, a costa de mucha energía.

**EN:** Let's run numbers at three hundred kelvin. A one-megaohm resistor measured with a one-megahertz bandwidth has a noise of about one hundred twenty-nine microvolts rms. A one-femtofarad capacitor, typical of a node in a modern chip, fluctuates about two millivolts. With one picofarad, the noise drops to sixty-four microvolts. And the energy of a digital signal on that one-femtofarad node, at 0.8 volts, is about seventy-seven thousand times k_B T: thermal noise is irrelevant to digital logic, at the cost of a lot of energy.

### [03:12.3] Problem or resource — `manim:S07`

**ES:** Comparemos las escalas en una sola regla logarítmica de energía. En un extremo, k_B T y la cota de Landauer. En el otro, la energía de conmutar un nodo digital, decenas de miles de veces mayor, que garantiza que el ruido nunca voltee un bit. El cómputo termodinámico se ubica deliberadamente cerca de k_B T: diseña dispositivos donde la señal y el ruido son comparables, para que el ruido haga el trabajo de muestrear.

**EN:** Let's compare the scales on a single logarithmic energy ruler. At one end, k_B T and the Landauer bound. At the other, the energy of switching a digital node, tens of thousands of times larger, which guarantees that noise never flips a bit. Thermodynamic computing deliberately sits close to k_B T: it designs devices where signal and noise are comparable, so that noise does the work of sampling.

### [03:39.2] Applications — `slide`

**ES:** En ingeniería, el ruido de Johnson limita sensores y amplificadores, y el ruido k_B T/C fija la precisión de los convertidores analógicos. En el cómputo termodinámico, el mismo ruido impulsa los osciladores acoplados que muestrean gaussianas y los pbits que fluctúan entre cero y uno.

**EN:** In engineering, Johnson noise limits sensors and amplifiers, and k_B T/C noise sets the precision of analog converters. In thermodynamic computing, the same noise drives the coupled oscillators that sample Gaussians and the pbits that fluctuate between zero and one.

### [03:58.6] Connections — `slide`

**ES:** En la próxima unidad escribiremos la ecuación de Langevin, que describe exactamente este voltaje ruidoso; veremos el proceso de Ornstein y Uhlenbeck en detalle, y el teorema de fluctuación y disipación, que generaliza la fórmula de Nyquist.

**EN:** In the next unit we will write the Langevin equation, which describes exactly this noisy voltage; we will study the Ornstein–Uhlenbeck process in detail, and the fluctuation–dissipation theorem, which generalizes Nyquist's formula.

### [04:14.4] Common mistakes — `slide`

**ES:** Errores comunes: creer que una resistencia más grande da más ruido total en un RC. Confundir densidad espectral con varianza. Usar la fórmula de Nyquist a frecuencias donde la mecánica cuántica importa. Y confundir el ruido térmico con el ruido de disparo o el ruido uno sobre efe.

**EN:** Common mistakes: believing a larger resistor gives more total noise in an RC. Confusing spectral density with variance. Using Nyquist's formula at frequencies where quantum mechanics matters. And confusing thermal noise with shot noise or one-over-f noise.

### [04:33.5] Summary — `manim:S11`

**ES:** En resumen: toda resistencia a temperatura T genera ruido blanco con densidad 4 k_B T R. Un capacitor en equilibrio fluctúa con varianza k_B T/C, por equipartición e independientemente de R. Los chips digitales se alejan de k_B T para ignorar el ruido; los termodinámicos se acercan para usarlo.

**EN:** In summary: every resistor at temperature T generates white noise with density 4 k_B T R. A capacitor at equilibrium fluctuates with variance k_B T/C, by equipartition and independently of R. Digital chips move away from k_B T to ignore noise; thermodynamic ones move close to use it.

### [04:55.1] Self-assessment — `slide`

**ES:** Para practicar: calcula el ruido de una resistencia de cincuenta ohmios en un gigahercio. Encuentra la capacidad que da un milivoltio de ruido. Demuestra la integral espectral del ruido k_B T/C. Y compara la energía de un nodo digital con k_B T.

**EN:** To practice: compute the noise of a fifty-ohm resistor over one gigahertz. Find the capacitance that gives one millivolt of noise. Prove the spectral integral of k_B T/C noise. And compare the energy of a digital node with k_B T.

## Key equations
- $$S_V(f) = 4k_BTR,\quad \langle V^2\rangle = 4k_BTR\,\Delta f$$ — Johnson–Nyquist noise (one-sided spectral density, open circuit).
- $$\langle V^2\rangle_{RC} = \frac{k_BT}{C}$$ — $kT/C$ noise: equipartition, independent of $R$.
- $$\tfrac12 C\langle V^2\rangle = \tfrac12 k_BT$$ — Equipartition for one quadratic degree of freedom.

## Summary
- Johnson–Nyquist: $S_V = 4k_BTR$ (white noise).
- RC: $\langle V^2\rangle = k_BT/C$, independent of $R$.
- 1 fF at 300 K: $\approx 2$ mV of noise.
- Digital: signal $\gg k_BT$; thermodynamic: signal $\sim k_BT$.

## Further reading
- [1] C. W. Gardiner, Handbook of Stochastic Methods (Ornstein–Uhlenbeck processes).
- [6] T. Conte et al., Thermodynamic Computing, 2019.
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, 2025.
