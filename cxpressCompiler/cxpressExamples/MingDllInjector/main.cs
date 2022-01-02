using std;

namespace dllinjector {
    public static void Main(string[] args) {
        DLLInjector injector = new DLLInjector("C:\\some.dll");
        injector.Inject(1234);
        return;
    }
}