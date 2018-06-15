def usage():
    print('You have to provide exactly two arguments.')

if __name__ == '__main__':
    pattern = sys.argv[1]
    substitution = sys.argv[2]

    for line in sys.stdin:
        sys.stdout.write(line.replace(pattern, substitution))
