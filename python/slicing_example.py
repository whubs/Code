#! /usr/bin/python

# Split up a URL of the form http://something.com

url = raw_input('Please enter the URL: ');
domain = url[11:-4];

print "Domain name: " + domain;