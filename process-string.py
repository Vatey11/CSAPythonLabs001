# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")

# Application 1 
def duplicate_string(str):
    str = list(str)
    for item in str:
        print(2*item, end='')

duplicate_string("hello world")

# Application 2
def letters_range(str):
    result = ""
    str = str.split("-")
    start_ord = ord(str[0])
    end_ord = ord(str[-1])

    for i in range(start_ord,end_ord + 1):
        result += chr(i)
    print(result)

letters_range("A-D")