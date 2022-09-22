#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 2:
        word = "argument"
    else:
        word = "arguments"
    if argc == 1:
        print(f"{0:d} {word}.")
    elif argc > 1:
        print(f"{argc - 1:d} {word}:")
        for index in range(1, argc):
            print(f"{index}: {argv[index]}")
