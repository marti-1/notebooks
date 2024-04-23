# Church's Theorem

Let $\Gamma$ be a consistent extension of NN. Then $\Gamma$ is undecidable:

$$
\neg \text{THM}_{\Gamma}(\text{DIA}(p)) \Leftrightarrow \Gamma \vdash A\_{x\_1}\[0^p\]
$$

* $\text{THM}_{\Gamma}$ -- a [relation](https://github.com/marti-1/notebooks/blob/master/math/on-functions-and-relations.md) in a formal system NN extended with $\Gamma$ extension \[TODO: what is an extension?\].
* $\text{DIA}(a)$ -- a computable function: `decode_formula(a) | replace free param x_1 with a | encode`. Deals only with one free param formulas.
* $\neg \text{THM}_{\Gamma}(\text{DIA}(a))$ -- a formula that claims that diagonalization of a formula whose code is $a$ is not a theorem!
* The assumption is made that $\text{THM}\_{\Gamma}$ is a decidable relation. The proof eventually ends by showing that this leads to a contradiction, and therefore $\text{THM}_{\Gamma}$ has to be undecidable. Using Corollary 1, $\Gamma~\text{is undecidable}$.
* Since we assume that $\neg \text{THM}_{\Gamma}$ is decidable (negation of decidable is decidable), and $DIA(a)$ is computable there is a formula $A$ that [represents](https://github.com/marti-1/notebooks/blob/master/math/on-representing.md) $\neg \text{THM}\_{\Gamma}(\text{DIA}(a))$, namely $A\_{x\_1}\[0^a\]$.
* The formula $A\_{x\_1}\[0^a\]$ has a Godel's number $p$.

## Appendix: Lemma 1

**Lemma 1**: Let $\Gamma \subseteq \text{FOR}_{NN}$. Then $\Gamma ~\text{is decidable} \Leftrightarrow \text{THM}\_{\Gamma}$ is a decidable relation. 

**Corollary 1**: $\text{THM}\_{\Gamma}~\text{is an undecidable relation} \rightarrow \Gamma ~\text{is undecidable}$



## Appendix: Lemma 3

**Lemma 3**: Let $\Gamma$ be a consistent extension of NN, let R be a 1-ary relation on $\mathbb{N}$ and let A be a formula that represents R. Then for all $a\in \mathbb{N}$, $R(a) \Leftrightarrow \Gamma \vdash A_{x_1}[0^a]$.

**Proof**: Since A represents R, it follows that for all $a \in \mathbb{N}$,

**EX1** If $R(a)$, then $\text{NN} \vdash A_{x_1}[0^a]$.

**EX2** If $\neg R(a)$, then $\text{NN} \vdash \neg A_{x_1}[0^a]$.
