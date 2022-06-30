#!/usr/bin/env python3
import sys
import os
import re


def search(logs):
  """Reads and appends Error messages to a list, then returns it."""
  error = input("Error to look for: ")
  errors = []
  with open(logs, mode='r', encoding='UTF-8') as file:
    for log in file.readlines():
      epatterns = ['error']
      for i in range(len(error.split(' '))):
        epatterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(epattern, log.lower()) for epattern in epatterns):
        errors.append(log)
  return errors


def output(errors):
  """Creates a new log. Be careful, it rewrites it every single time the program runs.
  Maybe use append method within the context manager."""
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in errors:
      file.write(error)


if __name__ == "__main__":
  """Main function executes and runs the program."""
  logs = sys.argv[1]
  errors = search(logs)
  output(errors)
  sys.exit(0)
