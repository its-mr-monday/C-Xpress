using System;
using System.IO;

namespace std {
    public class file {
        public static bool isFile(string path) { return File.Exists(path); }
        public static bool isDir(string path) { return Directory.Exists(path); }
        public static string getFileName(string path) { return Path.GetFileName(path); }
        public static string getFileNameWithoutExtension(string path) { return Path.GetFileNameWithoutExtension(path); }
        public static string getFileExtension(string path) { return Path.GetExtension(path); }
        public static string getFileDir(string path) { return Path.GetDirectoryName(path); }
        public static byte[] readFile(string path) { return File.ReadAllBytes(path); }
        public static str[] readFileLines(string path) { return File.ReadAllLines(path); }
        public static string getDirName(string path) { return Path.GetDirectoryName(path); }
        public static string getDirNameWithoutExtension(string path) { return Path.GetDirectoryName(path); }
        public static string getDirExtension(string path) { return Path.GetExtension(path); }
        public static void writeToFile(string path, byte[] data) { File.WriteAllBytes(path, data); }
        public static void writeToFile(string path, string data) { File.WriteAllText(path, data); }
        public static void appendToFile(string path, string data) { File.AppendAllText(path, data); }
        public static void appendToFile(string path, byte[] data) { File.AppendAllBytes(path, data); }
        public static string[] listFiles(string path) { return Directory.GetFiles(path); }
        public static string[] listDirectories(string path) { return Directory.GetDirectories(path); }
        public static void createDir(string path) { Directory.CreateDirectory(path); }
        public static void deleteDir(string path) { Directory.Delete(path); }
        public static void deleteFile(string path) { File.Delete(path); }
        public static void copyFile(string src, string dst) { File.Copy(src, dst); }
        public static void moveFile(string src, string dst) { File.Move(src, dst); }
        public static void copyDir(string src, string dst) { Directory.Copy(src, dst); }
        public static void moveDir(string src, string dst) { Directory.Move(src, dst); }
        public static string pathCombine(string dir, string file) { return Path.Combine(dir, file); }
    }
}