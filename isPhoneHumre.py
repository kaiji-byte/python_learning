import re
from humre import *

phone_regex = group(
    optional_group(
        either(
            exactly(3, DIGIT),  # Area code
            OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN,
        )
    ),
    optional(group_either(WHITESPACE, "-", PERIOD)),  # Separator
    group(exactly(3, DIGIT)),  # First three digits
    group_either(WHITESPACE, "-", PERIOD),  # Separator
    group(exactly(4, DIGIT)),  # Last four digits
    optional_group(  # Extension
        zero_or_more(WHITESPACE),
        group_either("ext", "x", r"ext\."),
        zero_or_more(WHITESPACE),
        group(between(2, 5, DIGIT)),
    ),
)

pattern = re.compile(phone_regex)
match = pattern.search("My number is 415-555-1212.")
print(match.group())
