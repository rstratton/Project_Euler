#!/usr/bin/env python
import sys
import os

JAVA_TEMPLATE_NAME = "Problem.java.template"
ANT_TEMPLATE_NAME = "build.xml.template"

def verify_template_existance():
    for filename in (JAVA_TEMPLATE_NAME, ANT_TEMPLATE_NAME):
        if not os.path.isfile(filename):
            print "Error: Required file '{0}' doesn't exist.".format(filename)
            sys.exit(1)

def validate_environment():
    """
    Check that the proper template files and command line arguments are present

    """
    verify_template_existance()
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    try:
        int(sys.argv[1])
    except ValueError as ex:
        print "Error: Received a non-integral problem number"
        print_usage()
        sys.exit(1)

def create_class_stub(problem_num):
    with open(JAVA_TEMPLATE_NAME) as f:
        template = f.read()
    with open("{0}/Prob{0}.java".format(problem_num), "wb") as f:
        f.write(template % (problem_num, problem_num))

def create_build_file(problem_num):
    with open(ANT_TEMPLATE_NAME) as f:
        template = f.read()
    with open("{0}/build.xml".format(problem_num), "wb") as f:
        f.write(template % (problem_num))

def create_problem_dir(problem_num):
    if not os.path.exists(problem_num):
        os.mkdir(problem_num)

def print_usage():
    usage_string = "Usage: {0} <problem_number>".format(sys.argv[0])
    print usage_string


if __name__ == "__main__":

    validate_environment()
    problem_num = sys.argv[1]

    create_problem_dir(problem_num)
    create_class_stub(problem_num)
    create_build_file(problem_num)


