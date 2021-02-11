#/usr/bin/python3

import sys

def init_list(line, l):
    line = line.replace('\n','').split(' ')
    a = int(line[0])
    b = int(line[1])
    for i in range(a):
        c = []
        for j in range(b):
            c.append(float(line[j + i * b + 2]))
        l.append(c)

def solve(transition, emission, init):
    solution = []
    solution.append(1)
    solution.append(len(emission[0]))
    for i in range(len(emission[0])):
        sum = 0.0
        for j in range(len(init[0])):
            for k in range(len(transition)):
                sum += init[0][j] * transition[j][k] * emission[k][i]
        solution.append(round(sum, 3))
    print_list(solution)

def print_list(l):
    s = ""
    for e in l:
        s += str(e) + " "
    print(s)

transition = []
emission = []
init = []

line = sys.stdin.readline()
init_list(line, transition)
line = sys.stdin.readline()
init_list(line, emission)
line = sys.stdin.readline()
init_list(line, init)

solve(transition, emission, init)