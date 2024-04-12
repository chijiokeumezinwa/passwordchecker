'''1. Password Strength Checker: Build a tool that assesses the strength of passwords by analyzing factors like
 length, complexity, and the presence of common patterns.
 

At least 12 characters long but 14 or more is better.

A combination of uppercase letters, lowercase letters, numbers, and symbols.
'''

import re

def analyze_pw(userinput):
    #test for combination of uppercase letters lowercase letters numbers and symbols
    regex = ("^(?=.*[a-z])(?=.*[A-Z])"
             +"(?=.*\\d)"
             +"(?=.*[-+_!@#$%^&*., ?]).+$")
    regex_check = False
    dictionary_check=False
    p = re.compile(regex)
    if re.search(p, userinput):
        print("Passes regex check")
        regex_check=True

    
    return regex_check 
    

def main():
    while True:
        print("Password minimum requirements: \nAt least 12 characters long but 14 or more is better.")
        print("A combination of uppercase letters, lowercase letters, numbers, and symbols.")
        print("Significantly different from your previous passwords.")
        userinput = input("Please enter a password that passes the above requirements or press enter to quit: ")
        #check length of words
        longenough = len(userinput)
        status_check= analyze_pw(userinput)
        if userinput == "" or longenough < 12:
            print("Password must be of at least 12 characters try again.")
            continue
        if status_check:
            print("password is compatible")
            return
        else:
            print("password is not compatible try again")



if __name__ == "__main__":
    main()