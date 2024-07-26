# Decidable Set

A set $\Gamma$ is _decidable_, if there is an algorithm that for every formula* $A$ tells if $\Gamma \vdash A$ or $\Gamma \vdash \neg A$. For example, the pq-system presented in GEB is decidable -- given any formula of [pq-system](https://godel-escher-bach.fandom.com/wiki/Chapter_2), we can check whether it is a theorem or not with the following algorithm:

1. Input formula A.
2. Start with the axioms.
3. Continuesly apply the rules of the pq-system in order to get the new theorems.
4. If A is in one of the theorems in #3, return Yes and halt.
5. If shortest theorem in #3 is longer than A, return No and halt.
6. Go to step #3.

Since pq-system theorems are always increasing, the above algorithm is guaranteed to halt with the correct answer.

---

\* -- for the first-order logic I would assume the question is instead about every **statement**.
