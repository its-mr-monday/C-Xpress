#STD.LIB.M
using System;
using System.IO;

namespace std {
    public class lib {
        public static IntPtr NULL = IntPtr.Zero;
        public static void print(string s) { Console.WriteLine(s); }
        public static void printf(string s) { Console.Write(s); }
        public static void exit(int code) { Environment.Exit(code); }
        public static byte[] strToBytes(string e) { return System.Text.Encoding.ASCII.GetBytes(e); }
        public static string bytesToStr(byte[] e) { return System.Text.Encoding.ASCII.GetString(e); }
        public static bool isInt(string e) { return int.TryParse(e, out int i); }
        public static int strToInt(string e) { return int.Parse(e); }
        public static string slice(string source, string remove) { return source.Replace(remove, ""); }
    }
}

