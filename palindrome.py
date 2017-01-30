# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:29:23 2017

@author: miniesta4
"""

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    def length(slice): 
        a,b = slice
        return b-a
        
    candidates = [grow(text, start, end) 
                   for start in range(len(text)) 
                   for end in (start, start+1)]
    return max(candidates, key=length)
    
def grow(text, start, end):
    "Start with a 0- or 1- lenght palindrome; try to get a bigger one."
    while (start > 0 and end < len(text) and
            text[start-1].upper() == text[end].upper()):
        start -= 1
        end += 1
    return (start, end)                
        



def longest_subpalindrome_slice_fast(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    result = (0,0)
    max_l = 0    # max length so far
    text_low = text.lower()
    for i in range(len(text)-1):
        # From 2 letters
        l = i # low index
        h = i+1 #high index
        while l >= 0 and h < len(text_low) and text_low[l] == text_low[h]: #in bound
            if  h - l > max_l:
                result = (l,h+1)
                max_l = h-l
            l -= 1
            h += 1
        # From 3 letters
        l = i-1 # low index
        h = i+1 #high index
        while l >= 0 and h < len(text_low) and text_low[l] == text_low[h]: #in bound
            if h - l > max_l:
                result = (l,h+1)
                max_l = h-l
            l -= 1
            h += 1
    return result


def longest_subpalindrome_slice_slow(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    result = (0,0)
    longest = 0
    for i in range(0,len(text)):
        for j in range(i+1, len(text)+1):
            subtext = text[i:j]
            if is_palindrome(subtext) and len(subtext) > longest:
                result = (i, j)
                longest = len(subtext)
    return result

def is_palindrome(text):
    "Return true if text is a palindrome"
    text_low = text.lower()
    return text_low == text_low[::-1]


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print (test())