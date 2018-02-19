#! /usr/bin/python

seq1 = [1, 2, 3];
seq2 = [4, 5, 6];
strng1 = 'Hello, ';
strng2 = 'world!';
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
print "\n";
# Longer Steps
# The third parameter shows the number of steps it moves from one element to the next
# Shows entire sequence one by one
print numbers[0:10:1];
# Shows sequence 2 by 2
print numbers[0:10:2];
# Shows sequence 3 by 3
print numbers[3:7:3];
# Shows entire sequence 4 steps at a time
print numbers[::4];
# The step can't be zero but it can be negative, meaning it extracts the elements from right to left
print numbers[8:3:-1];
print numbers[10:0:-2];
print numbers[0:10:-2];
print numbers[::-2];
print numbers[5::-2];
print numbers[:5:-2];
print '\n';
# Adding Sequences
print '[1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]'; 
print "\"Hello, \" + \"world!\" = \"Hello, world!\"";
# Next one gives an error, because you can't concatenate a list to a string
#print seq1 + strng1;
# Multiplication
print 'python' * 5;
print [42] * 10;