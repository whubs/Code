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