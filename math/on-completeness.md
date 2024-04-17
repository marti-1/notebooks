# Completeness

_The following are the notes taken from the book [An Introduction to Mathematical Logic](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852)_

The following example helps to gain some additional intuition about completeness (Example 2 p98):

The set $\Gamma=\\{p_n : n \geq 2\\}$ is not complete. To prove this, we show that neither $p_1$ nor $!p_1$ is a theorem of $\Gamma$. Suppose $\Gamma \vdash p_1$; by soundness theorem $\Gamma \vDash p_1$. Define truth assignment $\phi(p_1) = F$ and $\phi(p_{n \geq 2}) = T$. Clearly $\phi$ satisfies $\Gamma$, and sinice $\Gamma \vDash p_1$. we have that $p_1$ is satisfied by all truthh-assignments that satisfy $\Gamma$, thus $\phi(p_1)=T$, which is a contradiction.

