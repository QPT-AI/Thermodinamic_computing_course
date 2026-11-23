# Lesson 7.6 — Physical realization with RC networks

**Unit:** Unit 7 — Diffusion computing and the Shor analogy  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Implement the Cayley diffusion as an RC network $C_0\dot V = -LV$ and bound its error by $e^{-2gt/C_0}$.
- Account for the physical resources: $\Omega(r)$ nodes and about $2\log_2 B$ bits of readout precision.
- Quantify the effect of capacitance mismatch and of $k_BT/C$ readout noise.

## Prerequisites
- Lesson 5.5: RC diffusion networks.
- Lesson 7.4: the diffusion order-finding theorem.

## Narrated script

### [00:05.9] Introduction — `manim:S01`

**ES:** El teorema de la lección siete punto cuatro supone un difusor físico: un dispositivo que promedia en todos los nodos a la vez. La realización más natural es una red de resistencias y capacitores, como la de la lección cinco punto cinco. Hoy vemos qué tan bien funciona y, sobre todo, cuánto cuesta de verdad.

**EN:** The theorem of lesson 7.4 assumes a physical diffuser: a device that averages at all nodes at once. The most natural realization is a network of resistors and capacitors, like the one in lesson 5.5. Today we see how well it works and, above all, how much it really costs.

### [00:25.9] The RC network — `manim:S02`

**ES:** Cada nodo del grafo de Cayley es un capacitor C_0 a tierra, y cada arista es una conductancia g. Las leyes de Kirchhoff dan C_0 V̇ = −L V, con L el laplaciano del grafo: el voltaje se difunde como el calor, en tiempo continuo. Inyectando carga en la identidad, el voltaje normalizado ahí se acerca a uno sobre r con un error menor que e^(−2gt/C_0), de forma exacta, sin aproximaciones de discretización. Para r = 33, tras una unidad de tiempo el error real es de cinco diezmillonésimas, frente a la cota de cero coma uno cuatro.

**EN:** Each node of the Cayley graph is a capacitor C_0 to ground, and each edge is a conductance g. Kirchhoff's laws give C_0 V̇ = −L V, with L the graph Laplacian: voltage diffuses like heat, in continuous time. Injecting charge at the identity, the normalized voltage there approaches one over r with an error smaller than e^(−2gt/C_0), exactly, without discretization approximations. For r = 33, after one time unit the actual error is five ten-millionths, against the bound of 0.14.

### [01:05.9] Resource: nodes — `manim:S03`

**ES:** El primer costo son los nodos. La red necesita al menos r nodos, uno por elemento del grupo, y r puede ser comparable a N. Peor aún: construir un ciclo de r nodos supone conocer r. La solución honesta usa una dirección por cada residuo módulo N, es decir, N nodos, y deja que la carga ocupe solo la órbita. Para un número de dos mil cuarenta y ocho bits, eso es un número de nodos con más de seiscientas cifras.

**EN:** The first cost is nodes. The network needs at least r nodes, one per group element, and r can be comparable to N. Worse: building a cycle of r nodes assumes knowing r. The honest solution uses one address per residue modulo N, that is, N nodes, and lets the charge occupy only the orbit. For a two-thousand-forty-eight-bit number, that is a number of nodes with more than six hundred digits.

### [01:35.5] Resource: precision — `manim:S04`

**ES:** El segundo costo es la precisión. Las lecturas para órdenes vecinos, uno sobre r y uno sobre r + 1, difieren en 1/(r(r + 1)). Para distinguir órdenes hasta B hace falta precisión absoluta del orden de 1/B²: unos 2 log₂ B bits. Para treinta y tres son diez bits; para cinco mil trescientos trece, veinticinco. Para un número criptográfico serían miles de bits analógicos: algo que ningún voltímetro alcanza.

**EN:** The second cost is precision. The readings for neighboring orders, one over r and one over r + 1, differ by 1/(r(r + 1)). To distinguish orders up to B, absolute precision of order 1/B² is needed: about 2 log₂ B bits. For thirty-three that is ten bits; for five thousand three hundred thirteen, twenty-five. For a cryptographic number it would be thousands of analog bits: something no voltmeter achieves.

### [02:07.9] Capacitance mismatch — `manim:S05`

**ES:** Las conductancias desiguales solo cambian la velocidad; los capacitores desiguales cambian el resultado. En equilibrio, el voltaje en la identidad es su capacitancia dividida por la suma total, así que la lectura es r(1 + ε̄)/(1 + ε_e). Para redondear bien hace falta ∣ε̄ − ε_e∣ < (1 + ε_e)/(2r). Con r = 33 y diez mil redes con desajustes aleatorios, un medio por ciento acierta el noventa y nueve coma seis por ciento de las veces, un uno por ciento el ochenta y ocho, y un tres por ciento apenas el cuarenta.

**EN:** Unequal conductances only change the speed; unequal capacitors change the result. At equilibrium, the voltage at the identity is its capacitance divided by the total sum, so the reading is r(1 + ε̄)/(1 + ε_e). To round correctly one needs ∣ε̄ − ε_e∣ < (1 + ε_e)/(2r). With r = 33 and ten thousand networks with random mismatches, half a percent is right 99.6 percent of the time, one percent 88 percent, and three percent only 40 percent.

### [02:44.9] Readout noise — `manim:S06`

**ES:** Finalmente, el ruido térmico de la lectura. Un muestreo con capacitor C tiene una varianza de k_B T/C. Para alcanzar la precisión necesaria hay que promediar muchas muestras: con un picofaradio, un voltio y temperatura ambiente, para órdenes de mil hacen falta unas doscientas sesenta y cinco mil muestras; para un millón, del orden de diez a la diecisiete; para mil millones, diez a la veintinueve. Son números de un modelo simple, no cotas universales, pero muestran que contar celdas no basta para demostrar factibilidad.

**EN:** Finally, the thermal noise of the readout. Sampling with a capacitor C has a variance of k_B T/C. To reach the required precision many samples must be averaged: with one picofarad, one volt and room temperature, for orders of a thousand about two hundred sixty-five thousand samples are needed; for a million, on the order of ten to the seventeen; for a billion, ten to the twenty-nine. These are numbers from a simple model, not universal bounds, but they show that counting cells is not enough to demonstrate feasibility.

### [03:20.1] Applications — `slide`

**ES:** Un prototipo honesto debe reproducir el núcleo de calor exacto en casos pequeños, calibrar los capacitores por debajo de uno sobre dos r, y reportar nodos, bits de precisión y muestras por lectura. En el proyecto cinco simularás la red con desajuste y ruido.

**EN:** An honest prototype must reproduce the exact heat kernel in small cases, calibrate the capacitors below one over two r, and report nodes, bits of precision and samples per readout. In project five you will simulate the network with mismatch and noise.

### [03:37.6] Common mistakes — `slide`

**ES:** Errores comunes: contar pasos de difusión e ignorar los nodos. Construir un ciclo de longitud r, que supone la respuesta. Creer que dos log₂ B bits son baratos, cuando son precisión analógica. Y calibrar conductancias ignorando el desajuste de capacitores.

**EN:** Common mistakes: counting diffusion steps and ignoring the nodes. Building a cycle of length r, which assumes the answer. Believing that two log₂ B bits are cheap, when they are analog precision. And calibrating conductances while ignoring capacitor mismatch.

### [03:56.4] Summary — `manim:S09`

**ES:** En resumen: una red RC realiza la difusión exactamente, con error que decae como e^(−2gt/C_0). Pero necesita del orden de r nodos, unos dos log₂ B bits de precisión, capacitores ajustados mejor que uno sobre dos r, y una cantidad de muestras que crece como la cuarta potencia del orden. El tiempo es corto; el costo se ha movido al hardware.

**EN:** In summary: an RC network realizes diffusion exactly, with error decaying as e^(−2gt/C_0). But it needs on the order of r nodes, about two log₂ B bits of precision, capacitors matched better than one over two r, and a number of samples growing as the fourth power of the order. Time is short; the cost has moved to the hardware.

### [04:22.8] Self-assessment — `slide`

**ES:** Para practicar: deduce la lectura de equilibrio con conservación de carga. Calcula los bits para órdenes de hasta un millón. Calcula la tolerancia de desajuste para un orden de mil. Y explica por qué hace falta una dirección por residuo.

**EN:** To practice: derive the equilibrium reading with charge conservation. Compute the bits for orders up to a million. Compute the mismatch tolerance for an order of a thousand. And explain why one address per residue is needed.

## Key equations
- $$C_0\dot V = -LV,\quad L = g\sum_{t=0}^{M}\big(2I - T^{2^t} - T^{-2^t}\big),\quad 0 \le v_e(t) - \tfrac1r \le e^{-2gt/C_0}$$ — Exact continuous-time RC diffusion on the Cayley orbit.
- $$\frac{V_0}{V_e(\infty)} = r\,\frac{1+\bar\varepsilon}{1+\varepsilon_e},\qquad |\bar\varepsilon - \varepsilon_e| < \frac{1+\varepsilon_e}{2r}$$ — Capacitance mismatch changes the equilibrium reading.
- $$\frac1r - \frac1{r+1} = \frac{1}{r(r+1)}\ \Rightarrow\ \approx 2\log_2 B\ \text{bits},\qquad J\,C_{\text{read}} \ge \frac{64\,k_BT\,B^4}{V_0^2}$$ — Precision and kT/C sample requirements (simple readout model).

## Summary
- RC network: C₀ dV/dt = −LV; error ≤ e^(−2gt/C₀) (r = 33: 5·10⁻⁷ at t = 1 vs bound 0.14) [S].
- Resources: Ω(r) nodes (N with residue addresses); ≈ 2 log₂ B bits.
- Mismatch: need ∣ε̄ − ε_e∣ < 1/(2r); r = 33: 0.5 % → 99.6 %, 1 % → 88 %, 3 % → 40 % correct [S].
- kT/C readout: samples ∝ B⁴ (10³ → 2.65·10⁵; 10⁹ → 2.65·10²⁹).

## Further reading
- Cadavid et al., Treatise on diffusion-driven factorization (course data/), Section 20, 2026.
- [32] C. A. Cadavid et al., An integer factorization algorithm which uses diffusion as a computational engine, 2023.
- [25] D. Melanson et al., Thermodynamic computing system for AI applications, Nat. Commun. 16, 3757 (2025).
