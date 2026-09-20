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

