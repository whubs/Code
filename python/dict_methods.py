# /usr/bin/python

# Dictionary Methods

# .clear() method

d = {};
d['name'] = 'Gumby';
d['age'] = 42;
print d;

returned_value = d.clear();
print d;
print '\n';

# Why is this useful?
# Here's why, scenario 1:
x = {};
y = x;
x['key'] = 'value';
print y;
x = {};
print y;
# Returns {'key': 'value'}
print '\n';

# Scenario 2:
x = {};
y = x;
x['key'] = 'value';
print y;
x.clear()
print y;
# Returns {}
print '\n';

# .copy() method

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']};
y = x.copy();
y['username'] = 'mlh';
y['machines'].remove('bar');
print y;
print x;

#  When you replace a value in the copy, the original is unaffected.
# However, If i modify a value (instead of replacing it),
# the original is also affected. (for example the list in both y and x),
# one way to avoid this is to use deepcopy function from the copy module

from copy import deepcopy
d = {};
d['names'] = ['Alfred', 'Bertrand'];
c = d.copy();
dc = deepcopy(d);
d['names'].append('Clive');
print d;
print c;
print dc;