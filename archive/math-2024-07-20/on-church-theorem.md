# Church's Theorem

**Theorem**: Let $\Gamma$ be a consistent extension of NN. Then $\Gamma$ is undecidable:

$$
\neg \text{THM}_{\Gamma}(\text{DIA}(p)) \Leftrightarrow \Gamma \vdash A\_{x\_1}\[0^p\]
$$

1. $\text{THM}_{\Gamma}$ -- a [relation](https://github.com/marti-1/notebooks/blob/master/math/on-functions-and-relations.md) in a formal system NN [extended](https://github.com/marti-1/notebooks/blob/master/math/on-extension.md#formal-arithmetic) with $\Gamma$.
2. $\text{DIA}(a)$ -- a computable function: `decode_formula(a) | replace free param x_1 with a | encode`. Deals only with one free variable formulas.
3. $\neg \text{THM}_{\Gamma}(\text{DIA}(a))$ -- a formula that claims that diagonalization of a formula whose code is $a$ is not a theorem!
4. The assumption is made that $\text{THM}\_{\Gamma}$ is a decidable relation. The proof eventually ends by showing that this leads to a contradiction, and therefore $\text{THM}_{\Gamma}$ has to be undecidable. Using Corollary 1, $\Gamma$ is undecidable.
5. Since we assume that $\neg \text{THM}_{\Gamma}$ is decidable (negation of decidable is decidable), and $DIA(a)$ is computable there is a formula $A$ that [represents](https://github.com/marti-1/notebooks/blob/master/math/on-representing.md) $\neg \text{THM}\_{\Gamma}(\text{DIA}(a))$, namely $A\_{x\_1}\[0^a\]$.
6. By Lemma 3: $\neg \text{THM}_{\Gamma}(\text{DIA}(a)) \Leftrightarrow A\_{x_1}\[0^a\]$ for all $a\in \mathbb{N}$.
7. The formula $A\_{x\_1}\[0^a\]$ has a Godel's number $p$.
8. #6 & #7 imply that $\neg \text{THM}_{\Gamma}(\text{DIA}(p)) \Leftrightarrow A\_{x_1}\[0^p\]$
9. $Decode(\text{DIA}(p)) = A\_{x_1}\[0^p\]$
10. $\neg \text{THM}_{\Gamma}(\text{DIA}(p))$ claims that $A\_{x_1}\[0^p\]$ is not a theorem, therefore $\neg A\_{x_1}\[0^p\]$. However, this is a contradiction.

## Appendix: Lemma 1

**Lemma 1**: Let $\Gamma \subseteq \text{FOR}_{NN}$. Then $\Gamma$ is decidable $\Leftrightarrow \text{THM}\_{\Gamma}$ is a decidable relation. 

**Proof**:

First, $\Gamma$ is decidable $\rightarrow \text{THM}_{\Gamma}$ is decidable. The gist of the proof is that since $\Gamma$ is [decidable](https://github.com/marti-1/notebooks/blob/master/math/on-decidable-set.md)), we can make $\text{THM}\_{\Gamma}$ as follows:

1. Input encoded formula $a\in \mathbb{N}$.
2. Decode $a$ -- $A$
3. Does $\Gamma \vdash A$? If yes, return YES and halt;
4. if no, return NO and halt.

Second, $\text{THM}_{\Gamma}$ is decidable $\rightarrow $\Gamma$ is decidable:

1. Input formula $A$ of $L_{NN}$.
2. Encode $A$ into $a$.
3. if $THM_{\Gamma}(a)$, return YES and halt;
4. otherwise return NO, and ahlt.
 
**Corollary 1**: $\text{THM}\_{\Gamma}$ is an undecidable relation $\rightarrow \Gamma$ is undecidable.

## Appendix: Lemma 2

**Lemma 2**: There is a 1-ary computable function $DIA(a)$ s.t. $a$ is the code of a formula $A$ of $L_{NN}$ with exactly one free variable $x_1$, then $DIA(a) = \text{code of the formula} ~A\_{x_1}\[0^a\]$.

**Proof**: Defina DIA as follows:

```
def DIA(a)
  if a is the code of a formula A of L_{NN} with exactly one free variable x_1:
    Code of A_{x_1}[0^a]
  else:
    0
```

The proof seems obvious. For reference check [[p304]](https://github.com/marti-1/notebooks/blob/master/math/on-representing.md).

## Appendix: Lemma 3

**Lemma 3**: Let $\Gamma$ be a consistent extension of NN, let $R$ be a 1-ary relation on $\mathbb{N}$ and let $A$ be a formula that represents $R$. Then for all $a\in \mathbb{N}$, $R(a) \Leftrightarrow \Gamma \vdash A_{x_1}[0^a]$.

**Proof**: Since A [represents](https://github.com/marti-1/notebooks/blob/master/math/on-representing.md) $R$, it follows that for all $a \in \mathbb{N}$,

* **EX1** If $R(a)$, then $\text{NN} \vdash A_{x_1}[0^a]$.
* **EX2** If $\neg R(a)$, then $\text{NN} \vdash \neg A_{x_1}[0^a]$.

First, $R(a) \rightarrow \Gamma \vdash A_{x_1}[0^a]$:

1. By EX1, $NN \vdash A_{x_1}\[0^a\]$
2. Since $\Gamma$ is an extension of NN, it follows that $\Gamma \vdash A_{x_1}\[0^a\]$.

Second, $\Gamma \vdash A_{x_1}[0^a] \rightarrow R(a)$:
1. Let's assume that $\neg R(a)$.
2. By EX2 $NN \vdash \neg A_{x_1}\[0^a\]$.
3. Since $\Gamma$ is an extension of NN, it follows that $\Gamma \vdash \neg A_{x_1}\[0^a\]$.
4. #3 contradicts [consistency](https://github.com/marti-1/notebooks/blob/master/math/on-consistency.md) of $\Gamma$.
