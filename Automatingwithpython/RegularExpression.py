"""Regular expressions, called regexes for short, are a sort of mini language that describes a pattern of text. For example, the characters \d in a regex stand for a decimal numeral between 0 and 9. Python uses the regex string r'\d\d\d-\d\d\d-\d\d\d\d' to match the same text pattern the previous is_phone_number() function did: a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. Any other string would not match the r'\d\d\d-\d\d\d-\d\d\d\d' regex.

Regular expressions can be much more sophisticated than this one. For example, adding a numeral, such as 3, in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.” So the slightly shorter regex r'\d{3}-\d{3}-\d{4}' also matches the phone number pattern.

Note that we often write regex strings as raw strings, with the r prefix. This is useful, as regex strings often have backslashes. Without using raw strings, we would have to enter expressions such as '\\d'."""

#Import the re module.
#Pass the regex string to re.compile() to get a Pattern object.
# Pass the text string to the Pattern object’s search() method to get a Match object.
#Call the Match object’s group() method to get the string of the matched text.

import re
phone_num_patter_obj=re.compile(r'\d{3}-\d{3}-\d{3}')
match_obj=phone_num_patter_obj.search('My number is 415-555-4242')
print(match_obj.group())

"""Grouping with Parentheses
Say you want to separate one smaller part of the matched text, such as the area code, from the rest of the phone number (to, for example, perform some operation on it). Adding parentheses will create groups in the regex string: r'(\d\d\d)-(\d\d\d-\d\d\d\d)'. Then, you can use the group() method of Match objects to grab the matching text from just one group.

The first set of parentheses in a regex string will be group 1. The second set will be group 2. By passing the integer 1 or 2 to the group() method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text."""

phone=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo=phone.search('MY Number is 415-555-4242.')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

"""Using Escape Characters
Parentheses create groups in regular expressions and are not interpreted as part of the text pattern. So, what do you do if you need to match a parenthesis in your text? For instance, maybe the phone numbers you are trying to match have the area code set in parentheses: '(415) 555-4242'.

In this case, you need to escape the (and) characters with a backslash. The \(and \) escaped parentheses will be interpreted as part of the pattern you are matching"""

pattern=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d)')
mo=pattern.search("My phone number is (415) 555-4242")
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
print(mo.group())

"""Matching Characters from Alternate Groups
The | character is called a pipe, and it’s used as the alternation operator in regular expressions. You can use it anywhere you want to match one of multiple expressions. For example, the regular expression r'Cat|Dog' will match either 'Cat' or 'Dog'.

You can also use the pipe to match one of several patterns as part of your regex. For example, say you wanted to match any of the strings 'Caterpillar', 'Catastrophe', 'Catch', or 'Category'. Since all of these strings start with Cat, it would be nice if you could specify that prefix only once. You can do this by using the pipe within parentheses to separate the possible suffixes."""

pattern=re.compile(r'cat(egory|ch|astrophe|egory)')
mo=pattern.search('catch me if you can')
print(mo.group())
print(mo.group(1))

"""Returning All Matches
In addition to a search() method, Pattern objects have a findall() method. While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string.

There is one detail you need to keep in mind when using findall(). The method returns a list of strings as long as there are no groups in the regular expression. """

import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
print(pattern.findall('Cell : 415-555-9999 Work : 212-555-0000'))
pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#Also keep in mind that findall() doesn’t overlap matches. For example, matching three numbers with the regex string r'\d{3}' matches the first three numbers in '1234' but not the last three:
pattern=re.compile(r'\d{3}')
print(pattern.findall('1234'))
print(pattern.findall('123456'))

# Regular Expressions are split into two parts: the qualifiers that dictate
# what characters you are trying to match by the quantifiers that dictate how many characters you are trying to match
# in r'\d{3}-\d{3}-\d{4}' in which r'\d' and '-' are qualifiers and {3} and {4} are called quantifiers.

"""Using Character Classes and Negative Character Classes
Although you can define a single character to match, as we’ve done in the previous examples, you can also define a set of characters to match inside square brackets. This set is called a character class. For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase. It’s the equivalent of writing a|e|i|o|u|A|E|I|O|U, but it’s easier to type"""

vowel_pattern=re.compile(r'[aeiouAEIOU]')
print(vowel_pattern.findall('Robocop eats baby Food'))
#You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

#By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.
constant_pattern=re.compile(r'[^aeiouAEIOU]')
print(constant_pattern.findall('RoboCop eats Baby food'))

#using shorthand character classes
#\d  Any numeric digit from 0 to 9
#\D Any character that is not a numeric digit from 0 to 9
#\w Any letter, numeric digit,or the underscore character.
#\W Any character that is not a letter,numeric digit,or the underscore character
#\s Any space,tab, or newline character
#\S Any character thatb is not a space,tab, or newline character
pattern=re.compile(r'\d+\s\w+')
print(pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)

# #Matching Everything with the Dot Character
# The . (or dot) character in a regular expression string matches any character except for a newline.
#Remember that the dot character will match just one character, which is why the text flat in the previous example matched only lat. To match an actual period, escape the dot with a backslash: \.
atre=re.compile(r'.at')
print(atre.findall('The cat in the hat sat on the flat mat'))

# #Matching an Optional Pattern
# Sometimes you may want to match a pattern only optionally. That is, the regex should match zero or one of the preceding qualifiers. The ? character flags the preceding qualifier as optional.
pattern=re.compile(r'42!?')
print(pattern.search('42!'))
print(pattern.search('42'))
#in this example ? part of regualr expression means that the pattern ! is optional.so it matches both 42!(with the exclamation mark) and 42(without it).

# #Matching Zero or More Qualifiers
# The * (called the star or asterisk) means “match zero or more.” In other words, the qualifier that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again.

pattern=re.compile(r'Eggs( and spam)*')
print(pattern.search('Eggs'))
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))

#while * means 'match zero or more',the + means 'match one or more'
pattern=re.compile(r'Eggs( and spam)+')
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))

#Matching a Specific Number of Qualifiers
#(Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances. Curly brackets can help make your regular expressions shorter
haregex=re.compile(r'(ha){3}')
print(haregex.search('hahahaha'))
print(haregex.search('haha'))

#Greedy and Non-greedy Matching
#Because (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous curly bracket example returns 'HaHaHaHaHa' instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.
#python regular expressions are greedy 9n nature,which means that in ambigous situations,they will try to match the longest possible string 
greedy=re.compile(r'(ha){3,5}')
print(greedy.search('hahahahaha'))

lazy=re.compile(r'(ha){3,5}')
print(lazy.search('hahahahaha'))
#Because it is lazy, it matches the fewest repetitions possible to satisfy the regex condition. Since the minimum required repetition is 3, it stops as soon as it finds 3 matches of 'Ha', returning 'HaHaHa'.

#ou can use the dot-star (.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”
namepattern=re.compile(r'First Name: (.*) Last Name: (.*)')
namematch=namepattern.search('First Name: Ai Last Name: Sweigert')
print(namematch.group())
print(namematch.group(1))
print(namematch.group(2))
print(namematch.groups())
#(.*) is a greedy mode which gives the max possible value
#(.*?) is a lazy mode which uses lesser possible length
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
print(match1.group())
greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
print(match2.group())

#The dot in .* will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.\
newline=re.compile(r'.*',re.DOTALL)
print(newline.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

#You can use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate that the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.
begins=re.compile(r'^Hello')
print(begins.search('Hello World!').group())

#The r'\d$' regular expression string matches strings that end with a numeric character between 0 and 9. 
endswithnumber=re.compile(r'\d$')
print(endswithnumber.search('Your number is 42').group())
#The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters.
wholestring=re.compile(r'^\d+$')
print(wholestring.search('123456789').group())

#Use \b when you want to match a specific word but avoid matching it when it is inside a larger word.
pattern=re.compile(r'\bcat.*?\b')
print(pattern.findall('The cat was found a catapult catalog in a catacombs.'))
#Use \B when you want to find a pattern only when it is embedded inside another word, preventing it from matching as a standalone word.
pattern = re.compile(r'\Bcat\B')
print(pattern.findall('certificate')) #Match
print(pattern.findall('catastrophe')) #No Match

#Case Insenesitive matching-use re.I or re.IGNORECASE as a second argument in re.compile
pattern=re.compile(r'robocop',re.I)
print(pattern.search('RoboCop is a part machine, all cop.').group())

# Substituting Strings
# Regular expressions don’t merely find text patterns; they can also substitute new text in place of those patterns. The sub() method for Pattern 
# objects accepts two arguments. The first is a string that should replace any matches. The second is the string of the regular expression. The sub() method returns a string with the substitutions applied.
agentpattern=re.compile(r'Agent \w+')
print(agentpattern.sub('CENSORED','Agent Alice contacted Agent Bob'))
agent_pattern = re.compile(r'Agent (\w)\w*')
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.'))
#The \1 in the regular expression string is replaced by whatever text was matched by group 1—that is, the (\w) group of the regular expression.
#re.VERBOSE is used to write complex regex in multiple lines which is easy to understand

#For simple regex it will be simple but for complex regex we have to write it in multiple lines for that we have to use ''' quotes which makes the regex written in multiple lines
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)

"""Humre: A Module for Human-Readable Regexes
Code is read far more often than it’s written, so it’s important for your code to be readable. 
But the punctuation-dense syntax of regular expressions can be hard for even experienced programmers to read.
To solve this, the third-party Humre Python module takes the good ideas of verbose mode even further by using human-readable, plain-English names to create readable regex code."""
from humre import *
phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
print(phone_regex)
#Humre’s constants (like DIGIT) contain strings, and Humre’s functions (like exactly()) return strings. Humre doesn’t replace the re module. Rather, it produces regex strings that can be passed to re.compile():
# Humre has constants and functions for each feature of regular expression syntax. You can then concatenate the constants and returned strings like any other string. For example, here are Humre’s constants for the shorthand character classes:

# DIGIT and NONDIGIT represent r'\d' and r'\D', respectively.
# WORD and NONWORD represent r'\w' and r'\W', respectively.
# WHITESPACE and NONWHITESPACE represent r'\s' and r'\S', respectively.

#once look at this and research about it
import re
from humre import *
phone_regex = group(
    optional_group(either(exactly(3, DIGIT),  # Area code
                          OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN)),
    optional(group_either(WHITESPACE, '-', PERIOD)),  # Separator
    group(exactly(3, DIGIT)),  # First three digits
    group_either(WHITESPACE, '-', PERIOD),  # Separator
    group(exactly(4, DIGIT)),  # Last four digits
    optional_group(  # Extension
      zero_or_more(WHITESPACE),
      group_either('ext', 'x', r'ext\.'),
      zero_or_more(WHITESPACE),
      group(between(2, 5, DIGIT))
      )
    )

pattern = re.compile(phone_regex)
match = pattern.search('My number is 415-555-1212.')
print(match.group())
