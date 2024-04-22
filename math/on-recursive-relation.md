# Recursive Relation


**Definition**: An n-ary  relation $R$ is _recursive_ if its characteristic function $K_{R}$ is recursive. For example, the 2-ary relation < is recursive since its characteristic function $K_{<}$ is a starting (one of the Church's axioms of formalized computability) function and hence recursive. [[p44]](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852)

**Corollary**: Every recursive relation is [decidable](https://github.com/marti-1/notebooks/blob/master/math/on-decision-problem.md).

**Proof**:
1. Let $R$ be a recursive relation.
2. $K_{R}$ is recursive (from the definition).
3. $K_{R}$ is decidable (since every recursive function is decidable).
4. $R$ is a decidable relation.

For example, $\text{EVEN?}$ has the following characteristic function:

Piecewise definition:

$$
f(n) = \begin{cases} 
1 & \text{if } n \text{ is even} \\
0 & \text{if } n \text{ is odd}
\end{cases}
$$

Expression using the modulus operator:

$$
f(n) = 1 - (n \mod 2)
$$
