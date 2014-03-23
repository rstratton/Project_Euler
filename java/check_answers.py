#!/usr/bin/env python

from __future__ import print_function
from optparse import OptionParser
import sys
import os
import subprocess

DEV_NULL = open(os.devnull, 'w')

def problem_assets_exist(problem_num):
    problem_dir = "problems/" + problem_num
    build_file = problem_dir + "/build.xml"
    if not os.path.exists(problem_dir):
        print("Error: Directory '{0}' doesn't exist.".format(problem_dir),
              file=sys.stderr)
        return False
    elif not os.path.exists(build_file):
        print("Error: Build file '{0}' doesn't exist.".format(build_file),
              file=sys.stderr)
        return False
    else:
        return True

def validate_args(args):
    for arg in args:
        try:
            int(arg)
        except ValueError as ex:
            print("Error: '{0}' is not an integer.".format(arg), file=sys.stderr)
            sys.exit(1)

def build(problem_num):
    print("{0}: Building...".format(problem_num), end="")
    build_file = "problems/{0}/build.xml".format(problem_num)
    build_exit_code = subprocess.call(["ant", "-q", "-f", build_file],
                                      stdout=DEV_NULL,
                                      stderr=DEV_NULL)
    if build_exit_code == 0:
        print("OK.")
        return True
    else:
        print("FAILED.")
        return False

def check_answer(problem_num):
    print("     Checking...", end="")
    output_filename = "problems/{0}/output.out".format(problem_num)
    answer_filename = "../answers/{0}/answer".format(problem_num)
    for filename in (output_filename, answer_filename):
        if not os.path.exists(filename):
            print("'{0}' missing.".format(filename))
    command = ["diff", output_filename, answer_filename]
    diff_exit_code = subprocess.call(command, stdout=DEV_NULL, stderr=DEV_NULL)
    if diff_exit_code == 0:
        print("OK.")
    else:
        print("FAILED.")


if __name__ == "__main__":
    problems = sys.argv[1:] or os.listdir("./problems")
    validate_args(problems)

    for problem_num in problems:
        if problem_assets_exist(problem_num) and build(problem_num):
            check_answer(problem_num)
        print("")
