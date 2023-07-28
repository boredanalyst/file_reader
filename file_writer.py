## This stores a reusable prompt.
prompt = ("> ")

## This asks for the user's file name.
file_name = input("Please provide the name of your file: {}".format(prompt))

## This opens the file in read-only mode.
txt = open(file_name)

## This prints the current content of the file.
print(txt.read())

## This asks the user for the text they want to write.
text_towrite = input("Please provide the text you want to add: {}".format(prompt))

## This re-opens the file in append mode.
txt = open(file_name,"a")

## This writes the new line.
txt.write("\n")
txt.write(text_towrite)

## This closes the append-version of the file.
txt.close()

## This opens the file in read-only mode.
txt = open(file_name)

## This prints the current content of the file.
print("---------------------")
print("This is the content of your file: {}".format(prompt))
print(txt.read())

txt.close()