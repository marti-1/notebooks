The definition of truth predicate for arithmatic is in a set that is bigger than the set of all arithmetical formulas.

---

1. The set of all 1-free var formulas $F$ is countable. The set of all instances of $F$ is also countable: $S(x,y) \Leftrightarrow \text{SUB}(x,y)$.
2. Assume we can define the truth predicate as arithmetical formula: $T(x)$. Therefore, the set of all true/false interpretations of all 1-free var formula instances is also countable: $T(S(x,y))$:

|   | 1 | 2 | 3 | ... |
|---|---|---|---|---|
| 1 | $T(S(1,1))$ | $T(S(1,2))$ | $T(S(1,3))$ | ... |
| 2 | $T(S(2,1))$ | $T(S(2,2))$ | $T(S(2,3))$ | ... |
| 3 | $T(S(3,1))$ | $T(S(3,2))$ | $T(S(3,3))$ | ... |
| ... | ... |... |... |... |

3. Then $D(x) \Leftrightarrow T(S(x,x))$ is a 1-free var formula that can also be defined.
4. Then $\bar{D}(x) \Leftrightarrow \neg D(x)$ is a 1-free var formula that can also be defined.
5. Is the row of truths of all $\bar{D}(x)$ instances in the above table? Assume yes, then it has some index $p$: $\bar{D} = T(S(p))$.
6. Then the truth of the sentence $\bar{D}(p)$ is in the above table. However, if it is then:

$$
\begin{aligned}
\bar{D}(p) &= T(S(p,p)) \\
&= \neg D(p) \\
&= \neg T(S(p,p))
\end{aligned}
$$

7. Since we get a contradiction, $\bar{D}(p)$ is not in the table above, as well as $\bar{D}$.
8. Since all 1-free var arithmetical formulas are in the table above, and $\bar{D}$ isn't, it is not an arithmetical formula. However, $\neg$ is part of the language of arithmetic, and $S$ can also be defined arithmetically. This leaves only $T$ as something that can't be defined arithmetically.

---

The truth of $\bar{D}(p)$ is undecidable. Why is this a problem? When a function maps some input into an infinite loop, it is undecidable for that input, therefore it is not defined for that input. So $\bar{D}$ is not defined for the input $p$. $T$ is not defined for $\bar{D}(p)$. If $T$ is defined for all sentences, but not for $\bar{D}(p)$ then it must be that $\bar{D}$ is not a formula of arithmetic. However, the only non-arithmetic part is $T$ in its definition.


---

```
def even(x):
	return x % 2 == 0
	
def odd(x):
	return x % 2 != 0

def true(f,x):
	return f(x) == True
	
	
true(even, 2) # 2 % 2 = 0
```