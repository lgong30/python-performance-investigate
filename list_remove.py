"""This script compares different methods to
remove elements from it.
"""
import timeit


setup = '''
from copy import deepcopy
n = 10000
x = range(n)
y = range(20,2001)
'''

test_group = 1
test_num = 10000



s = '''
i = 20
while i < 2000:
    y[i - 20] = x[i]
    i += 1
'''

print "splicing: ", timeit.Timer('[z for z in x[20:2001]]', setup=setup).repeat(test_group, test_num)[0]
print "list creating: ", timeit.Timer('[x[i] for i in xrange(20,2001)]', setup=setup).repeat(test_group, test_num)[0]
print "while loop: ", timeit.Timer(s, setup=setup).repeat(test_group, test_num)[0]



print "removing first element: ", timeit.Timer('del x[0]', setup=setup).repeat(test_group, test_num)[0]
print "removing the last element: ", timeit.Timer('del x[-1]', setup=setup).repeat(test_group, test_num)[0]