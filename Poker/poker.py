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
    
    
def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks) 

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    return len(set([s for (r, s) in hand])) == 1
    
def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    """
    If there are two pair, return the two ranks as a tuple:
     (highest, lowest); otherwise return None.
    """
    highest = kind(2, ranks)
    ranks.reverse()
    lowest = kind(2, ranks)
    if highest and lowest and highest != lowest:
        return (highest, lowest)
    return None

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
    fk_ranks = card_ranks(fk)
    tp_ranks = card_ranks(tp)
    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) == None
    assert kind(2, fk_ranks) == None
    assert kind(1, fk_ranks) == 7
    assert two_pair(fk_ranks) == None
    assert two_pair(tp_ranks) == (9, 5)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + [fh] * 99) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'test passed'


