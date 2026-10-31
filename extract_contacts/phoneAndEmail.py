import pyperclip, re

phone_re = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )""",
    re.VERBOSE,
)

# DONE: Create email regex.
#    Parts of an email
#    foo
#    @
#    bar
email_re = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+  # Username
    @  # @ symbol
    [a-zA-Z0-9.-]+  # Domain name
    (\.[a-zA-Z]{2,4})  # Dot-something
    )""",
    re.VERBOSE,
)


# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(
    text
):  # loops and enumerates through groups in pattern-matched text
    phone_num = "-".join([groups[1], groups[3], groups[5]])  # formats phone numbers
    if groups[6] != "":
        phone_num += " x" + groups[6]
    matches.append(phone_num)  # adds phones to matches list
for groups in email_re.findall(text):
    matches.append(groups[0])  # adds emails to matches list


# TODO: Copy results to the clipboard.
# Do some formatting of results for clipboard

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
