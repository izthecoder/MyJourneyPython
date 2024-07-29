import re

''' 1) Write a Python program to check that a string 
contains only a certain set of characters 
(in this case a-z, A-Z and 0-9) .'''

def is_allowed_specific_char(string):
    chaRe = re.compile(r'[^a-zA-Z0-9.]')
    string = chaRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

'''2) matches a string that has an 
a followed by zero or more b's'''

import re
def text_match(text):
    patterns = 'ab*?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched')


print(text_match("bc"))
print(text_match("abc"))
print(text_match("abbc"))

''' 3) matches a string that has an a 
followed by one or more b's'''

import re
def text_match(text):
    pattern = 'ab+?'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not Match'

print(text_match("abc"))

'''4) matches a string that has an a followed
by zero or more b'''

import re

def text_match(text):
    pattern = 'ab?'
    if re.search(pattern, text):
        return 'Found a match'
    else:
        return 'Not matched'

print(text_match("acd"))

'''5)matches a string that has
an a followed by three b'''

import re

def text_match(text):
    pattern = 'ab{3}'
    if re.search(pattern, text):
        return 'A mathced!'
    else:
        return 'Not a match.'

print(text_match("abbb"))