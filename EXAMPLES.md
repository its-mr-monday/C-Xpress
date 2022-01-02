# Some examples for those who need it

## Writing a function
    //func foo return void
    func foo() = void {

    }
    //func bar return int
    func bar() = int {
        return 1;
    }

    //func boo return string
    func boo() = str {
        return "foobarboo";
    }

## Writing a struct
    //Example struct human
    struct Human {
        str name;
        int age;
        int weight;
        //Constructor method
        Human(str name, int age, int weight) {
            this.name = name;
            this.age = age;
            this.weight = weight;
        }
    }

## Writing a class
    //Example Human class
    class Human {
        params {
            //class paramaters go here
            str name;
            int age;
            int weight;
        }
        //Constructor method
        Human(str name, int age, int weight) {
            this.name = name;
            this.age = age;
            this.weight = weight;
        }
        func change_name(str new_name) = void {
            name = new_name;
        }
        func fetch_age() = int {
            return age;
        }
    }

## Using a struct
    //Using the example human struct within "human_struct.cx"
    #INCLUDE <std.lib>
    #import "human_struct.cx"

    func main(str[] args) {
        Human human("David", 22, 180);
        
    }

## Using a class
    //Using the Example human class within "human.cx"
    #INCLUDE <std.lib>
    #import "human.cx"

    func main(str[] args) {
        //Create a instance of the Human class to var 'human'
        Human human("David", 22, 180);
        human.change_name("Dave");
        int age = human.fetch_age();
        print(age.toString());
    }

## For loop and While loop
    //For each loop
    #INCLUDE <std.lib>

    func main(str[] args) {
        foreach (str arg in args) {
            printf(arg + "\n\n");
        }
    }

    //For loop
    #INCLUDE <std.lib>

    func main(str[] args) {
        for (int i = 0; i < args.length; i++) {
            printf(args[i] + "\n\n");
        }   
    }

    //While loop
    #INCLUDE <std.lib>

    func main(str[] args) {
        int x = 0;
        while (x < args.length) {
            printf(args[x] + "\n\n");
        }
    }

## Exceptions try's and catch's
Exception in cxpress are the same as they were in C# all .NET exception types are supported with cxpress

    //Program to catch all Exceptions for the purposes of a example
    #INCLUDE <std.lib>
    #framework System

    func main(str[] args) {
        try {
            //some work
            print("No exception");
            //Catch all exceptions and print them
        } catch (Exception e) {
            print(e);
        }
    }

## If, else if and else statements

    //Program will look at arg[0] and determine wether to print it
    #INCLUDE <std.lib>

    func main(str[] args) {
        if (args[0] == "0") {
            print("zero");
        }
        else if (args[0] == "ten") {
            print("10");
        }
        else {
            print("NADA");
        }
    }

## Switch cases

    //Program will switch through all args and if one is equal to 0 it will print
    #INCLUDE <std.lib>

    func main(str[] args) {
        foreach (str arg in args) {
            switch(arg) {
                case "0":
                    print(arg);
                    break;
                default:
                    break;
            }
        }
    }

## Importing .NET namespaces ! Note: this can be used as well to import .NET DLL's !
    //Importing the System namespace and using the Console object
    #INCLUDE <std.lib>
    #framework System

    func main(str[] args) {
        Console.WriteLine("Hello World!");
    }

## Utilizing Native DLL's
    //Using some c++ dll named printSpam.dll with exported function "print_spam(std::string s) => void"
    #INCLUDE <std.lib>
    #framework System.InteropServices

    [DLLImport("printSpam.dll")]
    extern func print_spam(str s) = void;

    func main(str[] args) {
        print_spam("Hello World");
    }