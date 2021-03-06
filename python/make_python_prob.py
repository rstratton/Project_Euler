#!/usr/bin/python3
import os

problem_number = str(input("Enter problem number: ")).zfill(3)

dirname = "prob" + problem_number
filename = dirname + ".py"

if not os.path.exists(dirname):
    os.makedirs(dirname)

if not os.path.isfile(dirname + os.path.sep + filename):
    f = open(dirname + os.path.sep + filename, "w+")
    f.write('"""\n' +
            '===========================\n'                        +
            'Project Euler - Problem {0}\n'.format(problem_number) +
            '---------------------------\n'                        +
            'Description:\n'                                       +
            '===========================\n'                        +
            '"""\n'.format(problem_number))
    f.close()

