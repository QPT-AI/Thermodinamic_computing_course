# Computación Termodinámica para Inteligencia Artificial

*Física, hardware probabilístico, algoritmos y modelos de lenguaje termodinámicos*

[![YouTube](https://img.shields.io/badge/YouTube-ver%20las%20sesiones-red?logo=youtube)](https://www.youtube.com/channel/UCoelf_Gdb0nwqkI1VwEeg3g)

> **¿Cuándo, por qué y en cuánto puede el hardware probabilístico basado en la física hacer la IA más eficiente energéticamente, y qué debe cambiar en nuestros algoritmos para que eso ocurra?**

Curso completo en español: 12 unidades, 90 lecciones en video con notas, ejercicios, diapositivas, guiones y subtítulos (ES/EN), quices por unidad y laboratorios.

- **Nivel:** Maestría (MSc / MEng), curso electivo de especialización
- **Duración:** 16 semanas · 64 h de contacto · 128 h de trabajo independiente · 4 créditos
- **Videos de las sesiones:** [canal de YouTube](https://www.youtube.com/channel/UCoelf_Gdb0nwqkI1VwEeg3g)

## Estructura del repositorio

```
syllabus/      pensum original (PDF), curriculum.json, objetivos de aprendizaje
references/    bibliografía, videos de referencia y club de revista
latex/         estilos LaTeX del curso (curso.sty, tema beamer)
modules/
  module_XX/
    lessons/lesson_YY/   notes.pdf · exercises.pdf · slides.pdf · script.md · subtitles.srt · subtitles.en.srt
    assessments/         quiz de la unidad (con clave de respuestas)
    projects/            laboratorios (enunciado + código de inicio)
```

Cada lección incluye:

| Archivo | Contenido |
|---|---|
| `notes.pdf` / `.tex` | Notas de la lección |
| `exercises.pdf` / `.tex` | Ejercicios |
| `slides.pdf` | Diapositivas del video |
| `script.md` | Guion narrado |
| `subtitles.srt` / `subtitles.en.srt` | Subtítulos en español / inglés |

## Contenido

### Unidad 0 — Orientación y nivelación matemática

Semanas 1

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [0.1](modules/module_00/lessons/lesson_01) | El muro energético de la IA | [PDF](modules/module_00/lessons/lesson_01/notes.pdf) | [PDF](modules/module_00/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_01/slides.pdf) | [MD](modules/module_00/lessons/lesson_01/script.md) |
| [0.2](modules/module_00/lessons/lesson_02) | Mapa de paradigmas de cómputo | [PDF](modules/module_00/lessons/lesson_02/notes.pdf) | [PDF](modules/module_00/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_02/slides.pdf) | [MD](modules/module_00/lessons/lesson_02/script.md) |
| [0.3](modules/module_00/lessons/lesson_03) | Repaso de probabilidad | [PDF](modules/module_00/lessons/lesson_03/notes.pdf) | [PDF](modules/module_00/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_03/slides.pdf) | [MD](modules/module_00/lessons/lesson_03/script.md) |
| [0.4](modules/module_00/lessons/lesson_04) | Repaso de álgebra lineal | [PDF](modules/module_00/lessons/lesson_04/notes.pdf) | [PDF](modules/module_00/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_04/slides.pdf) | [MD](modules/module_00/lessons/lesson_04/script.md) |
| [0.5](modules/module_00/lessons/lesson_05) | Cadenas de Markov | [PDF](modules/module_00/lessons/lesson_05/notes.pdf) | [PDF](modules/module_00/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_05/slides.pdf) | [MD](modules/module_00/lessons/lesson_05/script.md) |
| [0.6](modules/module_00/lessons/lesson_06) | Análisis de Fourier en grupos abelianos finitos | [PDF](modules/module_00/lessons/lesson_06/notes.pdf) | [PDF](modules/module_00/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_06/slides.pdf) | [MD](modules/module_00/lessons/lesson_06/script.md) |
| [0.7](modules/module_00/lessons/lesson_07) | Lo esencial de JAX | [PDF](modules/module_00/lessons/lesson_07/notes.pdf) | [PDF](modules/module_00/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_00/lessons/lesson_07/slides.pdf) | [MD](modules/module_00/lessons/lesson_07/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_00/assessments/quiz_unidad_00.pdf) · [Laboratorio L1](modules/module_00/projects/L1_jax_markov.pdf) ([código de inicio](modules/module_00/projects/L1_inicio.py))

### Unidad 1 — Termodinámica e información

Semanas 2

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [1.1](modules/module_01/lessons/lesson_01) | Leyes de la termodinámica y energía libre | [PDF](modules/module_01/lessons/lesson_01/notes.pdf) | [PDF](modules/module_01/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_01/slides.pdf) | [MD](modules/module_01/lessons/lesson_01/script.md) |
| [1.2](modules/module_01/lessons/lesson_02) | Mecánica estadística y la distribución de Boltzmann | [PDF](modules/module_01/lessons/lesson_02/notes.pdf) | [PDF](modules/module_01/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_02/slides.pdf) | [MD](modules/module_01/lessons/lesson_02/script.md) |
| [1.3](modules/module_01/lessons/lesson_03) | Entropía de Shannon y entropía de Gibbs | [PDF](modules/module_01/lessons/lesson_03/notes.pdf) | [PDF](modules/module_01/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_03/slides.pdf) | [MD](modules/module_01/lessons/lesson_03/script.md) |
| [1.4](modules/module_01/lessons/lesson_04) | El demonio de Maxwell y la máquina de Szilard | [PDF](modules/module_01/lessons/lesson_04/notes.pdf) | [PDF](modules/module_01/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_04/slides.pdf) | [MD](modules/module_01/lessons/lesson_04/script.md) |
| [1.5](modules/module_01/lessons/lesson_05) | El principio de Landauer | [PDF](modules/module_01/lessons/lesson_05/notes.pdf) | [PDF](modules/module_01/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_05/slides.pdf) | [MD](modules/module_01/lessons/lesson_05/script.md) |
| [1.6](modules/module_01/lessons/lesson_06) | Ruido térmico | [PDF](modules/module_01/lessons/lesson_06/notes.pdf) | [PDF](modules/module_01/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_06/slides.pdf) | [MD](modules/module_01/lessons/lesson_06/script.md) |
| [1.7](modules/module_01/lessons/lesson_07) | Arco histórico | [PDF](modules/module_01/lessons/lesson_07/notes.pdf) | [PDF](modules/module_01/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_01/lessons/lesson_07/slides.pdf) | [MD](modules/module_01/lessons/lesson_07/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_01/assessments/quiz_unidad_01.pdf) · [Laboratorio L2](modules/module_01/projects/L2_landauer.pdf) ([código de inicio](modules/module_01/projects/L2_inicio.py))

### Unidad 2 — Dinámica estocástica

Semanas 3

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [2.1](modules/module_02/lessons/lesson_01) | Movimiento browniano, proceso de Wiener y cálculo de Itô | [PDF](modules/module_02/lessons/lesson_01/notes.pdf) | [PDF](modules/module_02/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_01/slides.pdf) | [MD](modules/module_02/lessons/lesson_01/script.md) |
| [2.2](modules/module_02/lessons/lesson_02) | La ecuación de Langevin | [PDF](modules/module_02/lessons/lesson_02/notes.pdf) | [PDF](modules/module_02/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_02/slides.pdf) | [MD](modules/module_02/lessons/lesson_02/script.md) |
| [2.3](modules/module_02/lessons/lesson_03) | La ecuación de Fokker–Planck | [PDF](modules/module_02/lessons/lesson_03/notes.pdf) | [PDF](modules/module_02/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_03/slides.pdf) | [MD](modules/module_02/lessons/lesson_03/script.md) |
| [2.4](modules/module_02/lessons/lesson_04) | El proceso de Ornstein–Uhlenbeck | [PDF](modules/module_02/lessons/lesson_04/notes.pdf) | [PDF](modules/module_02/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_04/slides.pdf) | [MD](modules/module_02/lessons/lesson_04/script.md) |
| [2.5](modules/module_02/lessons/lesson_05) | El teorema de fluctuación–disipación | [PDF](modules/module_02/lessons/lesson_05/notes.pdf) | [PDF](modules/module_02/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_05/slides.pdf) | [MD](modules/module_02/lessons/lesson_05/script.md) |
| [2.6](modules/module_02/lessons/lesson_06) | Ergodicidad | [PDF](modules/module_02/lessons/lesson_06/notes.pdf) | [PDF](modules/module_02/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_06/slides.pdf) | [MD](modules/module_02/lessons/lesson_06/script.md) |
| [2.7](modules/module_02/lessons/lesson_07) | EDEs numéricas | [PDF](modules/module_02/lessons/lesson_07/notes.pdf) | [PDF](modules/module_02/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_07/slides.pdf) | [MD](modules/module_02/lessons/lesson_07/script.md) |
| [2.8](modules/module_02/lessons/lesson_08) | Procesos de saltos de Markov en tiempo continuo | [PDF](modules/module_02/lessons/lesson_08/notes.pdf) | [PDF](modules/module_02/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_02/lessons/lesson_08/slides.pdf) | [MD](modules/module_02/lessons/lesson_08/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_02/assessments/quiz_unidad_02.pdf) · [Laboratorio L3](modules/module_02/projects/L3_ou_solver.pdf) ([código de inicio](modules/module_02/projects/L3_inicio.py))

### Unidad 3 — Termodinámica estocástica

Semanas 4

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [3.1](modules/module_03/lessons/lesson_01) | Calor, trabajo y entropía a nivel de trayectoria | [PDF](modules/module_03/lessons/lesson_01/notes.pdf) | [PDF](modules/module_03/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_01/slides.pdf) | [MD](modules/module_03/lessons/lesson_01/script.md) |
| [3.2](modules/module_03/lessons/lesson_02) | Producción de entropía y la segunda ley para trayectorias | [PDF](modules/module_03/lessons/lesson_02/notes.pdf) | [PDF](modules/module_03/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_02/slides.pdf) | [MD](modules/module_03/lessons/lesson_02/script.md) |
| [3.3](modules/module_03/lessons/lesson_03) | Teoremas de fluctuación: Crooks y Jarzynski | [PDF](modules/module_03/lessons/lesson_03/notes.pdf) | [PDF](modules/module_03/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_03/slides.pdf) | [MD](modules/module_03/lessons/lesson_03/script.md) |
| [3.4](modules/module_03/lessons/lesson_04) | Límites termodinámicos de velocidad | [PDF](modules/module_03/lessons/lesson_04/notes.pdf) | [PDF](modules/module_03/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_04/slides.pdf) | [MD](modules/module_03/lessons/lesson_04/script.md) |
| [3.5](modules/module_03/lessons/lesson_05) | Diseño de protocolos y aceleración de reloj | [PDF](modules/module_03/lessons/lesson_05/notes.pdf) | [PDF](modules/module_03/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_05/slides.pdf) | [MD](modules/module_03/lessons/lesson_05/script.md) |
| [3.6](modules/module_03/lessons/lesson_06) | Relaciones de incertidumbre termodinámica | [PDF](modules/module_03/lessons/lesson_06/notes.pdf) | [PDF](modules/module_03/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_06/slides.pdf) | [MD](modules/module_03/lessons/lesson_06/script.md) |
| [3.7](modules/module_03/lessons/lesson_07) | Termodinámica del reinicio y de la lectura sin errores | [PDF](modules/module_03/lessons/lesson_07/notes.pdf) | [PDF](modules/module_03/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_07/slides.pdf) | [MD](modules/module_03/lessons/lesson_07/script.md) |
| [3.8](modules/module_03/lessons/lesson_08) | Longitud termodinámica y compromisos energía–tiempo | [PDF](modules/module_03/lessons/lesson_08/notes.pdf) | [PDF](modules/module_03/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_08/slides.pdf) | [MD](modules/module_03/lessons/lesson_08/script.md) |
| [3.9](modules/module_03/lessons/lesson_09) | Matrices de conductancia de no equilibrio | [PDF](modules/module_03/lessons/lesson_09/notes.pdf) | [PDF](modules/module_03/lessons/lesson_09/exercises.pdf) | [PDF](modules/module_03/lessons/lesson_09/slides.pdf) | [MD](modules/module_03/lessons/lesson_09/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_03/assessments/quiz_unidad_03.pdf)

### Unidad 4 — Modelos basados en energía, modelos de Ising y redes neuronales

Semanas 5–6

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [4.1](modules/module_04/lessons/lesson_01) | Modelos basados en energía y modelos gráficos | [PDF](modules/module_04/lessons/lesson_01/notes.pdf) | [PDF](modules/module_04/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_01/slides.pdf) | [MD](modules/module_04/lessons/lesson_01/script.md) |
| [4.2](modules/module_04/lessons/lesson_02) | El modelo de Ising | [PDF](modules/module_04/lessons/lesson_02/notes.pdf) | [PDF](modules/module_04/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_02/slides.pdf) | [MD](modules/module_04/lessons/lesson_02/script.md) |
| [4.3](modules/module_04/lessons/lesson_03) | MCMC: Metropolis–Hastings y Gibbs | [PDF](modules/module_04/lessons/lesson_03/notes.pdf) | [PDF](modules/module_04/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_03/slides.pdf) | [MD](modules/module_04/lessons/lesson_03/script.md) |
| [4.4](modules/module_04/lessons/lesson_04) | Diagnósticos de muestreo | [PDF](modules/module_04/lessons/lesson_04/notes.pdf) | [PDF](modules/module_04/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_04/slides.pdf) | [MD](modules/module_04/lessons/lesson_04/script.md) |
| [4.5](modules/module_04/lessons/lesson_05) | El pbit como neurona estocástica | [PDF](modules/module_04/lessons/lesson_05/notes.pdf) | [PDF](modules/module_04/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_05/slides.pdf) | [MD](modules/module_04/lessons/lesson_05/script.md) |
| [4.6](modules/module_04/lessons/lesson_06) | Redes de Hopfield y memoria asociativa | [PDF](modules/module_04/lessons/lesson_06/notes.pdf) | [PDF](modules/module_04/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_06/slides.pdf) | [MD](modules/module_04/lessons/lesson_06/script.md) |
| [4.7](modules/module_04/lessons/lesson_07) | Máquinas de Boltzmann y su regla de aprendizaje | [PDF](modules/module_04/lessons/lesson_07/notes.pdf) | [PDF](modules/module_04/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_07/slides.pdf) | [MD](modules/module_04/lessons/lesson_07/script.md) |
| [4.8](modules/module_04/lessons/lesson_08) | RBMs y divergencia contrastiva | [PDF](modules/module_04/lessons/lesson_08/notes.pdf) | [PDF](modules/module_04/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_08/slides.pdf) | [MD](modules/module_04/lessons/lesson_08/script.md) |
| [4.9](modules/module_04/lessons/lesson_09) | Teoría de campo medio | [PDF](modules/module_04/lessons/lesson_09/notes.pdf) | [PDF](modules/module_04/lessons/lesson_09/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_09/slides.pdf) | [MD](modules/module_04/lessons/lesson_09/script.md) |
| [4.10](modules/module_04/lessons/lesson_10) | Optimización con Ising y lógica probabilística invertible | [PDF](modules/module_04/lessons/lesson_10/notes.pdf) | [PDF](modules/module_04/lessons/lesson_10/exercises.pdf) | [PDF](modules/module_04/lessons/lesson_10/slides.pdf) | [MD](modules/module_04/lessons/lesson_10/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_04/assessments/quiz_unidad_04.pdf)

### Unidad 5 — Hardware probabilístico y termodinámico

Semanas 7

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [5.1](modules/module_05/lessons/lesson_01) | Por qué el hardware digital es ineficiente para la IA probabilística | [PDF](modules/module_05/lessons/lesson_01/notes.pdf) | [PDF](modules/module_05/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_01/slides.pdf) | [MD](modules/module_05/lessons/lesson_01/script.md) |
| [5.2](modules/module_05/lessons/lesson_02) | p-bits: MTJ y CMOS | [PDF](modules/module_05/lessons/lesson_02/notes.pdf) | [PDF](modules/module_05/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_02/slides.pdf) | [MD](modules/module_05/lessons/lesson_02/script.md) |
| [5.3](modules/module_05/lessons/lesson_03) | Los TSU de Extropic | [PDF](modules/module_05/lessons/lesson_03/notes.pdf) | [PDF](modules/module_05/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_03/slides.pdf) | [MD](modules/module_05/lessons/lesson_03/script.md) |
| [5.4](modules/module_05/lessons/lesson_04) | Unidades de procesamiento estocástico continuo | [PDF](modules/module_05/lessons/lesson_04/notes.pdf) | [PDF](modules/module_05/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_04/slides.pdf) | [MD](modules/module_05/lessons/lesson_04/script.md) |
| [5.5](modules/module_05/lessons/lesson_05) | Otros sustratos físicos | [PDF](modules/module_05/lessons/lesson_05/notes.pdf) | [PDF](modules/module_05/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_05/slides.pdf) | [MD](modules/module_05/lessons/lesson_05/script.md) |
| [5.6](modules/module_05/lessons/lesson_06) | No idealidades analógicas | [PDF](modules/module_05/lessons/lesson_06/notes.pdf) | [PDF](modules/module_05/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_06/slides.pdf) | [MD](modules/module_05/lessons/lesson_06/script.md) |
| [5.7](modules/module_05/lessons/lesson_07) | Abstracciones de hardware | [PDF](modules/module_05/lessons/lesson_07/notes.pdf) | [PDF](modules/module_05/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_07/slides.pdf) | [MD](modules/module_05/lessons/lesson_07/script.md) |
| [5.8](modules/module_05/lessons/lesson_08) | Contabilidad energética en sistemas heterogéneos | [PDF](modules/module_05/lessons/lesson_08/notes.pdf) | [PDF](modules/module_05/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_05/lessons/lesson_08/slides.pdf) | [MD](modules/module_05/lessons/lesson_08/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_05/assessments/quiz_unidad_05.pdf)

### Unidad 6 — Algoritmos termodinámicos I: álgebra lineal e inferencia

Semanas 8

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [6.1](modules/module_06/lessons/lesson_01) | Sistemas lineales desde el primer momento de un OU | [PDF](modules/module_06/lessons/lesson_01/notes.pdf) | [PDF](modules/module_06/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_01/slides.pdf) | [MD](modules/module_06/lessons/lesson_01/script.md) |
| [6.2](modules/module_06/lessons/lesson_02) | Inversa de matrices y ecuaciones de Lyapunov | [PDF](modules/module_06/lessons/lesson_02/notes.pdf) | [PDF](modules/module_06/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_02/slides.pdf) | [MD](modules/module_06/lessons/lesson_02/script.md) |
| [6.3](modules/module_06/lessons/lesson_03) | Determinantes desde estadísticas de trabajo | [PDF](modules/module_06/lessons/lesson_03/notes.pdf) | [PDF](modules/module_06/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_03/slides.pdf) | [MD](modules/module_06/lessons/lesson_03/script.md) |
| [6.4](modules/module_06/lessons/lesson_04) | Complejidad de los algoritmos termodinámicos | [PDF](modules/module_06/lessons/lesson_04/notes.pdf) | [PDF](modules/module_06/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_04/slides.pdf) | [MD](modules/module_06/lessons/lesson_04/script.md) |
| [6.5](modules/module_06/lessons/lesson_05) | Modelos de tiempo | [PDF](modules/module_06/lessons/lesson_05/notes.pdf) | [PDF](modules/module_06/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_05/slides.pdf) | [MD](modules/module_06/lessons/lesson_05/script.md) |
| [6.6](modules/module_06/lessons/lesson_06) | Panorama: inferencia y más allá | [PDF](modules/module_06/lessons/lesson_06/notes.pdf) | [PDF](modules/module_06/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_06/lessons/lesson_06/slides.pdf) | [MD](modules/module_06/lessons/lesson_06/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_06/assessments/quiz_unidad_06.pdf)

### Unidad 7 — Algoritmos termodinámicos II: cómputo por difusión y la analogía con Shor

Semanas 9

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [7.1](modules/module_07/lessons/lesson_01) | De la factorización a la búsqueda de orden | [PDF](modules/module_07/lessons/lesson_01/notes.pdf) | [PDF](modules/module_07/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_01/slides.pdf) | [MD](modules/module_07/lessons/lesson_01/script.md) |
| [7.2](modules/module_07/lessons/lesson_02) | El algoritmo de Shor | [PDF](modules/module_07/lessons/lesson_02/notes.pdf) | [PDF](modules/module_07/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_02/slides.pdf) | [MD](modules/module_07/lessons/lesson_02/script.md) |
| [7.3](modules/module_07/lessons/lesson_03) | Caminatas aleatorias en grafos de Cayley | [PDF](modules/module_07/lessons/lesson_03/notes.pdf) | [PDF](modules/module_07/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_03/slides.pdf) | [MD](modules/module_07/lessons/lesson_03/script.md) |
| [7.4](modules/module_07/lessons/lesson_04) | El teorema de búsqueda de orden por difusión | [PDF](modules/module_07/lessons/lesson_04/notes.pdf) | [PDF](modules/module_07/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_04/slides.pdf) | [MD](modules/module_07/lessons/lesson_04/script.md) |
| [7.5](modules/module_07/lessons/lesson_05) | Identidades de sumas trigonométricas | [PDF](modules/module_07/lessons/lesson_05/notes.pdf) | [PDF](modules/module_07/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_05/slides.pdf) | [MD](modules/module_07/lessons/lesson_05/script.md) |
| [7.6](modules/module_07/lessons/lesson_06) | Realización física con redes RC | [PDF](modules/module_07/lessons/lesson_06/notes.pdf) | [PDF](modules/module_07/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_06/slides.pdf) | [MD](modules/module_07/lessons/lesson_06/script.md) |
| [7.7](modules/module_07/lessons/lesson_07) | La variante por colisiones | [PDF](modules/module_07/lessons/lesson_07/notes.pdf) | [PDF](modules/module_07/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_07/slides.pdf) | [MD](modules/module_07/lessons/lesson_07/script.md) |
| [7.8](modules/module_07/lessons/lesson_08) | Complejidad comparada | [PDF](modules/module_07/lessons/lesson_08/notes.pdf) | [PDF](modules/module_07/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_07/lessons/lesson_08/slides.pdf) | [MD](modules/module_07/lessons/lesson_08/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_07/assessments/quiz_unidad_07.pdf)

### Unidad 8 — Aprendizaje automático termodinámico: entrenamiento

Semanas 10–11

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [8.1](modules/module_08/lessons/lesson_01) | Geometría de la información y gradiente natural | [PDF](modules/module_08/lessons/lesson_01/notes.pdf) | [PDF](modules/module_08/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_01/slides.pdf) | [MD](modules/module_08/lessons/lesson_01/script.md) |
| [8.2](modules/module_08/lessons/lesson_02) | Matrices de curvatura | [PDF](modules/module_08/lessons/lesson_02/notes.pdf) | [PDF](modules/module_08/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_02/slides.pdf) | [MD](modules/module_08/lessons/lesson_02/script.md) |
| [8.3](modules/module_08/lessons/lesson_03) | Descenso de gradiente natural termodinámico (TNGD) | [PDF](modules/module_08/lessons/lesson_03/notes.pdf) | [PDF](modules/module_08/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_03/slides.pdf) | [MD](modules/module_08/lessons/lesson_03/script.md) |
| [8.4](modules/module_08/lessons/lesson_04) | K-FAC | [PDF](modules/module_08/lessons/lesson_04/notes.pdf) | [PDF](modules/module_08/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_04/slides.pdf) | [MD](modules/module_08/lessons/lesson_04/script.md) |
| [8.5](modules/module_08/lessons/lesson_05) | K-FAC termodinámico | [PDF](modules/module_08/lessons/lesson_05/notes.pdf) | [PDF](modules/module_08/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_05/slides.pdf) | [MD](modules/module_08/lessons/lesson_05/script.md) |
| [8.6](modules/module_08/lessons/lesson_06) | Computadores de Langevin no lineales como clasificadores | [PDF](modules/module_08/lessons/lesson_06/notes.pdf) | [PDF](modules/module_08/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_06/slides.pdf) | [MD](modules/module_08/lessons/lesson_06/script.md) |
| [8.7](modules/module_08/lessons/lesson_07) | Entrenamiento consciente del hardware | [PDF](modules/module_08/lessons/lesson_07/notes.pdf) | [PDF](modules/module_08/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_08/lessons/lesson_07/slides.pdf) | [MD](modules/module_08/lessons/lesson_07/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_08/assessments/quiz_unidad_08.pdf)

### Unidad 9 — Modelos generativos en hardware termodinámico

Semanas 12

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [9.1](modules/module_09/lessons/lesson_01) | Modelos de difusión | [PDF](modules/module_09/lessons/lesson_01/notes.pdf) | [PDF](modules/module_09/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_09/lessons/lesson_01/slides.pdf) | [MD](modules/module_09/lessons/lesson_01/script.md) |
| [9.2](modules/module_09/lessons/lesson_02) | Difusión discreta | [PDF](modules/module_09/lessons/lesson_02/notes.pdf) | [PDF](modules/module_09/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_09/lessons/lesson_02/slides.pdf) | [MD](modules/module_09/lessons/lesson_02/script.md) |
| [9.3](modules/module_09/lessons/lesson_03) | Modelos termodinámicos de eliminación de ruido (DTM) | [PDF](modules/module_09/lessons/lesson_03/notes.pdf) | [PDF](modules/module_09/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_09/lessons/lesson_03/slides.pdf) | [MD](modules/module_09/lessons/lesson_03/script.md) |
| [9.4](modules/module_09/lessons/lesson_04) | Modelo de costo de la difusión | [PDF](modules/module_09/lessons/lesson_04/notes.pdf) | [PDF](modules/module_09/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_09/lessons/lesson_04/slides.pdf) | [MD](modules/module_09/lessons/lesson_04/script.md) |
| [9.5](modules/module_09/lessons/lesson_05) | Análisis de eficiencia: Ruta A vs Ruta B | [PDF](modules/module_09/lessons/lesson_05/notes.pdf) | [PDF](modules/module_09/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_09/lessons/lesson_05/slides.pdf) | [MD](modules/module_09/lessons/lesson_05/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_09/assessments/quiz_unidad_09.pdf)

### Unidad 10 — Modelos de lenguaje termodinámicos

Semanas 13–14

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [10.1](modules/module_10/lessons/lesson_01) | Repaso de transformers | [PDF](modules/module_10/lessons/lesson_01/notes.pdf) | [PDF](modules/module_10/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_01/slides.pdf) | [MD](modules/module_10/lessons/lesson_01/script.md) |
| [10.2](modules/module_10/lessons/lesson_02) | Atención libre y atención lineal | [PDF](modules/module_10/lessons/lesson_02/notes.pdf) | [PDF](modules/module_10/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_02/slides.pdf) | [MD](modules/module_10/lessons/lesson_02/script.md) |
| [10.3](modules/module_10/lessons/lesson_03) | Normalización DyT | [PDF](modules/module_10/lessons/lesson_03/notes.pdf) | [PDF](modules/module_10/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_03/slides.pdf) | [MD](modules/module_10/lessons/lesson_03/script.md) |
| [10.4](modules/module_10/lessons/lesson_04) | Transformers dispersos | [PDF](modules/module_10/lessons/lesson_04/notes.pdf) | [PDF](modules/module_10/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_04/slides.pdf) | [MD](modules/module_10/lessons/lesson_04/script.md) |
| [10.5](modules/module_10/lessons/lesson_05) | Codificar números en pbits | [PDF](modules/module_10/lessons/lesson_05/notes.pdf) | [PDF](modules/module_10/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_05/slides.pdf) | [MD](modules/module_10/lessons/lesson_05/script.md) |
| [10.6](modules/module_10/lessons/lesson_06) | Unidades tanh-lineales | [PDF](modules/module_10/lessons/lesson_06/notes.pdf) | [PDF](modules/module_10/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_06/slides.pdf) | [MD](modules/module_10/lessons/lesson_06/script.md) |
| [10.7](modules/module_10/lessons/lesson_07) | La arquitectura Z1T e inferencia desagregada | [PDF](modules/module_10/lessons/lesson_07/notes.pdf) | [PDF](modules/module_10/lessons/lesson_07/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_07/slides.pdf) | [MD](modules/module_10/lessons/lesson_07/script.md) |
| [10.8](modules/module_10/lessons/lesson_08) | Métricas de energía para LLMs | [PDF](modules/module_10/lessons/lesson_08/notes.pdf) | [PDF](modules/module_10/lessons/lesson_08/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_08/slides.pdf) | [MD](modules/module_10/lessons/lesson_08/script.md) |
| [10.9](modules/module_10/lessons/lesson_09) | Caso de estudio: pipeline AFT-Transformer + TNGD en JAX | [PDF](modules/module_10/lessons/lesson_09/notes.pdf) | [PDF](modules/module_10/lessons/lesson_09/exercises.pdf) | [PDF](modules/module_10/lessons/lesson_09/slides.pdf) | [MD](modules/module_10/lessons/lesson_09/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_10/assessments/quiz_unidad_10.pdf)

### Unidad 11 — Pila de software, agentes de investigación y fronteras

Semanas 15

| Lección | Título | Notas | Ejercicios | Diapositivas | Guion |
|---|---|---|---|---|---|
| [11.1](modules/module_11/lessons/lesson_01) | THRML | [PDF](modules/module_11/lessons/lesson_01/notes.pdf) | [PDF](modules/module_11/lessons/lesson_01/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_01/slides.pdf) | [MD](modules/module_11/lessons/lesson_01/script.md) |
| [11.2](modules/module_11/lessons/lesson_02) | Torx | [PDF](modules/module_11/lessons/lesson_02/notes.pdf) | [PDF](modules/module_11/lessons/lesson_02/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_02/slides.pdf) | [MD](modules/module_11/lessons/lesson_02/script.md) |
| [11.3](modules/module_11/lessons/lesson_03) | Thermalizers | [PDF](modules/module_11/lessons/lesson_03/notes.pdf) | [PDF](modules/module_11/lessons/lesson_03/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_03/slides.pdf) | [MD](modules/module_11/lessons/lesson_03/script.md) |
| [11.4](modules/module_11/lessons/lesson_04) | La API del simulador y flujos de investigación agéntica | [PDF](modules/module_11/lessons/lesson_04/notes.pdf) | [PDF](modules/module_11/lessons/lesson_04/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_04/slides.pdf) | [MD](modules/module_11/lessons/lesson_04/script.md) |
| [11.5](modules/module_11/lessons/lesson_05) | Agentes de investigación con LLM | [PDF](modules/module_11/lessons/lesson_05/notes.pdf) | [PDF](modules/module_11/lessons/lesson_05/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_05/slides.pdf) | [MD](modules/module_11/lessons/lesson_05/script.md) |
| [11.6](modules/module_11/lessons/lesson_06) | Problemas abiertos | [PDF](modules/module_11/lessons/lesson_06/notes.pdf) | [PDF](modules/module_11/lessons/lesson_06/exercises.pdf) | [PDF](modules/module_11/lessons/lesson_06/slides.pdf) | [MD](modules/module_11/lessons/lesson_06/script.md) |

**Evaluación y laboratorios:** [Quiz](modules/module_11/assessments/quiz_unidad_11.pdf)

## Compilar los documentos LaTeX

Los PDF ya están incluidos. Para recompilar una lección, apunte `TEXINPUTS` a la carpeta `latex/`:

```bash
cd modules/module_01/lessons/lesson_05
TEXINPUTS=../../../../latex//: pdflatex notes.tex
```

Los laboratorios usan Python con `jax` y `numpy`.

## Referencias

- [Bibliografía](references/bibliografia.md)
- [Videos de referencia y club de revista](references/videos_y_club_de_revista.md)
- [Objetivos de aprendizaje](syllabus/learning_objectives.md)
- [Pensum original](syllabus/original_syllabus.pdf)

## Licencia

[GNU GPL v3](LICENSE)
