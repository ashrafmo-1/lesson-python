# [w ===> write] ====> remove all lines from the file and new typing
# [a ===> append] ===> add a new line at the end of the file
writeControls = open('D:\learn python\lessons-python/strings.py', 'a') #open the file
arr = ['\nhello', 'world', '!']
print(writeControls.writelines(arr))
print(writeControls.readable())
writeControls.close()