#!/usr/bin/python3
"""
takes 2 arguments:
    1. markdown file
    2. output file
writes to output file
"""

import os
import sys


def main():
    """
    Takes in the arguments
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # check if markdown file exists
    if not os.path.exists(markdown_file):
        print("Missing {}".format(markdown_file), file=sys.stderr)
        sys.exit(1)
    
    # read the markdown file
    


if __name__ == "__main__":
    main()
