REPLACE_OPERATORS = [[" > ", " < "], [" < ", " > "], [" >= ", " > "],
             [" >= ", " <= "], [" <= ", " > "], [ " == ", " != "],
             [" != ", " == "], [" + ", " - "],  [" - ", " + "],
             [" && ", " || "], [ " || ", " && "], [" / ", " * "],
             [" += ", " -= "], [" -= ", " += "], [" % ", " * "],
             [" /= ", " *= "], [" *= ", " /= "], [" * ", " / "],
             [" break", " continue"], [" continue", " break"],
             ["std::all_of", "std::any_of"], ["std::any_of", "std::all_of"],
             ["std::min", "std::max"], ["std::max", "std::min"], ["std::begin", "std::end"],
             ["std::end", "std::begin"], ["true", "false"], ["false", "true"]]

REGEX_OPERATORS = [["at(\(.*\))", r"at(0)"], ["CAmount\s+(\w+)\s*=\s*([0-9]+)", r"CAmount \1 = RANDOM_INT"],
                   ["CAmount\s+(\w+)\s*=\s*([0-9]+)", r"CAmount \1 = LESS"],
                   ["CAmount{+(\w+)}", "CAmount{RANDOM_INT}"], ["int\s+(\w+)\s*=\s*([0-9]+)", r"int \1 = RANDOM_INT"],
                   ["int\s+(\w+)\s*=\s*([0-9]+)", r"int \1 = LESS"], ["int\s+(\w+)\s*=\s*([0-9]+)", r"int \1 = GREATER"],
                   ["int32_t\s+(\w+)\s*=\s*([0-9]+)", r"int32_t \1 = LESS"], ["int32_t\s+(\w+)\s*=\s*([0-9]+)", r"int32_t \1 = GREATER"],
                   ["int64_t\s+(\w+)\s*=\s*([0-9]+)", r"int64_t \1 = RANDOM_INT"], ["int64_t\s+(\w+)\s*=\s*([0-9]+)", r"int64_t \1 = GREATER"],
                   ["bool\s+(\w+)\s*=\s+(.*)", r"bool \1 = true;"], ["int64_t\s+(\w+)\s*=\s*([0-9]+)", r"int64_t \1 = LESS"],
                   ["bool\s+(\w+)\s*=\s+(.*)", r"bool \1 = false;"], [r"std::chrono::seconds (\w+){+(\w+)}", r"std::chrono::seconds \1{RANDOM_INT}"],
                   ["int32_t\s+(\w+)\s*=\s*([0-9]+)", r"int32_t \1 = RANDOM_INT"], ["const\s+size_t\s+(\w+)\s*=\s*([0-9]+)", r"const size_t \1 = 10000"],
                   #[r"(^\s*)(\S+.*)\n", r"\1\2\n\1break;\n"], [r"(^\s*)(\S+.*)\n", r"\1\2\n\1continue;\n"], 
                   [r"std::chrono::seconds (\w+){+(\w+)}", r"std::chrono::seconds \1{RANDOM_INT}"],
                   [r"std::chrono::seconds (\w+)\s*=\s*(.*)", r"std::chrono::seconds \1 = RANDOM_INT;"]]