# [w ===> write] ====> remove all lines from the file and new typing
# [a ===> append] ===> add a new line at the end of the file
writeControls = open('D:\learn python\lessons-python/index.html', 'a') #open the file
arr = ['\nhello', 'world', '!']
print(writeControls.writelines("<body><h2>make file by by python</h2>todo-applcation/></body>"))
writeControls.close()