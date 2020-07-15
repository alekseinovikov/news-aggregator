import sys

from aggregator import aggregate

modules = ["habr"]


def main(argv):
    aggregate(modules)


if __name__ == "__main__":
    main(sys.argv)
