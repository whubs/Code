#! /usr/bin/python

# string.digits: A string containing the digits 0-9
# string.letters: A string containing all letters (uppercase and lowercase)
# string.lowercase: A string containing all lowercase
# string.printable: A string containing all printable characters
# string.punctuation: A string containing al ponctuation characters
# string.uppercase: A string containing all uppercase letters

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