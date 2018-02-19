#! /usr/bin/python

tag = '<a href = "http://www.python.org">Python web sites</a>';
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print "\n";
print tag[0:33];
print tag[32:-1];
print "\n";
print numbers[3:6];
print numbers[0:1];
print "\n";
# A nifty shortcut to access the last 3 elements
# Method 1:
print numbers[7:10];
# Method 2 (only shows [8,9]):
print numbers[-3:-1];
# Method 3 (shows []):
print numbers[-3:0];
# Method 4 (shows [8,9,10]) which fulfills the purpose:
print numbers[-3:];
# The same thing works from the beginning
print numbers[:3];
# To copy the entire sequence, leave both indices
print numbers[:];