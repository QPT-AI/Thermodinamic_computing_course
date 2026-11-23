# Lesson 4.10 — Ising optimization and invertible probabilistic logic

**Unit:** Unit 4 — Energy-based models, Ising models and neural networks  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write Max-Cut as an Ising ground state: $J = -w$, $\text{cut} = \sum_{(i,j)} w_{ij}(1 - s_is_j)/2$.
- Build Boolean gates as energy penalties whose minima are the truth table, and run them backward by clamping outputs.
- Factor a small integer by clamping the output of a multiplier, and understand the limits of the approach.

## Prerequisites
- Lesson 4.4: simulated annealing.
- Lesson 4.5: pbits.

## Narrated script

### [00:06.9] Introduction — `manim:S01`

**ES:** Un modelo de Ising a temperatura baja se concentra en sus estados de mínima energía. Si logramos escribir un problema de forma que su solución sea el mínimo de una energía de Ising, podemos resolverlo dejando que un chip de pbits se enfríe. Muchos problemas de optimización combinatoria, como el corte máximo o la satisfacibilidad, admiten esa escritura. Y hay algo más sorprendente: los circuitos lógicos escritos así se pueden ejecutar hacia atrás.

**EN:** An Ising model at low temperature concentrates on its minimum-energy states. If we manage to write a problem so that its solution is the minimum of an Ising energy, we can solve it by letting a pbit chip cool down. Many combinatorial optimization problems, like maximum cut or satisfiability, admit that formulation. And there is something more surprising: logic circuits written this way can be run backward.

### [00:35.9] Max-Cut — `manim:S02`

**ES:** El problema del corte máximo pide dividir los nodos de un grafo en dos grupos de modo que el mayor número posible de aristas cruce de un grupo al otro. Asignemos un espín a cada nodo: más uno para un grupo y menos uno para el otro. Una arista está cortada si sus extremos tienen espines opuestos, y el corte vale Σ (1 − s_i s_j)/2. Maximizar el corte es minimizar una energía de Ising con acoplamientos antiferromagnéticos, J = −w.

**EN:** The maximum-cut problem asks to split the nodes of a graph into two groups so that as many edges as possible cross from one group to the other. Let's assign a spin to each node: plus one for one group and minus one for the other. An edge is cut if its endpoints have opposite spins, and the cut equals Σ (1 − s_i s_j)/2. Maximizing the cut is minimizing an Ising energy with antiferromagnetic couplings, J = −w.

### [01:08.2] Annealing a Max-Cut — `manim:S03`

**ES:** Tomemos un grafo aleatorio de diez nodos y dieciocho aristas. Por fuerza bruta sabemos que el corte máximo es catorce. Con pbits y un recocido de trescientos barridos, la red encuentra un corte de catorce en las cien corridas que probamos. Para grafos grandes no hay garantías, pero los pbits exploran muchas soluciones buenas en paralelo y muy rápido.

**EN:** Let's take a random graph with ten nodes and eighteen edges. By brute force we know the maximum cut is fourteen. With pbits and a three-hundred-sweep anneal, the network finds a cut of fourteen in all hundred runs we tried. For large graphs there are no guarantees, but pbits explore many good solutions in parallel and very fast.

### [01:30.9] Gates as energies — `manim:S04`

**ES:** Ahora un circuito lógico. Para la compuerta AND, con variables cero o uno, la penalización P = uv − 2uz − 2vz + 3z vale cero exactamente en las cuatro filas de la tabla de verdad, y es positiva en todas las demás. A β = 2, las cuatro filas válidas aparecen cada una con probabilidad cero coma dos tres: la red muestrea la tabla de verdad. Cualquier circuito se construye sumando las penalizaciones de sus compuertas.

**EN:** Now a logic circuit. For the AND gate, with variables zero or one, the penalty P = uv − 2uz − 2vz + 3z is exactly zero on the four rows of the truth table, and positive on all the others. At β = 2, the four valid rows each appear with probability 0.23: the network samples the truth table. Any circuit is built by adding the penalties of its gates.

### [02:02.8] Running logic backward — `manim:S05`

**ES:** Aquí está la magia. Fijemos la salida z = 1 y dejemos libres las entradas. La red encuentra la única entrada compatible, uno y uno, con probabilidad cero coma siete nueve. Si fijamos z = 0, reparte la probabilidad entre las tres entradas que dan cero. Es lógica invertible: el mismo circuito calcula hacia adelante, fijando las entradas, y hacia atrás, fijando las salidas.

**EN:** Here is the magic. Let's clamp the output z = 1 and leave the inputs free. The network finds the only compatible input, one and one, with probability 0.79. If we clamp z = 0, it spreads the probability over the three inputs that give zero. It is invertible logic: the same circuit computes forward, by clamping the inputs, and backward, by clamping the outputs.

### [02:29.5] Factoring by clamping — `manim:S06`

**ES:** Si invertimos un multiplicador, fijando su salida en un número N, las entradas buscan dos factores cuyo producto sea N. Es factorización sin algoritmo de factorización. Con un modelo de juguete para N = 143, con factores impares de cuatro bits, el recocido encuentra once por trece en setenta y nueve de doscientas corridas. Cuidado: esto no rompe la criptografía. El paisaje de energía de la factorización es muy rugoso, y el tiempo de búsqueda crece rápidamente con el número de bits.

**EN:** If we invert a multiplier, clamping its output to a number N, the inputs search for two factors whose product is N. It is factoring without a factoring algorithm. With a toy model for N = 143, with odd four-bit factors, annealing finds eleven times thirteen in seventy-nine of two hundred runs. Careful: this does not break cryptography. The energy landscape of factoring is very rugged, and the search time grows rapidly with the number of bits.

### [03:03.5] Applications — `slide`

**ES:** Cualquier problema QUBO, de variables binarias con costo cuadrático, se convierte en Ising con x = (1 + s)/2. La satisfacibilidad usa una penalización por cláusula. Los p-computadores en FPGA ya hacen miles de millones de volteos por segundo. Y en la unidad siete veremos un algoritmo de factorización por difusión con garantías demostradas.

**EN:** Any QUBO problem, of binary variables with quadratic cost, becomes Ising with x = (1 + s)/2. Satisfiability uses one penalty per clause. P-computers on FPGA already perform billions of flips per second. And in unit seven we will see a factoring-by-diffusion algorithm with proven guarantees.

### [03:27.8] Common mistakes — `slide`

**ES:** Errores comunes: penalizaciones demasiado débiles, que hacen más baratos los estados inválidos. Olvidar la constante al pasar de QUBO a Ising. Esperar soluciones en tiempo polinomial de problemas NP-difíciles. Y olvidar que los términos de orden alto necesitan espines auxiliares en hardware de pares.

**EN:** Common mistakes: penalties that are too weak, which make invalid states cheaper. Forgetting the constant when going from QUBO to Ising. Expecting polynomial-time solutions of NP-hard problems. And forgetting that higher-order terms need auxiliary spins on pairwise hardware.

### [03:48.4] Summary — `manim:S09`

**ES:** En resumen: muchos problemas de optimización son mínimos de energías de Ising, y los pbits los buscan enfriándose. Las compuertas lógicas se escriben como penalizaciones cuyos mínimos son la tabla de verdad, y fijando las salidas los circuitos corren hacia atrás. Es una herramienta poderosa, pero no elimina la dificultad intrínseca de los problemas.

**EN:** In summary: many optimization problems are minima of Ising energies, and pbits search for them by cooling down. Logic gates are written as penalties whose minima are the truth table, and by clamping the outputs circuits run backward. It is a powerful tool, but it does not remove the intrinsic difficulty of the problems.

### [04:10.9] Self-assessment — `slide`

**ES:** Para practicar: verifica la penalización AND. Escribe el Ising del corte máximo en un triángulo. Convierte la penalización a espines. Y explica por qué la salida fijada no da certeza a temperatura finita.

**EN:** To practice: check the AND penalty. Write the Ising model for the maximum cut on a triangle. Convert the penalty to spins. And explain why the clamped output does not give certainty at finite temperature.

## Key equations
- $$\text{cut}(s) = \sum_{i<j} w_{ij}\,\frac{1 - s_is_j}{2},\qquad J_{ij} = -w_{ij}$$ — Max-Cut as an Ising ground state.
- $$P_{\text{AND}}(u,v,z) = uv - 2uz - 2vz + 3z,\qquad x_k = \frac{1 + s_k}{2}$$ — AND gate penalty (zero exactly on its truth table) and the QUBO ↔ Ising map.
- $$p(x_{\text{in}}\mid x_{\text{out}}) \propto e^{-\beta P(x_{\text{in}}, x_{\text{out}})}$$ — Invertible logic: clamping outputs samples consistent inputs.

## Summary
- Optimization = Ising ground state; pbits search by annealing.
- Max-Cut: $J = -w$; 10 nodes, cut 14 found in 100/100 anneals.
- Gates as penalties; clamping outputs runs logic backward (AND: P(1,1 | z=1) = 0.79 at β = 2).
- Factoring by clamping a multiplier: works on toys, scales poorly.

## Further reading
- [17] K. Y. Camsari, B. M. Sutton and S. Datta, p-bits for probabilistic spin logic, 2019.
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, 2022.
- A. Lucas, Ising formulations of many NP problems, Front. Phys. 2, 5 (2014).
