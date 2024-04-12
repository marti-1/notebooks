# Hofstadter and Limits of Human Brain

> There is no recursively related notation-system which gives a name to every constructive ordinal.

-- Alonzo Church & Stephen C. Kleene

Hofstadter in his book "Gödel, Escher, Bach" uses the theorem above to claim the following:

> No single scheme, no matter how complex, can name all the ordinals. And from this, it follows that no algorithmic method can tell how to apply the method of Godel to all possible kinds of formal systems. And unless one is rather mystically inclined, therefore one must conclude that any human being simply will reach the limits of his own ability to Godelize at some point. From there on out, formal systems of that complexity, though admittedly incomplete for the Godel reason, will have as much power as that human being.

**Construcive Ordinal Notation System (CONS)**

_The following are my notes from the ["Constructive Ordinal Notation Systems"](https://www.jstor.org/stable/2689658) paper by Frederick Gass_

Let's break things down and see what the arguments are all about. In general there is a _maximal_ CONS that can name all constructive ordinals -- ordinals that can be constructed using first two [Cantor's principles](https://math.stackexchange.com/questions/956779/an-easy-to-understand-definition-of-omega-1/972010#972010). Specifically, think of a system that has the following notation:

1. 0 is 0.
1. $2^{x}$ -- successor notation. $x$ is ordinal, and this notation gives $x + 1$ e.g. $2^{2^{0}} = 2$.
2. $3^{e}$ -- a limit ordinal $\lambda$ notation, where $e$ is a Godel number of a program that outputs notations for a fundamental sequence for $\lambda$:

$\\{e\\}(0),\\{e\\}(1),\\{e\\}(2),\dots$

where the $\\{e\\}$ notation signifies an actual program. For brevity, let's assume a Godel number of a program is just a quoted version of the program's code. We can then have a more formal definition of the $\\{e\\}$ as follows:

```
{e} => (x) => eval(e, {x: x})
```

In short, $\\{e\\}$ returns a program represented by $e$ that has input $x$. The following Godel's number `e = 2^x` can be used to generate $\omega$ limit:

```
{"2^x"}(0) = 2^0 = 1 <=> 1
{"2^x"}(1) = 2^1 = 2 <=> 2
{"2^x"}(2) = 2^2 = 4 <=> 3
{"2^x"}(3) = 2^3 = 8 <=> 4
...
```

The paper then proceeds by asking whether the set of constructive ordinal notations ($2^x$ and $3^e$) is [recursive](https://github.com/marti-1/notebooks/blob/master/math/on-recursive-set.md) -- can we tell if some number $3^{x}$ is a limit ordinal notation number or just some random number? The question can be generalized by asking a) whether some Godel number $e$ represents a program, and b) whether $\\{e\\}$ terminates for every input $x$?

a) is a yes. This is because Godel coding is bijective and well-formdness of a program is decidable.

b) is a [Halting problem](https://github.com/marti-1/notebooks/blob/master/math/on-halting-problem-proof.md), so no.

If the set of ordinal notations produced by a CONS was recursive, then the system would be a **recursive ordinal notation system**. Our maximal CONS is not recursive though. This gives us the Church & Kleene theorem above.

Why do we care if the set of notations is recursive or not? If we could tell whether some random $3^x$ number was a notation of a limit ordinal, then we could enumerate all the limit ordinal notations by using increasingly larger Godel numbers that represent programs. In short, it would mean that there is an algorithm for generating all constructive ordinals. Since the set of the notations produced by the maximal CONS is not recursive, it means that there is no such algorithm.

**Back to Hofstadter**

Forming a Godel's sentence of a formal system aka. Godelization is akin to constructing an ordinal. Whilst ordinal is a number that is "one bigger", Godel's sentence makes a system "one incomplete":

$$G = \\{t_0, t_1, t_3, \dots | \\}$$

where $t_i$ are theorems of a formal system (e.g. TNT). Since there is no single algorithm that can enumerate every constructive ordinal, there is no single algorithm that can enumerate every Godel's sentence. In other words, there is no **single** algorithm that could Godelize every formal system. However, the important thing to note that the theorem only says that there is no **single algorithm**, it [does not mean that there are no infinity of algorithms, which at a limit could Godelize](https://math.stackexchange.com/questions/4897209/does-undecidability-allow-infinite-number-of-algorithms-for-limited-ranges)! The limit would not be an algorithm anymore.

The conclusion about the limit human brain has is not really backed by anything strong, like the Church & Kleene theorem, but rather by Hofstadter's own belief in the AI version of Church-Turing thesis:

> Mental processes of any sort can be simulated by a computer program whose underlying language is of power equal to that of a Turing machine.

This version claims that the brain is just **one big algorithm**. If you believe in it, then yes, the human brain being a single algorithm indeed would not be able to Godelize every formal system. Personally, I don't see anything "mystically inclined" in believing that the brain is a limit of all algorithms.

