# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:26:32 2017

@author: miniesta4
"""

# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars).

def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):
    f_opt_p = opt(plus(x))
    return lambda Ns: f_opt_p(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
def oneof(chars):
    set_c = set(chars)
    return lambda Ns: set_c if 1 in Ns else null
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.

null = frozenset([])

def genseq(x, y, Ns, startx=0):
    "Set of matches to xy whose total len is in Ns"
#    Tricky part: x+ is defined as: x+= xx*
#    To stop the recursion, the first x must generate at least 1 char,
#    and then the recursive x* has that many few caracters. We use startx=1 
#    to say that x must match al least 1 character.
    if not Ns:
        return null
    xmatches = x(set(range(startx, Ns+1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m > 0)
    ymatches = y(Ns_y)
    return set(m1+m2 
                for m1 in xmatches
                for m2 in ymatches
                if len(m1 + m2) in Ns)

def test():

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    return 'tests pass'
    
    
print (test())