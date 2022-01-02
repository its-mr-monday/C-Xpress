using win;
using std;
using System.InteropServices;

namespace dllinjector {
    public class DLLInjector {
        
        public byte[] dll;

        public DLLInjector(string dll_path) {
            load_dll(dll_path);
        }
        public void load_dll(string dll_path) {
            dll = File.ReadAllBytes(dll_path);
        }
        public bool Inject(int pid) {
            uint dllSize = uint.ConvertInt(dll.count);
            IntPtr hProc = kernel32.OpenProcess(PROCESS_ALL_ACCESS, false, pid);
            if (hProc == lib.NULL) {
                return false;
            }

            IntPtr MyAlloc = kernel32.VirtualAllocEx(hProc, lib.NULL, dllSize, proctypes.MEM_COMMIT, proctypes.PAGE_READWRITE);
            if (MyAlloc == lib.NULL) {
                return false;
            }

            IntPtr bytesWritten;
            bool isWriteOk = kernel32.WriteProcessMemory(hProc, MyAlloc, dll, dllSize, out bytesWritten);
            if (!isWriteOk || bytesWritten == lib.NULL) {
                return false;
            }

            IntPtr dWord;
            IntPtr addrLoadLibrary = kernel32.GetProcAddress(kernel32.LoadLibrary("kernel32.dll"), "LoadLibraryA");
            IntPtr ThreadReturn = kernel32.CreateRemoteThread(hProc, lib.NULL, lib.NULL, addrLoadLibrary, MyAlloc, proctypes.CREATE_SUSPENDED, out dWord);
            if (ThreadReturn == lib.NULL) {
                return false;
            }
            if ((hProc != LIB.NULL) && (MyAlloc != LIB.NULL) && (isWriteOk != false) && (ThreadReturn != lib.NULL) && (bytesWritten != lib.NULL)) {
                return true;
            }
		
		    return false;
        }
    }
}