import osimport sysdef args_check(args):    if len(args) < 2:        return False    def main(args):    #Get C# converted file and compile using dotnet and the system provided    if args_check(args) == False:        return 1    if __name__ == '__main__':        return_code = main(sys.argv)    sys.exit(return_code)