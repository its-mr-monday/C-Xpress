# All M Files with the compiler and their exported functions

# std namespace
## std.lib
    IMPORT LINE: #INCLUDE <std.lib>

    Functions & Variables:
        func print(str s) = void;

        func printf(str s) = void;

        func strToBytes(str e) = byte[];

        func bytesToStr(byte[] e) = str;

        func exit(int code) = void;

        func isInt(str s) = bool;

        func strToInt(str s) = int;

        pointer NULL = pointer.Zero;

## std.file
    IMPORT LINE: #INCLUDE <std.file>

    Functions & Variables:
        func isFile(str path) = bool;

        func isDir(str path) = bool;

        func getFileName(str path) = str;

        func getFileNameWithoutExtension(str path) = str;

        func getFileExtension(str path) = str;

        func getFileDir(str path) = str;

        func readFile(str path) = byte[];

        func readFileLines(str path) = str[];

        func getDirName(str path) = str;

        func getDirNameWithoutExtension(str path) = str;

        func getDirExtension(str path) = str;

        func writeToFile(str path, byte[] data) = void;

        func writeToFile(str path, str data) = void;

        func appendToFile(str path, str data) = void;

        func appendToFile(str path, byte[] data) = void;

        func listFiles(str path) = str[];

        func listDirectories(str path) = str[];

        func createDir(str path) = void;

        func deleteDir(str path) = void;

        func copyFile(str src, str dst) = void;

        func moveFile(str src, str dst) = void;

        func copyDir(str src, str dst) = void;

        func moveDir(str src, str dst) = void;

        func pathCombine(str dir, str file) = str;


# win namespace
## win.kernel32
    IMPORT LINE: #INCLUDE <win.kernel32>

    Functions & Variables:
        UInt32 INVALID_HANDLE_VALUE = 0xffffffff;

        func ReadProcessMemory(int hProcess, int lpBaseAddress, byte[] buffer, int, size, int lpNumberOfBytesRead) = bool;

        func OpenProcess(uint processAccess, bool bInheritHandle, int processId) = pointer;

        func WriteProcessMemory(pointer hProcess, pointer lpBaseAddress, byte[] lpBuffer, int nSize, out pointer lpNumberOfBytesWritten) = bool;

        func VirtualAllocEx(pointer hProcess, pointer lpAddress, uint dwSize, uint flAllocationType, uint flProtect) = pointer;

        func CreateRemoteThread(pointer hProcess, pointer lpThreadAttributes, uint dwStackSize, pointer lpStartAddress, pointer lpParameter, uint dwCreation) = pointer;

        func FindFirstFile(str lpFileName, out WIN32_FIND_DATA lpFindFileData) = pointer;

        func FindFirstFile(str lpFileName, out WIN32_FIND_DATA lpFindFileData) = SafeFindHandle;

        func LoadLibrary(str dllToLoad) = pointer;

        func GetProcAddress(pointer hModule, str procedureName) = pointer;

        func FreeLibrary(pointer hModule) = bool;

## win.proctypes
    IMPORT LINE: #INCLUDE <win.proctypes>

    Functions & Variables:

        uint PAGE_EXECUTE_READWRITE = 0x40;

        uint MEM_COMMIT = 0x00001000;

        uint DELETE = 0x00010000;

        uint READ_CONTROL = 0x00020000;

        uint WRITE_DAC = 0x00040000;

        uint WRITE_OWNER = 0x00080000;

        uint SYNCHRONIZE = 0x00100000;
        
        uint END = 0xFFF;

        uint PROCESS_ALL_ACCESS = (DELETE | READ_CONTROL | WRITE_DAC | WRITE_OWNER | SYNCHRONIZE | END);

## win.console
    IMPORT LINE: #INCLUDE <win.console>

    Functions & Variables:
        int SW_HIDE = 0;

        int SW_SHOW = 5;

        func GetConsoleWindow() = pointer;

        func ShowWindow(pointer hWmnd, int nCmdShow) = bool;

        func AllocConsole() = bool;

        func AttachConsole(uint dwProcessId) = bool;

        func AddConsoleAlias(str Source, str Target, str ExeName) = bool;

        func CreateConsoleScreenBuffer(uint dwDesiredAccess, uint dwShareMode, pointer lpSecurityAttributes, uint dwFlags, pointer lpScreenBufferData) = pointer;


        

## win.asm

## win.dll

## win.shell
    IMPORT LINE: #INCLUDE <win.shell>

    Functions & Variables:

        func exec(str command) = str;

        func execp(str command) = str;

# Writing your own M files
Some of you may not be so keen to switch over from cs to cx
that is okay C-Xpress supports C# code 100% as m files
However M files must contain static methods only
M files must be accompanied with a mh file think of this like a header file see bellow for mh file instructions

## Example m file
for the purposes of this example the m file will contain a method to return the bytes of a file

    FILENAME = "reader.m" within directory "file"

    using System.IO;
    using System;

    namespace file {
        public class reader {
            public static byte[] read_file(string file_path) {
                return File.ReadAllBytes(file_path);
            }
        }
    }

## Using the example m file in a cx file
The following ming file will be used to read a local file and print its contents

    //Importing file "reader.m" within directory "file"
    #INCLUDE <std.lib>
    #INCLUDE "file.reader"

    func main(str[] args) {
        byte[] file_data = read_file("C:\\Windows\\some_file.txt");
        print(bytesToStr(file_data));
    }

# Writing a MH file for a M file
MH files are cx headers and simply tell the compiler what parsing is required for functions written in M files

## Using the example M file from above
For the purposes of this example this mh file will contain method translations for the M file "reader.m" above

    #SAMPLE MH FILE "reader.mh"
    read_file => reader.read_file
