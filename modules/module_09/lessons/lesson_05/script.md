# Lesson 9.5 — Efficiency analysis: Route A vs Route B

**Unit:** Unit 9 — Thermodynamic generative models  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Distinguish Route A (port a neural diffusion model, DiT or masked-diffusion transformer, to a TSU system) from Route B (native thermodynamic denoising).
- Apply Amdahl's law to the digital-glue share of a heterogeneous system.
- Choose a route with an explicit decision checklist.

## Prerequisites
- Lessons 5.8 and 9.3–9.4: energy accounting, DTMs, diffusion cost model.

## Narrated script

### [00:06.6] Introduction — `manim:S01`

**ES:** Si queremos generar con hardware termodinámico, hay dos caminos. La ruta A toma un modelo de difusión neuronal existente, como un transformer de difusión o un modelo de lenguaje enmascarado, y lo porta a un sistema con TSU. La ruta B diseña desde cero un modelo nativo, como una DTM, que vive en el hardware. Hoy las comparamos con números.

**EN:** If we want to generate with thermodynamic hardware, there are two paths. Route A takes an existing neural diffusion model, such as a diffusion transformer or a masked language model, and ports it to a system with TSUs. Route B designs a native model from scratch, such as a DTM, that lives in the hardware. Today we compare them with numbers.

### [00:29.7] Route A: porting — `manim:S02`

**ES:** La ventaja de la ruta A es que reutiliza modelos que ya funcionan. El problema es que un transformer es, sobre todo, multiplicaciones de matrices, y un TSU no multiplica matrices: muestrea. Las partes deterministas quedan en lógica digital, una FPGA o un acelerador, y el TSU solo hace el muestreo. En la cifra que Extropic reporta para su modelo Z1T, de doscientos noventa y cuatro nanojulios por token, doscientos ochenta y seis son trabajo de la FPGA: el noventa y siete por ciento.

**EN:** The advantage of route A is that it reuses models that already work. The problem is that a transformer is mostly matrix multiplications, and a TSU does not multiply matrices: it samples. The deterministic parts stay in digital logic, an FPGA or an accelerator, and the TSU only does the sampling. In the figure Extropic reports for its Z1T model, of two hundred ninety-four nanojoules per token, two hundred eighty-six are FPGA work: ninety-seven percent.

### [01:03.6] Amdahl's law — `manim:S03`

**ES:** La ley de Amdahl pone el límite. Si el noventa y siete por ciento de la energía es pegamento digital, hacer gratis la parte termodinámica mejora el total a lo sumo un tres por ciento. Para acercarse a ganancias de mil veces hay que atacar el pegamento: llevar más funciones al chip probabilístico, reducir la precisión de lo digital o cambiar la arquitectura del modelo.

**EN:** Amdahl's law sets the limit. If ninety-seven percent of the energy is digital glue, making the thermodynamic part free improves the total by at most three percent. To approach thousand-fold gains one must attack the glue: move more functions onto the probabilistic chip, lower the digital precision or change the model architecture.

### [01:26.6] Route B: native denoising — `manim:S04`

**ES:** La ruta B invierte la lógica: el modelo entero se diseña como una cadena de modelos de energía condicionales que el hardware muestrea directamente. Casi no hay pegamento: en la DTM de la lección nueve punto tres, la energía es la de las celdas, unos veinte nanojulios por imagen. El precio es la expresividad: estos modelos son más limitados, y para conjuntos de datos grandes hacen falta híbridos con una red neuronal, que reintroducen parte del pegamento, aunque con una red diez veces más pequeña.

**EN:** Route B reverses the logic: the whole model is designed as a chain of conditional energy models that the hardware samples directly. There is almost no glue: in the DTM of lesson 9.3, the energy is that of the cells, about twenty nanojoules per image. The price is expressivity: these models are more limited, and large datasets need hybrids with a neural network, which reintroduce part of the glue, though with a network ten times smaller.

### [01:58.8] Side by side — `manim:S05`

**ES:** Comparémoslas. La ruta A tiene modelos maduros y calidad conocida, pero su ganancia energética está limitada por el pegamento digital. La ruta B tiene una ventaja energética potencial de órdenes de magnitud, pero con modelos jóvenes, bancos de prueba pequeños y estimaciones, no mediciones. Ninguna es mejor en todo: depende de si el cuello de botella es la calidad o la energía.

**EN:** Let's compare them. Route A has mature models and known quality, but its energy gain is limited by the digital glue. Route B has a potential energy advantage of orders of magnitude, but with young models, small benchmarks and estimates, not measurements. Neither is better at everything: it depends on whether the bottleneck is quality or energy.

### [02:24.3] A decision checklist — `manim:S06`

**ES:** Una lista para decidir. Primero, mide la fracción de pegamento digital de la ruta A: si pasa del noventa por ciento, la ganancia máxima es de diez veces o menos. Segundo, pregunta si existe un modelo nativo de calidad suficiente para tu tarea. Tercero, cuenta toda la energía, incluida la entrada y la salida. Y cuarto, etiqueta cada cifra como medida, simulada, proyectada o estimada.

**EN:** A checklist for deciding. First, measure the digital-glue fraction of route A: if it exceeds ninety percent, the maximum gain is ten times or less. Second, ask whether a native model of sufficient quality exists for your task. Third, count all the energy, including input and output. And fourth, label each figure as measured, simulated, projected or estimated.

### [02:50.6] Applications — `slide`

**ES:** Este análisis sirve para planificar productos, orientar la investigación hacia modelos nativos de calidad y decidir qué funciones llevar al chip, como veremos en la unidad diez con Z1T. En el proyecto ocho construirás un planificador de inferencia heterogénea.

**EN:** This analysis helps plan products, steer research toward native models of sufficient quality and decide which functions to move onto the chip, as we will see in unit ten with Z1T. In project eight you will build a heterogeneous inference planner.

### [03:07.2] Common mistakes — `slide`

**ES:** Errores comunes: citar la energía del TSU como la del sistema. Comparar un modelo nativo con uno de GPU con calidades distintas. Suponer que los híbridos no tienen costo digital. Y tratar proyecciones como mediciones.

**EN:** Common mistakes: quoting the TSU's energy as the system's. Comparing a native model with a GPU one at different qualities. Assuming hybrids have no digital cost. And treating projections as measurements.

### [03:22.6] Summary — `manim:S09`

**ES:** En resumen: la ruta A porta modelos maduros pero queda limitada por el pegamento digital, que en Z1T es el noventa y siete por ciento de la energía. La ruta B, nativa, promete órdenes de magnitud con modelos todavía jóvenes. La ley de Amdahl y una contabilidad completa deciden en cada caso.

**EN:** In summary: route A ports mature models but is limited by the digital glue, which in Z1T is ninety-seven percent of the energy. Route B, native, promises orders of magnitude with models that are still young. Amdahl's law and complete accounting decide in each case.

### [03:42.4] Self-assessment — `slide`

**ES:** Para practicar: calcula la fracción de la FPGA en Z1T. Calcula la ganancia máxima si el TSU fuera gratis. Di qué debe cambiar para acercarse a mil veces. Y explica cuándo elegirías igual la ruta A.

**EN:** To practice: compute the FPGA share in Z1T. Compute the maximum gain if the TSU were free. Say what must change to approach a thousand times. And explain when you would still choose route A.

## Key equations
- $$f_{\text{glue}} = \frac{285.78}{294.52} \approx 0.97\qquad (\text{Z1T, nJ/token, reported})$$ — Digital-glue share of a ported model.
- $$S_{\max} = \frac{1}{f_{\text{glue}}} \approx 1.03$$ — Amdahl bound if the thermodynamic part became free.
- $$E_{\text{native}} \approx T\,K_{\text{mix}}\,L^2 E_{\text{cell}}\ (+\ E_{\text{NN}}\ \text{for hybrids})$$ — Route B cost: cells, plus any neural component.

## Summary
- Route A: port DiT/MDLM; matmuls stay digital; Z1T: 97 % of 294.52 nJ/token is FPGA [P].
- Amdahl: free TSU part → ≤ 1.03× overall.
- Route B: native DTM, ~20 nJ/sample, less expressive; hybrids with 10× smaller NN [E].
- Decide with glue share, native-model quality, full accounting and evidence labels.

## Further reading
- Extropic (G. Verdon et al.), Z1T: Sparse transformer-like models for probabilistic hardware, 2026.
- [48] A. Jelinčič et al., An efficient probabilistic hardware architecture for diffusion-like models, 2025.
- G. M. Amdahl, Validity of the single processor approach to achieving large scale computing capabilities, AFIPS (1967).
