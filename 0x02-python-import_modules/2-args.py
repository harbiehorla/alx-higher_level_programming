#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    print(f"{length} {'argument' if length == 1 else 'arguments'}{'.' if length == 0 else ':'}")
    for i in range(1, length + 1):
        print(f"{i}: {argv[i]}")
