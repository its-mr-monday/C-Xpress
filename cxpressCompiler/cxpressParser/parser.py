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

#Will format the data for a class
def format_class(class_data: str, project: str, included_namespaces: list, frameworks: list, imports: list):
    namespaces = ""
    for name in included_namespaces:
        namespace = name.split('.')[0]
        namespaces += f"using {namespace};\n"
    for name in frameworks:
        namespaces += f"using {name};\n"
    
    
    curly_front = "{"
    curly_back = "}" 
    namespace_str = f'''
    {namespaces}
    namespace {project} {curly_front}
        public {class_data}
    {curly_back}'''

    return namespace_str

def fromat_file(file_str: str):
    cs_file = ""
    #Convert all variables to C# variables
    for var in variable_dict.keys():
        file_str.replace(var, variable_dict[var])
        
    for line in file_str:
        if line.contains("//"):
            pass
        
    return cs_file

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
        
def convert_line_to_cs(line: str):
    cs_line = line
    for var in variable_dict.keys():
        if var in cs_line:
            cs_line.replace(var, variable_dict[var])
    
    return cs_line

def object_parser(file_data: str, object_pointer: int):
    cs_obj = ""
    
    return cs_obj
    
        
def parse_ming_file(ming_file: str):

    return 0
    
    
def generate_cs_file(file_data: str):

    return ""
    
    
def compile_cs_file(filename: str):
    
    return

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