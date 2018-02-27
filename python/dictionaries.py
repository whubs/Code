# /usr/bin/python

# Dictionaries

# Works but impractical
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl'];
numbers = ['2341', '9102', '3158', '0142', '5551'];
print numbers[names.index('Cecil')];

# Creating and using dictionaries
phonebook = {'Alice': '2341', 'Beth':'9102', 'Cecil':'3158', 'Dee-Dee':'0142', 'Earl':'5551'};

# dict Function
items = [('name', 'Gumby'), ('age', 42)];
d = dict(items);
print d;
print d['name'];
print '\n';
# OR
# d = dict(name = 'Gumby', age = 42);
# print d;

# len(d);
# d[k];
# d[k] = v;
# del d[k];
# k in d;
print "Cecil's phone number is %(Cecil)s." % phonebook;