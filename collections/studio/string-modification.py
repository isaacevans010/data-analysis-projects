my_string = "LaunchCode"
num = len(my_string)

# a) Use string methods to remove the first three characters from the string and add them to the end.
my_string1 = my_string[3:]+my_string[0:3]
print(my_string1)


# Use a template literal to print the original and modified string in a descriptive phrase.
print("Removing the first three letters of", my_string, "and placing them at the end makes it", my_string1)


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

original_word = "LaunchCode"
num_input = int(input("How many letters would you like to move to the end: "))
new_word = original_word[int(num_input):] + original_word[0:int(num_input)]
if int(num_input) > num:
    print("my_string1", "Please enter a valid number.")
else:
    print(new_word)


