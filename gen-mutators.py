#!/usr/bin/env python3

import pathlib
import re
from operators import (
    REGEX_OPERATORS
)
from config import (
    FILES_TO_MUTATE,
    BITCOIN_CORE_PATH
)
from utils import mkdir_mutation_folder, replace_value


BASE_PATH = str(pathlib.Path().resolve())
BASE_MUT = f'{BASE_PATH}/muts'
REPLACEMENT_IN_REGEX = ["LESS", "RANDOM_INT", "GREATER"]


def write_mutation(file_name, lines, i, line_mutated):
    mutator_file = f'{BASE_MUT}/{file_name}.mutant.{i}.cpp'
    with open(mutator_file, 'w', encoding="utf8") as file:
        print(f"After: {line_mutated}")
        file.writelines(lines)
        return i + 1


def mutate(file_to_mutate):
    input_file = f'{BITCOIN_CORE_PATH}/{file_to_mutate}'

    file_name = file_to_mutate.split('/')
    file_name = file_name[len(file_name) - 1].split('.')[0]

    with open(input_file, 'r', encoding="utf8") as source_code:
        source_code = source_code.readlines()
        num_lines = len(source_code)

    OPERATORS = REGEX_OPERATORS
    
    i = 0
    for operator in OPERATORS:
        lines_num_list = list(range(1, num_lines - 1))
        for line_num in lines_num_list:
            lines = source_code.copy()
            line_before_mutation = lines[line_num]

            if line_before_mutation.lstrip().startswith(("//", "*", "assert", "/*")):
                continue

            if re.search(operator[0], line_before_mutation):
                    print(f"Before: {line_before_mutation}")
                    operators_sub = [operator[1]]
                    res = [op for op in REPLACEMENT_IN_REGEX if(op in operator[1])]
                    if bool(res):
                        operators_sub = replace_value(res[0], operator[0], operator[1], line_before_mutation)
                        if not operators_sub:
                            continue
                    for op_sub in operators_sub:
                        line_mutated = re.sub(operator[0], op_sub, line_before_mutation)
                        lines[line_num] = f'{line_before_mutation[:-len(line_before_mutation.lstrip())]}{line_mutated}'
                        i = write_mutation(file_name, lines, i, line_mutated)
            else:
                continue


if __name__ == "__main__":
    mkdir_mutation_folder()

    for file in FILES_TO_MUTATE:
        mutate(file)
