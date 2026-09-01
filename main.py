"""Minimal entry point; also used by the DEBUG launch config to verify the interpreter."""

import os
import sys


def main() -> None:
    print("cwd:   ", os.getcwd())
    print("python:", sys.executable)


if __name__ == "__main__":
    main()
