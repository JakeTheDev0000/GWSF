import GWSF as gw
import os, time

# afa

def main():
    os.system("cls")
    print("This is a library\nnot a program\n\n")
    test_GWSF_FILE = "python/test.gwsf"
    print(gw.getGWSFValue(test_GWSF_FILE, "NAME"))
    print(gw.getGWSFValue(test_GWSF_FILE, "VERSION"))
    print(gw.getGWSFValue(test_GWSF_FILE, "AGE"))
    print(gw.getGWSFValue(test_GWSF_FILE, "LIKES_APPLES"))

    
    age = gw.getGWSFValue(test_GWSF_FILE, "AGE"); #print(age)

    if age == 14:
        gw.changeGWSFValue(test_GWSF_FILE, "AGE", 15)
        pass
    if age == 15:
        gw.changeGWSFValue(test_GWSF_FILE, "AGE", 14)
        pass
    pass

    if gw.getGWSFValue(test_GWSF_FILE, "LIKES_APPLES") == "True":
        print("i like apples")
    else:
        print("i dont like apples")

    # print(gw.getGWSFValue("python/test.gwsf", "NAME"))

if __name__ == '__main__':
    main()