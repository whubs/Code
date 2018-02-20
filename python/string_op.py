#! /usr/bin/python

format = "Hello, %s. %s enough for ya?";
values = ('world', 'Hot');
print format % values;
print '\n';

format1 = "Pi with three decimals: %.3f";
from math import pi;
print format1 % pi;