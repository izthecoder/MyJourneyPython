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

'''
Regex (Regular Expressions) Summary Notes:
1. Basics
Literal Characters: Matches exactly the same character in the text.
Example: a matches the character "a".

2. Metacharacters
. (Dot): Matches any single character except newline.
Example: a.b matches "aab", "a9b", etc.
^ (Caret): Asserts the start of a string.
Example: ^a matches "a" only if it is the first character.
$ (Dollar): Asserts the end of a string.
Example: a$ matches "a" only if it is the last character.

3. Character Classes
[abc]: Matches any one of the characters a, b, or c.
[^abc]: Matches any character not listed (negation).
[a-z]: Matches any lowercase letter.
[A-Z]: Matches any uppercase letter.
[0-9]: Matches any digit.
\d: Matches any digit (equivalent to [0-9]).
\D: Matches any non-digit character.
\w: Matches any word character (alphanumeric + underscore).
\W: Matches any non-word character.
\s: Matches any whitespace character (space, tab, newline).
\S: Matches any non-whitespace character.

4. Quantifiers
*: Matches 0 or more occurrences of the preceding element.
Example: a* matches "", "a", "aa", etc.
+: Matches 1 or more occurrences of the preceding element.
Example: a+ matches "a", "aa", "aaa", etc.
?: Matches 0 or 1 occurrence of the preceding element.
Example: a? matches "" or "a".
{n}: Matches exactly n occurrences.
Example: a{2} matches "aa".
{n,}: Matches n or more occurrences.
Example: a{2,} matches "aa", "aaa", etc.
{n,m}: Matches between n and m occurrences.
Example: a{2,4} matches "aa", "aaa", "aaaa".

5. Groups and Alternation
(abc): Groups multiple characters together.
|: Acts as an OR operator.
Example: a|b matches "a" or "b".

6. Escaping Special Characters
****: Used to escape special characters.
Example: \., \*, \\ to match ".", "*", and "" respectively.

7. Anchors
^: Start of string.
$: End of string.

8. Lookahead and Lookbehind (Advanced)
(?=...): Positive lookahead assertion.
(?!...): Negative lookahead assertion.
(?<=...): Positive lookbehind assertion.
(?<!...): Negative lookbehind assertion.

Common Examples:
Email: ^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
Phone Number: ^\d{3}-\d{3}-\d{4}$ (US format)
URL: ^https?://[^\s/$.?#].[^\s]*$

Usage Tips:
Test regex with tools like regex101.com.
Use raw strings in Python (e.g., r'\d+') to avoid escaping backslashes.
'''
