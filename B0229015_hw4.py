from matplotlib import pyplot
from collections import namedtuple
from pprint import pprint as pp
from math import floor
 
Stem = namedtuple('Stem', 'data, leafdigits')
 
data0 = Stem((4285,2066,2584,1009,318,1429,981,1402,1137,414,
              564,604,14,4152,737,852,1560,1786,520,396,
              1278,209,349,478,3032,1461,701,1406,261,83,
              205,602,3770,726,3894,2662,497,35,2778,1379,
              3920,1379,99,510,582,308,3367,99,373,454),
             3.0)
 
def stemplot(stem):
    d = []
    interval = int(10**int(stem.leafdigits))
    for data in sorted(stem.data):
        data = int(floor(data))
        stm, lf = divmod(data,interval)
        d.append( (int(stm), int(lf)) )
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s,l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % ( stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    out.append('\n\nKey:\n Stem multiplier: %i\n X | Y  =>  %i*X+Y\n'
               % (interval, interval))
    return ''.join(out)
 
def plot_line(data):
    pyplot.subplot(2,1,1).hist(data)
 
def plot_box(data):
    pyplot.subplot(2,1,2).boxplot(data)
    pyplot.show()
     
if __name__ == '__main__':
    data = (4285,564,1278,205,3920,
              2066,604,209,602,1379,
              2584,14,349,3770,99,
              1009,4152,478,726,510,
              318,737,3032,3894,582,
              1429,852,1461,2662,308,
              981,1560,701,497,3367,
              1402,1786,1406,35,99,
              1137,520,261,2778,373,
              414,396,83,1379,454)
    print( stemplot(data0) )
    plot_line(data)
    plot_box(data)
