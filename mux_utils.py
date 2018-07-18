import sys

def logio(msg, stdio=sys.stderr):
    try:
        stdio.isatty()
    except:
        stdio = sys.stderr
    print(msg, file=stdio)

