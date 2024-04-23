# Godel's Theorem on [Representability](https://github.com/marti-1/notebooks/blob/master/math/on-representing.md)

**Theorem**: Let R be an n-ary relation of $\mathbb{N}$. If R is [recursive](https://github.com/marti-1/notebooks/tree/master/math), then R is _representable_.

* In other words: if R is computable with a Turing Machine, then R is representable.
* Why this matters? It binds formalization of computation with theoremhood.

**Example**:

Define $R$ by $R(a) \Leftrightarrow \~\text{a is even}, a \geqslant 4, \~\text{and}\~ a \~ \text{is the sum of two prime numbers}$.

The relation $R$ is decidable, and hence recursive (Church's thesis `decidable => recursive`); by Godel's theorem of representability, R is representable.
