# Lesson 11.3 — Thermalizers: compiling stochastic programs

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define a thermodynamic kernel: clamp the inputs of an EBM, let it thermalize, read the outputs.
- Fit a target kernel by variational compilation (forward KL, positive and negative phases).
- Bound how compilation error accumulates through a deep stochastic program.

## Prerequisites
- Lesson 11.2: parametrized stochastic circuits.
- Lesson 4.8: RBMs and contrastive divergence.

## Narrated script

### [00:06.3] Introduction — `manim:S01`

**ES:** Torx describe un programa estocástico como un circuito de compuertas. Pero el chip Z1 no ejecuta compuertas arbitrarias: solo sabe muestrear modelos de Ising con conexiones locales. ¿Cómo se traduce un programa a lo que el chip sabe hacer? El artículo compañero de Extropic, termalizar programas estocásticos, propone compilar cada compuerta en un pequeño modelo basado en energía.

**EN:** Torx describes a stochastic program as a circuit of gates. But the Z1 chip does not execute arbitrary gates: it only knows how to sample Ising models with local connections. How is a program translated into what the chip can do? Extropic's companion paper, thermalizing stochastic programs, proposes compiling each gate into a small energy-based model.

### [00:30.1] The thermodynamic kernel — `manim:S02`

**ES:** La idea es fijar. Tomamos un modelo basado en energía con espines de entrada, ocultos y de salida. Fijamos las entradas a x, dejamos que el resto se termalice y leemos las salidas. La distribución de las salidas dada la entrada es un núcleo de transición: los ocultos se marginalizan, nunca se leen. Si sumamos a la energía cualquier función solo de la entrada, el núcleo no cambia: es una libertad de calibre.

**EN:** The idea is clamping. We take an energy-based model with input, hidden and output spins. We clamp the inputs to x, let the rest thermalize and read the outputs. The distribution of the outputs given the input is a transition kernel: the hidden spins are marginalized, never read. If we add to the energy any function of the input alone, the kernel does not change: it is a gauge freedom.

### [00:57.2] Variational compilation — `manim:S03`

**ES:** Para compilar, minimizamos la divergencia de Kullback-Leibler del núcleo objetivo al núcleo del modelo, promediada sobre las entradas: es máxima verosimilitud condicional. El gradiente tiene dos fases, como en la divergencia contrastiva. En la fase positiva fijamos entrada y salida y muestreamos los ocultos. En la fase negativa fijamos solo la entrada. Cada compuerta se entrena por separado.

**EN:** To compile, we minimize the Kullback-Leibler divergence from the target kernel to the model kernel, averaged over inputs: it is conditional maximum likelihood. The gradient has two phases, as in contrastive divergence. In the positive phase we clamp input and output and sample the hidden spins. In the negative phase we clamp only the input. Each gate is trained separately.

### [01:22.9] A tiny thermalizer — `manim:S04`

**ES:** Lo probamos nosotros: un núcleo objetivo al azar de dos bits a dos bits, compilado en una máquina de Boltzmann con gradientes exactos por enumeración. Sin espines ocultos, la distancia de variación total queda en cero coma dos dos: un Ising de pares no puede expresar el núcleo. Con un oculto, cero coma cero uno dos; con dos, prácticamente cero. Y si limitamos la intensidad de los acoplamientos, como en un chip real, el error sube: cero coma dos con un tope de cero coma dos cinco, cero coma cero cero tres con un tope de tres.

**EN:** We test it ourselves: a random target kernel from two bits to two bits, compiled into a Boltzmann machine with exact gradients by enumeration. Without hidden spins, the total variation distance stays at 0.22: a pairwise Ising model cannot express the kernel. With one hidden spin, 0.012; with two, practically zero. And if we cap the strength of the couplings, as in a real chip, the error rises: 0.2 with a cap of 0.25, 0.003 with a cap of three.

### [01:58.2] Errors through depth — `manim:S05`

**ES:** Un programa profundo encadena muchos núcleos compilados. Por la regla de la cadena, la divergencia sobre trayectorias es la suma de los errores de cada núcleo, y cualquier lectura final tiene un error menor o igual: en el peor caso crece de forma lineal con la profundidad. Pero si los núcleos contraen, el error se satura. Lo vemos: con un programa casi determinista, el error pasa de cero coma cero dos a cero coma tres uno en treinta pasos; con un programa que contrae, se queda en cero coma cero cero tres, bajo la cota de cero coma uno.

**EN:** A deep program chains many compiled kernels. By the chain rule, the divergence over trajectories is the sum of the errors of each kernel, and any final readout has an error less than or equal: in the worst case it grows linearly with depth. But if the kernels contract, the error saturates. We see it: with an almost deterministic program, the error goes from 0.02 to 0.31 in thirty steps; with a contracting program, it stays at 0.003, under the bound of 0.1.

### [02:33.4] What the paper shows — `manim:S06`

**ES:** El artículo demuestra el marco en simulación con THRML, sobre un modelo del dispositivo Z1. En un Ising de tres cuerpos compilado con espines ocultos, el error estacionario baja de cero coma cuatro seis a cero coma cero dos cuatro al relajar el tope de acoplamiento. En un circuito gaussiano para diseño de experimentos, el programa compilado logra un error de cero coma dos cinco nueve, igual al posterior exacto, frente a cero coma tres cero cinco al azar. Los autores advierten que todo programa compilado es aproximado y que no hay aún validación en un chip físico.

**EN:** The paper demonstrates the framework in simulation with THRML, on a model of the Z1 device. In a three-body Ising model compiled with hidden spins, the stationary error drops from 0.46 to 0.024 as the coupling cap is relaxed. In a Gaussian circuit for experiment design, the compiled program achieves an error of 0.259, equal to the exact posterior, against 0.305 at random. The authors warn that every compiled program is approximate and that there is no validation on a physical chip yet.

### [03:11.1] Applications — `slide`

**ES:** El flujo: escribe el programa en torx, compila cada compuerta en un modelo fijado, reparte espines ocultos y topes de acoplamiento, y valida primero cada compuerta y después la medida que importa a la tarea. Un ajuste final sobre trayectorias puede ayudar, con cuidado de no premiar trampas.

**EN:** The workflow: write the program in torx, compile each gate into a clamped model, distribute hidden spins and coupling caps, and validate first each gate and then the measure that matters for the task. A final tuning over trajectories can help, taking care not to reward cheating.

### [03:29.8] Common mistakes — `slide`

**ES:** Errores comunes: esperar que un Ising de pares sin ocultos exprese cualquier núcleo. Ignorar los topes de acoplamiento y la topología del chip. Confiar solo en el error por compuerta. Y presentar una compilación simulada como evidencia de hardware.

**EN:** Common mistakes: expecting a pairwise Ising model without hidden spins to express any kernel. Ignoring the coupling caps and topology of the chip. Relying only on the per-gate error. And presenting a simulated compilation as hardware evidence.

### [03:46.0] Summary — `manim:S09`

**ES:** En resumen, un termalizador realiza un núcleo estocástico fijando las entradas de un modelo basado en energía y leyendo sus salidas. Se compila minimizando una divergencia con fases positiva y negativa, y los espines ocultos le dan expresividad. Los errores se suman a lo largo del programa, en el peor caso linealmente, y se saturan si los núcleos contraen.

**EN:** In summary, a thermalizer realizes a stochastic kernel by clamping the inputs of an energy-based model and reading its outputs. It is compiled by minimizing a divergence with positive and negative phases, and hidden spins give it expressivity. Errors add up along the program, linearly in the worst case, and saturate if the kernels contract.

### [04:09.3] Self-assessment — `slide`

**ES:** Para practicar: escribe el núcleo de un modelo fijado. Explica la libertad de calibre. Nombra las fases del gradiente. Y acota el error estacionario de un programa que contrae.

**EN:** To practice: write the kernel of a clamped model. Explain the gauge freedom. Name the phases of the gradient. And bound the stationary error of a contracting program.

## Key equations
- $$\tilde P^F(y\mid x;\phi) = \frac{\sum_w e^{-E_\phi(x,w,y)}}{\sum_{w,y'} e^{-E_\phi(x,w,y')}}$$ — Thermodynamic kernel: clamp x, marginalize hidden w, read y.
- $$-\nabla_\phi\log\tilde P^F = \mathbb E_{w,y'\mid x}[\Phi_\phi] - \mathbb E_{w\mid x,y}[\Phi_\phi],\quad \Phi_\phi = -\nabla_\phi E_\phi$$ — Negative minus positive phase (Amico et al. 2026).
- $$D_{\mathrm{KL}}(P\,\|\,\tilde P_\phi) = \sum_\ell \varepsilon_\ell,\qquad \tilde\delta_L \le \frac{\max_\ell \iota_\ell}{1-\rho_0}\ \ (\rho \le \rho_0 < 1)$$ — Additive error budget; saturation for contracting kernels.

## Summary
- Thermalizer: clamp inputs, thermalize, read outputs = Markov kernel.
- Compile by forward KL; positive/negative phases; per-gate training.
- Own toy: TV 0.22 (0 hidden) → 0.012 (1) → ~0 (2) [S].
- Depth: error adds up (worst case linear), saturates if kernels contract [S].

## Further reading
- M. Amico et al., Thermalizing stochastic programs, arXiv:2608.01615 (2026).
- G. Verdon et al., A framework for stochastic differentiable programming, arXiv:2608.01612 (2026).
- G. E. Hinton, Training products of experts by minimizing contrastive divergence, Neural Computation 14, 1771 (2002).
