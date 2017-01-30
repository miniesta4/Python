# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 20:12:44 2016

@author: miniesta4
"""

import poker
import deal


def hand_percenteges(n=700*1000):
    '''
    Sample n random hands and print a table of percentages for each type of hand.
    '''
    hand_names = ('High Card', 'Pair', '2 Pair', '3 Kind', 'Straight', 'Flush',
                  'Full House', '4 Kind', 'Straight Flush')

    counts = [0]*9
    for i in range(n//10):
        for poker.hand in deal.deal(10):
            counts[poker.hand_rank(poker.hand)[0]] += 1
    for j in reversed(range(9)):
        print ('{:14} {:6.3%}'.format(hand_names[j], counts[j]/n))