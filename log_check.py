#!/usr/bin/env python3

import re
import csv

errors = {}
users = {}

with open('somelogfile.log') as file:
  """context manager opens log file in read only mode"""
  for line in file:
    """looping through line by line in the log file"""
    user = re.compile(r"\((.*)\)")
    """compiling a match object for simpler usage"""
    if user.search(line):
      """Checking if there is a match for regular expression in the log files
      then .groups() unpacks the match object tuples or sets – no documentation found – and eventually adds them to a dictionary."""
      for user in user.search(line).groups():
        users[user] = users.get(user, 0) + 1

    error = re.compile(r"ERROR ([\w ']* )|INFO ([\w ']* )")
    """Similarly to above, but this case we have two case scenarios. One with ERROR and one with INFO
    so when we try to match them in the line, we will receive one None answer for each grouping so we will have to
    skip that line with a statement before appending the dictionary."""
    if error.search(line):
      for error in error.search(line).groups():
        if error != None:
          errors[error] = errors.get(error, 0) + 1

"""lambda function sorts the dictionary by items in descending order thanks to the reverse=True flag.
  Be careful, if not declared dict() it will return a list instead."""
users = dict(sorted(users.items()))
errors = dict(sorted(errors.items(), key=lambda item: item[1], reverse=True))

"""Using the %s we format all values to strings in a simple way and add them to the required csv file."""
with open('error_message.csv', 'w') as file:
  for key in errors.keys():
    file.write("%s, %s\n" % (key, errors[key]))

with open('user_statistics.csv', 'w') as file:
  for key in users.keys():
    file.write("%s, %s\n" % (key, users[key]))
