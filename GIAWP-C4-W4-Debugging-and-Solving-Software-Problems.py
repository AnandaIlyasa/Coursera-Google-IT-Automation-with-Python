#!/usr/bin/env python3


import csv
import datetime
import requests
from operator import itemgetter

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer():
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    date_employees_dict = {}

    for row in reader:
        row_firstname = row[0]
        row_lastname = row[1]
        row_date = row[3]
        employees = date_employees_dict.get(row_date)
        if employees != None:
            date_employees_dict[row_date] = employees.append("{} {}".format(row_firstname, row_lastname))
        else:
            date_employees_dict[row_date] = ["{} {}".format(row_firstname, row_lastname)]

    return date_employees_dict

def list_newer(start_date):
    date_employees_dict = get_same_or_newer()
    while start_date < datetime.datetime.today():
        start_date_str = start_date.strftime("%Y-%m-%d")
        employees = date_employees_dict.get(start_date_str)

        if employees != None:
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
