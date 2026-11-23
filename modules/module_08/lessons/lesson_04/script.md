# Lesson 8.4 — K-FAC

**Unit:** Unit 8 — Thermodynamic optimization and training  
**Narration:** Spanish (Grok TTS) · **On-screen text:** English

## Objectives
- Approximate each layer's curvature block by a Kronecker product $A \otimes G$ of activation and gradient covariances.
- Apply $(A\otimes G)^{-1}\mathrm{vec}(\nabla W) = \mathrm{vec}(G^{-1}\nabla W A^{-1})$ and estimate the factors with exponential moving averages.
- Know the expand and reduce variants for weight-sharing layers.

## Prerequisites
- Lesson 8.2: GGN and the natural-gradient system.
- Kronecker products (Lesson 0.2).

## Narrated script

### [00:03.9] Introduction — `manim:S01`

**ES:** Incluso con trucos, el gradiente natural completo es caro para redes grandes. K-FAC, propuesto por Martens y Grosse en dos mil quince, hace dos aproximaciones: ignora las correlaciones entre capas distintas, y dentro de cada capa factoriza la curvatura como un producto de Kronecker de dos matrices pequeñas. El resultado es un optimizador de segundo orden casi tan barato como uno de primero.

**EN:** Even with tricks, the full natural gradient is expensive for large networks. K-FAC, proposed by Martens and Grosse in two thousand fifteen, makes two approximations: it ignores correlations between different layers, and within each layer it factors the curvature as a Kronecker product of two small matrices. The result is a second-order optimizer almost as cheap as a first-order one.

### [00:28.9] The Kronecker factors — `manim:S02`

**ES:** En una capa lineal, el gradiente respecto de los pesos es el producto exterior de la activación de entrada a y el gradiente de la salida g. El bloque de Fisher de la capa es entonces el valor esperado de (a aᵀ) ⊗ (g gᵀ). K-FAC supone que activaciones y gradientes son independientes y lo aproxima por A ⊗ G, con A = E[a aᵀ] y G = E[g gᵀ].

**EN:** In a linear layer, the gradient with respect to the weights is the outer product of the input activation a and the output gradient g. The layer's Fisher block is then the expected value of (a aᵀ) ⊗ (g gᵀ). K-FAC assumes activations and gradients are independent and approximates it by A ⊗ G, with A = E[a aᵀ] and G = E[g gᵀ].

### [00:57.0] Cheap inversion — `manim:S03`

**ES:** La ventaja está en la inversión. La inversa de un producto de Kronecker es el producto de las inversas, y aplicarla a un gradiente es G⁻¹ ∇W A⁻¹: dos matrices pequeñas en lugar de una gigante. Para una capa de veinte entradas y diez salidas, en lugar de invertir una matriz de doscientos por doscientos se invierten una de veinte y otra de diez. Para capas de mil por mil, se pasa de una matriz de un millón por un millón a dos de mil por mil.

**EN:** The advantage is in the inversion. The inverse of a Kronecker product is the product of the inverses, and applying it to a gradient is G⁻¹ ∇W A⁻¹: two small matrices instead of a giant one. For a layer with twenty inputs and ten outputs, instead of inverting a two-hundred-by-two-hundred matrix one inverts a twenty and a ten. For thousand-by-thousand layers, one goes from a million-by-million matrix to two thousand-by-thousand ones.

### [01:27.3] How good is it? — `manim:S04`

**ES:** Lo medimos en una capa softmax con quinientos ejemplos. La aproximación de Kronecker difiere del bloque exacto en un veintiuno por ciento en norma. Pero lo que importa es la dirección del paso: el gradiente natural de K-FAC forma un coseno de cero coma nueve cuatro con el exacto, mientras que el gradiente ordinario apenas llega a cero coma cinco. La matriz es aproximada; la dirección es casi la correcta.

**EN:** We measure it on a softmax layer with five hundred examples. The Kronecker approximation differs from the exact block by twenty-one percent in norm. But what matters is the step direction: K-FAC's natural gradient has a cosine of 0.94 with the exact one, while the ordinary gradient only reaches 0.5. The matrix is approximate; the direction is almost right.

### [01:53.4] Moving averages and damping — `manim:S05`

**ES:** En la práctica, los factores A y G se estiman con promedios móviles exponenciales a lo largo de las iteraciones, y se invierten solo cada cierto número de pasos, porque cambian lentamente. El amortiguamiento se reparte entre los dos factores, sumando una raíz de λ a cada uno. Así, el costo extra frente a Adam es pequeño y se amortiza.

**EN:** In practice, the factors A and G are estimated with exponential moving averages across iterations, and inverted only every so many steps, because they change slowly. Damping is split between the two factors, adding a square root of λ to each. That way, the extra cost compared with Adam is small and amortized.

### [02:15.9] Weight sharing: expand and reduce — `manim:S06`

**ES:** Las capas modernas comparten pesos: una convolución usa el mismo filtro en todas las posiciones, y un transformer, la misma matriz en todos los tokens. Eschenhagen y colaboradores propusieron dos variantes. K-FAC expand trata cada posición como un ejemplo más del lote. K-FAC reduce primero suma activaciones y gradientes sobre las posiciones y después forma los factores, lo que es más barato. Ambas son exactas en casos lineales particulares y funcionan bien en la práctica.

**EN:** Modern layers share weights: a convolution uses the same filter at every position, and a transformer, the same matrix for every token. Eschenhagen and colleagues proposed two variants. K-FAC expand treats each position as one more example in the batch. K-FAC reduce first sums activations and gradients over the positions and then forms the factors, which is cheaper. Both are exact in particular linear cases and work well in practice.

### [02:47.1] Applications — `slide`

**ES:** K-FAC se usa para entrenar redes convolucionales y transformers con información de segundo orden, y también para aproximaciones de Laplace que estiman incertidumbre. Su cuello de botella es invertir los factores, y eso es lo que acelera la versión termodinámica de la próxima lección.

**EN:** K-FAC is used to train convolutional networks and transformers with second-order information, and also for Laplace approximations that estimate uncertainty. Its bottleneck is inverting the factors, and that is what the thermodynamic version of the next lesson accelerates.

### [03:04.2] Common mistakes — `slide`

**ES:** Errores comunes: olvidar que K-FAC ignora la curvatura entre capas. Aplicar los factores en el orden equivocado. Amortiguar solo uno de los dos. Y mezclar las estadísticas de las variantes expand y reduce.

**EN:** Common mistakes: forgetting that K-FAC ignores curvature between layers. Applying the factors in the wrong order. Damping only one of the two. And mixing the statistics of the expand and reduce variants.

### [03:18.6] Summary — `manim:S09`

**ES:** En resumen, K-FAC aproxima cada bloque de curvatura por un producto de Kronecker de la covarianza de activaciones y la de gradientes, lo que convierte una inversión gigante en dos pequeñas. En el ejemplo, la matriz tiene un error del veintiuno por ciento, pero la dirección del paso tiene un coseno de cero coma nueve cuatro con la exacta.

**EN:** In summary: K-FAC approximates each curvature block by a Kronecker product of the activation covariance and the gradient covariance, which turns one giant inversion into two small ones. In the example, the matrix has a twenty-one percent error, but the step direction has a cosine of 0.94 with the exact one.

### [03:39.3] Self-assessment — `slide`

**ES:** Para practicar: demuestra la inversa del producto de Kronecker. Verifica la identidad con la vectorización. Calcula el costo de invertir los factores. Y explica la suposición de independencia.

**EN:** To practice: prove the inverse of the Kronecker product. Verify the identity with vectorization. Compute the cost of inverting the factors. And explain the independence assumption.

## Key equations
- $$F_\ell = \mathbb E\big[(aa^\top)\otimes(gg^\top)\big] \approx A\otimes G,\qquad A = \mathbb E[aa^\top],\ G = \mathbb E[gg^\top]$$ — Kronecker-factored curvature of a linear layer.
- $$(A\otimes G)^{-1}\mathrm{vec}(\nabla W) = \mathrm{vec}\big(G^{-1}\,\nabla W\,A^{-1}\big)$$ — Inverting two small factors instead of one large block.
- $$O\big(d_\text{in}^3 + d_\text{out}^3\big)\ \text{vs}\ O\big((d_\text{in}d_\text{out})^3\big)$$ — Inversion cost per layer.

## Summary
- Layer curvature ≈ A ⊗ G (activations ⊗ output gradients), layers independent.
- Inverse applied as G⁻¹ ∇W A⁻¹: two small inversions.
- Softmax layer: 21 % matrix error, cosine 0.94 with exact NG (gradient: 0.50) [S].
- EMA factors, split damping; expand/reduce variants for weight sharing.

## Further reading
- J. Martens and R. Grosse, Optimizing neural networks with Kronecker-factored approximate curvature, ICML (2015).
- R. Eschenhagen et al., Kronecker-factored approximate curvature for modern neural network architectures, NeurIPS (2023).
- [41] K. Donatella et al., Scalable thermodynamic second-order optimization, 2025.
