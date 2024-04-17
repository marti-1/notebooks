# Tautological Consequence

Let $B$ be a formula and let $\Gamma$ a set of formulas. We say that $B$ is a _tautological consequence_ of $\Gamma$, written $\Gamma \vDash B$, if every [truth assignment](https://github.com/marti-1/notebooks/blob/master/math/on-truth-assignment.md) that satisfies $\Gamma$ also satisfies $B$. To prove that $\Gamma \vDash B$, proceed as follows: let $\phi$ be a truth assignment such that $\phi(A)=T$ for every $A \in \Gamma$; show that $\phi(B) = T$.
