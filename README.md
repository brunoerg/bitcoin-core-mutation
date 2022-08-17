# Mutation testing for Bitcoin Core

## How to run
1. Open `config.py`
2. Fill:
   - `FILES_TO_MUTATE` with the files you'd like to mutate.
   - `BITCOIN_CORE_PATH` with the path to the Bitcoin Core source code

E.g:
```py
FILES_TO_MUTATE = [
    "src/wallet/coinselection.cpp",
    "src/wallet/spend.cpp",
    'src/net.cpp',
    "src/wallet/feebumper.cpp",
    "src/script/interpreter.cpp"
]

BITCOIN_CORE_PATH = "/Users/youruser/projects/bitcoin"
```

3. Execute `./gen-mutators.py`

It will create a folder (`muts`) with the mutators (one file per mutator)