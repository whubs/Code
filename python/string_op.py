#! /usr/bin/python

format = "Hello, %s. %s enough for ya?";
values = ('world', 'Hot');
print format % values;
print '\n';

format1 = "Pi with three decimals: %.3f";
from math import pi;
print format1 % pi;
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