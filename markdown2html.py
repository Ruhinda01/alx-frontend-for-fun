#!/usr/bin/python3
"""
takes 2 arguments:
    1. markdown file
    2. output file
writes to output file
"""

import os
import sys


def read_file(file):
    """
    reads the file
    """
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()


def to_html(file_content):
    """
    Converts markdown to html
    """
    content = []
    in_list = False
    ul_open = False
    for line in file_content:
        if line.startswith('#'):
            parts = line.split(' ', 1)
            level = len(parts[0])
            title = parts[1].strip()
            if in_list:
                content.append("</ul>")
                in_list = False
                ul_open = False
            if 1 <= level <= 6:
                content.append("<h{}>{}</h{}>"
                               .format(level, title, level))
            else:
                content.append(line)
        elif line.startswith('-'):
            parts = line.split(' ', 1)
            if not ul_open:
                content.append("<ul>")
                ul_open = True
                in_list = True
            item = parts[1].strip()
            content.append("<li>{}</li>".format(item))
        else:
            if ul_open:
                content.append("</ul>")
                in_list = False
                ul_open = False
            content.append(line)

    if ul_open:
        content.append("</ul>")

    return '\n'.join(content)


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
    file_content = read_file(markdown_file)

    # convert the markdown to html
    html_content = to_html(file_content)

    # write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)


if __name__ == "__main__":
    main()
