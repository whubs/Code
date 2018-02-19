#! /usr/bin/python
# Print out a date, given year, month, and day as numbers

months = [
'January', 
'February', 
'March', 
'April', 
'May', 
'June', 
'July', 
'August', 
'September', 
'October', 
'November', 
'December'
];

# A list with one ending for each number from 1 to 31

f3 = ['st', 'nd', 'rd'];
th = ['th'];
f1 = ['st'];

endings = f3 + 17 * th + f3 + 7 * th + f1;

year = raw_input('Year: ');
month = raw_input('Month (1-12): ');
day = raw_input('Day (1-31): ');

month_num = int(month);
day_num = int(day);

# Subtract 1 from month and day to get a correct index

month_name = months[month_num - 1];
day_end = day + endings[day_num - 1];

print month_name + ' ' + day_end + ', ' + year;
