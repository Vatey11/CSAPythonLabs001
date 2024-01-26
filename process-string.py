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
str = input("Enter a string: ") # take user input
str = list(str) # put the string in list
# muliple all char by 2
for item in str:
    print(2*item, end='')
    
print("\n")

# Application 2
user_range = input("Enter a range of letters (e.g., a-z): ")
start, end = user_range.split('-') # split the letter into list
start_ord = ord(start) # change the start char to ascii decimal
end_ord = ord(end) # change the end char to ascii decimal

 # empty string to combine everything together
result = ""
# add all the char that has ascii decimal between the start_ord and the end_ord
for i in range(start_ord,end_ord + 1):
    result += chr(i)
print(result)