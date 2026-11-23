# Lesson 3.9 — Non-equilibrium conductance matrices

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the thermodynamic force of a reaction $f_\rho = k_BT\ln\frac{k_\rho^+[Z]^{\nu_\rho^+}}{k_\rho^-[Z]^{\nu_\rho^-}}$ and its resistance $r_\rho = f_\rho/j_\rho$.
- Show that resistances of reactions in series add at a stationary state: $R = r_1 + r_2$, $G = 1/R$.
- Compare the linear regime ($r_\rho \approx k_BT/j_\rho^{\text{eq}}$) with the non-equilibrium conductance far from equilibrium.

## Prerequisites
- Lesson 2.8: master equation and jump processes.
- Lesson 3.2: entropy production.
- Lesson 1.6: Ohm's law and resistors.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Una red de reacciones químicas abierta, alimentada por quimiostatos que fijan algunas concentraciones, se parece a un circuito eléctrico. Las corrientes son flujos de reacción y los voltajes son diferencias de potencial químico. Raux, Goupil y Verley mostraron que esa analogía puede hacerse precisa con matrices de conductancia de no equilibrio. Así, una red grande se analiza conectando módulos, como resistencias.

**EN:** An open chemical reaction network, fed by chemostats that fix some concentrations, looks like an electrical circuit. Currents are reaction fluxes and voltages are chemical-potential differences. Raux, Goupil and Verley showed that this analogy can be made precise with non-equilibrium conductance matrices. That way, a large network is analyzed by connecting modules, like resistors.

### [00:32.3] Force and current — `manim:S02`

**ES:** Tomemos una reacción reversible con cinética de acción de masas. La corriente es el flujo directo menos el inverso, j = k⁺[A] − k⁻[B]. La fuerza termodinámica es k_B T por el logaritmo del cociente entre ambos flujos, que es menos el cambio de energía libre de la reacción. Corriente y fuerza tienen siempre el mismo signo: su producto es la producción de entropía, que nunca es negativa.

**EN:** Take a reversible reaction with mass-action kinetics. The current is the forward flux minus the backward one, j = k⁺[A] − k⁻[B]. The thermodynamic force is k_B T times the log of the ratio of the two fluxes, which is minus the reaction's free-energy change. Current and force always have the same sign: their product is the entropy production, which is never negative.

### [00:59.9] Resistance of a reaction — `manim:S03`

**ES:** Definimos la resistencia de la reacción como el cociente r = f/j, igual que la ley de Ohm. Cerca del equilibrio, la fuerza es pequeña y la corriente es proporcional a ella: r ≈ k_B T/j_eq, donde j_eq es el flujo de intercambio, lo que va y viene en cada sentido. Una reacción rápida conduce bien; una lenta es una resistencia grande. Lejos del equilibrio la resistencia ya no es constante: depende del estado estacionario.

**EN:** We define the reaction's resistance as the ratio r = f/j, just like Ohm's law. Near equilibrium, the force is small and the current is proportional to it: r ≈ k_B T/j_eq, where j_eq is the exchange flux, what goes back and forth in each direction. A fast reaction conducts well; a slow one is a large resistance. Far from equilibrium the resistance is no longer constant: it depends on the stationary state.

### [01:33.3] Resistances in series — `manim:S04`

**ES:** Ahora conectemos dos reacciones en serie: A ⇄ B ⇄ C, con A y C fijadas por quimiostatos. En el estado estacionario la concentración de B se ajusta hasta que por ambas reacciones pasa la misma corriente. Las fuerzas se suman, porque las diferencias de potencial químico se encadenan. Con la misma corriente y fuerzas que se suman, las resistencias se suman: R = r₁ + r₂, y la conductancia del módulo es G = 1/R. Es la ley de suma de resistencias, ahora para química.

**EN:** Now let's connect two reactions in series: A ⇄ B ⇄ C, with A and C fixed by chemostats. In the stationary state the concentration of B adjusts until the same current flows through both reactions. The forces add, because chemical-potential differences chain together. With the same current and forces that add, the resistances add: R = r₁ + r₂, and the module's conductance is G = 1/R. It is the resistance-addition law, now for chemistry.

### [02:06.4] Conductance matrices — `manim:S05`

**ES:** En una red con varios ciclos y varios quimiostatos, las resistencias se vuelven matrices. Cada ciclo tiene su corriente, y la matriz de resistencias de ciclos relaciona fuerzas y corrientes: F = R J. Su inversa es la matriz de conductancia. Es simétrica y semidefinida positiva, porque la producción de entropía no puede ser negativa. Al conectar módulos en serie, sus matrices se combinan como resistencias, y el resultado coincide con el cálculo directo de toda la red.

**EN:** In a network with several cycles and several chemostats, the resistances become matrices. Each cycle has its current, and the cycle resistance matrix relates forces and currents: F = R J. Its inverse is the conductance matrix. It is symmetric and positive semi-definite, because entropy production cannot be negative. When modules are connected in series, their matrices combine like resistances, and the result matches the direct calculation for the whole network.

### [02:38.0] Numerical example — `manim:S06`

**ES:** Con todas las constantes iguales a uno y C fijada en uno, variemos la concentración de A. Cerca del equilibrio, con A en uno coma uno, la conductancia vale cero coma cinco dos, muy cerca del valor lineal, un medio. Con A igual a cinco, la corriente es dos, la fuerza total uno coma seis k_B T y la conductancia uno coma dos cuatro. Con A igual a cien, la conductancia supera diez. Lejos del equilibrio la red conduce mucho más de lo que predice la respuesta lineal, pero la suma de resistencias sigue siendo exacta en cada estado estacionario.

**EN:** With all rate constants equal to one and C fixed at one, let's vary the concentration of A. Near equilibrium, with A at 1.1, the conductance is 0.52, very close to the linear value, one half. With A equal to five, the current is two, the total force 1.6 k_B T and the conductance 1.24. With A equal to a hundred, the conductance exceeds ten. Far from equilibrium the network conducts much more than linear response predicts, but resistance addition is still exact at each stationary state.

### [03:13.7] Applications — `slide`

**ES:** Esta teoría de circuitos permite analizar redes grandes por módulos, diseñar computadores químicos donde corrientes y fuerzas son señales, y llevar la cuenta de la disipación, que es una forma cuadrática positiva en las fuerzas. En un reto de laboratorio compararás una corriente estacionaria simulada con la predicción de la matriz de conductancia.

**EN:** This circuit theory lets us analyze large networks by modules, design chemical computers where currents and forces are signals, and keep track of dissipation, which is a positive quadratic form in the forces. In a lab challenge you will compare a simulated stationary current with the conductance-matrix prediction.

### [03:35.1] Common mistakes — `slide`

**ES:** Errores frecuentes: tratar la resistencia como constante lejos del equilibrio. Sumar fuerzas de reacciones que no están en serie. Olvidar que son los quimiostatos los que fijan las fuerzas. Y confundir la conductancia, corriente sobre fuerza, con la conductancia diferencial, la derivada de la corriente.

**EN:** Frequent mistakes: treating the resistance as constant far from equilibrium. Adding forces of reactions that are not in series. Forgetting that it is the chemostats that fix the forces. And confusing the conductance, current over force, with the differential conductance, the derivative of the current.

### [03:55.1] Summary — `manim:S09`

**ES:** En resumen: cada reacción tiene una fuerza, k_B T por el logaritmo del cociente de flujos, y una resistencia, fuerza sobre corriente. En serie, las resistencias se suman exactamente en el estado estacionario. En redes con varios ciclos, matrices de conductancia simétricas y positivas generalizan la ley de Ohm a la química fuera del equilibrio.

**EN:** In summary: each reaction has a force, k_B T times the log of the flux ratio, and a resistance, force over current. In series, resistances add exactly at the stationary state. In networks with several cycles, symmetric positive conductance matrices generalize Ohm's law to non-equilibrium chemistry.

### [04:17.5] Self-assessment — `slide`

**ES:** Para practicar: calcula fuerza, corriente y resistencia de una reacción. Demuestra el límite lineal. Encuentra el estado estacionario de la cadena y verifica la suma de resistencias. Y explica por qué la matriz de conductancia es semidefinida positiva.

**EN:** To practice: compute the force, current and resistance of a reaction. Prove the linear limit. Find the chain's stationary state and check resistance addition. And explain why the conductance matrix is positive semi-definite.

## Key equations
- $$j_\rho = k_\rho^+[A] - k_\rho^-[B],\qquad f_\rho = k_BT\ln\frac{k_\rho^+[A]}{k_\rho^-[B]} = -\Delta_\rho G$$ — Current and thermodynamic force of a mass-action reaction ($f_\rho j_\rho \ge 0$).
- $$r_\rho = \frac{f_\rho}{j_\rho} \;\xrightarrow{\ \text{near eq.}\ }\; \frac{k_BT}{j_\rho^{\text{eq}}}$$ — Reaction resistance and its linear-response limit (exchange flux $j^{\text{eq}}$).
- $$R = r_1 + r_2,\qquad G = R^{-1};\qquad F = R\,J\ \ (\text{cycles})$$ — Resistance addition in series and the cycle resistance/conductance matrices.

## Summary
- Force $f = k_BT\ln(\text{forward}/\text{backward flux})$; current $j$; $f j \ge 0$.
- Resistance $r = f/j$; near equilibrium $r \approx k_BT/j_{\text{eq}}$.
- Series at a stationary state: $R = r_1 + r_2$ exactly.
- Matrices $F = RJ$, $G = R^{-1}$ symmetric and positive semi-definite; modules compose like circuits.

## Further reading
- [27] P. Raux, C. Goupil and G. Verley, Thermodynamic circuits: modeling chemical reaction networks with nonequilibrium conductance matrices, 2025. arXiv:2412.15028.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics.
- [11] U. Seifert, Stochastic thermodynamics..., 2012.
