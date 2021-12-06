# myls.py
# Import the argparse library
from compute_M import compute_M
from plot_cheaters import plot_cheaters
from plot_population import plot_population
from plot_initial import plot_initial
from compute_cheaters import compute_cheaters
import argparse
from random import randrange

import numpy as np
from collections import Counter

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('-P',
                       action='store',
                       default=10000,
                       type=int,
                       help="Number of town's inhabitants.")
my_parser.add_argument('-I',
                       action='store',
                       # dest=I,
                       default=100,
                       type=int,
                       help="Number of initial positive cases")
my_parser.add_argument('-N',
                       action='store',
                       type=int,
                       help="Number of 'cheaters' or else people that ignore lockdown measures and visit other houses")
my_parser.add_argument('-S',
                       action='store',
                       default=1,
                       type=float,
                       help="Number of initial positive cases")
my_parser.add_argument('-D1',
                       action='store',
                       default=3,
                       type=int,
                       help="Days after on which an infected person becomes infectious")
my_parser.add_argument('-D2',
                       action='store',
                       default=10,
                       type=int,
                       help=" Days after on which an infected person stops being infectious")

my_parser.add_argument('--compute_M',
                       action='store_true',
                       help="Prints M for the given set of parameters")
my_parser.add_argument('--plot_population',
                       nargs=3,
                       type=int,
                       action='store',
                       help=" shows or saves (whatever you want) a plot. On X axis are the values of the population (parameter P) from A to B with C intermediate steps (use np.linspace(A, B, C)). On Y axis there are the corresponding M values.")
my_parser.add_argument('--plot_initial',
                       nargs=3,
                       type=int,
                       action='store',
                       help="shows or saves (whatever you want) a plot. On X axis are the initial cases (parameter I) from A to B with C steps (use np.linspace(A, B, C)). On Y axis there are the corresponding M values.")
my_parser.add_argument('--plot_cheaters',
                       nargs=3,
                       type=int,
                       action='store',
                       help="shows or saves (whatever you want) a plot. On X axis are the cheaters (parameter N) from A to B with C steps (use np.linspace(A, B, C)). On Y axis there are the corresponding M values")
my_parser.add_argument('--compute_cheaters',
                       nargs=1,
                       type=int,
                       action='store',
                       help="prints the maximum number of cheaters (N) that can be if don't want Μ to go over the given value.")

# Execute parse_args()
args = my_parser.parse_args()
# print("You passed "+(str)(len(sys.argv)-1)+" arguments");

print(vars(args))

if vars(args)['N'] is None and vars(args)['compute_cheaters'] is None and vars(args)['plot_cheaters'] is None:
    raise Exception('You have to specify N.')

activeElem = 0
list = [args.compute_M, args.plot_population, args.plot_initial, args.compute_cheaters, args.plot_cheaters]
# print(list)
for argument in list:
    # print(argument)
    if argument:
        if not argument is None:
            activeElem = activeElem + 1
            # print(activeElem)

if activeElem > 1:
    raise Exception('You have specified more than one operation.')


P = vars(args)["P"]
I = vars(args)["I"]
N = vars(args)["N"]
D1 = vars(args)["D1"]
D2 = vars(args)["D2"]
S = vars(args)["S"]



if args.compute_M:
    compute_M(P, I, N, D1, D2, S)
elif args.plot_population:
    temp_list = (vars(args)["plot_population"])
    A = temp_list[0]
    B = temp_list[1]
    C = temp_list[2]
    plot_population(A, B, C, I, N, D1, D2, S)

elif args.plot_initial:
    temp_list = (vars(args)["plot_initial"])
    A = temp_list[0]
    B = temp_list[1]
    C = temp_list[2]
    plot_initial(A, B, C, P, N, D1, D2, S)

elif args.compute_cheaters:
    M = vars(args)["compute_cheaters"][0]
    N = compute_cheaters(M, P, I, D1, D2, S)
    print(N)
elif args.plot_cheaters:
    temp_list = (vars(args)["plot_cheaters"])
    print(temp_list)
    A = temp_list[0]
    B = temp_list[1]
    C = temp_list[2]
    print(A,B,C)
    N = plot_cheaters(A, B, C, P, I, D1, D2, S)
