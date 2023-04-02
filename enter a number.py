sen = input('Enter a number:')

try:
    ival = int(sen)
except:
    ival = -1

if ival > 0 :
    print('good job')
else:
    print('not a number')
