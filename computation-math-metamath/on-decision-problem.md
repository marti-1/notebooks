## [Tex Talks](https://www.youtube.com/@TexTalksSometimes)

### [Mathematical Representations of Decision Problems](https://www.youtube.com/watch?v=wxwxt8w60K0&ab_channel=TexTalks)

A decision problem is a set of strings for which the answer is "yes". Example:

FACTORING = {4,6,8,9,10,12,14,...}

A **language** is a decision problem. Language $L$ consists of 1 ('yes') and 0 ('no') answers. 'No' answers are rejections or endless loops.

### [Diagonalization and Uncountability](https://youtu.be/XFZQfdfZNGY?si=z_-zF2GKuKbeypFq&t=632)

"Every decision problem is an infinite bit string" -- every bit has an index. A 13th bit equal to 1 means that a decision for input 13 is "yes".

The set of all infinite sequences of bit strings is uncountable. The set of all Turing machines is countable. Therefore there are decision problems that don't have a TM that could compute it.

### [The Halting Problem and Uncomputability](https://www.youtube.com/watch?v=73mY82UOclc&ab_channel=TexTalks)

"Every computable function or problem can be executed by some Turing machine, but not every Turing machine corresponds directly to a function or problem that is explicitly and completely computable (as some might not halt on certain inputs)." -- from ChatGPT.

---

We can characterize every TM as an infinite sequence of bits: 1 (accept), 0 (reject or loop forever).

$\bar{D} = \neg D$ is a decision problem that is not computable. What is $\bar{D}$: given an integer $n$, does the n'th TM either reject or not halt at all on the n'th input?

Let's see why $\bar{D}$ isn't computable. Suppose it were computable. Then there exists a TM $M_{\bar{d}}$ which given $m$ accepts if the m'th machine doesn't accept the m'th input and rejects if m'th machine does accept the input. Therefore $M_{\bar{d}}$ is on the list: $M_{\bar{d}} = \text{TM}_{\bar{d}}$.

Consider $M_{\bar{d}}(\bar{d})$:

1. Let's say $M_{\bar{d}}(\bar{d}) = 1$ (accept). This means $\text{TM}_{\bar{d}}(\bar{d}) = 0$ rejects. A contradiction.
2. Let's say $M_{\bar{d}}(\bar{d}) = 0$ (reject). This means $\text{TM}_{\bar{d}}(\bar{d})=1$ accepts. Again, a contradiction.

Therefore $\bar{D}$ is not decidable (or computable).

**The Halting Problem H**: given two integers m and n, does the m'th TM halt on the n'th input?

Suppose H was computable by some machine $M_H$. Then I could create a machine deciding $\bar{D}$ as follows:

```
def M_bar_d(n):
    if M_H(n,n) == 1:
        simulate n'th TM on n input
        if it halts in 1:
            return 0
        else:
            return 1
    else:
        return 0
```

### [Computable Enumerability Revisited](https://www.youtube.com/watch?v=gzc89VL9rcc&t=1141s&ab_channel=TexTalks)

A decision problem is **recursive** (**R**) (or **computable**) (or **decidable**) if there exists a TM $M$ s.t. for all $x$:

1. If $x \in L$ then $M(x)$ halts and accepts.
2. If $x \notin L$ then $M(x)$ halts and rejects.

Note, $M$ always halts.

A decision problem is **recursively enumerable** (**RE**) (or **computably enumerable**) (definition 1) if there exists a TM $M$ s.t. for all $x$:

1. If $x \in L$ then $M(x)$ halts and accepts.
2. If $x \notin L$ then $M(x)$ loops forever.

Computably enumerable (definition 2): there is an algorithm that can list all elements of $L$.

---

Fact 1: $R \subseteq RE$. If it is computable, then it is recursively enumerable.
Proof:

```
def M(x):
    if R(x) == 1:
        return 1
    else:
        loop forever
```

Fact 2: definition 1 and 2 of computably enumerable are equivalent.

### [The Halting Problem is RE-complete](https://www.youtube.com/watch?v=VvKcxu9bFR4&ab_channel=TexTalks)

$H \notin R$. $H \in \text{RE}$. Proof:

```
def M(H,x):
    loop k=1 to infinity:
        if H(x) halts in k steps:
            return 1
```

### [Computable Enumerability, Existential Quantification, and Unbounded Searching](https://youtu.be/4_MMZrRQvjY?si=nV-9hm3gKnbVSO4n)



### [Let's Define Definability](https://www.youtube.com/watch?v=KRlFIm4AmJM&ab_channel=TexTalks)

TBD