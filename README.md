# C-Xpress Programming Language
The cxpress programming language is a High Level object oriented programming language running on the .NET Framework

C-Xpress tries to be a middle gap between Visual C++ and C# by simplifying the programming experience

C-Xpress has a more basic approach to objects

C-Xpress structures and classes members are all considered public however non static

C-Xpress funcs are considered static methods in C# or normal functions in C++

C-Xpress allows for full access of the entire .NET Framework allowing you to build .NET DLL's and Exectuables

# Some Examples
# Hello World
        #INCLUDE <std.lib>

        func main(str[] args) {
            print("Hello world");
        }

# Importing a cx file
        //Within the same directory
        #INCLUDE <std.lib>
        #import "somefile.cx"

        func main(str[] args) {
            //some func in "somefile.cx"
            some_func();
        }

        //Within subdirectory some
        #INCLUDE <std.lib>
        #import "some.somefile.cx"

        func main(str[] args) {
            some_func();
        }

# Importing a local m file
        //Within same directory
        #INCLUDE <std.lib>
        #INCLUDE "webclient"

        func main(str[] args) {

        }

        //Within subdirectory web
        #INCLUDE <std.lib>
        #INCLUDE "web.webclient"

        func main(str[] args) {

        }

# Importing a .NET Framework Namespace
        //Using namespace System
        #INCLUDE <std.lib>
        #framework System

        func main(str[] args) {
            print("Hello World");
            Console.WriteLine("Hello World x2");
        }
        
# Import types
        #INCLUDE <filename> : imports a std m file
        #INCLUDE "filename" : imports a custom m file within the same directory
        #import "filename.cx" : imports a cx file
        #framework namespace : imports a .NET framework namespace think of it like using in C#

# Different File Types
        C-Xpress uses two file types ".cx" files and ".m" files

        .m files are generally C# code they are the same as C# code the namespace must be the directory it is in, and the class name is the filename example/example.m #INCLUDE "example.example"

        .cx files are files written in  cxpress itself and are imported with #import "name.cx"
