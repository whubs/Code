#! /usr/bin/python

# In IDE

#>>permissions = 'rw';
#>>'w' in permissions;
#>>'x' in permissions;
#>>users = ['mlh', 'foo', 'bar'];
#>>raw_input('Enter your user name: ') in users;

#>>subject = '$$$ Get rich now!!! $$$'
#>>'$$$' in subject;

# Actual program

permissions = 'rw';
users = ['mlh', 'foo', 'bar'];
subject = '$$$ Get rich now!!! $$$';
print '\n';

if 'w' in permissions: print 'True';
else: print 'False';
if 'p' in permissions: print 'True';
else: print 'False';
print'\n';

a = raw_input('Enter your user name: ');
if a in users: print 'True';
else: print 'False'
print '\n';

if '$$$' in subject: print 'True';
else: print 'False';