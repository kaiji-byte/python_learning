import logging, sys, re

# strip does 2 things:
# strips whitespace from the beginning and end of a string
# OR strips specified characters from the beginning and end of a string (do character class, not pattern)
#
#
# Perhaps something like fr"{strip_pattern}*(.*){strip_pattern}*"
# where strip_pattern -> str is the second argument of the function, with the first being the text to be striped.

# Configure output format and baseline threshold
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # To log to a file instead of stdout, uncomment:
    # filename="app.log", filemode="a"
)


# logging.disable(logging.CRITICAL)
#
#
#
#
#
#
def regex_strip(text, chars=None):
    if chars is None:
        char_class = r"\s"
    elif chars == "":
        return text
    else:
        char_class = re.escape(chars)
    pattern = rf"[{char_class}]*(.*?)[{char_class}]*"
    return re.fullmatch(pattern, text, re.DOTALL).group(1)
