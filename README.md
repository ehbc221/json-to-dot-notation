# json-to-dot-notation

## Convert json (from file or from clipboard) into dot notation.

    1. Usage: python json-to-dot-notation.py [[-c | -i <input_file>] -o <output_file> | args...]
    Options and arguments:
    -h      : print this help message and exit (also --help)
    -c      : copy json from clipboard
    -i      : input file
    -o      : output file
    args... : -h or --help flags

    2. Examples:
       *    python json-to-dot-notation.py -c -o output_file.json (convert to dot notation json from clipboard to a file named output_file.json)
       *    python json-to-dot-notation.py -i input_file.json -o output_file.json (convert to dot notation a json from a file named input_file.json to another file named output_file.json)

    3. Dependencies:
       *    pyperclip: you can install it using 'pip install pyperclip'
