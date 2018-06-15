import sys


pattern = sys.argv[1]
substitution = sys.argv[2]

for line in sys.stdin:
    sys.stdout.write(line.replace(pattern, substitution))
