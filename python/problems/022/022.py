#!/usr/bin/env python2

def get_names_list():
    with open("names.txt") as f:
        quoted_names = f.read().split(",")
        return [name.strip('"') for name in quoted_names]

def name_score(index, name):
    return name_value(name) * (index + 1)

def name_value(name):
    return sum([char_value(char) for char in name])

def char_value(char):
    return ord(char.upper()) - ord("A") + 1

def main():
    sorted_names = sorted(get_names_list())
    print sum([name_score(i, name) for (i, name) in enumerate(sorted_names)])

if __name__ == "__main__":
    main()
