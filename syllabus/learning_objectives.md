# Objetivos de aprendizaje — Computación Termodinámica para IA

> Traducción fiel de las secciones 3 y 4 del pensum original (`original_syllabus.pdf`).

## Objetivo general
Formar estudiantes capaces de comprender, diseñar, simular y evaluar críticamente sistemas de cómputo termodinámicos y probabilísticos para inteligencia artificial, desde los principios físicos hasta los algoritmos conscientes del hardware y los modelos de lenguaje termodinámicos.

## Objetivos específicos
| Código | Objetivo |
|---|---|
| **OE1** | Dominar los fundamentos físicos: estadística de Boltzmann, dinámica de Langevin y Fokker–Planck, principio de Landauer, teoremas de fluctuación, límites de velocidad y relaciones de incertidumbre. |
| **OE2** | Formular problemas computacionales como programas basados en energía (modelos de Ising, potenciales cuadráticos, máquinas de Boltzmann) y resolverlos por muestreo o equilibración. |
| **OE3** | Analizar la arquitectura y las restricciones del hardware termodinámico: conectividad fija, precisión, desajuste, E/S y pegamento digital. |
| **OE4** | Implementar algoritmos termodinámicos para álgebra lineal, optimización (TNGD, K-FAC) y teoría de números (búsqueda de orden por difusión), y compararlos con enfoques digitales y cuánticos. |
| **OE5** | Diseñar modelos generativos conscientes del hardware: modelos termodinámicos de eliminación de ruido, modelos de lenguaje de difusión enmascarada y transformers dispersos tipo Z1T. |
| **OE6** | Construir y usar modelos y métricas energéticas explícitas (J/token, J/FLOP, MFU, producción de entropía, eficiencia η, fracción de E/S) para evaluar afirmaciones con rigor. |
| **OE7** | Llevar a cabo un proyecto de investigación reproducible y comunicarlo en un informe científico y una presentación oral, usando asistentes de IA de manera responsable. |

## Resultados de aprendizaje (competencias)
| Código | Al final del curso el estudiante es capaz de… | Nivel de Bloom | Evidencia |
|---|---|---|---|
| **RA1** | Explicar los principios físicos del cómputo termodinámico (distribución de Boltzmann, dinámica de Langevin, cota de Landauer, Jarzynski/Crooks, TUR, límite de velocidad de Wasserstein). | Comprender | Quices, parcial |
| **RA2** | Derivar y simular dinámicas estocásticas (OU, Langevin, Gibbs, ecuaciones maestras) y verificar distribuciones estacionarias, mezcla y promedios ergódicos. | Aplicar / Analizar | Labs 2–5 |
| **RA3** | Formular problemas de ML y de álgebra lineal como programas basados en energía y mapearlos a grafos de hardware. | Aplicar / Crear | Labs 5–8 |
| **RA4** | Analizar restricciones de hardware (grado, precisión, desajuste, E/S, pegamento digital) y su efecto en los algoritmos. | Analizar | Lab 7, Lab 14, seminario |
| **RA5** | Implementar y comparar algoritmos termodinámicos (solvers lineales, TNGD, K-FAC termodinámico, búsqueda de orden por difusión) contra líneas base digitales y cuánticas. | Aplicar / Evaluar | Labs 8–11 |
| **RA6** | Diseñar modelos generativos conscientes del hardware (DTM, LMs de difusión enmascarada, transformers tipo Z1T). | Crear | Labs 12–14, proyecto final |
| **RA7** | Evaluar afirmaciones energéticas con modelos de costo explícitos y distinguir evidencia medida, simulada, proyectada y estimada. | Evaluar | Todos los labs, proyecto final |
| **RA8** | Reproducir y extender un resultado de investigación; redactarlo y presentarlo profesionalmente; usar agentes de IA con divulgación y verificación. | Crear | Club de revista, Lab 15, proyecto final |

## Mapa unidades → objetivos
| Unidad | OE | RA |
|---|---|---|
| U0 Nivelación | — (prerrequisitos) | RA2 (base) |
| U1 Termodinámica e información | OE1 | RA1 |
| U2 Dinámica estocástica | OE1, OE2 | RA1, RA2 |
| U3 Termodinámica estocástica | OE1, OE6 | RA1, RA2, RA7 |
| U4 EBMs, Ising, redes neuronales | OE2 | RA2, RA3 |
| U5 Hardware | OE3, OE6 | RA4, RA7 |
| U6 Álgebra lineal termodinámica | OE2, OE4 | RA3, RA5 |
| U7 Difusión y analogía con Shor | OE4 | RA5 |
| U8 Entrenamiento termodinámico | OE4 | RA5 |
| U9 Modelos generativos | OE5, OE6 | RA6, RA7 |
| U10 LMs termodinámicos | OE5, OE6 | RA4, RA6, RA7 |
| U11 Software y agentes | OE7 | RA8 |

## Supuestos documentados
- Se toma el PDF v1 (12 unidades, 16 semanas) como fuente de verdad; `pensum_v2.tex` no se usa.
- Idioma de todo el material: español neutro internacional.
- Las cifras de hardware de fabricantes (p. ej. Z1) se reportan tal como aparecen en el pensum y se etiquetan como [P] (proyección del fabricante) salvo indicación contraria.
