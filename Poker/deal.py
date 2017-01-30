# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 19:55:37 2016

@author: miniesta4
"""
import random

# This builds a deck of 52 cards.
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
    '''
    Deals numhands hands with n cards each.
    '''
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    
    
    
    