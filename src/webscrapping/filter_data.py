import datetime
import re


def find_nage(text: str):
    # Use a regular expression to find the distance and the swimming style
    match = re.search(r'(\d+)\s(.+?)\s', text)

    if match:
        # If a match was found, print the distance and the swimming style
        change = {"Nage":"NL",
                  "Dos":"DOS",
                  "Brasse":"BRASSE",
                  "Papillon":"PAP",
                  "4":"4N"}
        distance = match.group(1)
        swimming_style = match.group(2)
        swimming_style = change[swimming_style]
        return f"{distance} {swimming_style}"
    else:
        # If no match was found, print a message
        print('No match found.')


def remove_extra_spaces(text):
    """
    Removes all spaces from a given string, except those between words.

    Args:
        text (str): The string to remove spaces from.

    Returns:
        str: The string with extra spaces removed.
    """
    # Use a regular expression to remove all spaces except those between words
    return re.sub(r'\s(?=\s)|\s(?<=\s)', '', text)


def extract_city(text: str):
    """
    Extracts the city name from a given string.

    Args:
        text (str): The string to extract the city name from.

    Returns:
        str: The extracted city name, or 'No match found.' if no match was found.
    """
    # Use a regular expression to find the city name
    match = re.search(r'\((.*?)\)\s*([A-ZÀ-Ÿ\s-]+)', text)

    if match:
        # If a match was found, return the city name
        return remove_extra_spaces(match.group(2))
    else:
        # If no match was found, return a message
        return 'No match found.'


def convert_time(time_string):
    """
    Converts a time string to a datetime object.

    Args:
        time_string (str): The time string to convert.

    Returns:
        datetime: The converted time as a datetime object.
    """
    # Convert the string to a datetime object
    return datetime.datetime.strptime(time_string, "%M:%S.%f")

def convert_date(date_string):
    """
    Converts a date string to a datetime object.

    Args:
        date_string (str): The date string to convert.

    Returns:
        datetime: The converted date as a datetime object.
    """
    # Convert the string to a datetime object
    return datetime.datetime.strptime(date_string, "%d/%m/%Y")