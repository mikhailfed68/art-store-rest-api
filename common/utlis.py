import re


def array_has_regex(path_to_match, array):
    for regex in array:
        if re.search(regex, path_to_match):
            return True
    return False
