#! /usr/bin/python

# string.digits: A string containing the digits 0-9
# string.letters: A string containing all letters (uppercase and lowercase)
# string.lowercase: A string containing all lowercase
# string.printable: A string containing all printable characters
# string.punctuation: A string containing al ponctuation characters
# string.uppercase: A string containing all uppercase letters

# .find('');
print 'With a moo-moo here, and a moo-moo there'.find('moo');
title = "Monty Python's Flying Circus";
print title.find('Monty');
print title.find('Python');
print title.find('Flying');
print title.find('Zirqus');
print '\n';

subject = '$$$ Get rich now!!! $$$';
print subject.find('$$$');
print subject.find('$$$', 1); # Only supplying the start
print subject.find('!!!');
print subject.find('!!!', 1, 16);
print '\n';

# .join
seq = ['1', '2', '3', '4', '5', '6']; # Doesn't work if [1, 2, ...] because it's a list of numbers
sep = '+';
print sep.join(seq); # Joining a list of strings
dirs = '','usr','bin','env';
print '/'.join(dirs);
print 'C:' + '\\'.join(dirs);
print '\n';

# .lower
print 'Trondheim Hammer Dance'.lower();
# >>>if 'Gumby' in ['gumby', 'smith', 'jones']: print 'Found it!'
# >>>
name = 'Gumby';
names =  ['gumby', 'smith', 'jones'];
if name.lower() in names: print 'Found it!';
print '\n';

# .title()
print "that's all, folks!".title();
# OR
import string
print string.capwords("that's all, folks!");
print '\n';

# .replace()
print 'This is a test'.replace('is', 'eez');
print '\n';

# .split()
print '1+2+3+4+5'.split('+');
print '/usr/bin/env'.split('/');
print 'Using the default'.split();
print '\n';

# .strip() works a bit like .lower()
names =  ['gumby', 'smith', 'jones'];
name = 'gumby ';
# >>>if name in names: print 'Found it!'
# >>>
if name.strip() in names: print 'Found it!';
print '**** SPAM * for * everyone!!! ***'.strip(' *!');
print '\n';

# .translate() works a bit like .replace
from string import maketrans;
table = maketrans('cs','kz');
print len(table);
print table[:];
print table[97:123];
print maketrans('', '')[97:123];
print '\n';

print 'this is an incredible test'.translate(table);
# the next example contains a second parameter, it represents the element that should be deleted
print 'this is an incredible test'.translate(table, ' ');