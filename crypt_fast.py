# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:42:52 2017

@author: miniesta4
"""
import itertools, re

def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompile the formula; only one eval per formula"""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((0,1,2,3,4,5,6,7,8,9), len(letters)):    
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))    
                return formula.translate(table)
        except ArithmeticError:
            pass
        
def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also returns letters found as a str, 
    in same order as param function.
    The first digit of a multi-digit number can't be 0. 
    So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False.
    For example:
    'YOU == ME**2 => lambda Y, M, E, U, O: Y!=0 and M!=0 and (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'
    """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z]', formula))    
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        tests = ' and '.join(L + '!=0' for L in firstletters)
        body = '{} and ({})'.format(tests, body)
    f = 'lambda {}: {}'.format(parms, body)
    if verbose: print (f)
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        word_rev = word[::-1]
        #terms = [str(10**i) + '*' + c for (i, c) in enumerate(word_rev)]
        terms = ['{}*{}'.format(10**i, c) for (i, c) in enumerate(word_rev)] 
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def test():
    assert faster_solve('A + B == BA') == None # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') == ('289 == 17**2' or '576 == 24**2' or '841 == 29**2')
    assert faster_solve('X / X == X') == '1 / 1 == 1'
    return 'tests pass'

test()