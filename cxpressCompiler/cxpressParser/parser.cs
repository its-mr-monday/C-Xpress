/*
    CXPRESS COMPILER PARSER WRITTEN IN C# *FOR EXAMPLE PURPOSES*
    CYBERM TECHNOLOGIES 2022

*/
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Collections;

namespace cxc {
    public class parser {
        public static string getParserDir() {
            string parser_dir = AppContext.BaseDirectory;
            return parser_dir;
        }
        public static Dictionary<string, string> variable_dict() {
            Dictionary<string, string> dict = new Dictionary<string, string>();
            dict.Add("str", "string");
            dict.Add("uint32", "UInt32");
            dict.Add("int32", "Int32");
            dict.Add("pointer", "IntPtr");
            dict.Add("datetime", "DateTime");
            return dict;
        }
        public static Dictionary<string, string> return_format_types() {
            Dictionary<string, string> format_types = new Dictionary<string, string>();
            format_types.Add("TAB", "   ");
            format_types.Add("SPACE", " ");
            format_types.Add("FUNCTIONAL", "var x = some_func(args); || some_func(args);");
            format_types.Add("OBJECT", "Type name(args);");
            format_types.Add("ARRAY", "var[] x[length];");
            return format_types;
        }
        public static Dict<string, string> return_func_translations() {
            Dictionary<string, string> format_types = new Dictionary<string, string>();
            format_types.Add("TAB", "   ");
            format_types.Add("SPACE", " ");
            format_types.Add("FUNCTIONAL", "var x = some_func(args); || some_func(args);");
            format_types.Add("OBJECT", "Type name(args);");
            format_types.Add("ARRAY", "var[] x[length];");
            return format_types;
        }
    }
}