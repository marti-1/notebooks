# _Representing_

_I think that GEB uses "represents" whilst [[1]](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852) "expresses". So I will just use "represents"._

**Definition**: An NT relation $R$ is representable in NN if there is a formula $A$ with exactly n free variables $x_1,\dots,x_n$ s.t. for all $a_1,\dots,a_n \in \mathbb{N}$:

- **EX1** If $R(a)$, then $\text{NN} \vdash A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$.
- **EX2** If $\neg R(a)$, then $\text{NN} \vdash \neg A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$.

Basically, there is a formula $A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$ that is provable in NN if $R(a)$. Otherwise, if $\neg R(a)$, then the $\neg A$ is provable.
