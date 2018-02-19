#! /usr/bin/python

# Changing Lists: Item Assignments
x = [1, 1, 1];
x[1] = 2;
print x;
print '\n';

# Deleting Elements
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl'];
del names[2];
print names;
print '\n';

# Assigning to Slices
n1 = list('Perl');
print n1;
n1[2:] = list('ar');
print n1;
print '\n';

n2 = list('Perl');
n2[1:] = list('ython');
print n2;
print'\n';

numbers = [1, 5];
print numbers[1:1];
numbers[1:1] = [2, 3, 4];
print numbers;
numbers[1:4] = [];
print numbers;