import re


def compare_strings(string1, string2):
  # Convert both strings to lowercase
  # and remove leading and trailing blanks
  string1 = string1.strip().lower()
  string2 = string2.strip().lower()

  # Ignore everything that isn't a word or a whitespace
  string1 = re.sub(r"[^\w\s]", r"", string1)
  string2 = re.sub(r"[^\w\s]", r"", string2)

  # DEBUG CODE GOES HERE
  print(string1, string2)
  # print(n_string1, n_string2)

  return string1 == string2
