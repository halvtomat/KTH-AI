#/usr/bin/python3

import sys

def init_float_list(line, l):
    line = line.replace('\n','').split(' ')
    a = int(line[0])
    b = int(line[1])
    for i in range(a):
        c = []
        for j in range(b):
            c.append(float(line[j + i * b + 2]))
        l.append(c)

def init_seq(line, l):
    line = line.replace('\n','').split(' ')
    a = int(line[0])
    for i in range(a):
        l.append(int(line[i + 1]))

def print_list(l):
    s = ""
    for e in l:
        s += str(e) + " "
    print(s)

def observe(emission, state, seq, k):
    for i in range(len(state[0])):
        state[0][i] = state[0][i] * emission[i][seq[k]]

def next_state(transition, state, argmax):
    argmax_temp = []
    next_state = [[]]
    for i in range(len(state[0])):
        temp = []
        for j in range(len(state[0])):
            temp.append(state[0][j] * transition[j][i])
            
        argmax_temp.append(temp.index(max(temp)))
        next_state[0].append(state[0][max(argmax_temp)] * transition[max(argmax_temp)][i])

    argmax.append(argmax_temp)
    state[0] = next_state[0]


def solve(transition, emission, state, seq):
    solution = []
    argmax = []

    for i in range(len(seq)):
        observe(emission, state, seq, i)
        if(i != len(seq)-1):
            next_state(transition, state, argmax)

    back = state[0].index(max(state[0]))
    solution.append(back)
    for i in range(len(seq) - 1):
        back = argmax[len(seq) - i - 2][back]
        solution.append(back)
    solution.reverse()
    print_list(solution)
    

transition = []
emission = []
init = []
seq = []

line = sys.stdin.readline()
init_float_list(line, transition)
line = sys.stdin.readline()
init_float_list(line, emission)
line = sys.stdin.readline()
init_float_list(line, init)
line = sys.stdin.readline()
init_seq(line, seq)

solve(transition, emission, init, seq)