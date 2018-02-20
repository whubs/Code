#! /usr/bin/python

# object.method(arguments)

# append

lst = [1, 2, 3];
lst.append(4);
print lst;
print '\n';

['to', 'be', 'or', 'not', 'to', 'be'].count('to')
x = [[1,2], 1, 1, [2, 1, [ 1, 2]]];
print x.count(1);
print x.count([1,2]);
print '\n';

# extend

a = [1, 2, 3];
b = [4, 5, 6];
a.extend(b);
print a;
print '\n';

# This would equivalent to:
# a = [int1, int2, int3]
# b = [int4, int5, int6]
# a = a + b
# print a

# OR

# a = [int1, int2, int3]
# b = [int4, int5, int6]
# a[len(a):] = b
# print a

#-------------------------

# index

knights = ['We', 'are', 'knights', 'who', 'say', 'ni'];
print knights.index('who');
print knights[3];
print '\n';

# insert

numbers = [1, 2, 3, 4, 5, 6, 7];
numbers.insert(3, 'four');
print numbers;
print '\n';

# As with extend, I can implement insert with slice assignment

# numbers = [1, 2, 3, 4, 5, 6, 7];
# numbers[3:3] = ['four'];
# print numbers;

# pop

x = [1, 2, 3];
print x.pop();
print x;
print x.pop(0);
print x;
print '\n';

# to reverse pop() use append()
# example:

x = [1, 2, 3];
x.append(x.pop());
print x;
print '\n';

# remove

x = ['to', 'be', 'or', 'not', 'to', 'be'];
x.remove('be');
print x;
print '\n';

# reverse

x = [1, 2, 3];
x.reverse();
print x;
print '\n';

# sort

x = [4, 6, 2, 1, 7, 9];
x.sort();
print x;

# DON'T DO
# x = [4, 6, 2, 1, 7, 9];
# y = x.sort();
# print y;
# None, because x.sort() doesn't return a value

# OR

# y = x;
# y.sort()
# print x;
# print y;
# y will be equal to x

# DO INSTEAD
# x = [4, 6, 2, 1, 7, 9];
# y = x[:];
# y.sort();
# print x;
# print y;

# OR

# x = [4, 6, 2, 1, 7, 9];
# y = sorted(x);
# print x;
# print y;

print sorted('Python');
print '\n';

# Advanced Sorting

print cmp(42, 32); # if x > y return a positive number
print cmp(99, 100); # if x < y return a negative number
print cmp(2, 2); # if x == y return 0
