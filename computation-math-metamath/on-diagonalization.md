

## GEB

_"Bluediag" -- "Godel, Escher, Bach", p420_

```
Bluediag(N) = 1 + Blueprogram[#N](N)
```

Supose, Bluediag is a Blue Program, then it has an index:

```
Bluediag(N) = Blueprogram[#X](N)
```

But by definition, for input X, Bluediag is:

```
Bluediag(X) = 1 + Blueprogram[#X](X)
```

and also:

```
Bluediag(X) = Blueprogram[#X](X)
```

A contradiction.

## [On The Unreasonably Broad Uses of Diagonalization](https://robertcunningham.xyz/diagonalization/)

### Trilemma

1. $\delta:Y \rightarrow Y$ has a fixed point.
2. There exists some $g:X \rightarrow Y$ which isn't found in $f(n)$ for $n \in \mathbb{N}$, but g is obviously the right kind of object, so the list of objects $f(n)$ must not be exhaustive. (_the set is uncountable e.g. think of reals_)
3. There exists some $g:X \rightarrow Y$
which isn't found in $f(n)$ for $n \in \mathbb{N}$, but $f(n)$ obviously lists all the possible objects, so $g$ must actually be a new and different kind of object. (_the set is countable, but g is in a bigger set e.g. eval is not in p.r. set_).

### Example: Primitive Recursion

>  But it turns out that they aren't Turing complete, since they can't simulate the eval function.

So at the point above, I had the following question: why can't a primitive recursive function eval a primitive recursive function? Suppose it could, then it could compute the Bluediag. But we know that Bluediag is not a primitive recursive function. In the definition only the `Blueprogram[#X](X)` is not p.r. (+1 is). Therefore, there is no p.r. function that could eval any other p.r. function. This makes sense, because of the former function existed, what would be the result of it evaluating itself? An endless loop, which is not possible.

### Example: Church-Turing & Rogers' Theorem

> **all programs mapping functions to functions have a fixed point.**

$\delta : (X \rightarrow Y) \rightarrow (X \rightarrow Y) \Leftrightarrow Y \rightarrow Y$ (I think)

Then $\delta$ is a function mapping functions to functions:

```
delta = (x) => x + 1
plus1 = delta(eval(f(x)))
```

For the above delta an input function whose output is mapped to the same is:

```
f = (x) => while true { console.log('+')}
delta(eval(f(x))) // +++...
```

If the delta was `delta(x) => 1 + x`. We would get the same result, since the evaluation of the endless loop would be performed first.

---

> These correspond to the (1) and (3) branches of the trilemma respectively.

In p.r. `halt(x,y)` is decidable. So (1) exists, and (2) is the case, this leaves (3) -- there is a function that can't be expressed in p.r., namely the interpreter. In a Turing complete language, (1) doesn't exist, therefore (3) is the case, in particular one can write an interpreter in the language for the language.

### New Tool: Diagonal Lemma

Lemma:

$$
\forall A \, \exists \phi \quad T \vdash (\phi \iff A(\ulcorner \phi \urcorner))
$$

Suppose: 

* $A(x) := x * 2 = 4$  
* $\ulcorner 2*2=4 \urcorner \Leftrightarrow 2$;
* then $A(\ulcorner 2*2=4 \urcorner) \Leftrightarrow 2*2=4$

The $\ulcorner 2*2=4 \urcorner$ is a fixed point -- a numerical representation of a statement is mapped by $A$ to itself.

## Question

* Can diagonalization be performed at the object language?

## Further Reading

* [Why doesn't Cantor's diagonal argument also apply to natural numbers?](https://math.stackexchange.com/questions/35107/why-doesnt-cantors-diagonal-argument-also-apply-to-natural-numbers)