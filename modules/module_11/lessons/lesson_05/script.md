# Lesson 11.5 — LLM research agents

**Unit:** Unit 11 — Software stack, research agents and frontiers  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Explain GRPO: group-relative advantages without a value network.
- Combine execution and rubric rewards, with an LLM as judge, and show how reward hacking is learned.
- Read the Thermo-RSI results critically: what was demonstrated and what remains a goal.

## Prerequisites
- Lesson 11.4: verifiable tasks and rewards.

## Narrated script

### [00:05.9] Introduction — `manim:S01`

**ES:** En la lección anterior calificamos propuestas. Ahora entrenamos al que propone. Si un modelo de lenguaje recibe la recompensa de cada intento, puede aprender por refuerzo a escribir mejores experimentos. Extropic, con Prime Intellect, lo intentó en octubre de dos mil veintiséis, y lo llamó las primeras chispas de la inteligencia recursiva termodinámica. Veamos el método, un experimento propio sobre trampas, y lo que de verdad se demostró.

**EN:** In the previous lesson we graded proposals. Now we train the proposer. If a language model receives the reward of each attempt, it can learn by reinforcement to write better experiments. Extropic, with Prime Intellect, tried this in October twenty twenty-six, and called it the first sparks of thermodynamic recursive intelligence. Let's look at the method, our own experiment on cheating, and what was really demonstrated.

### [00:34.0] GRPO — `manim:S02`

**ES:** GRPO, la optimización de política relativa al grupo, fue introducida con DeepSeekMath en dos mil veinticuatro. Para cada tarea, el modelo genera un grupo de intentos. La ventaja de cada intento es su recompensa menos la media del grupo, dividida por la desviación del grupo. Se refuerzan los intentos mejores que el promedio y se penalizan los peores, sin necesidad de una red de valor que estime la recompensa esperada.

**EN:** GRPO, group relative policy optimization, was introduced with DeepSeekMath in twenty twenty-four. For each task, the model generates a group of attempts. The advantage of each attempt is its reward minus the group mean, divided by the group's standard deviation. Attempts better than average are reinforced and worse ones penalized, with no need for a value network that estimates the expected reward.

### [01:01.6] Execution and judge — `manim:S03`

**ES:** La recompensa de Extropic combina dos señales. La ejecución, con setenta por ciento del peso, es determinista: el código corre y reproduce la métrica de referencia, o no. La rúbrica, con treinta por ciento, la califica un modelo juez, Nemotron 3 Super de ciento veinte mil millones de parámetros, con criterios escritos de antemano para cada tarea. Los autores dan más peso a la ejecución porque es más difícil de engañar.

**EN:** Extropic's reward combines two signals. Execution, with seventy percent of the weight, is deterministic: the code runs and reproduces the reference metric, or it does not. The rubric, with thirty percent, is graded by a judge model, Nemotron 3 Super with one hundred twenty billion parameters, with criteria written in advance for each task. The authors give more weight to execution because it is harder to fool.

### [01:28.9] How cheating is learned — `manim:S04`

**ES:** Lo probamos con un GRPO de juguete. La política elige entre las cinco propuestas de la lección anterior, con grupos de ocho y trescientos pasos, promediado sobre doscientas semillas. Con la recompensa completa, la política termina eligiendo el método correcto el noventa y nueve coma ocho por ciento de las veces. Con solo la ejecución, el método correcto baja al treinta y dos por ciento: el sampler incorrecto se queda con el treinta y tres y la trampa con el treinta y cinco. El agente aprende exactamente lo que la recompensa premia.

**EN:** We test it with a toy GRPO. The policy chooses among the five proposals of the previous lesson, with groups of eight and three hundred steps, averaged over two hundred seeds. With the full reward, the policy ends up choosing the correct method 99.8 percent of the time. With execution only, the correct method drops to thirty-two percent: the incorrect sampler keeps thirty-three and the cheat thirty-five. The agent learns exactly what the reward rewards.

### [02:01.7] Thermo-RSI results — `manim:S05`

**ES:** El experimento real entrenó Qwen tres punto seis, con treinta y cinco mil millones de parámetros y tres mil millones activos, durante cien pasos de GRPO, unas veinticinco horas, sobre unas cincuenta tareas que reproducen experimentos clásicos como máquinas de Boltzmann y el algoritmo de vigilia y sueño. La recompensa en tareas no vistas subió de cero coma uno dos siete a cero coma tres seis uno, casi el triple. Como referencia, en el mismo conjunto, Claude Opus 4.8 obtuvo cero coma cuatro seis cuatro y GPT 5.5, cero coma siete cuatro siete.

**EN:** The real experiment trained Qwen 3.6, with thirty-five billion parameters and three billion active, for one hundred GRPO steps, about twenty-five hours, on about fifty tasks that reproduce classic experiments such as Boltzmann machines and the wake-sleep algorithm. The reward on unseen tasks rose from 0.127 to 0.361, almost triple. For reference, on the same set, Claude Opus 4.8 scored 0.464 and GPT 5.5, 0.747.

### [02:40.3] What was shown, what is a goal — `manim:S06`

**ES:** Leamos con cuidado. Lo demostrado es que un modelo pequeño mejora mucho al reproducir experimentos conocidos. Lo que el nombre promete, agentes que descubren algoritmos nuevos para el hardware y lo mejoran en un ciclo recursivo, es por ahora un objetivo: los autores dicen que el siguiente paso es pasar de reproducir a descubrir, y que las tareas aún no corren sobre su simulador. Tampoco reportan observaciones de trampas. Son primeras chispas, como dice el título.

**EN:** Let's read carefully. What was demonstrated is that a small model improves a lot at reproducing known experiments. What the name promises, agents that discover new algorithms for the hardware and improve it in a recursive cycle, is for now a goal: the authors say the next step is to move from reproducing to discovering, and that the tasks do not yet run on their simulator. Nor do they report observations of cheating. They are first sparks, as the title says.

### [03:10.0] Applications — `slide`

**ES:** En la práctica, GRPO sobre tareas verificables, recompensa dominada por la ejecución con un juez para la rúbrica, y auditoría de las ejecuciones en busca de trampas. En el laboratorio treinta evaluarás modelos de lenguaje sobre tus tareas.

**EN:** In practice, GRPO over verifiable tasks, a reward dominated by execution with a judge for the rubric, and auditing of runs in search of cheating. In lab thirty you will evaluate language models on your tasks.

### [03:26.0] Common mistakes — `slide`

**ES:** Errores comunes: premiar solo la métrica. Confiar en un juez sin criterios fijados de antemano. Leer la automejora recursiva como algo demostrado. Y comparar puntuaciones sobre conjuntos de tareas distintos.

**EN:** Common mistakes: rewarding only the metric. Trusting a judge without criteria fixed in advance. Reading recursive self-improvement as something demonstrated. And comparing scores over different task sets.

### [03:40.3] Summary — `manim:S09`

**ES:** En resumen, GRPO refuerza los intentos mejores que el promedio de su grupo. La recompensa mezcla ejecución y rúbrica, y nuestro experimento muestra que sin rúbrica el agente aprende trampas y métodos incorrectos. Thermo-RSI casi triplicó la recompensa de un modelo pequeño al reproducir experimentos; descubrir algoritmos nuevos sigue siendo la meta.

**EN:** In summary, GRPO reinforces attempts better than their group's average. The reward mixes execution and rubric, and our experiment shows that without a rubric the agent learns cheats and incorrect methods. Thermo-RSI almost tripled the reward of a small model at reproducing experiments; discovering new algorithms remains the goal.

### [04:03.8] Self-assessment — `slide`

**ES:** Para practicar: calcula las ventajas de un grupo. Explica por qué GRPO no necesita red de valor. Explica por qué la política sin rúbrica eligió la trampa. Y di qué demostraría de verdad la automejora recursiva.

**EN:** To practice: compute the advantages of a group. Explain why GRPO does not need a value network. Explain why the policy without a rubric chose the cheat. And say what would really demonstrate recursive self-improvement.

## Key equations
- $$A_i = \frac{r_i - \mathrm{mean}(r_{1:G})}{\mathrm{std}(r_{1:G})}$$ — GRPO group-relative advantage (Shao et al. 2024).
- $$r = 0.7\,\text{exec} + 0.3\,\text{rubric}\ (\text{judge: Nemotron 3 Super 120B})$$ — Thermo-RSI reward [P].
- $$0.127 \to 0.361\ \text{held-out reward (100 GRPO steps)}$$ — Qwen3.6-35B-A3B; Opus 4.8: 0.464; GPT-5.5: 0.747 [P].

## Summary
- GRPO: advantage = reward normalized within a group of attempts.
- Toy GRPO: full reward → 99.8% correct; exec-only → 68% wrong or cheat [S].
- Thermo-RSI: 0.127 → 0.361 (≈2.8×) on reproduction tasks [P].
- Discovery of new algorithms: stated goal, not yet shown.

## Further reading
- A. Neagoe, G. Verdon and S. Morton (Extropic, with Prime Intellect), First sparks of thermodynamic recursive intelligence, 1 October 2026.
- Z. Shao et al., DeepSeekMath: pushing the limits of mathematical reasoning (introduces GRPO), arXiv:2402.03300 (2024).
- L. Zheng et al., Judging LLM-as-a-judge with MT-Bench and Chatbot Arena, NeurIPS (2023).
