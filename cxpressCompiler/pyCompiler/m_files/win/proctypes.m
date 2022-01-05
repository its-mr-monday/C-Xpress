#WIN_32_STATIC_UNSIGNED_INTEGER

namespace win {

    public class proctypes {
        public static uint PAGE_EXECUTE_READWRITE = 0x40;
        public static uint MEM_COMMIT = 0x00001000;
        public static uint DELETE = 0x00010000;
        public static uint READ_CONTROL = 0x00020000;
        public static uint WRITE_DAC = 0x00040000;
        public static uint WRITE_OWNER = 0x00080000;
        public static uint SYNCHRONIZE = 0x00100000;
        public static uint END = 0xFFF;
        public static uint PROCESS_ALL_ACCESS = (DELETE | READ_CONTROL | WRITE_DAC | WRITE_OWNER | SYNCHRONIZE | END);
    }

}