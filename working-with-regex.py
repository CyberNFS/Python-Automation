#!/usr/bin/env python3
import csv
import re


def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
  d_pattern = r'[\w\.-]+@' + domain + '$'
  if re.match(d_pattern, address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in
    the received address."""
  o_pattern = r'' + old_domain + '$'
  address = re.sub(o_pattern, new_domain, address)
  return address


def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  old_domain, new_domain = 'someolddmain.edu', 'newdomain.edu'
  csvloc = '/home/data/user_emails.csv'
  report = '/home/data/updated_user_emails.csv'
# this might be useremails - users
  useremails = []
  old_emails = []
  new_emails = []
  with open(csvloc, 'r') as f:
    userdata = list(csv.reader(f))
    useremails = [data[1].strip() for data in userdata[1:]]
    for emails in useremails:
      if contains_domain(emails, old_domain):
        old_emails.append(emails)
        re_emails = replace_domain(emails, old_domain, new_domain)
        new_emails.append(re_emails)
    ekey = ' ' + 'Email Address'
    endex = userdata[0].index(ekey)
    for user in userdata[1:]:
      for old_domain, new_domain in zip(old_emails, new_emails):
        if user[endex] == ' ' + old_domain:
          user[endex] = ' ' + new_domain
  with open(report, 'w+') as out:
    writer = csv.writer(out)
    writer.writerows(userdata)


main()
