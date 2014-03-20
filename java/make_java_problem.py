#!/usr/bin/env python

from __future__ import print_function
from optparse import OptionParser
import sys
import os

JAVA_TEMPLATE_NAME = "Problem.java.template"
ANT_TEMPLATE_NAME = "build.xml.template"

def parse_cmd_line_args():
    parser = OptionParser()
    parser.add_option("-b", "--build", action="store_true", default=False,
                      help="Generate a build file for the problem")
    parser.add_option("-c", "--code", action="store_true", default=False,
                      help="Generate a code stub for the problem")
    parser.add_option("-o", "--overwrite", action="store_true", default=False,
                      help="Overwrite pre-existing build/code files")
    return parser.parse_args()

def verify_template_existance():
    for filename in (JAVA_TEMPLATE_NAME, ANT_TEMPLATE_NAME):
        if not os.path.isfile(filename):
            print("Error: Required file '{0}' doesn't exist.".format(filename),
                  file=sys.stderr)
            sys.exit(1)

def validate_args(args):
    for arg in args:
        try:
            int(arg)
        except ValueError as ex:
            print("Error: '{0}' is not an integer.".format(arg), file=sys.stderr)
            sys.exit(1)

def create_code_stub(problem_num, overwrite=False):
    filename = "problems/{0}/Prob{0}.java".format(problem_num)
    if overwrite or not os.path.exists(filename):
        with open(JAVA_TEMPLATE_NAME) as f:
            template = f.read()
        with open(filename, "wb") as f:
            f.write(template % (problem_num, problem_num))

def create_build_file(problem_num, overwrite=False):
    filename = "problems/{0}/build.xml".format(problem_num)
    if overwrite or not os.path.exists(filename):
        with open(ANT_TEMPLATE_NAME) as f:
            template = f.read()
        with open(filename, "wb") as f:
            f.write(template % (problem_num))

def create_problem_dir(problem_num):
    problem_dir = "problems/" + problem_num
    if not os.path.exists(problem_dir):
        os.mkdir(problem_dir)

if __name__ == "__main__":

    options, args = parse_cmd_line_args()
    verify_template_existance()
    validate_args(args)

    for problem_num in args:
        create_problem_dir(problem_num)
        if options.build:
            create_build_file(problem_num, options.overwrite)
        if options.code:
            create_code_stub(problem_num, options.overwrite)
