# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:21:12 2017

@author: miniesta4
"""
import random
#import collections

def shuffle(deck):
    '''Knuth's Algorith P.'''
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i, N))

def shuffle1(deck):
    '''My teacher algorithm'''
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)
        
def shuffle2(deck):
    '''A modification of my teacher's algorithm'''
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)

def shuffle3(deck):
    '''An easier modification of my teacher's algorithm'''
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))


def swap(deck, i, j):
    '''Swap elements i and j of a collection'''
    #print('swap', i, j)
    deck[i], deck[j] = deck[j], deck[i]


def test_shuffler(shuffler, deck='abcd', n=10000, verbose=False):
    #counts = collections.defaultdict(int)
    counts = {}
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] = counts.get(''.join(input),0) + 1
    e = n/factorial(len(deck)) ## expected count
    ok = all((0.9*e <= counts[item] <= 1.1*e) for item in counts)
    name = shuffler.__name__
    print('{:s}({:s}) {:s}'.format(name, deck, ('ok' if ok else '***BAD***')))
    if verbose:
        for k in sorted(counts):
            print('{:s}: {:n} {:.2%}'.format(k, counts[k], counts[k]/n), )

def factorial(n):
    return 1 if (n <= 1) else n*factorial(n-1)
    
def test_shufflers(shufflers=[shuffle, shuffle1, shuffle2, shuffle3], decks=['abc', 'ab']):
    for d in decks:
        for s in shufflers:
            test_shuffler(s, d, verbose=True)
            print()
