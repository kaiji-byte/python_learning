import re, pyperclip, sys, logging

"""
TODO
    print out string that takes in rule phrases in accordance to strong or weak
"""


# Configure output format and baseline threshold
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # To log to a file instead of stdout, uncomment:
    # filename="app.log", filemode="a"
)
# logging.disable(logging.CRITICAL)

"""
strong psswd rules:
1. greater than or equal to 8 passwords
2. contains both upper and lower case chracters
3. has at least 1 digit

Do regex rules for each condition, returning a boolean for each one.

Use booleans to determine if psswd is strong or not.
    If not strong, say so and have user enter in new one.

Set up option to copy inputted in psswd to clipboard.

"""
logging.info("test")


# function determines if password is 8 characters or not; returns a boolean and phrase
def has8chr(text):
    isPattern = re.compile(r".{8,}")
    return {"boolean": bool(isPattern.search(text)), "phrase": "8 or more characters"}


# function determines if password has upper & lower letters or not; returns a boolean and phrase
def hasUpperAndLower(text):
    isPattern = re.compile(r"([A-Z]{1}.*[a-z]{1})|([a-z]{1}.*[A-Z]{1})")
    return {
        "boolean": bool(isPattern.search(text)),
        "phrase": "both uppercase and lowercase characters",
    }


# function determines if password has digits or not; returns a boolean and phrase
def hasDigit(text):
    isPattern = re.compile(r"\d+")
    return {"boolean": bool(isPattern.search(text)), "phrase": "one or more digits"}


# function sorts which rules pass the test and which rules don't
def sortWeakOrStrong(listToSort):
    strongList = []
    weakList = []
    for i in listToSort:
        if i["boolean"]:
            strongList.append(i["phrase"])
        else:
            weakList.append(i["phrase"])
    return {"strongList": strongList, "weakList": weakList}


while True:
    userInputText = input("Please enter in a strong password:\n")

    has8chrResult = has8chr(userInputText)
    hasUpperAndLowerResult = hasUpperAndLower(userInputText)
    hasDigitResult = hasDigit(userInputText)
    listToSort = [has8chrResult, hasUpperAndLowerResult, hasDigitResult]

    if (
        has8chrResult["boolean"]
        and hasUpperAndLowerResult["boolean"]
        and hasDigitResult["boolean"]
    ):
        print("Your password is strong! Would you like to copy it to the clipboard?")
        while True:
            userInputChoice = input("Y or N?\n").upper()
            if userInputChoice == "Y":
                pyperclip.copy(userInputText)
                print(
                    "Your password has been copied to the clipboard! Thank you, have a good day."
                )
                sys.exit()
            elif userInputChoice == "N":
                print("Thank you, have a good day!")
                sys.exit()
            else:
                print("Please choose Y or N.")
    else:
        sortedList = sortWeakOrStrong(listToSort)
        print(f"""\
Your password is strong in: {", ".join(sortedList["strongList"])}
Your password is weak in: {", ".join(sortedList["weakList"])}""")
        """
        Strong List:
        Weak List:
        Sort it out into those 2

        Then put strong list and weak list into string. Perhaps two strings?

        Your password is strong in: {', '.join(strongList)}
        Your password is weak in: {', '.join(weakList)}

        """
