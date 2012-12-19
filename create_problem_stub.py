import os

problem_number = str(input("Enter problem number: ")).zfill(3)

dirname = "prob_" + problem_number
filename = dirname + ".py"

if not os.path.exists(dirname):
    os.makedirs(dirname)

if not os.path.isfile(dirname + os.path.sep + filename):
    f = open(dirname + os.path.sep + filename, "w+")
    f.write('"""\n' +
            '===========================\n' +
            'Project Euler - Problem {0}\n'.format(problem_number) +
            '===========================\n' +
            '<PROBLEM DESCRIPTION HERE>\n' +
            '"""\n'.format(problem_number))
    f.close()

