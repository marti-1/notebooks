A predicate can be defined in English e.g. `SUM(a,b,c)` returns 1 if a + b = c, 0 otherwise. This predicate can be _expressed_ in [pq-system](https://godel-escher-bach.fandom.com/wiki/Chapter_2) as `apbqc`. A predicate can be [represented](https://github.com/marti-1/notebooks/blob/master/math/on-representability.md) in a formal system:

1) All true instances of the predicate are theorems;
2) All false instances are nontheorems.

Where "instance" means replacing all free variables (e.g. a, b and c) by numerals (e.g. --- for 3, etc). The `SUM(a,b,c)` is represented in the pq-system, because every each true instance of the predicate is a thereom, each false instance is a non-theorem. For example SUM(2,3,5) expressed in pq is `--p---q-----`, and it is a theorem, whilst SUM(2,1,4) in pq is `--p-q----` and is not a theorem.