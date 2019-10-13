# Shauna Byrne
# 13/10/2019

#Code adapted from Lab03 Webscraping instructions given by Andrew Beatty - GMIT - Computing & Data Analytics 2019

import csv

employee_file = open('employee_file.csv', mode="w")
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['John Smith', 'Account', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

employee_file.close()