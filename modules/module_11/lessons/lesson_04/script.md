# Lesson 11.4 — Simulators and agentic research workflows

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Place the simulator layer (THRML, torx, Extropic's simulator API) in a research loop.
- Package an experiment as a verifiable task: specification, sandboxed execution, reference metric, rubric.
- Recognize under-specified metrics and how a rubric catches what execution checks miss.

## Prerequisites
- Lessons 11.1–11.3.

## Narrated script

### [00:06.1] Introduction — `manim:S01`

**ES:** Hasta aquí hemos escrito los programas nosotros. La siguiente idea es que un agente, un modelo de lenguaje con herramientas, proponga experimentos, los ejecute en un simulador, lea los resultados y los mejore. Para eso hace falta algo más que un simulador: hace falta convertir cada experimento en una tarea que una máquina pueda calificar sin ayuda. Hoy construimos esa pieza.

**EN:** So far we have written the programs ourselves. The next idea is for an agent, a language model with tools, to propose experiments, run them on a simulator, read the results and improve them. That requires more than a simulator: each experiment must be turned into a task a machine can grade on its own. Today we build that piece.

### [00:29.7] The simulator layer — `manim:S02`

**ES:** La capa de simulación tiene tres niveles. THRML simula muestreo por bloques en GPU. Torx describe y deriva programas estocásticos. Y Extropic ofrece una interfaz de simulación en acceso anticipado, pensada para que los agentes busquen algoritmos que compilen y corran bien en su hardware; su documentación no es pública, así que aquí trabajamos con las bibliotecas abiertas. Lo importante es que el agente solo ve una interfaz: código de entrada, métricas de salida.

**EN:** The simulation layer has three levels. THRML simulates block sampling on GPUs. Torx describes and differentiates stochastic programs. And Extropic offers a simulation interface in early access, meant for agents to search for algorithms that compile and run well on its hardware; its documentation is not public, so here we work with the open libraries. What matters is that the agent only sees an interface: code in, metrics out.

### [01:00.3] A verifiable task — `manim:S03`

**ES:** Una tarea verificable tiene cuatro partes. Un enunciado: estimar las magnetizaciones de un Ising de cuatro por cuatro con un muestreador por bloques. Una ejecución aislada: el código del agente corre en un proceso separado, con tiempo límite. Una métrica de referencia: error máximo de cero coma cero tres frente a la enumeración exacta. Y una rúbrica: que use un muestreador y que el coloreado sea válido. La recompensa combina ejecución y rúbrica.

**EN:** A verifiable task has four parts. A statement: estimate the magnetizations of a four-by-four Ising model with a block sampler. An isolated execution: the agent's code runs in a separate process, with a time limit. A reference metric: maximum error of 0.03 against exact enumeration. And a rubric: that it uses a sampler and that the coloring is valid. The reward combines execution and rubric.

### [01:30.4] Five proposals — `manim:S04`

**ES:** Un proponente programado, que hace las veces de agente, envía cinco soluciones. El ejecutor da quince centésimas por correr y ochenta y cinco por reproducir la métrica. Gibbs cromático con treinta barridos: recompensa uno. Con tres barridos corre pero no converge: cero coma cuatro. Un error de sintaxis: cero. Y una trampa, que calcula la respuesta por enumeración exacta: pasa la ejecución con nota máxima, pero la rúbrica la detecta, y queda en cero coma siete.

**EN:** A scripted proposer, standing in for the agent, submits five solutions. The executor gives fifteen hundredths for running and eighty-five for reproducing the metric. Chromatic Gibbs with thirty sweeps: reward one. With three sweeps it runs but does not converge: 0.4. A syntax error: zero. And a cheat, which computes the answer by exact enumeration: it passes execution with full marks, but the rubric catches it, and it ends at 0.7.

### [02:01.9] An under-specified metric — `manim:S05`

**ES:** La quinta propuesta da la lección más útil. Actualizar todos los espines a la vez es un error clásico: no es Gibbs. Y sin embargo pasa la métrica, con error de cero coma cero diecinueve. ¿Por qué? En un grafo bipartito, la actualización simultánea equivale a dos cadenas entrelazadas, cada una correcta, así que las magnetizaciones salen bien. Pero las correlaciones entre vecinos tienen un error de cero coma ocho, frente a cero coma cero cuatro con Gibbs cromático. La métrica estaba mal especificada; solo la rúbrica lo notó.

**EN:** The fifth proposal gives the most useful lesson. Updating all spins at once is a classic mistake: it is not Gibbs. And yet it passes the metric, with an error of 0.019. Why? On a bipartite graph, simultaneous updating is equivalent to two interleaved chains, each correct, so the magnetizations come out right. But the correlations between neighbors have an error of 0.8, against 0.04 with chromatic Gibbs. The metric was under-specified; only the rubric noticed.

### [02:36.7] Designing the loop — `manim:S06`

**ES:** De aquí salen reglas de diseño. Mide todo lo que define el resultado, no solo lo más fácil: momentos de primer y segundo orden. Ejecuta el código en un entorno aislado y con límite de tiempo, porque es código no confiable. Da más peso a la ejecución, que es más difícil de engañar, y usa la rúbrica para lo que la ejecución no ve. Y guarda cada versión del entorno: cada cambio en la recompensa cambia lo que el agente aprende.

**EN:** Design rules follow from this. Measure everything that defines the result, not just the easiest thing: first- and second-order moments. Run the code in an isolated environment with a time limit, because it is untrusted code. Give more weight to execution, which is harder to fool, and use the rubric for what execution does not see. And keep every version of the environment: each change in the reward changes what the agent learns.

### [03:04.1] Applications — `slide`

**ES:** En la práctica, empaqueta laboratorios anteriores como tareas con métricas de referencia, califica la ejecución con quince centésimas por correr y ochenta y cinco por reproducir, y añade una rúbrica con reglas o con un modelo juez. En el laboratorio treinta construirás un pequeño banco de pruebas.

**EN:** In practice, package earlier labs as tasks with reference metrics, grade execution with fifteen hundredths for running and eighty-five for reproducing, and add a rubric with rules or with a judge model. In lab thirty you will build a small benchmark.

### [03:22.7] Common mistakes — `slide`

**ES:** Errores comunes: verificar solo la estadística más fácil. Ejecutar código no confiable sin aislamiento. Premiar la respuesta en lugar del método. Y cambiar la recompensa sin versionar el entorno.

**EN:** Common mistakes: checking only the easiest statistic. Running untrusted code without isolation. Rewarding the answer instead of the method. And changing the reward without versioning the environment.

### [03:36.6] Summary — `manim:S09`

**ES:** En resumen, un agente de investigación necesita un simulador y, sobre todo, tareas verificables: enunciado, ejecución aislada, métrica de referencia y rúbrica. En nuestro arnés, la rúbrica detectó tanto una trampa como un algoritmo incorrecto que pasaba la métrica. Diseñar la recompensa es diseñar lo que el agente aprenderá.

**EN:** In summary, a research agent needs a simulator and, above all, verifiable tasks: statement, isolated execution, reference metric and rubric. In our harness, the rubric caught both a cheat and an incorrect algorithm that passed the metric. Designing the reward is designing what the agent will learn.

### [03:58.5] Self-assessment — `slide`

**ES:** Para practicar: calcula la recompensa de una solución que corre sin reproducir. Explica por qué la actualización simultánea acierta las magnetizaciones. Propón la métrica que la habría detectado. Y explica por qué hay que aislar la ejecución.

**EN:** To practice: compute the reward of a solution that runs without reproducing. Explain why simultaneous updating gets the magnetizations right. Propose the metric that would have caught it. And explain why execution must be isolated.

## Key equations
- $$r = 0.7\,\text{exec} + 0.3\,\text{rubric},\qquad \text{exec} = 0.15\,[\text{runs}] + 0.85\,[\text{reproduces}]$$ — Reward used in Extropic's Thermo-RSI environment and in our harness.
- $$\max|\hat m - m|\colon\ 0.019\ (\text{parallel})\ \text{vs}\ \max|\hat C - C|\colon\ 0.80\ (\text{parallel}),\ 0.04\ (\text{chromatic})$$ — An under-specified metric hides a wrong sampler [S].

## Summary
- Simulator layer: THRML, torx; Extropic simulator API (early access, undocumented).
- Verifiable task = statement + sandbox + reference metric + rubric.
- Our harness: correct 1.0, under-converged 0.405, crash 0, cheat 0.7 [S].
- Parallel updates pass magnetizations, fail correlations (0.80) [S].

## Further reading
- A. Neagoe, G. Verdon and S. Morton (Extropic, with Prime Intellect), First sparks of thermodynamic recursive intelligence, 1 October 2026.
- Extropic, THRML and torx documentation; simulator API early access (extropic.dev), 2026.
- J. Gonzalez et al., Parallel Gibbs sampling: from colored fields to thin junction trees, AISTATS (2011).
