'''
    CXPRESS COMPILER PARSER WRITTEN IN PYTHON3
    CYBERM TECHNOLOGIES 2022
'''


import os
import subprocess

PARSER_DIR = os.path.dirname(os.path.realpath(__file__))
variable_dict = {'str': 'string', 'int': 'int', 'double': 'double',
                 'bool': 'bool', 'char': 'char', 'byte' : 'byte',
                 'pointer': 'IntPtr', 'void': 'void', 'datetime': 'DateTime',
                 'int32' : 'Int32', 'uint32': 'UInt32'}

def readFileLines(file_path):
    filelines = []
    file = open(file_path, 'r')
    for line in file.readlines():
        filelines.append(line)
    
    return filelines


def return_format_types():
    TAB = "    "
    SPACE = " "
    FUNCTIONAL = "var x = some_func(args); || some_func(args);"
    OBJECT = "Type name(args);"
    ARRAY = "var[] x[length];"
    return {'FUNCTIONAL': FUNCTIONAL, 'OBJECT': OBJECT, 'TAB': TAB, 'SPACE': SPACE}

def return_obj_format_translations():
     return {'OBJECT': "Type name = new Type(args)",
             'ARRAY' : "var[] x = new var[length];"}

def function_translation(function_data: str):
    return ""

def load_m_files(include_table: list, file_path: str):
    file_path = os.path.join(file_path, 'm_files')
    include_files = []
    for include in include_table:
        if (include.startswith('#INCLUDE <')):
            fname = include.replace('#INCLUDE <', '').replace('>', '')
            fnames = fname.split('.')
            dir = fnames[0]
            fname = fnames[1]
            fname += ".m"
            fname = os.path.join(PARSER_DIR, dir, fname)
            include_files.append(fname)
        elif (include.startswith('#INCLUDE "')):
            fname = include.replace('#INCLUDE "', '').replace('"', '')
            fnames = fname.split('.')
            dir = fnames[0]
            fname = fnames[1]
            fname += ".m"
            fname = os.path.join(file_path, dir, fname)
            include_files.append(fname)
        else:
            include_files.append(None)
    
    return include_files
    
def parse_mh_file(mh_file_path: str, function_translations = {}):
    #will parse a loaded m file
    file_lines = readFileLines(mh_file_path)
    for line in file_lines:
        split_line = line.split(' => ')
        cs_ver = split_line[1]
        cx_ver = split_line[0]
        function_translations[cx_ver] = cs_ver
        
    return function_translations

def fromat_cs_file(using_statements: str, fname: str, classes: list, functions: list, main_block: str, proj_name: str):
    cs_file = ""
    cs_file += using_statements + "\n"
    cs_file += "namespace "+ proj_name +" {\n"
    for class_ in classes:
        cs_file += class_ + "\n"
    cs_file += "public class " + fname + "{\n"
    for function in functions:
        cs_file += function + "\n"
    if main_block != None:
        cs_file += "public static void Main(string[] args) {\n"
        cs_file += main_block + "\n"
        cs_file += "}\n"
    cs_file += "}\n|\n"
    return cs_file

def remove_comments(file_data: list):
    lines = file_data
    for x in range(0, len(lines)):
        line = lines[x]

    return lines

def load_framework_files(framework_table: list, file_path: str):
    frameworks = framework_table
    for x in range(0, len(frameworks)):
        file = frameworks[x]
        file.replace("#framework ")
        file = "using " + file + ";"
        frameworks[x] = file
    
    return frameworks

def parse_file(filename: str):
    return None

def parser_main(args):
    #Get args; args[0] is the file to parse; args[1] is the project name; args[2] is the project type
    # Possible project types: Console, Library
    if (args[0] == '-h' or args[0] == '--help'):
        print("Usage: cxc.py <filename> <project name> <project type>")
        print("Example: cxc.py test.cx test Console")
        return
    
    if (len(args) < 3):
        print("Not enough arguments")
        return
    
    
    
    
    return ""