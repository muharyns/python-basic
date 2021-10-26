import sys
print('Total arguments:', len(sys.argv), 'arguments.')
print('Argument Lists:', str(sys.argv))
for i in range(len(sys.argv)):
    print('Argument [{}] is {} '.format(i, sys.argv[i]))
