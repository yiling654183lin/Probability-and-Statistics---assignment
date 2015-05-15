'''

b0229018_graph.py

參考http://rosettacode.org/wiki/Stem-and-leaf_plot#Python

使用課本p93,ex 5.2.1的數據畫出
1. 莖葉圖
2. Histogram
3. BoxPlot

'''
from collections import namedtuple#簡易py內建
from pprint import pprint as pp
from math import floor
from matplotlib import pyplot#需另外裝
 
Stem = namedtuple('Stem', 'data, leafdigits')

data0 = Stem((4285, 564, 1278, 205, 3920, 2066, 604, 209, 602, 1379,#
              2584, 14,  349, 3770, 99, 1009, 4125, 478, 726, 510,
              318, 737, 3032, 3894, 582, 1429, 852, 1461, 2662, 308,
              981, 1560, 701, 497, 3367, 1402, 1786, 1406, 35, 99,
              1137, 520, 261, 2778, 373, 414, 396, 83, 1379, 454), (3.0))
 
data = (4285, 564, 1278, 205, 3920, 2066, 604, 209, 602, 1379,
        2584, 14,  349, 3770, 99, 1009, 4125, 478, 726, 510,
        318, 737, 3032, 3894, 582, 1429, 852, 1461, 2662, 308,
        981, 1560, 701, 497, 3367, 1402, 1786, 1406, 35, 99,
        1137, 520, 261, 2778, 373, 414, 396, 83, 1379, 454)

 
def main():
    print(stemplot(data0))
    Histogram(data)
    Boxplot(data)
    
    
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

def Histogram(data):
    pyplot.subplot(3,1,1).hist(data)#直接用函式
    pyplot.xlabel('data')#中文無法顯示
    pyplot.ylabel('n')
    
def Boxplot(data):
    pyplot.subplot(3,1,3).boxplot(data)
    pyplot.xlabel('data')
    pyplot.show()
    
    
if __name__ == '__main__':
    main()
