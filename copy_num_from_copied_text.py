import pyperclip, sys

"""
Copy text from clipboard, find phone num, present as a list of options by list of ints, copy phone num to clipboard..
"""


def isPhoneNumber(maybe_phone_num):  # returns a list of a boolean and perhaps a value
    maybe_phone_num = list(maybe_phone_num)
    """
    maybe_phone_num = (
        "".join(
            "".join("".join("".join(maybe_phone_num).split("-")).split("(")).split(")")
        ).split()
    )  # this mess splits the string apart, with the joins ensuring the splits can work
    #This snippet of code is obsolete, kept around only for reference purposes
    """
    ints_of_maybe_phone_num = []
    for i in range(
        len(maybe_phone_num)
    ):  # effectively strips down maybe_phone_num to its integers and saves result
        if maybe_phone_num[i].isdecimal():
            ints_of_maybe_phone_num.append(maybe_phone_num[i])
    str_maybe_phone_num = "".join(ints_of_maybe_phone_num)
    try:
        if (
            len(str_maybe_phone_num) == 10
        ):  # tests if phone num has right amount of numbers
            list_maybe_phone_num = list(str_maybe_phone_num)
            for i in [3, 7]:  # formats phone num properly
                list_maybe_phone_num.insert(i, "-")
            final_phone_num = "".join(list_maybe_phone_num)
            return [True, final_phone_num]
        else:
            return [False]
    except Exception:  # noqa: BLE001
        return [False]


def text_scanner(text_to_scan):
    phone_list = []
    i = 0
    while (
        i <= len(text_to_scan)
    ):  # creates essentially a scanning window 14 characters wide that evaluates whether text is a phone number or not.
        segment = text_to_scan[i : i + 14]
        isPhone_result = isPhoneNumber(segment)
        if isPhone_result[0]:
            phone_list.append(isPhone_result[1])
            i += 10
        else:
            i += 1
    return phone_list


while True:
    user_or_clip = input(
        "Input text from user (1) or input text from clipboard (2)? (All results will be copied to clipboard)\nChoose (1) or (2): "
    )
    if not user_or_clip in ["1", "2"]:
        print("Unrecognized input. Please enter in (1) or (2).\n")
        continue
    break

# Perhaps later add an option to associate names with the phone numbers? Also choose to copy all presented phone numbers at once?

if user_or_clip == "1":
    result = text_scanner(input("Please enter text to be scanned here:\n"))
    if result == []:
        sys.exit("No phone numbers found. Exiting...")
    len_of_result = []
    print("Please choose a phone number to be copied.")
    for i in range(len(result)):
        print(f"({i + 1}) | {result[i]}")
        len_of_result.append(str(i + 1))
    while True:
        user_phone_choice = input("Choose a number: ")
        if not user_phone_choice in len_of_result:
            print("Please choose an actually listed number.")
            continue
        break
    user_phone_choice = int(user_phone_choice) - 1
    pyperclip.copy(result[user_phone_choice])
    text_scanner(pyperclip.paste())

if user_or_clip == "2":
    result = text_scanner(pyperclip.paste())
    if result == []:
        sys.exit("No phone numbers found. Exiting...")
    len_of_result = []
    print("Please choose a phone number to be copied.")
    for i in range(len(result)):
        print(f"({i + 1}) | {result[i]}")
        len_of_result.append(str(i + 1))
    while True:
        user_phone_choice = input("Choose a number: ")
        if not user_phone_choice in len_of_result:
            print("Please choose an actually listed number.")
            continue
        break
    user_phone_choice = int(user_phone_choice) - 1
    pyperclip.copy(result[user_phone_choice])
    text_scanner(pyperclip.paste())


"""
    block of code for testing purposes
print(
    text_scanner(
        "heyfhdji32jhgh3454hdfsfh412-345-2345hfhghgjkjhfhf535-453-3354dksfjkdjsf8474jf83hf74hgf927dfhf74g(123) 324 1345sdajfhdshfkashdfk"
    )
)

print(isPhoneNumber("-341-343-1241"))

"""
