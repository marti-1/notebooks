# Completeness

_The following are the notes taken from the book [An Introduction to Mathematical Logic](https://www.amazon.com/Introduction-Mathematical-Logic-Dover-Mathematics/dp/0486497852)_

What does it mean to be a theorem in a formal system? A theorem is a product of a repetitive application of axioms and rules. In propositional logic, a formal system $P$ has its axioms and rules designed in such way that all theorems would come out as tautologies. One can ask if that always happens? Proving this to be the case is a proof of soundness: $\vdash A \rightarrow ~\vDash A$.

In addition to soundness, one can also ask if a system $P$ is _semantically complete_ ("An Introduction to Mathematical Logic" uses the word _adequacy_): $\vDash A \rightarrow ~\vdash A$ -- is every tautology a theorem in $P$? It happens to be the case for $P$. Due to Gödel's completeness theorem, it also happens to be the case for  first-order logic.

Something to have in mind, that is not presented in intro to logic books, is that there are many flavours of completeness. In addition to the semantic completeness, there is also a _syntactic completeness_. A formal system $F$ is syntactically complete if for all [wffs](https://github.com/marti-1/notebooks/blob/master/math/on-formulas.md) $A$ either $\vdash A$ or $\vdash \neg A$. In this respect, a system $P$ is not complete, since it can only produce tautologies as theorems, it can't produce a [propositional variable](https://github.com/marti-1/notebooks/blob/master/math/on-propositional-variables.md) ($p$) or it's negation ($\neg p$). For first-order logic systems, the completeness requirement is for sentences (closed formulas) to be either a theorem or their negation to be a theorem. Gödel's incompleteness theorem showed that powerful enough first-order languages (languages that embed first-order logic) like Peano arithmetic are incomplete.

In additon, the following is noted in "An Introduction to Mathematical Logic":

> The word "complete" has a technical meaning: every formula or its negation is a theorem. There is, however, an informal, nontechnical meaning of complete that is used in logic and applies to any formal system $F$. Quite generally, a formal system $F$ is complete if everything we want to be a theorem is a theorem. For the formal system $P$ (Propositional Logic), we want tautologies to be theorems, so in this nontechnical sense $P$ is complete.

... for formal systems like Peano arithmetic we want all arithmetical truths to be theorems.
