#Project:-Extract Contact Information from Large Documnets

"""Say you’ve been given the boring task of finding every phone number and email address in a long web page or document. 
If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses,
 you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds."""

#so for this we have to 
#1.Get the text from the clipboard
#2.Find all phone numbers and the email adress from the text
#3.paste them on the clipboard

#using pyperclip module for pasting the text
#create 2 regex for matching phone numbers and emails
#we have to find all the matches(not just one kind of match)
#neatly have to format matching strings into a single string to paste
#Display some kind of message if no matches found in the text

#using pyperclip module for pasting the text
import pyperclip, re
#create 2 regex for matching phone numbers and emails
phone=re.compile(r'''
    (\d{3}|\(\d{3}\))? #
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?
    ''',re.VERBOSE)
email=re.compile(r'''
    [a-zA-Z0-9._%+-]+ #username
    @ #Symbol
    [a-zA-Z0-9.-]+ #Domainname
    (?:\.[a-zA-Z]{2,4}) #dot-matching
''',re.VERBOSE)

text=pyperclip.paste()
#we have to find all the matches(not just one kind of match)
matches=[]
for groups in phone.findall(text):
    phonenum='-'.join([groups[0],groups[2],groups[4]])
    if groups[6]!="":
        phonenum+=" x"+groups[6]
    matches.append(phonenum)
for address in email.findall(text):
    matches.append(address)

#neatly have to format matching strings into a single string to paste
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard: ')
    print('\n'.join(matches))
#Display some kind of message if no matches found in the text
else:
    print('No phone number or email address found')
    