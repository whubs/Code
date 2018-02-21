#! /usr/bin/python

format = "Hello, %s. %s enough for ya?";
values = ('world', 'Hot');
print format % values;
print '\n';

format1 = "Pi with three decimals: %.3f";
from math import pi;
print format1 % pi;
print '\n';

print '%s plus %s equals %s' % (1, 1, 2);
print '\n';

# ## TEMPLATE STRINGS ## #

from string import Template;
s = Template('$x, glorious $x');
print s.substitute(x = 'slurm');
print '\n';

# Replacing part of a word

s = Template("It's ${x}tastic!");
print s.substitute(x = 'slurm');
print '\n';

# To use a dolar sign

s = Template("Make $$ selling $x!");
print s.substitute(x = 'slurm');
print '\n';

# Supply the value-name pairs in a dictionary

s = Template('A $thing must never $action.');
d = {};
d['thing'] = 'gentlemen';
d['action'] = 'show his socks';
print d;
print s.substitute(d);
print '\n';

# Conversion # some examples

print 'Price of eggs: $%d' % 42;
print 'Hexadecimal price of eggs: %x' % 42;
print 'Pi: %f...' % pi;
print 'Very inexact estimate of pi: %i' % 42;
print 'Using str: %s' % 42L;
print 'Using repr: %r' % 42L;
print '\n';

# Width and Precision

print '%10f' % pi; # Field width 10
print '%10.2f' % pi; # Field width 10, precision 2
print '%.2f' % pi; # Precision 2
print '%.5s' % 'Guido van Rossum';
print '%.*s' % (5, 'Guido van Rossum'); # I can link the width with an asterisk (*) via tuple argument
print '\n';

# Signs, alignment, and Zero-padding
print '%010.2f' % pi; # Field width 10, precision 2 with 0 padding on pi's right
print '%-10.2f' % pi; # Left-aligns the value
print '\n';
print ('% 5d' % 10) + '\n' + ('% 5d' % -10);
print '\n';
print ('%+5d' % 10) + '\n' + ('%+5d' % -10);