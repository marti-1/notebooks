# Completeness

_The following are the notes taken from the book [An Introduction to Mathematical Logic](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852)_

What does it mean to be a theorem in a formal system? A theorem is a product of a repetitive application of axioms and rules. In propositional logic, a formal system $P$ has its axioms and rules designed in such way that all theorems would come out as tautologies. One can ask if that always happens? Proving this to be the case is a proof of soundness: $\vdash A \rightarrow ~\vDash A$.

In addition to soundness, one can also ask if a system $P$ is _semantically complete_ ("An Introduction to Mathematical Logic" uses the word _adequacy_): $\vDash A \rightarrow ~\vdash A$ -- is every tautology a theorem in $P$? It happens to be the case for $P$. Due to Gödel's completeness theorem, it also happens to be the case for  first-order logic.
