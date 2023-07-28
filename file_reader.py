from sys import argv

script, filename = argv

txt = open(filename)
prompt = "> "

print("Here is the file: {} ".format(filename))
print(prompt)
print(txt.read())