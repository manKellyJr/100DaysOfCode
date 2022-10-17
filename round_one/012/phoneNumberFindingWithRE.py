import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
"""MO  is Matching Object variable"""
mo = phoneNumRegex.search('My number is 097-453-2178.')
print('Phone number found: ' + mo.group())

