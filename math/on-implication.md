# Implication

My intuition about the implication is that it is a formalization of **causation** in mathematics. It has an arbitrary truth assignment that "works":

| $P$ | $Q$ | $P \rightarrow Q$ |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   T   |
| F | F |   T   |

The truth table for $\rightarrow$ is not straight forward (IMO). The only clear case is that if trigger P is true and the outcome Q is false, then P's causality of Q is false. The rest of the values is the best approximation of if...then. For example, if the following interpretation was used:


| P | Q | P -> Q |
|---|---|-------|
| T | T |   F   |
| T | F |   F   |
| F | T |   T   |
| F | F |   **F**   |

Then $p\rightarrow q \vDash \neg p \rightarrow q$ (modus tolens) is invalid:

| $P$ | $Q$ | $P \rightarrow Q$ | $\neg P$ | $\neg P \rightarrow Q$ | $P \rightarrow Q \vDash \neg P \rightarrow Q$ |
|-----|-----|-------------------|---------|-----------------------|---------------------------------------------|
|  T  |  T  |         T         |    F    |           T           |                      T                      |
|  T  |  F  |         F         |    F    |           T           |                      **F**                      |
|  F  |  T  |         T         |    T    |           T           |                      T                      |
|  F  |  F  |         T         |    T    |           F           |                      **F**                      |

It is kind of intuitive that the modus tolens should work, so the latter truth assignment is not used.
