proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for string in strings:
    if "," in string:
        print("Commas delimiter used in list", string)
    elif ";" in string:
        print("Semi-colon delimiter used in list", string)
    elif " " in string:
        print("Space delimiter used in string", string)


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, 
# and then join the array into a new comma separated string.
separator = ", "
for string in strings:
    if "," in string:
        new_comma_string = string.split()
        new_comma_string.reverse()
        new_comma_string = separator.join(new_comma_string)
print(new_comma_string)



# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the 
# entries, and then join the array into a new comma separated string.



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries,
#  and then join the array into a new space separated string.



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result 
# as part “b”, making sure that the extra spaces are NOT part of the final string.
