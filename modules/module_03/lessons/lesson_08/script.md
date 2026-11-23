# Lesson 3.8 — Thermodynamic length and energy–time trade-offs

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Define the friction tensor $\zeta(\lambda) = \beta\int_0^\infty\langle\delta X(t)\,\delta X(0)\rangle\,dt$ and the excess work $\langle W_{\text{ex}}\rangle \approx \int \dot\lambda\,\zeta\,\dot\lambda\,dt$.
- Compute the thermodynamic length $\mathcal L = \int\sqrt{\zeta}\,|d\lambda|$ and the bound $\langle W_{\text{ex}}\rangle \ge \mathcal L^2/\tau$.
- Build the optimal protocol: constant thermodynamic speed.

## Prerequisites
- Lesson 2.5: fluctuation–dissipation and autocorrelation.
- Lessons 3.4–3.5: speed limits and protocol design.

## Narrated script

### [00:06.5] Introduction — `manim:S01`

**ES:** En la lección anterior vimos que cargar un problema lentamente disipa menos. Pero con un tiempo fijo hay infinitas maneras de ir de la energía inicial a la final. ¿Cuál disipa menos? La respuesta es geométrica: el espacio de parámetros de control tiene una métrica, y el mejor protocolo recorre su geodésica a velocidad constante. Esa métrica define la longitud termodinámica.

**EN:** In the previous lesson we saw that loading a problem slowly dissipates less. But with a fixed time there are infinitely many ways to go from the initial energy to the final one. Which one dissipates least? The answer is geometric: the space of control parameters has a metric, and the best protocol travels its geodesic at constant speed. That metric defines the thermodynamic length.

### [00:30.5] Intuition — `manim:S02`

**ES:** Imagina cruzar un terreno con barro de profundidad variable en un tiempo fijo. Cada tramo cuesta más cuanto más rápido lo cruzas y cuanto más profundo es el barro. Si vas a la misma velocidad todo el camino, pagas mucho en las zonas profundas. Conviene ir despacio donde el barro es profundo y rápido donde es firme. En un sistema físico, el barro es la fricción: lo lento que el sistema se reacomoda cuando movemos el control.

**EN:** Imagine crossing ground with mud of varying depth in a fixed time. Each stretch costs more the faster you cross it and the deeper the mud. If you go at the same speed the whole way, you pay a lot in the deep zones. It is better to go slowly where the mud is deep and fast where it is firm. In a physical system, the mud is friction: how slowly the system readjusts when we move the control.

### [00:57.1] Friction tensor — `manim:S03`

**ES:** Sea λ el parámetro de control y X = −∂_λ V la fuerza conjugada. Cerca del equilibrio, el trabajo en exceso es ⟨W_ex⟩ ≈ ∫ λ̇ ζ(λ) λ̇ dt, cuadrático en la velocidad del control. El coeficiente es el tensor de fricción, ζ = β ∫ ⟨δX(t) δX(0)⟩ dt: la varianza de la fuerza multiplicada por su tiempo de correlación. Es otra cara del teorema de fluctuación y disipación: donde las fluctuaciones son grandes y lentas, mover el control disipa más.

**EN:** Let λ be the control parameter and X = −∂_λ V the conjugate force. Near equilibrium, the excess work is ⟨W_ex⟩ ≈ ∫ λ̇ ζ(λ) λ̇ dt, quadratic in the control speed. The coefficient is the friction tensor, ζ = β ∫ ⟨δX(t) δX(0)⟩ dt: the variance of the force times its correlation time. It is another face of the fluctuation–dissipation theorem: where fluctuations are large and slow, moving the control dissipates more.

### [01:33.9] Thermodynamic length — `manim:S04`

**ES:** El tensor de fricción es una métrica. Con ella definimos la longitud termodinámica, ℒ = ∫ √ζ , que no depende de la velocidad. La desigualdad de Cauchy y Schwarz da la cota ⟨W_ex⟩ ≥ ℒ²/τ. La igualdad se alcanza cuando la velocidad termodinámica, √ζ λ̇, es constante. El protocolo óptimo va despacio donde la fricción es alta y rápido donde es baja, igual que en el barro.

**EN:** The friction tensor is a metric. With it we define the thermodynamic length, ℒ = ∫ √ζ |dλ|, which does not depend on speed. The Cauchy–Schwarz inequality gives the bound ⟨W_ex⟩ ≥ ℒ²/τ. Equality is reached when the thermodynamic speed, √ζ λ̇, is constant. The optimal protocol goes slowly where friction is high and fast where it is low, just like in the mud.

### [02:07.6] Example: stiffening a trap — `manim:S05`

**ES:** Volvamos a la trampa que endurecemos de rigidez uno a cuatro. Aquí X = −x²/2, y con μ = k_B T = 1 el tensor de fricción es ζ(κ) = 1/(4κ³): la trampa blanda es lenta y fluctúa mucho, así que es cara de mover. La longitud termodinámica es 1/√κᵢ − 1/√κ_f, exactamente un medio. El protocolo óptimo es κ(t) = (1 − t/2τ)⁻²: empieza despacio y acelera al final, cuando la trampa ya es rígida.

**EN:** Let's return to the trap we stiffen from one to four. Here X = −x²/2, and with μ = k_B T = 1 the friction tensor is ζ(κ) = 1/(4κ³): the soft trap is slow and fluctuates a lot, so it is costly to move. The thermodynamic length is 1/√κᵢ − 1/√κ_f, exactly one half. The optimal protocol is κ(t) = (1 − t/2τ)⁻²: it starts slowly and speeds up at the end, when the trap is already stiff.

### [02:46.6] Numerical example — `manim:S06`

**ES:** Comparemos con el cálculo exacto de la varianza de la partícula. Con τ = 4, la rampa lineal disipa cero coma cero siete seis k_B T en exceso; el protocolo óptimo, cero coma cero seis tres; y la cota ℒ²/τ es cero coma cero seis dos cinco. El protocolo óptimo casi la satura, y la rampa lineal disipa un veinte por ciento más. Duplicar el tiempo divide el exceso a la mitad: ese es el compromiso entre energía y tiempo.

**EN:** Let's compare with the exact computation of the particle's variance. With τ = 4, the linear ramp dissipates 0.076 k_B T in excess; the optimal protocol, 0.063; and the bound ℒ²/τ is 0.0625. The optimal protocol almost saturates it, and the linear ramp dissipates twenty percent more. Doubling the time halves the excess: that is the energy–time trade-off.

### [03:16.6] Applications — `slide`

**ES:** La longitud termodinámica guía el diseño de calendarios de recocido, que deben ir despacio cerca de los puntos críticos, la carga de los acoplamientos de un chip termodinámico, y los protocolos de borrado y reinicio. En la unidad nueve veremos que el calendario de ruido de un modelo de difusión cumple el mismo papel.

**EN:** Thermodynamic length guides the design of annealing schedules, which must slow down near critical points, the loading of a thermodynamic chip's couplings, and erasure and reset protocols. In unit nine we will see that the noise schedule of a diffusion model plays the same role.

### [03:36.5] Common mistakes — `slide`

**ES:** Cuidado: la cota vale en el régimen lento de respuesta lineal. No confundas la longitud termodinámica, que vive en el espacio de parámetros, con la distancia de Wasserstein, que vive en el espacio de estados. El protocolo óptimo no es lineal en el parámetro, sino en la velocidad termodinámica. Y cerca de un punto crítico la fricción crece, y con ella el costo.

**EN:** Careful: the bound holds in the slow, linear-response regime. Don't confuse thermodynamic length, which lives in parameter space, with the Wasserstein distance, which lives in state space. The optimal protocol is not linear in the parameter, but in the thermodynamic speed. And near a critical point friction grows, and with it the cost.

### [04:00.2] Summary — `manim:S09`

**ES:** En resumen: cerca del equilibrio, el trabajo en exceso es cuadrático en la velocidad del control, con el tensor de fricción como métrica. La longitud termodinámica acota el exceso, ⟨W_ex⟩ ≥ ℒ²/τ, y el protocolo óptimo recorre la geodésica a velocidad termodinámica constante.

**EN:** In summary: near equilibrium, the excess work is quadratic in the control speed, with the friction tensor as the metric. The thermodynamic length bounds the excess, ⟨W_ex⟩ ≥ ℒ²/τ, and the optimal protocol travels the geodesic at constant thermodynamic speed.

### [04:21.7] Self-assessment — `slide`

**ES:** Para practicar: deriva el tensor de fricción de la trampa armónica. Calcula la longitud y el exceso mínimo para otro cambio de rigidez. Escribe el protocolo óptimo general. Y explica por qué el recocido debe ir despacio cerca de la temperatura crítica.

**EN:** To practice: derive the friction tensor of the harmonic trap. Compute the length and the minimum excess for another stiffness change. Write the general optimal protocol. And explain why annealing must slow down near the critical temperature.

## Key equations
- $$\zeta(\lambda) = \beta\int_0^\infty \langle\delta X(t)\,\delta X(0)\rangle_\lambda\,dt,\qquad \langle W_{\text{ex}}\rangle \approx \int_0^\tau \dot\lambda\,\zeta(\lambda)\,\dot\lambda\,dt$$ — Friction tensor (fluctuation × correlation time) and linear-response excess work.
- $$\mathcal L = \int \sqrt{\zeta(\lambda)}\,|d\lambda|,\qquad \langle W_{\text{ex}}\rangle \ge \frac{\mathcal L^2}{\tau}$$ — Thermodynamic length and the energy–time bound (equality at constant thermodynamic speed).
- $$\zeta(\kappa) = \frac{k_BT}{4\mu\kappa^3},\qquad \mathcal L = \sqrt{\tfrac{k_BT}{\mu}}\Big(\tfrac{1}{\sqrt{\kappa_i}} - \tfrac{1}{\sqrt{\kappa_f}}\Big)$$ — Overdamped harmonic trap whose stiffness is changed.

## Summary
- Near equilibrium, $\langle W_{\text{ex}}\rangle \approx \int\dot\lambda\,\zeta\,\dot\lambda\,dt$, with $\zeta$ from fluctuation–dissipation.
- Thermodynamic length $\mathcal L$: $\langle W_{\text{ex}}\rangle \ge \mathcal L^2/\tau$.
- Optimal protocol: constant thermodynamic speed (slow where $\zeta$ is large).
- Trap $\kappa: 1\to4$: $\mathcal L = 1/2$; at $\tau = 4$, optimal 0.063 vs linear 0.076.

## Further reading
- D. A. Sivak and G. E. Crooks, Thermodynamic metrics and optimal paths, Phys. Rev. Lett. 108, 190602 (2012).
- [42] S. Whitelam, The thermodynamic freedom of a thermodynamic computer, 2026.
- [2] Peliti and Pigolotti, Stochastic Thermodynamics.
