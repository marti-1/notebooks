# Representability

_I think that GEB uses "represents" whilst [[1]](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852) "expresses". So I will just use "represents"._

**Definition**: An NT relation $R$ is representable in NN if there is a formula $A$ with exactly n free variables $x_1,\dots,x_n$ s.t. for all $a_1,\dots,a_n \in \mathbb{N}$:

- **EX1** If $R(a)$, then $\text{NN} \vdash A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$.
- **EX2** If $\neg R(a)$, then $\text{NN} \vdash \neg A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$.

Basically, there is a formula $A_{x_1,\dots,x_n}[0^a,\dots,0^{a_n}]$ that is provable in NN if $R(a)$. Otherwise, if $\neg R(a)$, then the $\neg A$ is provable.

For example if $EQUALS(a,b)$, then $NN \vdash (0^a = 0^b)$. We can prove that $(0^a = 0^b)$ is a theorem of NN when a = b. 

**Proof**:
1) Assume a = b
2) $\forall x_1(x_1 = x_1)$ (REF AX)
3) $0^a = 0^a$ ($\forall$-ELIM)
4) $0^a = 0^b$ (#1)

Similarly, we can show that if $\neg EQUALS(a,b)$, then $NN \vdash \neg (0^a = 0^b)$. This proof would conclude the fact that $EQUALS$ is representable in a formal system NN.
