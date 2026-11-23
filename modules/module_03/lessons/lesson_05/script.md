# Lesson 3.5 — Protocol design and clock acceleration

**Unit:** Unit 3 — Stochastic thermodynamics  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Compare sudden and gradual loading of a problem into a physical system, and their dissipation.
- Understand clock acceleration: scaling energies by $\lambda$ speeds up the dynamics by $\lambda$ with the same entropy production.
- Distinguish heat (×λ), power (×λ²) and entropy (unchanged) in the speed–energy trade-off.

## Prerequisites
- Lessons 3.1–3.4: work, entropy production, speed limits.

## Narrated script

### [00:05.7] Introduction — `manim:S01`

**ES:** Para resolver un problema con un computador termodinámico hay que cargarlo: llevar el hardware desde un estado inicial a la energía que codifica el problema. ¿Conviene hacerlo de golpe o despacio? ¿Y si queremos ir más rápido, qué tenemos que pagar? En esta lección vemos dos herramientas de diseño: la carga gradual y la aceleración de reloj.

**EN:** To solve a problem with a thermodynamic computer you have to load it: take the hardware from an initial state to the energy that encodes the problem. Is it better to do it all at once or slowly? And if we want to go faster, what do we have to pay? In this lesson we see two design tools: gradual loading and clock acceleration.

### [00:27.0] Sudden versus gradual loading — `manim:S02`

**ES:** Endurezcamos otra vez una trampa de rigidez uno a cuatro. Si lo hacemos de golpe, la partícula no tiene tiempo de reaccionar y el trabajo es uno coma cinco k_B T, más del doble de la energía libre, cero coma seis nueve. Si lo hacemos en un tiempo τ, el trabajo baja: uno coma cero ocho con τ igual a medio, cero coma ochenta y tres con τ igual a dos, cero coma setenta y tres con τ igual a ocho. Para tiempos largos, el trabajo disipado decae como uno sobre τ, como predicen los límites de velocidad.

**EN:** Let's stiffen a trap from one to four again. If we do it all at once, the particle has no time to react and the work is 1.5 k_B T, more than twice the free energy, 0.69. If we do it over a time τ, the work drops: 1.08 with τ equal to one half, 0.83 with τ equal to two, 0.73 with τ equal to eight. For long times, the dissipated work decays as one over τ, as the speed limits predict.

### [01:00.1] Clock acceleration — `manim:S03`

**ES:** Ahora la pregunta inversa: ¿cómo acelerar un cómputo sin cambiar lo que hace? Tomemos la ecuación de Langevin y multipliquemos el potencial por un factor λ, junto con la intensidad del ruido, como si subiéramos la temperatura en el mismo factor. Si además medimos el tiempo con un reloj λ veces más rápido, s = λ t, la ecuación es exactamente la original. Las trayectorias son las mismas, solo que recorridas λ veces más deprisa.

**EN:** Now the inverse question: how do we speed up a computation without changing what it does? Let's take the Langevin equation and multiply the potential by a factor λ, together with the noise strength, as if we raised the temperature by the same factor. If we also measure time with a clock λ times faster, s = λ t, the equation is exactly the original one. The trajectories are the same, only traversed λ times faster.

### [01:28.8] What changes and what doesn't — `manim:S04`

**ES:** ¿Qué se paga? Todas las energías se multiplican por λ, así que el calor disipado por operación crece por λ. Como además la operación dura λ veces menos, la potencia crece por λ al cuadrado. Pero la producción de entropía, que es calor dividido por temperatura, no cambia, y la eficiencia tampoco. Las dos trayectorias que ves son la misma realización de ruido: la rápida, con λ = 4, llega al mismo resultado en un cuarto del tiempo.

**EN:** What do we pay? All energies are multiplied by λ, so the heat dissipated per operation grows by λ. Since the operation also takes λ times less time, power grows by λ squared. But entropy production, which is heat divided by temperature, does not change, and neither does efficiency. The two trajectories you see are the same noise realization: the fast one, with λ = 4, reaches the same result in a quarter of the time.

### [01:58.3] Numerical example — `manim:S05`

**ES:** Supongamos un cómputo que disipa diez k_B T en un microsegundo. Con aceleración de reloj λ = 10, tarda cien nanosegundos y disipa cien k_B T. La potencia pasa de diez k_B T por microsegundo a mil k_B T por microsegundo: cien veces más. La entropía producida sigue siendo diez. En hardware real, la aceleración está limitada por el ancho de banda de los componentes y por la potencia que el chip puede disipar.

**EN:** Suppose a computation dissipates ten k_B T in one microsecond. With clock acceleration λ = 10, it takes a hundred nanoseconds and dissipates a hundred k_B T. Power goes from ten k_B T per microsecond to a thousand k_B T per microsecond: a hundred times more. The entropy produced is still ten. In real hardware, acceleration is limited by the bandwidth of the components and by the power the chip can dissipate.

### [02:26.7] Applications — `slide`

**ES:** En la práctica, cargar el problema con una rampa reduce la disipación, y la aceleración de reloj permite cambiar velocidad por potencia sin alterar la producción de entropía. En el laboratorio cuatro verificarás esas leyes de escala y buscarás el tiempo de carga que maximiza la eficiencia.

**EN:** In practice, loading the problem with a ramp reduces dissipation, and clock acceleration lets us trade speed for power without changing entropy production. In lab four you will check those scaling laws and look for the loading time that maximizes efficiency.

### [02:44.6] Common mistakes — `slide`

**ES:** Cuidado: escalar solo el potencial sin el ruido cambia la distribución. Que la entropía no cambie no significa que acelerar sea gratis: el calor y la potencia crecen. El hardware tiene un ancho de banda finito. Y una carga gradual sigue disipando algo.

**EN:** Careful: scaling only the potential without the noise changes the distribution. Entropy not changing does not mean acceleration is free: heat and power grow. Hardware has a finite bandwidth. And a gradual load still dissipates something.

### [03:02.1] Summary — `manim:S08`

**ES:** En resumen: cargar un problema de forma gradual reduce la disipación como uno sobre τ. La aceleración de reloj escala energías y ruido por λ, y recorre las mismas trayectorias λ veces más rápido: el calor crece por λ, la potencia por λ al cuadrado, y la producción de entropía y la eficiencia no cambian.

**EN:** In summary: loading a problem gradually reduces dissipation as one over τ. Clock acceleration scales energies and noise by λ, and traverses the same trajectories λ times faster: heat grows by λ, power by λ squared, and entropy production and efficiency do not change.

### [03:23.6] Self-assessment — `slide`

**ES:** Para practicar: explica la aceleración de reloj, demuestra el cambio de variable, calcula el trabajo de una carga súbita y aplica las leyes de escala con lambda igual a tres.

**EN:** To practice: explain clock acceleration, prove the change of variables, compute the work of a sudden load and apply the scaling laws with lambda equal to three.

## Key equations
- $$dx = -\mu\,\lambda V'(x)\,dt + \sqrt{2\mu\,\lambda k_BT}\,dW,\quad s = \lambda t$$ — Clock acceleration: the same dynamics in rescaled time.
- $$Q \to \lambda Q,\quad P \to \lambda^2 P,\quad \Sigma \to \Sigma,\quad \eta \to \eta$$ — What changes and what doesn't when the clock is accelerated.
- $$W_{\text{sudden}} = \tfrac12(\kappa_f - \kappa_i)\langle x^2\rangle_i = \tfrac{k_BT}{2}\Big(\frac{\kappa_f}{\kappa_i} - 1\Big)$$ — Work of an instantaneous stiffness load.

## Summary
- Gradual loading: $W_{\text{dis}} \propto 1/\tau$.
- Clock acceleration: same trajectories, $\lambda$ times faster.
- Heat ×λ, power ×λ², $\Sigma$ and $\eta$ invariant.
- Practical limit: hardware bandwidth and dissipation.

## Further reading
- [42] S. Whitelam, The thermodynamic freedom of a thermodynamic computer, 2026.
- [43] S. Whitelam and C. Casert, Thermodynamic computing out of equilibrium, 2024.
