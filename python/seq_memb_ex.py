#! /usr/bin/python

# Check a user name and PIN code

database = [
	['albert', '1234'],
	['dilbert', '4242'],
	['smith', '0101'],
	['jones', '5555']
];

username = raw_input('User name: ');
pin = raw_input('PIN code: ');

if [username, pin] in database: print 'Access granted';