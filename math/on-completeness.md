# Completeness

_The following are the notes taken from the book [An Introduction to Mathematical Logic](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852)_

The following example helps to gain some additional intuition about completeness (Example 2 p98):


**Completeness**: for every [formula](https://github.com/marti-1/notebooks/blob/master/math/on-formulas.md) $A$ of $P$, either $\vdash A$ or $\vdash \neg A$. 

_(A propositional logic system is complete if for every formula A of that system, the system can prove if it is a theorem or not)_

For example. The set $\Gamma=\\{p_n : n \geq 2\\}$ is not complete. To prove this, we show that neither [proposition](https://github.com/marti-1/notebooks/blob/master/math/on-propositional-variables.md) $p_1$ nor $!p_1$ is a theorem of $\Gamma$. Suppose $\Gamma \vdash p_1$; by soundness theorem $\Gamma \vDash p_1$. Define [truth assignment](https://github.com/marti-1/notebooks/blob/master/math/on-truth-assignment.md) $\phi(p_1) = F$ and $\phi(p_{n \geq 2}) = T$. Clearly $\phi$ [satisfies](https://github.com/marti-1/notebooks/blob/master/math/on-satisfiable.md) $\Gamma$, and since $\Gamma \vDash p_1$ we have that $p_1$ is satisfied by all truth assignments that satisfy $\Gamma$ [[1]](https://github.com/marti-1/notebooks/blob/master/math/on-tautological-consequence.md), thus $\phi(p_1)=T$, which is a contradiction.

