# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 19:11:40 2016

@author: miniesta4
"""

def poker(hands):
    "Return the best poker hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)
    
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x:x)
    for item in iterable:
        if not maxval or key(item) > maxval:
            result, maxval = [item], key(item)
        elif key(item) == maxval:
            result.append(item)
    return result
    
count_rankings = {(5,0):10, (4,1):7, (3,2):6, (3,1,1): 3, (2,2,1):2, (2,1,1,1):1,
               (1,1,1,1,1):0}
    
def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (15, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks
   
    
def group(items):
    '''
    Return a list of [(count, x)...], highest count first, then highest x first.
    '''
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs):
    '''
    Convert a list of pairs into a pair of list
    '''
    return zip(*pairs)


def test():
    "Test cases for the functions in poker program."
    sf = '6C 7C 8C 9C TC'.split() # Straight flush
    fk = '9D 9H 9S 9C 7D'.split() # Four of a kind
    fh = 'TD TC TH 7C 7D'.split() # Full house
    tp = '5S 5D 9H 9C 6S'.split() # Two pair
    s1 = 'AS 2S 3S 4S 5C'.split() # A-5 straight
    s2 = '2C 3C 4C 5S 6S'.split() # 2-6 straight
    ah = 'AS 2S 3S 4S 6C'.split() # A high
    sh = '2S 3S 4S 6C 7D'.split() # 7 high
    assert poker([s1, s2, ah, sh]) == [s2]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + [fh] * 99) == [sf]
    assert hand_rank(sf) == (9, (10,9,8,7,6))
    assert hand_rank(fk) == (7, (9,7))
    assert hand_rank(fh) == (6, (10,7))
    return 'test passed'


