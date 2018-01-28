"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice


"""
from collections import Counter

def duplicate_count(text):
    q = 0
    for i in Counter(text.lower()).values():
        if i > 1:
            q += 1
    return q




def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)

test.assert_equals(duplicate_count(string.lowercase), 0)
test.assert_equals(duplicate_count(string.lowercase + "aaAb"), 2)

test.assert_equals(duplicate_count(string.lowercase+string.lowercase), 26)
test.assert_equals(duplicate_count(string.lowercase+string.uppercase), 26)
