Q = {'init', 'halt'}
S = {0, 1, None}
# transition function is a dictionary of tuples (q,s) -> (q_,s_,D)
f = {
    ('init',0) : ('init', 1, 'R'),
    ('init',1) : ('init', 0, 'R'),
    ('init',None) : ('halt', None, None)
}
q0 = 'init'
F = {'halt'}

T = [0,0,0,1,None]

# a Turing machine configuration that inverts its input
m = (Q, S, f, q0, F)

def make_TM(machine, tape):
    return lambda: run(machine, tape)

def run(machine, tape):
    _, _, f, q0, F = machine
    q = q0
    i = 0
    while q not in F:
        s = tape[i]
        q_, s_, D = f[(q,s)]
        tape[i] = s_
        q = q_
        if D == 'R':
            i = i + 1
        else:
            i = i - 1
    return tape

invert = make_TM(m, [0,0,0,1,None])
print(invert())
