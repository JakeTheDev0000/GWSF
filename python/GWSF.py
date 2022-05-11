_version_ = "0.3.1"
in_ex = False

def getGWSFValue(GWSF_file_path, VAR_NAME):
    try:
        GWSF_file = open(GWSF_file_path)
    except:
        raise Exception("GWSF file not found")
    
    for line in GWSF_file:
        if line.startswith(VAR_NAME):
            VALUE_TYPE = line.split("-")[1].strip()
            if VALUE_TYPE == 'S' or VALUE_TYPE == 's':
                VALUE = line.split("\"")[1]
                VALUE = VALUE.split("\"")[0]
                return str(VALUE)
            elif VALUE_TYPE == 'I' or VALUE_TYPE == 'i':
                VALUE = line.split("-")[2]
                VALUE = VALUE.split("ENDL")[0]
                return int(VALUE)
            if in_ex == True:
                if VALUE_TYPE == 'B' or VALUE_TYPE == 'b':
                    VALUE = line.split("-")[2]
                    VALUE = VALUE.split("ENDL")[0]
                    if VALUE != "True" or VALUE != "False":
                        print(VALUE)
                        raise Exception("VALUE is NOT \"True\" or \"False\"")
                    return VALUE

def changeGWSFValue(GWSF_file_path, VAR_NAME, NEW_VALUE):
    try:
        GWSF_file = open(GWSF_file_path, "r+")
    except:
        raise Exception("GWSF file not found")

    for line in GWSF_file:
        if line.startswith(VAR_NAME):
            VALUE_TYPE = line.split("-")[1].strip()
            print(line)
            print(VALUE_TYPE)
            print(NEW_VALUE)
            if VALUE_TYPE == "I" or VALUE_TYPE == "i":
                line = line.split("-")[2]
                line = line.split("ENDL")[0]
                line = line.replace(line, str(NEW_VALUE))

                print(line)
                pass
            pass
        pass
    pass

def main():
    print("This is a library\nnot a program\n\n")
    choice = input("What do you want to do?\n1. settings\n2. exit\n")
    if choice == "1":
        print("settings")
        choice2 = input("1. version\n2. exit\n")
        if choice2 == "1":
            print("version")
            print(_version_)
            pass
        elif choice2 == "2":
            print("exit")
            exit(0)
        pass
    elif choice == "2":
        print("exit")
        exit(0)
    else:
        print("Invalid choice")
        main()
    pass

if __name__ == '__main__':
    main()