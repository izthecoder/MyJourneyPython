'''
0) re module
1) Methods to search for matches & 2) Methods on a match object
import re

test_string = "123abc456789abc123ABC"

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string) #match(), search(), findall(), finditer()

#Another method 1 to write it:
#matches = re.finditer(test_string)

#obj.group(), obj.start(), obj.end(), obj.span()
for match in matches:
    #print(match)
    #print(match.span(), match.start(), match.end())
    print(match.group())

3) Meta characters
4) More special sequences
5) Sets
6) Quantifier
7) Conditions
8) Grouping
9) Modification
10) Compilation flags

Methods on a match:
match (): Determine if the RE matches at the beginning of the string.
search(): Scan through a string, looking for any location where this RE matches.
findall(): Find all substring where the RE matches, and returns them as a list.
finditer(): Find all substrings where the RE matches, and retruns them as an iterator.

Modification methods:

split(): Returns a list where the string has been split at each match
sub(): Replace one or many matches with a string

All meta characters: . ^ $ * + ? {} [] \ \ ()

. Any char (except newline char)
^ Starts with "^hello"
$ Ends with "world$"
* Zero or more occurrences "aix*"
+ One or more occurrences "aix+"
{} Exactly the specified number of occurrences "al{2}"
[] A set of chars "[a-m]"
\ Special sequence (or escape sepcial chars) "\d"
\ Either or "falls|stays"
() Capture and group

More special characters:

\d : Matches any decimal digit; [0-9].
\D : Matches any non-digit character;
\s : Matches any whitespace character; (space " ", tab "\t", newline "\n")
\S : Matches any non-whitespace character;
\w : Matches any alphnumeric (word) character; [a-zA_Z0-9].
\W : Matches any  non-alphanumeric character;
\b : Matches where the specified characters are at the beginning or at the end of a word
\B : Matches where the specified characters are present, but NOT at the beginning (or a word)
'''

