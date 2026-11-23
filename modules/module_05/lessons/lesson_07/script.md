# Lesson 5.7 — Hardware abstractions

**Unit:** Unit 5 — Probabilistic and thermodynamic hardware  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain the $N^2$ connectivity problem and why hardware uses a fixed, sparse parent graph.
- Embed a logical variable of high degree into a chain of physical pbits and choose the chain strength.
- Estimate the embedding overhead for a dense model on a degree-16 graph.

## Prerequisites
- Lesson 4.1: graphical models.
- Lesson 5.3: the Z1 graph (degree 16).

## Narrated script

### [00:04.8] Introduction — `manim:S01`

**ES:** Un modelo de Ising con todas las conexiones posibles tiene un acoplamiento por cada par de espines. Con diez mil espines eso son casi cincuenta millones de acoplamientos, y cada uno necesita un cable y un registro. Ningún chip puede cablear eso. Por eso el hardware ofrece un grafo fijo y disperso, y los programas tienen que adaptarse a él.

**EN:** An Ising model with every possible connection has one coupling per pair of spins. With ten thousand spins that is almost fifty million couplings, and each one needs a wire and a register. No chip can wire that. That is why hardware offers a fixed, sparse graph, and programs have to adapt to it.

### [00:26.2] The N² problem — `manim:S02`

**ES:** Un grafo completo de N nodos tiene N(N − 1)/2 aristas: crece como el cuadrado. Un grafo de grado fijo d tiene N d/2: crece linealmente. Para diez mil nodos y grado dieciséis, son ochenta mil aristas en lugar de cincuenta millones. Además, en un chip las conexiones deben ser cortas, así que los vecinos de cada pbit están cerca en el plano. Ese grafo fijo se llama el grafo padre.

**EN:** A complete graph on N nodes has N(N − 1)/2 edges: it grows as the square. A graph of fixed degree d has N d/2: it grows linearly. For ten thousand nodes and degree sixteen, that is eighty thousand edges instead of fifty million. Moreover, on a chip the connections must be short, so each pbit's neighbors are nearby in the plane. That fixed graph is called the parent graph.

### [00:54.5] Embedding with chains — `manim:S03`

**ES:** ¿Y si una variable del modelo necesita más vecinos de los que ofrece el hardware? La representamos con una cadena de pbits físicos unidos por acoplamientos ferromagnéticos fuertes, de modo que se comporten como un solo espín. Cada copia aporta sus propios vecinos libres. Con grado dieciséis, una variable con noventa y nueve vecinos necesita al menos siete copias. Esto se llama embebido de menores.

**EN:** What if a model variable needs more neighbors than the hardware offers? We represent it with a chain of physical pbits joined by strong ferromagnetic couplings, so that they behave as a single spin. Each copy contributes its own free neighbors. With degree sixteen, a variable with ninety-nine neighbors needs at least seven copies. This is called minor embedding.

### [01:20.1] Chain strength — `manim:S04`

**ES:** El acoplamiento de la cadena debe ser fuerte, porque si las copias discrepan, la variable lógica queda indefinida: la cadena se rompe. Para dos copias aisladas, la probabilidad de ruptura es 1/(1 + e^(2βJ_c)). Con βJ_c = 1 es del doce por ciento; con dos, menos del dos por ciento; con tres, un cuarto de punto porcentual. Pero un acoplamiento demasiado fuerte congela la cadena y hace lenta la mezcla. Hay que equilibrar.

**EN:** The chain coupling must be strong, because if the copies disagree, the logical variable is undefined: the chain breaks. For two isolated copies, the breaking probability is 1/(1 + e^(2βJ_c)). With βJ_c = 1 it is twelve percent; with two, under two percent; with three, a quarter of a percent. But a coupling that is too strong freezes the chain and slows mixing. It has to be balanced.

### [01:51.1] Overhead — `manim:S05`

**ES:** El costo del embebido es el número de pbits físicos por variable lógica. Para modelos dispersos de grado menor a dieciséis, es uno: el modelo cabe directo. Para grado treinta y uno, tres copias. Para un modelo denso de mil variables, cada una con novecientos noventa y nueve vecinos, hacen falta al menos setenta y dos copias por variable, más el ruteo. Por eso los algoritmos para hardware termodinámico se diseñan dispersos desde el principio, como veremos con los transformers dispersos de la unidad diez.

**EN:** The cost of embedding is the number of physical pbits per logical variable. For sparse models of degree below sixteen, it is one: the model fits directly. For degree thirty-one, three copies. For a dense model of a thousand variables, each with nine hundred ninety-nine neighbors, at least seventy-two copies per variable are needed, plus routing. That is why algorithms for thermodynamic hardware are designed sparse from the start, as we will see with the sparse transformers of unit ten.

### [02:23.7] Numerical example — `manim:S06`

**ES:** Calculemos con el Z1. Sus doscientos sesenta y nueve mil pbits de grado dieciséis tienen unos dos millones de acoplamientos. Un modelo disperso de grado dieciséis ocupa el chip entero con doscientas sesenta y nueve mil variables. Un modelo denso, en cambio, con setenta y dos copias por variable apenas alcanzaría para unas tres mil setecientas variables, sin contar el ruteo.

**EN:** Let's compute with the Z1. Its two hundred sixty-nine thousand degree-sixteen pbits have about two million couplings. A sparse degree-sixteen model fills the whole chip with two hundred sixty-nine thousand variables. A dense model, in contrast, with seventy-two copies per variable, would barely reach about three thousand seven hundred variables, not counting routing.

### [02:48.0] Applications — `slide`

**ES:** La regla de diseño es elegir modelos dispersos y locales desde el principio, y embeber con cadenas solo las pocas variables de grado alto. El coloreo del grafo padre fija cuántas fases de reloj tiene un barrido. En el laboratorio ocho embeberás un modelo denso pequeño en un grafo de grado dieciséis.

**EN:** The design rule is to choose sparse, local models from the start, and to embed with chains only the few high-degree variables. The coloring of the parent graph sets how many clock phases a sweep takes. In lab eight you will embed a small dense model into a degree-sixteen graph.

### [03:07.4] Common mistakes — `slide`

**ES:** Errores comunes: suponer que cualquier modelo corre directamente. Ignorar las cadenas rotas al decodificar las muestras. Usar acoplamientos de cadena tan fuertes que la mezcla se congela. Y contar las copias sin contar el ruteo.

**EN:** Common mistakes: assuming any model runs directly. Ignoring broken chains when decoding samples. Using chain couplings so strong that mixing freezes. And counting the copies without counting the routing.

### [03:22.9] Summary — `manim:S09`

**ES:** En resumen: la conectividad completa crece como N² y no se puede cablear, así que el hardware ofrece un grafo padre fijo y disperso. Las variables de grado alto se embeben como cadenas de copias acopladas, con una fuerza que equilibra rupturas y mezcla. El costo del embebido empuja a diseñar modelos dispersos desde el principio.

**EN:** In summary: full connectivity grows as N² and cannot be wired, so hardware offers a fixed, sparse parent graph. High-degree variables are embedded as chains of coupled copies, with a strength that balances breaks and mixing. The cost of embedding pushes toward designing sparse models from the start.

### [03:45.0] Self-assessment — `slide`

**ES:** Para practicar: cuenta las aristas de ambos grafos. Calcula las copias mínimas para un grado dado. Calcula la probabilidad de ruptura de una cadena. Y explica por qué una cadena demasiado fuerte hace lento el muestreo.

**EN:** To practice: count the edges of both graphs. Compute the minimum copies for a given degree. Compute the breaking probability of a chain. And explain why a chain that is too strong makes sampling slow.

## Key equations
- $$|E_{\text{complete}}| = \frac{N(N-1)}{2},\qquad |E_{d}| = \frac{Nd}{2}$$ — The N² connectivity problem vs a fixed-degree parent graph.
- $$c \ge \Big\lceil \frac{k - 2}{d - 2}\Big\rceil\quad (k > d)$$ — Minimum chain length to give a logical variable $k$ neighbors on a degree-$d$ graph.
- $$P_{\text{break}} = \frac{1}{1 + e^{2\beta J_c}}$$ — Two isolated copies coupled with $J_c$.

## Summary
- Full connectivity ∝ N²: 5·10⁷ couplings for N = 10⁴ vs 8·10⁴ at degree 16.
- Minor embedding: chains of ferromagnetically coupled copies.
- Chain strength: few breaks vs slow mixing (βJ_c = 2 ⇒ 1.8 % breaks).
- Dense model on Z1: ≥ 72 copies/variable ⇒ ~3,700 variables; design sparse.

## Further reading
- [22] Extropic, From One to One Billion: Torx, Thermalizers, and Z1, 2026.
- [19] N. A. Aadit et al., Massively parallel probabilistic computing with sparse Ising machines, 2022.
- V. Choi, Minor-embedding in adiabatic quantum computation, Quantum Inf. Process. 7, 193 (2008).
