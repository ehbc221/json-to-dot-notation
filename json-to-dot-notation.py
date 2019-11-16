import getopt
import json
import os
import pyperclip
import sys


def get_input_string_from_clipboard():
    input_string = json.loads(pyperclip.paste())
    return input_string


def get_input_string_from_file(input_file_name):
    with open(input_file_name, "r") as input_file:
        input_string = input_file.readlines()
    return input_string


def write_output_file(output_file, val, old=""):
    if isinstance(val, dict):
        for k in val.keys():
            write_output_file(output_file, val[k], old + "." + str(k))
    elif isinstance(val, list):
        for i, k in enumerate(val):
            write_output_file(output_file, k, old + "." + str(i))
    else:
        line = "\t\"{}\": \"{}\",\n".format(old, str(val))
        new_line = line[0:2] + line[3:]
        output_file.write(new_line)


def json_to_dot_notation(input_string, output_file_name):
    output_file = open(output_file_name, "w", 1, "UTF-8")

    output_file.write("{\n")
    write_output_file(output_file, input_string)
    output_file.write("}\n")
    output_file.close()

    with open(output_file_name, "rb+") as filehandle:
        filehandle.seek(-6, os.SEEK_END)
        filehandle.truncate()

    output_file = open(output_file_name, "a", 1, "UTF-8")
    output_file.write("\n}\n")
    output_file.close()


def print_help():
    print("Convert json (from file or from clipboard) into dot notation.")
    print("usage: python json-to-dot-notation.py [[-c | -i <input_file>] -o <output_file> | args...]")
    print("Options and arguments:")
    print("-h      :  print this help message and exit (also --help)")
    print("-c      :  copy json from clipboard")
    print("-i      :  input file")
    print("-o      :  output file")
    print("args... : -h or --help flags")
    print("\nExample 1: python json-to-dot-notation.py -c -o output_file.json " +
    "(convert to dot notation json from clipboard to a file named output_file.json)")
    print("\nExample 2: python json-to-dot-notation.py -i input_file.json -o output_file.json " +
    "(convert to dot notation a json from a file named input_file.json to another file named output_file.json)")


def main(argv):
    input_file_name = ""
    output_file_name = ""
    from_clipboard = False
    try:
        opts, args = getopt.getopt(argv, "hci:o:")
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        if opt in ("-c", "--clipboard"):
            from_clipboard = True
        elif opt in ("-i", "--ifile"):
            input_file_name = arg.strip()
        elif opt in ("-o", "--ofile"):
            output_file_name = arg.strip()
    if from_clipboard and output_file_name != "":
        print("\nConverting Json from clipboard")
        json_to_dot_notation(get_input_string_from_clipboard(), output_file_name)
        print("..........\nJson from clipboard converted in ", output_file_name)
    elif input_file_name != "" and output_file_name != "":
        print("\nConverting Json from file ", input_file_name)
        json_to_dot_notation(get_input_string_from_file(input_file_name), output_file_name)
        print("..........\nJson file converted in ", output_file_name)
    else:
        print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
