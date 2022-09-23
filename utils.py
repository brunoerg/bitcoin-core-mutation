import os
import re
import pathlib
import random


BASE_PATH = str(pathlib.Path().resolve())
PERCENTAGES = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def replace_value(code, regex_to_search, regex_to_mutate, to_be_mutated):
    search_regex = re.search(regex_to_search, to_be_mutated)
    final_values = []
    if code == "RANDOM_INT":
        regex_mutated = regex_to_mutate.replace("RANDOM_INT", str(random.randint(0, 100000)))
        final_values.append(regex_mutated)
    elif code == "LESS":
        for value in PERCENTAGES:
            search_regex = re.search(regex_to_search, to_be_mutated)
            if int(search_regex.group(2)) == 0:
                return False
            new_value = str(int(int(search_regex.group(2)) * (1 - value / 100)))
            regex_mutated = regex_to_mutate.replace("LESS", new_value)
            final_values.append(regex_mutated)
    elif code == "GREATER":
        for value in PERCENTAGES:
            search_regex = re.search(regex_to_search, to_be_mutated)
            if int(search_regex.group(2)) == 0:
                return False
            new_value = str(int(int(search_regex.group(2)) * (1 + value / 100)))
            regex_mutated = regex_to_mutate.replace("GREATER", new_value)
            final_values.append(regex_mutated)

    return final_values


def mkdir_mutation_folder():
    path = os.path.join(BASE_PATH, 'muts')
    if not os.path.isdir(f'{BASE_PATH}/muts'):
        os.mkdir(path)
