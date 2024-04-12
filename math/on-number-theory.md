* All of the mathematics can fit on a number line.
* A sequence is enough to encode a pattern.
* An intelligent receiver can decode a sequence that has a pattern.

Suppose we are some alien species that at some point in future visits Earth. By the time these aliens arrive the planet is completely vacated -- not a single soul insight. The only thing that is left is scribbles that have interesting structure to them and attracts the eye of an intelligent being.

In order not to a new notation used by some alien species, let's just imagine that arabic numeral were not invented on Earth, and instead numbers are represented just with 0's and S's. Meanwhile, the aliens only use numbers made from arabic numeral in their notation. The two systems are equivalent:

* "0" is $0$
* "S0" is $1$
* "SSSS0" is $4$
* etc

Back to the scientific mission of the aliens. After a while of collecting these countless scribbles that are just laying around, some of the aliens start to classify this weird "alien" language. First thing that catches their eye, is that there is A LOT of cases of the following sequences of symbols:

* 0
* S0
* SS0
* SSS0
* SSSS0
* ...
* 200 S's and 0
* [not yet found string of 201 S's and a 0]
* 202 S's and 0
* ...
* a one billions of S's and then 0

Some of the aliens start to notice a pattern. But what is a pattern for them? In their world a pattern is a _model_ that let's you predict the next set of symbols using previously seen symbols in a sequence. Actually in their world they don't call it a "pattern", but rather a **recursive relation**. Going back to our sequence, the pattern that one of the aliens notices is that if you put these strings of symbols in an increasing order, the next string that you are going to encounter is one prepends an "S" to the previous string. Coincidentally, the next day news arrive that a new string of S's was found, namely one made from 201 S's.

As the confidence in this "prepend S" pattern grows, a decoding mechanism is built that translates their arabic numerals to these new "alien" strings:

```python
def nS(x):
  if x == 0:
    return "0"
  else:
    return "S" + translate(x - 1)
```

They call these kind of decoding mechanism **primitive recursive**, because they primitive by nature and are guaranteed to terminate after a finite amount of time. 

Note, the code above is written in Python language that uses alphanumeric characters, this is just for us humans to understand how the decoding mechanims defined by our alien species looks like. The aliens themselves use only numerals from 0 to 9 to express everything. So this Python definition in alien is just a sequence of numbers (e.g. $231,111,222,404,\dots$). Let's call these numbers [Gödel numbers](https://en.wikipedia.org/wiki/G%C3%B6del_numbering).


## General Recursion

After a couple years of collecting the S's strings, there seems to another pattern to emerge, namely that no matter what was the largest string found so far, somebody eventually finds even longer string of S's, and then longer then that, and even longer than the latter. In short the pattern seems to be "a never ending lengthening of the S strings". One of the aliens captures these pattern with a number $231,111,301,201,...$, which translates into Python as follows:

```
def omega():
  def omega_(x):
    yield nS(x)
    yield from omega_(x+1)
  yield from omega_(0)
```

This kind of pattern by our aliens is called **general recursive**, because it is not guaranteed to terminate, but it might.

---

## Appendinx: Some Random Thoughts

1. $\pi$ whilst real and infinite is "patterned" in a sence that by knowing the previous symbols we can predict the next symbol in line. Therefore $\pi$ can be captured by a general recursive model.
