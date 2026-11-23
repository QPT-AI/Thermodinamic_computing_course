# Lesson 0.7 — JAX essentials

**Unit:** Unit 0 — Orientation and math refresher  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Write pure functions and handle reproducible randomness with explicit PRNG keys.
- Vectorize with vmap, compile with jit and iterate with scan.
- Distinguish the gradient, the Jacobian–vector product (jvp) and the vector–Jacobian product (vjp).

## Prerequisites
- Python and NumPy.
- Lesson 0.4: matrices; partial derivatives and the chain rule.

## Narrated script

### [00:04.6] Introduction — `manim:S01`

**ES:** Todos los laboratorios del curso se programan en JAX, y los simuladores de hardware termodinámico, como THRML y Torx, están construidos sobre él. JAX es NumPy con tres superpoderes: transformaciones de funciones que vectorizan, compilan y derivan automáticamente. Su estilo funcional encaja con la física: un paso de simulación recibe un estado y devuelve el siguiente, sin efectos ocultos.

**EN:** Every lab in the course is programmed in JAX, and the thermodynamic hardware simulators, such as THRML and Torx, are built on it. JAX is NumPy with three superpowers: function transformations that vectorize, compile and differentiate automatically. Its functional style fits physics: a simulation step takes a state and returns the next one, with no hidden effects.

### [00:31.2] Pure functions — `manim:S02`

**ES:** Una función pura es una caja que solo depende de sus entradas y solo produce su salida. No lee variables globales que cambian, no imprime, no modifica nada afuera. Si la llamas dos veces con lo mismo, obtienes lo mismo. Esa disciplina es lo que permite a JAX transformar tus funciones con seguridad: puede rastrearlas, compilarlas y derivarlas porque sabe exactamente qué entra y qué sale.

**EN:** A pure function is a box that depends only on its inputs and only produces its output. It does not read changing global variables, does not print, does not modify anything outside. Call it twice with the same thing and you get the same thing. That discipline is what lets JAX transform your functions safely: it can trace, compile and differentiate them because it knows exactly what goes in and what comes out.

### [00:56.4] PRNG keys — `manim:S03`

**ES:** ¿Y la aleatoriedad? En NumPy, el generador guarda un estado oculto que cambia en cada llamada: eso no es puro. JAX hace explícito ese estado: una clave. La misma clave produce siempre los mismos números. Para obtener números nuevos, se divide la clave con split, que genera claves hijas independientes, formando un árbol. Cada rama del árbol alimenta una parte del programa. Regla de oro: nunca reutilices una clave.

**EN:** And randomness? In NumPy, the generator keeps a hidden state that changes on every call: that is not pure. JAX makes that state explicit: a key. The same key always produces the same numbers. To get new numbers, you split the key, which creates independent child keys, forming a tree. Each branch of the tree feeds one part of the program. Golden rule: never reuse a key.

### [01:25.1] vmap — `manim:S04`

**ES:** Escribe una función para una sola partícula, por ejemplo un paso de Langevin. Con vmap, JAX la aplica a mil partículas a la vez, agregando un eje de lote, sin que escribas un solo bucle. El resultado es el mismo que llamar a la función mil veces, pero se ejecuta como una operación vectorizada. Se pueden anidar: vmap sobre partículas y, encima, vmap sobre temperaturas.

**EN:** Write a function for a single particle, for example one Langevin step. With vmap, JAX applies it to a thousand particles at once, adding a batch axis, without you writing a single loop. The result is the same as calling the function a thousand times, but it runs as one vectorized operation. They can be nested: vmap over particles and, on top, vmap over temperatures.

### [01:50.6] jit — `manim:S05`

**ES:** La primera vez que llamas a una función decorada con jit, JAX la ejecuta con valores abstractos, registra cada operación y construye un grafo. Ese grafo se entrega al compilador XLA, que fusiona operaciones y genera código optimizado para la CPU, la GPU o la TPU. Las llamadas siguientes con la misma forma de entrada reutilizan el código compilado. El costo es una compilación inicial; la ganancia, ejecuciones mucho más rápidas.

**EN:** The first time you call a jit-decorated function, JAX runs it with abstract values, records every operation and builds a graph. That graph is handed to the XLA compiler, which fuses operations and generates optimized code for the CPU, GPU or TPU. Later calls with the same input shape reuse the compiled code. The cost is an initial compilation; the payoff, much faster executions.

### [02:20.4] scan — `manim:S06`

**ES:** Las simulaciones son bucles: el estado de hoy produce el de mañana. scan expresa ese bucle de forma compilable. Recibe una función que toma un acarreo, el estado, y una entrada por paso, y devuelve el nuevo acarreo y una salida. Aquí el acarreo es la posición de una partícula y la entrada es una clave por paso: es el método de Euler y Maruyama para un proceso de Ornstein y Uhlenbeck. scan apila las salidas y devuelve la trayectoria completa.

**EN:** Simulations are loops: today's state produces tomorrow's. scan expresses that loop in a compilable way. It takes a function that receives a carry, the state, and a per-step input, and returns the new carry and an output. Here the carry is a particle's position and the input is one key per step: it is the Euler–Maruyama method for an Ornstein–Uhlenbeck process. scan stacks the outputs and returns the full trajectory.

### [02:49.9] jvp and vjp — `manim:S07`

**ES:** Para una función de n entradas y m salidas, la derivada es la matriz jacobiana, de m por n. Casi nunca la formamos. El producto jacobiano por vector, jvp, empuja una dirección de entrada hacia adelante y da una combinación de columnas: es la diferenciación en modo directo. El producto vector por jacobiano, vjp, tira de una dirección de salida hacia atrás y da una combinación de filas: es el modo inverso, la retropropagación. Para una pérdida escalar, el gradiente es un solo vjp, y por eso entrenar redes con millones de parámetros cuesta casi lo mismo que evaluarlas.

**EN:** For a function with n inputs and m outputs, the derivative is the m-by-n Jacobian matrix. We almost never form it. The Jacobian–vector product, jvp, pushes an input direction forward and gives a combination of columns: it is forward-mode differentiation. The vector–Jacobian product, vjp, pulls an output direction backward and gives a combination of rows: it is reverse mode, backpropagation. For a scalar loss, the gradient is a single vjp, which is why training networks with millions of parameters costs almost the same as evaluating them.

### [03:30.0] Numerical example — `manim:S08`

**ES:** Comprobemos con un ejemplo. Sea f(x) = sin(x) x². Su derivada es coseno de x por x², más dos x por seno de x. En x = 1 vale coseno de uno más dos por seno de uno, aproximadamente dos coma veintidós. jax punto grad devuelve exactamente ese número, dos coma dos dos tres dos, sin diferencias finitas ni errores de truncamiento.

**EN:** Let's check with an example. Let f(x) = sin(x) x². Its derivative is cosine of x times x², plus two x times sine of x. At x = 1 it equals cosine of one plus two times sine of one, about 2.22. jax.grad returns exactly that number, 2.2232, with no finite differences or truncation errors.

### [03:57.9] Applications — `slide`

**ES:** En el laboratorio uno generarás un millón de muestras de Bernoulli con vmap y medirás su entropía. A partir del laboratorio tres simularás dinámicas estocásticas con scan y jit. En los laboratorios diez y once usarás jvp y vjp para multiplicar por matrices de curvatura sin formarlas. Y en la unidad once trabajarás con THRML y Torx, que están escritas en JAX.

**EN:** In lab one you will generate a million Bernoulli samples with vmap and measure their entropy. From lab three on you will simulate stochastic dynamics with scan and jit. In labs ten and eleven you will use jvp and vjp to multiply by curvature matrices without forming them. And in unit eleven you will work with THRML and Torx, which are written in JAX.

### [04:23.9] Connections — `slide`

**ES:** Estas piezas reaparecen en todo el curso: Euler y Maruyama en la unidad dos, el muestreo de Gibbs cromático como un vmap sobre nodos de un mismo color en la unidad cuatro, los productos de Gauss y Newton por vector en la unidad ocho, y la simulación de chips termodinámicos con THRML en la unidad once.

**EN:** These pieces reappear throughout the course: Euler–Maruyama in unit two, chromatic Gibbs sampling as a vmap over same-color nodes in unit four, Gauss–Newton–vector products in unit eight, and the simulation of thermodynamic chips with THRML in unit eleven.

### [04:45.1] Common mistakes — `slide`

**ES:** Errores clásicos: reutilizar una clave y obtener números repetidos. Poner efectos secundarios dentro de jit, que solo ocurren al rastrear. Usar un if de Python que depende de un valor del arreglo, en lugar de las primitivas de control de flujo de JAX. Y mezclar el generador de NumPy con el de JAX.

**EN:** Classic mistakes: reusing a key and getting repeated numbers. Putting side effects inside jit, which only happen while tracing. Using a Python if that depends on an array value, instead of JAX's control-flow primitives. And mixing NumPy's generator with JAX's.

### [05:04.8] Summary — `manim:S12`

**ES:** En resumen: en JAX las funciones son puras y la aleatoriedad viaja en claves explícitas. vmap vectoriza, jit compila y scan itera. jvp empuja derivadas hacia adelante, vjp las tira hacia atrás, y el gradiente de una pérdida escalar es un solo vjp.

**EN:** In summary: in JAX functions are pure and randomness travels in explicit keys. vmap vectorizes, jit compiles and scan iterates. jvp pushes derivatives forward, vjp pulls them backward, and the gradient of a scalar loss is a single vjp.

### [05:25.3] Self-assessment — `slide`

**ES:** Para terminar la unidad cero: escribe una función que genere un millón de normales de forma reproducible y calcule su media con jit. Explica la diferencia entre gradiente y producto jacobiano por vector. Predice la forma de la salida de un vmap. Y cuenta cuántos jvp o vjp hacen falta para formar un jacobiano completo.

**EN:** To close unit zero: write a function that reproducibly generates a million normals and computes their mean with jit. Explain the difference between a gradient and a Jacobian–vector product. Predict the output shape of a vmap. And count how many jvps or vjps are needed to form a full Jacobian.

## Key equations
- $$\texttt{key}\to(\texttt{k}_1,\texttt{k}_2) = \texttt{split(key)}$$ — Explicit randomness: the same key gives the same numbers; split to get new ones.
- $$\mathrm{jvp}: v \mapsto J v,\qquad \mathrm{vjp}: u \mapsto u^\top J$$ — Forward mode (columns) and reverse mode (rows) of automatic differentiation.
- $$\nabla \ell(x) = \mathrm{vjp}_\ell(x)(1)$$ — For a scalar function, the gradient is a single vjp.
- $$\frac{d}{dx}\big(x^2\sin x\big)\Big|_{x=1} = \cos 1 + 2\sin 1 \approx 2.2232$$ — Example checked with jax.grad.

## Summary
- Pure functions + explicit PRNG keys = reproducible, transformable programs.
- vmap vectorizes, jit compiles with XLA, scan expresses loops with a carry.
- jvp (forward, $Jv$) and vjp (reverse, $u^\top J$); the scalar gradient is one vjp.

## Further reading
- JAX documentation: https://jax.readthedocs.io (technical reference, outside the syllabus bibliography).
- [54] G. Verdon et al., A framework for stochastic differentiable programming (Torx), 2026.
- Syllabus, Appendix D: lab environment setup.
