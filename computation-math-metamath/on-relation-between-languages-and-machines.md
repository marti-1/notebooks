If a language L is decidable, then there is a TM, that takes any word and if that word is in the language L, it will accept it and halt. Otherwise it will reject it and halt.

If a language L is r.e., then there is a TM, that takes any word and if that word is in the language Ls, it will accept it and halt. Otherwise, it will loop forever.

---

A machine M (e.g. finite state automaton) _accepts_ a word of some language, if for that particular word the machine halts in the accept state.

A machine M accepts some language $L$ if it _accepts_ all of its words. For example, a machine M (a finite state automaton) that accepts even numbers:

```python
def accepts(transitions,initial,accepting,tape):
    state = initial
    for c in tape:
        state = transitions[state][c]
    return state in accepting

even = {
    'EVEN': {'0': 'EVEN', '1': 'ODD'},
    'ODD': {'0': 'EVEN', '1': 'ODD'}
}

accepts(even, 'EVEN', {'EVEN'}, '000')
```