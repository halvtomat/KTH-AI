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

def transish(transition, state):
    state2 = [[]]
    for i in range(len(state[0])):
        sum = 0
        for j in range(len(state[0])):
            sum += state[0][j] * transition[j][i]
        state2[0].append(sum)
    return state2

def pre_transish(emission, state, seq, k):
    state2 = [[]]
    for i in range(len(state[0])):
        state2[0].append(state[0][i] * emission[i][seq[k]])
    return state2

def solve2(transition, emission, state, seq):
    for i in range(0,len(seq)):
        state = pre_transish(emission, state, seq, i)
        state = transish(transition, state)
    print(sum(state[0]))

def print_list(l):
    s = ""
    for e in l:
        s += str(round(e,3)) + " "
    print(s)

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

solve2(transition, emission, init, seq)