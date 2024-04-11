# Proof of a Halting Problem

Notes from the [Halting Problem](https://www.jimmorris.org/nerd-zone/halting-problem) article.

Turing asked if there is a program `Program-Halts-For-Input(i,j)`, where `i` is the i'th index of a program and `j` is a specific input.

Sketch of the proof:
1. Let's assume that `Program-Halts-For-Input(i,j)` exists. Show that from it we can build `Program-Halts(i)`.
2. Show that `Program-Halts(i)` does not exist, therefore `Program-Halts-For-Input(i,j)` can't exist either.

## Part 1

The set of all 1-param programs $M$ is countable, $M = \\{M_0,M_1,M_2,...\\}$

If `Program-Halts-For-Input(i,j)` exists, then there is a program $M_n(i)$ such that:

```
M_n(i) =
  for j in 0... do
    if Program-Halts-For-Input(i,j) == 'no'
      return 'yes'
    end
  end
```

NOTE: there $n$ is a known index of a program $M_n$.

If $i$ halts, $M_n(i)$ never halts. If $i$ does not halt for some input, $M_n(i)$ halts. We can use this program in order to create `Program-Halts(i)`:

```
Program-Halts(i) =
  if Program-Halts-For-Input(n,i) == 'no'
    # if M_n(i) does not halt, it means it halts
    return 'yes'
  else
    $ if M_n(i) halts, it means that it doesn't
    return 'no'
  end
```

## Part 2

1. If there is `Program-Halts(i)` we can enumerate all programs $M$ that always halt, let's call this set $H$.
2. If there is $H$ it means there is a function $B(i) = H_i(i) + 1$. $B(i)$ clearly halts.
3. $B$ has some index $\beta$ -- $B = H_{\beta}$. Therefore $B(\beta) = H_{\beta}(\beta)$ and also $B(\beta) = B(\beta) + 1$.
4. **A contradiction**.

NOTE: (1 -> (2 -> (3 -> false))) = false. Just a reminder, TA(true -> false) = false. Because of this, a chain of implications reduces to false if the last consequent is false.
