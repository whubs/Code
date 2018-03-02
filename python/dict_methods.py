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
print '\n';

# .fromkeys() method
print {}.fromkeys(['name', 'age']);

# But it's better
print dict.fromkeys(['name', 'age']);

# Or
print dict.fromkeys(['name', 'age'], '(unknown)');
print '\n';
# .get method
d = {};
print d.get('name');

# Or
# To use another default:
# print d.get('name', 'N/A');

# If a key is there, get works like ordinary dictionary lookup:
d['name'] = 'Eric';
print d.get('name');
print '\n';

# .has_keys()
d = {};
print d.has_keys('name');
d['name'] = 'Eric';
print d.has_keys('name');
print '\n';

# .items and .iteritems
# .items returns a list in which item is of the form (key,value)
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0};
print d.items();
print '\n';
# .iteritems returns an interator
it = d.iteritems();
print it;
print list(it); # Converts iterator into a list
print '\n';

# .keys and iterkeys works the same as above, except with keys instead of items

# .pop
d = {'x':1 , 'y':2};
print d.pop('x');
print d;
print '\n';

# .popitem
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0};
print d.popitem();
print d;
print '\n';

# .setdefault
d = {};
d.setdefault('name', 'N/A');
# OR
# d = {};
# print d.setdefault('name');
# None
# print d;
# {'name': None}
print d;
d['name'] = 'Gumby';
print d.setdefault('name', 'N/A');
print d;
print '\n';

# .update()
d = {
	'title': 'Python Web Stite',
	'url': 'http://www.python.org',
	'changed': 'Mar 14 22:09:15 MET 2008'
};

x = {'title': 'Python Language Website'};
d.update(x);
print d;
print '\n';

# .values and .itervaules
d = {};
d[1] = 1;
d[2] = 2;
d[3] = 3;
d[4] = 1;
print d.values();
