# Truth Assignment

$\phi:\text{PROP}\rightarrow\\{T,F\\}$. 

An example truth assignment: $\phi(p_1)=F, \phi(p_2)=T, \phi(p_3)=F$ -- a single truth assignment assigns truth values to 3 [propositional variables](https://github.com/marti-1/notebooks/blob/master/math/on-propositional-variables.md).

**Formulas**

$\phi:\text{FOR}\rightarrow\\{T,F\\}$.

Truth assignments for formulas:

$$
\begin{align*}
& \text{NOT (¬)} & & TA_{\neg}: \phi(A) \neq \phi(\neg A) \\
& \\
& \text{AND (∧)} & & TA_{\land}: \phi(A \land B) = T \iff \phi(A) = T \text{ and } \phi(B) = T \\
& & & TA_{\land}: \phi(A \land B) = F \iff \phi(A) = F \text{ or } \phi(B) = F \\
& \\
& \text{OR (∨)} & & TA_{\lor}: \phi(A \lor B) = T \iff \phi(A) = T \text{ or } \phi(B) = T \\
& & & TA_{\lor}: \phi(A \lor B) = F \iff \phi(A) = F \text{ and } \phi(B) = F \\
& \\
& \text{IMPLIES (→)} & & TA_{\rightarrow}: \phi(A \rightarrow B) = T \iff \phi(A) = F \text{ or } \phi(B) = T \\
& & & TA_{\rightarrow}: \phi(A \rightarrow B) = F \iff \phi(A) = T \text{ and } \phi(B) = F \\
& \\
& \text{IF AND ONLY IF (↔)} & & TA_{\leftrightarrow}: \phi(A \leftrightarrow B) = T \iff \phi(A) = \phi(B) \\
& & & TA_{\leftrightarrow}: \phi(A \leftrightarrow B) = F \iff \phi(A) \neq \phi(B) \\
\end{align*}
$$
