#! /usr/bin/python

# A simple database using get()

# Insert database  (people) from Listing 4-1 here.

labels = {
	'phone' = 'phone number',
	'addr' = 'address'
};

name = raw_input('Name: ');

# Are we looking for a phone number or an address
request = ('Phone number (p) or address (a)? ');

# Use correct key
key = request; # In case the request is neither 'p' not 'a'
if request == 'p': key = 'phone';
if request == 'a': key = 'addr';

# Use get to provide default values:
person = people.get(name, {});
label = labels.get(key, key);
result = person.get(key, 'not available');

print "%s's %s is %s." % (name, label, result);