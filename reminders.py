#!/usr/bin/env python3

import datetime
import email
import smtplib
import sys
import csv


def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("     send_reminders 'date|Meeting Title|Emails' ")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f"""
Hi {name}!

This is a quick reminder to you all that we have a meeting about:
'{title}'
the {weekday} {date}.

See you there.
""")
    return message


def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # create dictionary with key row[0], value row[1] - email and name
            names[row[0]] = row[1]
    return names


def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    # expensive operation outside the for loop
    names = read_names(contacts)
    for email in emails.split(','):
        name = names(email)
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Succesfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email with :{}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
