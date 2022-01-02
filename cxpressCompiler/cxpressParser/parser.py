import os
import subprocess

PARSER_DIR = os.path.dirname(os.path.realpath(__file__))
variable_dict = {'str': 'string', 'int': 'int', 'double': 'double',
                 'bool': 'bool', 'char': 'char', 'byte' : 'byte',
                 'pointer': 'IntPtr', 'void': 'void', 'datetime': 'DateTime',
                 'int32' : 'Int32', 'uint32': 'UInt32'}


def return_format_types():
    TAB = "    "
    SPACE = " "
    FUNCTIONAL = "var x = some_func(args) || some_func(args)"
    OBJECT = "Type name(args)"
    return {'FUNCTIONAL': FUNCTIONAL, 'OBJECT': OBJECT, 'TAB': TAB, 'SPACE': SPACE}

def return_obj_format_translations():
     return {'OBJECT': "Type name = new Type(args)"}

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
            fname += ".cx"
            fname = os.path.join(PARSER_DIR, dir, fname)
            include_files.append(fname)
        elif (include.startswith('#INCLUDE "')):
            fname = include.replace('#INCLUDE "', '').replace('"', '')
            fnames = fname.split('.')
            dir = fnames[0]
            fname = fnames[1]
            fname += ".cx"
            fname = os.path.join(file_path, dir, fname)
            include_files.append(fname)
    retVal = {}
    
    #Load the m files in the order they appear in the include table
    for f in include_files:
        fpath = os.path.join(PARSER_DIR, f)
        file = open(fpath, 'r')
        meta_data = ""
        for line in file:
            if line.contains('#'):
                pass
            meta_data.append(line + '\n')
            
        file.close()
        
        
    return retVal
    
def parse_m_file(m_file: str):
    #will parse a loaded m file
    function_translations = {}
    for line in m_file:
        split_line = line.split(' => ')
        cs_ver = split_line[1]
        ming_ver = split_line[0]
        
        
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