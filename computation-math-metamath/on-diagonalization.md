## [Diagonalization and Uncountability](https://youtu.be/XFZQfdfZNGY?si=D6d6oiAynnwdakOJ&t=404)

The set of all infnite sequences of binary strings is uncountable.

Assume it is. Create a new binary sequence by flipping bits on the diagonal:

$\bar{D}(i) = L(i,i)+1$

where $L$ is a 2D list structure. Since $L$ is countable, $\bar{D}$ has some index $m$, and it's m'th bit is $\bar{D}(m) = L(m,m)$. However, by the definition of $\bar{D}$ it is also $\bar{D}(m) = L(m,m)+1$. Now $\bar{D}(m)$ can't be equal to a bit and a flipped version of it. A contradiction. So our assumption is false. The set of all sequences of binary strings is uncountable.

## Further Reading

* "Bluediag" -- "Godel, Escher, Bach", p420
* [Why doesn't Cantor's diagonal argument also apply to natural numbers?](https://math.stackexchange.com/questions/35107/why-doesnt-cantors-diagonal-argument-also-apply-to-natural-numbers)

