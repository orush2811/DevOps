first_name = "Or"
last_name = "Itach"
age = 27
height = 1.85
full_name = first_name + " " + last_name
dog = "Maple"

print("Hello " + full_name + ", You are " + str(age) + " years old" + ", and you are " + str(
    height) + " centimeters tall!")
print("You also have a dog named " + dog)
print(len(first_name))  # Prints out the length of a string
print(first_name.find("r"))  # Finds a character in a string
print(first_name.capitalize())  # Capitalizes the first character in the given string
print(first_name.lower())  # Converts all characters in the string to lower case letters
print(first_name.upper())  # Converts all characters in the string to upper case
print(first_name.isdigit())  # Check if all the characters in the text are digits - returns true or false
print(first_name.isalpha())  # Check if all the characters in the text are letters
print(first_name.count("O"))  # Returns the value of a given character inside a string
print(first_name.replace("r", "R"))  # The replace() method replaces a specified phrase with another specified phrase
print(dog * 5)  # Printing our string multiple times - string.replace(oldvalue, newvalue, count)

###################################################################
# Type casting - converting data type of a value to another type - from string to int for example

x = 1  # int
y = 2.0  # float
z = "3"  # string(str)

print(x)
print(y)
print(int(z))
print("X is " + str(x))
