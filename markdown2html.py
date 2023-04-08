#!/usr/bin/python3

"""
Script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
"""

if __name__ == "__main__":
    import sys
    import os
    import markdown

    args = len(sys.argv)
    if args < 2:
        print(f"Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if args >= 2:
        if not os.path.exists(sys.argv[1]):
            print(f"Missing {sys.argv[1]}")
            exit(1)
        with open(sys.argv[1], "r") as f:
            markdown = markdown.markdown(f.read())
        with open(sys.argv[2], "w") as g:
            g.write(markdown)
        exit(0)
