# So how does this language work?
This language was built on top of the .NET Framework and C#

The cxpress compiler will first parse the m files included to C# files within a new project

The compiler will then parse all cx files and convert them to C# files within the same project

The compiler will then use the C# dotnet compiler to build the application to a executable or DLL

# Example conversion of simple cx file to cs file
## CX FILE
    //EXAMPLE.CX
    #INCLUDE <std.lib>

    func main(str[] args) {
        print("Hello World");
    }

## CS FILES
    //lib.cs
    using System;

    namespace std {
        public class lib {
            public static void print(string s) { Console.WriteLine(s); }
        }
    }

    //example.cs

    using std;

    namespace example {
        public class example {
            public static void Main(string[] args) {
                lib.print("Hello World");
            }
        }
    }