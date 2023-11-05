# control python files
# [w ===> write] ====> remove all lines from the file and new typing
# [r ===> read]
# [a ===> append] ===> add a new line at the end of the file
# [r+ ===> append] read && write

# functions to control python files
# readable ===> return True if file is readable or False if file is not readable
# read() ===> to read All lines from the file
# readline() ===> to read single line
# readlines() ===> to read all lines on the list ==> contrl list easy

open_File_Explorer = open('D:\learn python\lessons-python\master control/test.text','r') #open the file

# loop in all lines by for
for file in open_File_Explorer.readlines():
    print(file + 'programming')

print(open_File_Explorer.readable()) # return True if file is readable
open_File_Explorer.close()