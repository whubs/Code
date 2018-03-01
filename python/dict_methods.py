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
