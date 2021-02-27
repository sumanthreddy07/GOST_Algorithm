import sys

def progressbar(count, total, status=''):

    bar_length = 20
    filled_length = int(round(bar_length*count/float(total)))

    precentage = round(100.0*count/float(total), 1)
    bar = '='*filled_length + '>' + '-'*(bar_length - filled_length-1)

    sys.stdout.write('[%s] %s%s ... %s\r' % (bar, precentage, '%', status))
    sys.stdout.flush()