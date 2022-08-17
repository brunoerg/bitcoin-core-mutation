import os
import re
import pathlib
import random


BASE_PATH = str(pathlib.Path().resolve())
PERCENTAGES = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def replace_value(code, regex_to_search, regex_to_mutate, to_be_mutated):
    search_regex = re.search(regex_to_search, to_be_mutated)
    if code == "RANDOM_INT":
        regex_to_mutate = regex_to_mutate.replace("RANDOM_INT", str(random.randint(0, 100000)))
        return regex_to_mutate
    elif code == "LESS":
        value = random.choice(PERCENTAGES)
        search_regex = re.search(regex_to_search, to_be_mutated)
        if int(search_regex.group(2)) == 0:
            return False
        new_value = str(int(int(search_regex.group(2)) * (1 - value / 100)))
        regex_to_mutate = regex_to_mutate.replace("LESS", new_value)
    elif code == "GREATER":
        value = random.choice(PERCENTAGES)
        search_regex = re.search(regex_to_search, to_be_mutated)
        new_value = str(int(int(search_regex.group(2)) * (1 + value / 100)))
        regex_to_mutate = regex_to_mutate.replace("GREATER", new_value)

    return regex_to_mutate


def mkdir_mutation_folder():
    path = os.path.join(BASE_PATH, 'muts')
    if not os.path.isdir(f'{BASE_PATH}/muts'):
        os.mkdir(path)
