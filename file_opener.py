## This is a sample file to open a provided text name.

## This stores a reusable prompt.
prompt = "> "

## This asks the user for file name of the txt file.
file_name = input("Please provide a valid filename {}".format(prompt))

## This opens the file and stores the object to a variable.
txt = open(file_name)

## This reads the content of the text object stored in the variable.
print(txt.read())