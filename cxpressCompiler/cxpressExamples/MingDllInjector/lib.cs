using System;
using System.IO;

namespace std
{
	public class lib
    {
        IntPtr NULL = IntPtr.Zero;
        public static void print(string s) { Console.WriteLine(s);  }
        public static void exit(int code) { Environment.Exit(code); }
    }
}